#!/usr/bin/env python3
"""Full author lists from Crossref and arXiv  ->  data/bib_cache.json

Implements decision D2 (CLAUDE.md §6.3). This is the ONLY networked script in the
project, it is invoked explicitly (`make bib`), and it is ADVISORY: build.py works
without it and simply leaves `authors` absent.

    python3 scripts/fetch_bib.py                 # new sha256s only
    python3 scripts/fetch_bib.py --refetch       # ignore the cache, fetch everything
    python3 scripts/fetch_bib.py --limit 10      # stop after 10 lookups
    python3 scripts/fetch_bib.py --mailto you@example.org

Three conditions from D2, all implemented here and all load-bearing:

  1. KEYED BY sha256, not by DOI or position, so the cache survives an add-only
     update and only genuinely new papers cost a round trip.
  2. FULL AUTHOR LISTS OR NONE. A truncated list is not a partial answer, it is a
     false one, because it looks complete. If a record comes back without a usable
     list, `authors` stays absent for that paper.
  3. REPORT EVERY DISAGREEMENT, APPLY NONE. Where the registered first-author
     surname or year contradicts the filename, it goes to a report for the owner to
     apply upstream. This project never edits meta/ (§2).

On the polite pool: Crossref asks for a contact address in the query string, which
speeds up service. The owner's email is deliberately NOT sent by default -- it is
not this script's to hand to a third party. Pass --mailto to opt in.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
DATA, REPORTS = ROOT / "data", ROOT / "reports"
CACHE = DATA / "bib_cache.json"

UA = "TeamLibraryBrowser/0.1 (internal research tool; +http://lihw0056/)"
CROSSREF = "https://api.crossref.org/works/"
ARXIV = "http://export.arxiv.org/api/query"
ATOM = {"a": "http://www.w3.org/2005/Atom"}


# --------------------------------------------------------------------------- #
# http
# --------------------------------------------------------------------------- #

def get(url: str, *, timeout: float = 30.0, tries: int = 4) -> bytes | None:
    """GET with backoff. Returns None on a 404 (a real answer: no such record)."""
    delay = 2.0
    for attempt in range(1, tries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as fh:
                return fh.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503, 504) and attempt < tries:
                wait = float(e.headers.get("Retry-After") or delay)
                print(f"    HTTP {e.code}; retrying in {wait:.0f}s", flush=True)
                time.sleep(wait)
                delay *= 2
                continue
            print(f"    HTTP {e.code} (giving up)", flush=True)
            return None
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < tries:
                print(f"    {type(e).__name__}: {e}; retrying in {delay:.0f}s", flush=True)
                time.sleep(delay)
                delay *= 2
                continue
            print(f"    {type(e).__name__}: {e} (giving up)", flush=True)
            return None
    return None


# --------------------------------------------------------------------------- #
# parsing a registration into the cache shape
# --------------------------------------------------------------------------- #

def crossref_authors(msg: dict) -> list[str] | None:
    """Full list, in registered order, or None.

    Crossref gives `given`/`family` for people and a single `name` for group
    authors (consortia). A person with no `family` is unusable, and one unusable
    entry makes the whole list untrustworthy -- so return None rather than a list
    with a hole in it (condition 2).
    """
    raw = msg.get("author")
    if not isinstance(raw, list) or not raw:
        return None
    out = []
    for a in raw:
        if a.get("family"):
            given = (a.get("given") or "").strip()
            out.append(f"{given} {a['family']}".strip())
        elif a.get("name"):          # consortium / group author
            out.append(a["name"].strip())
        else:
            return None
    return out or None


def crossref_first_family(msg: dict) -> str | None:
    """The first author's `family`, or None for a group author or a missing one.

    None is not a gap to fill: a consortium has no family name, and inventing one
    from its display string is exactly the byline reconstruction that was measured
    and rejected (CLAUDE.md §3).
    """
    raw = msg.get("author")
    if not isinstance(raw, list) or not raw:
        return None
    fam = (raw[0].get("family") or "").strip()
    return fam or None


def crossref_year(msg: dict) -> int | None:
    for key in ("published", "published-print", "published-online", "issued", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0] and isinstance(parts[0][0], int):
            return parts[0][0]
    return None


def fetch_crossref(doi: str, mailto: str | None) -> dict | None:
    url = CROSSREF + urllib.parse.quote(doi, safe="")
    if mailto:
        url += "?" + urllib.parse.urlencode({"mailto": mailto})
    body = get(url)
    if body is None:
        return None
    try:
        msg = json.loads(body)["message"]
    except (ValueError, KeyError):
        return None
    title = (msg.get("title") or [None])[0]
    venue = (msg.get("container-title") or [None])[0]
    return {
        "source": "crossref",
        "id": doi,
        "authors": crossref_authors(msg),
        # The FIRST author's family name, as the publisher registered it, kept
        # separate from the joined display name. The ingest builds a filename from
        # it, and a filename is the join key: re-deriving a surname by splitting
        # "given family" back apart guesses, and guessed wrong on 3 of 60 real
        # papers -- `Mathias Fynbo Jensen` became `FynboJensen`. Crossref already
        # knows which part is the family name; nothing here should re-decide it.
        "registered_first_family": crossref_first_family(msg),
        "registered_title": title.strip() if isinstance(title, str) else None,
        "registered_venue": venue.strip() if isinstance(venue, str) else None,
        "registered_year": crossref_year(msg),
        "registered_type": msg.get("type"),
    }


def fetch_arxiv(arxiv_id: str) -> dict | None:
    url = ARXIV + "?" + urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    body = get(url)
    if body is None:
        return None
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return None
    entry = root.find("a:entry", ATOM)
    if entry is None:
        return None
    # A deleted or unknown id still returns an <entry>, with an error title.
    title_el = entry.find("a:title", ATOM)
    title = " ".join(title_el.text.split()) if title_el is not None and title_el.text else None
    if title and title.lower().startswith("error"):
        return None
    names = [
        " ".join(n.text.split())
        for a in entry.findall("a:author", ATOM)
        if (n := a.find("a:name", ATOM)) is not None and n.text
    ]
    pub = entry.findtext("a:published", default="", namespaces=ATOM)
    return {
        "source": "arxiv",
        "id": arxiv_id,
        "authors": names or None,
        "registered_title": title,
        "registered_venue": "arXiv",
        "registered_year": int(pub[:4]) if pub[:4].isdigit() else None,
        "registered_type": "preprint",
    }


# --------------------------------------------------------------------------- #
# disagreement checks (condition 3)
# --------------------------------------------------------------------------- #

def fold(s: str) -> str:
    """Compare surnames without being defeated by accents or case."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def filename_surname(source: str) -> str | None:
    m = re.match(r"^([^(]+)\(", source)
    return m.group(1).strip() if m else None


# Crossref returns titles with publisher markup in them: `<i>Bonsai</i>`, `<sub>2</sub>`,
# and stray newlines from the deposited XML. Comparing those raw manufactures a
# disagreement that is really a formatting difference.
TAGS = re.compile(r"<[^>]{1,40}>")


def clean_title(s: str) -> str:
    return re.sub(r"\s+", " ", TAGS.sub("", s)).strip()


def check(paper: dict, rec: dict) -> list[tuple[str, str]]:
    """-> [(kind, message)]. Never applied, only reported (condition 3)."""
    out, src = [], paper["source"]
    authors = rec.get("authors")

    if authors:
        want = filename_surname(src)
        first = authors[0]
        if want and fold(want) not in fold(first):
            # If the filename surname appears anywhere in the list, the registration
            # simply puts a consortium or a different author first -- a much weaker
            # finding than a name that is absent altogether.
            anywhere = any(fold(want) in fold(a) for a in authors)
            kind = "first-author order" if anywhere else "first-author surname"
            note = (" (the filename's name IS in the list, just not first)" if anywhere
                    else " (the filename's name is NOT in the registered list at all)")
            out.append((kind,
                        f"filename says {want!r}, {rec['source']} registers {first!r}"
                        f"{note}\n    [{src}]"))

    ry, sy = rec.get("registered_year"), paper.get("year")
    if ry and sy and ry != sy:
        delta = abs(ry - sy)
        if delta == 1:
            kind, note = "year off by one", " -- the ordinary online-first vs issue-year gap"
        else:
            kind, note = "year off by more than one", f" -- {delta} years apart; worth a look"
        out.append((kind, f"sidecar says {sy}, {rec['source']} registers {ry}{note}\n    [{src}]"))

    rt, pt = rec.get("registered_title"), paper.get("title")
    if rt and pt and not paper.get("title_from_filename"):
        rtc = clean_title(rt)
        if fold(rtc)[:60] != fold(pt)[:60]:
            out.append(("title", f"review has {pt[:70]!r},\n    {rec['source']} registers "
                                 f"{rtc[:70]!r}\n    [{src}]"))

    if authors is None:
        rtype = rec.get("registered_type") or "unknown type"
        if rtype in ("book", "book-chapter", "monograph", "edited-book", "reference-book"):
            why = (f"the registration is a `{rtype}` -- Crossref carries EDITORS for it, "
                   f"not authors. Correctly absent, not a gap to fill")
        else:
            why = (f"the registration is a `{rtype}` with NO author field at all -- an "
                   f"incomplete deposit by the publisher, not a defect in this base")
        out.append(("no author list",
                    f"{why}; `authors` left absent (condition 2)\n    [{src}]"))
    return out


# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refetch", action="store_true", help="ignore the cache")
    ap.add_argument("--limit", type=int, default=0, help="stop after N lookups")
    ap.add_argument("--mailto", default=None,
                    help="opt in to Crossref's polite pool with this address")
    ap.add_argument("--delay", type=float, default=0.2, help="seconds between requests")
    ap.add_argument("--recheck", action="store_true",
                    help="re-run the disagreement checks over the cache; no network")
    args = ap.parse_args()

    lib_path = DATA / "library.json"
    if not lib_path.exists():
        print("fetch_bib: data/library.json not found -- run `make build` first.",
              file=sys.stderr)
        return 1
    papers = json.loads(lib_path.read_text(encoding="utf-8"))["papers"]

    cache = {"by_sha256": {}}
    if CACHE.exists() and not args.refetch:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
        cache.setdefault("by_sha256", {})
    by = cache["by_sha256"]

    if args.recheck:
        problems = []
        for p in papers:
            rec = by.get(p["sha256"])
            if rec:
                problems += check(p, rec)
        print(f"fetch_bib: rechecked {len(by)} cached record(s), no network used")
        write_report(problems)
        return 0

    todo, no_id = [], []
    for p in papers:
        if not args.refetch and p["sha256"] in by:
            continue
        if p.get("doi"):
            todo.append((p, "doi", p["doi"]))
        elif p.get("arxiv"):
            todo.append((p, "arxiv", p["arxiv"]))
        else:
            no_id.append(p)

    print(f"fetch_bib: {len(papers)} papers · {len(by)} cached · {len(todo)} to fetch · "
          f"{len(no_id)} with no identifier (left labelled, D2)")
    if args.mailto:
        print(f"fetch_bib: polite pool as {args.mailto}")
    else:
        print("fetch_bib: public pool; no contact address sent "
              "(pass --mailto to opt in)")
    if not todo:
        print("fetch_bib: nothing to do")
        return 0

    problems, ok, failed = [], 0, []
    for i, (paper, kind, ident) in enumerate(todo, 1):
        if args.limit and i > args.limit:
            print(f"fetch_bib: --limit {args.limit} reached; {len(todo) - args.limit} left")
            break
        rec = fetch_crossref(ident, args.mailto) if kind == "doi" else fetch_arxiv(ident)
        if rec is None:
            failed.append((paper["source"], kind, ident))
            print(f"  [{i}/{len(todo)}] MISS {kind}:{ident}")
        else:
            rec["fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            by[paper["sha256"]] = rec
            n = len(rec["authors"]) if rec["authors"] else 0
            ok += 1
            print(f"  [{i}/{len(todo)}] {kind}:{ident} -> {n} author(s)")
            problems += check(paper, rec)
        time.sleep(args.delay)

    cache["by_sha256"] = dict(sorted(by.items()))
    cache["fetched_with"] = {
        "user_agent": UA,
        "polite_pool": bool(args.mailto),
        "last_run": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    DATA.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                     encoding="utf-8")

    with_authors = sum(1 for r in by.values() if r.get("authors"))
    print(f"\nfetch_bib: {ok} fetched · {len(failed)} missed · cache now {len(by)} records, "
          f"{with_authors} with a full author list")
    for src, kind, ident in failed:
        print(f"  miss: {kind}:{ident}  [{src}]")

    write_report(problems)
    print("\nfetch_bib: run `make build` to fold the authors into library.json")
    return 0


def write_report(problems: list[tuple[str, str]]) -> None:
    if not problems:
        print("fetch_bib: no disagreements")
        return
    groups: dict[str, list[str]] = {}
    for kind, msg in problems:
        groups.setdefault(kind, []).append(msg)
    order = ["first-author surname", "no author list", "title",
             "year off by more than one", "first-author order", "year off by one"]
    kinds = [k for k in order if k in groups] + [k for k in groups if k not in order]

    REPORTS.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = REPORTS / f"bib_disagreements_{stamp}.txt"
    lines = [
        "Disagreements between the publisher's registered record and this base.",
        "",
        "REPORTED, NOT APPLIED. Fixes belong upstream in KBase (CLAUDE.md §2, §2.1);",
        "this project never edits meta/. Ordered most-actionable first: a surname that",
        "is absent from the registration is a likely misattribution, whereas a year off",
        "by one is usually just online-first vs issue year and needs no action.",
        "",
    ]
    for k in kinds:
        lines.append(f"## {k}  ({len(groups[k])})")
        lines += [f"  - {m}" for m in groups[k]] + [""]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"fetch_bib: {len(problems)} disagreement(s) in {len(kinds)} kind(s) "
          f"-> {out.relative_to(ROOT)}")
    for k in kinds:
        print(f"  {len(groups[k]):>3}  {k}")
    return


if __name__ == "__main__":
    sys.exit(main())

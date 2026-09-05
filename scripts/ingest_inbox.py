#!/usr/bin/env python3
"""inbox/ -> raw/ + meta/  — rename a dropped paper, hash it, and write its sidecar.

The owner drops publisher PDFs into `inbox/` and they need to become part of the
corpus: renamed to the base's convention, copied into `raw/`, given a sidecar in
`meta/`, filed into a topic, and cleared from `inbox/`. This does the mechanical
part of that. See CLAUDE.md §6.11 for the whole runbook, including the parts a
script cannot do.

WHAT IT WILL NOT DO, and why each one is a person's job:

  * It does not write the PROSE. `## Abstract`, `## Summary`, `## Key points` and
    `## Limitations` are read off the paper by someone who read the paper. The
    script writes them from a `--prose` file keyed by sha256, and for any paper
    with no entry it writes a marked placeholder and sets `status:
    prose-pending` so the gap is loud rather than silent.
  * It does not pick a TOPIC. The taxonomy is the review's (D1), and a topic is
    assigned by reading -- D20 exists because that judgement matters.
  * It does not delete anything from `inbox/`. Clearing the inbox is a separate,
    verified step: `--clear` removes only files whose bytes are already in
    `raw/` under their new name, re-hashed at that moment.

`raw/` IS ADD-ONLY, NOT WRITABLE. A new file may be added; no existing file may
ever be modified, renamed or deleted (CLAUDE.md §2.0). This script refuses a
target name that already exists, so it can only ever add.

    python3 scripts/ingest_inbox.py                         # dry run: what would happen
    python3 scripts/ingest_inbox.py --prose p.json --apply   # write raw/ + meta/
    python3 scripts/ingest_inbox.py --clear                  # empty inbox/, verified

Standard library only. Networked (Crossref) unless --no-network, like `make bib`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import paperlib  # noqa: E402


def also_in_block(areas: list[str]) -> str:
    """The `also_in_areas:` frontmatter lines, or a comment saying there are none.

    NOT `duplicate_of_area`, which the upstream toolkit already uses for a paper
    filed under a second TOPIC inside one review. Two different senses of the word
    in one frontmatter block would be read wrong exactly once, by someone in a
    hurry, and the wrong reading is invisible.
    """
    if not areas:
        return "# also_in_areas: (none -- these bytes are held only here)"
    return "also_in_areas:\n" + "\n".join(f"  - {a}" for a in areas)

ROOT = build.ROOT
INBOX, RAW, META = ROOT / "inbox", ROOT / "raw", ROOT / "meta"
AREA = build.AREA
LEDGER = ROOT / "annotations" / "upstream_edits.json"

# This project is NOT KBase's ingest. A sidecar written here must not claim to be
# one written there: `processor: 5` is KBase's ingest version and copying it would
# forge the one field that says where a record came from. A distinct value means
# KBase's own validator will notice these files, which is the point.
PROCESSOR = "paperlib-ingest-1"

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
# Characters a filename must not carry, and the base's own convention: the venue
# and title are separated by `; ` and a colon inside the title is dropped.
BAD = re.compile(r'[/\\:*?"<>|\r\n\t]')
# PLoS and a few others mint a DOI for each figure, table and supplement by
# appending `.g001` / `.t002` / `.s001` to the article's. Stripping the suffix
# turns those into more evidence for the article DOI instead of a competitor.
ASSET_SUFFIX = re.compile(r"\.[gtse]\d{3,}$")

# A single letter, optionally with a stop: `C.`, `A`, `J.` — a middle initial.
INITIAL = re.compile(r"^[A-Za-z]\.?$")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def text_of(path: Path, pages: int = 3) -> str:
    try:
        return subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(pages), "-layout", str(path), "-"],
            capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def find_doi(txt: str) -> str | None:
    """The DOI printed on the paper, or None.

    NOT simply the first match. Four failure modes were measured against a real
    corpus of 60 papers on 2026-09-05, and every one produced a well-formed string
    that was not the article's DOI -- which is worse than finding nothing, because
    nothing is refused loudly while a wrong DOI fetches a wrong registration:

      * a DOI broken across a line yields a truncated PREFIX: the first match in
        the PLoS paper was `10.1371/journal.` while the real DOI appeared four
        times below it;
      * PNAS prints `.../suppl/doi:10.1073/pnas.2100542118/-/DCSupplemental`, and
        `/-/` is not part of any DOI;
      * PLoS mints a DOI per FIGURE and per TABLE -- `...pcbi.1003266.g001` --
        which is longer than the article's and appears earlier on the page;
      * the same article DOI is printed in the running header of every page, so it
        is reliably the most frequent candidate in the first three.

    Hence: normalise each candidate, then take the most frequent, earliest first
    on a tie. Frequency is what separates the article from everything else printed
    beside it, and it is read off the document rather than guessed.
    """
    counts: dict[str, int] = {}
    first: dict[str, int] = {}
    for m in DOI_RE.finditer(txt):
        d = m.group(0).rstrip(".,;)")
        d = d.split("/-/")[0].rstrip(".,;)")       # publisher supplemental path
        d = ASSET_SUFFIX.sub("", d)                # a figure/table/supplement DOI
        if len(d) > 7:
            counts[d] = counts.get(d, 0) + 1
            first.setdefault(d, m.start())
    if not counts:
        return None
    # A truncated prefix is a fragment of the thing it is a prefix of; it can only
    # win if the full form never appeared, in which case it is all there is.
    full = [d for d in counts if not any(o != d and o.startswith(d) for o in counts)]
    pool = full or list(counts)
    return min(pool, key=lambda d: (-counts[d], first[d]))


def surname_key(full: str) -> str:
    """`Tim Van Den Bossche` -> `VanDenBossche`; `Andrea Scafidi` -> `Scafidi`.

    The base's filenames use the first author's surname with spaces removed --
    `deAlmeida`, `LeitePereira`, `PriorLabsTeam`. Everything after the given
    name is the surname, and the given name is the leading token, which is the
    one thing a registration reliably puts first.
    """
    toks = [t for t in re.split(r"\s+", full.strip()) if t]
    if len(toks) < 2:
        return "".join(toks) or "Unknown"
    # Drop MIDDLE INITIALS. `Juan C. Almagro` was becoming `CAlmagro` and
    # `Jorg J. A. Calis` `JACalis` -- and the filename is the join key, so a wrong
    # one is permanent under the add-only rule. An initial is a single letter with
    # an optional stop; that is decidable, unlike a particle. This deliberately
    # does NOT try to split `Ben Hamza`, `Van Den Bossche` or `Leite Pereira`,
    # which are surnames and must survive intact (CLAUDE.md §4).
    rest = [t for t in toks[1:] if not INITIAL.match(t)]
    if not rest:                       # every remaining token was an initial
        rest = toks[1:]
    return "".join(rest).replace(".", "").replace("'", "")


def clean_title(s: str) -> str:
    """A registered title, made safe for a single-line YAML value.

    Crossref returns titles with publisher markup and hard line breaks in them:
    `...immunogenic CD8\n <sup>+</sup>\n T cell epitopes`. Written verbatim into
    `title: "..."` that produces a frontmatter value the parser truncates at the
    first newline, because the field regex is line-anchored. Measured on the first
    real ingest, 2026-09-05: 1 of 60 papers. Unlike clean_component this keeps
    colons and semicolons, which are legitimate in a title and only a problem in
    a filename.
    """
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"<[^>]+>", "", s)
    s = build.unescape_md(s)
    return re.sub(r"\s+", " ", s).strip()


def clean_component(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"<[^>]+>", "", s)
    s = build.unescape_md(s)
    s = s.replace(":", "").replace(";", ",")       # `; ` is the field separator
    s = BAD.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip(" .")


def target_name(reg: dict, media: str) -> str:
    # Prefer the family name the publisher REGISTERED over anything derived by
    # splitting a display name. surname_key is the fallback for registrations
    # that carry no structured family name (arXiv, consortium authors).
    fam = reg.get("registered_first_family")
    au = (reg.get("authors") or ["Unknown"])[0]
    key = re.sub(r"\s+", "", fam).replace(".", "").replace("'", "") if fam else surname_key(au)
    name = (f"{key}({reg['registered_year']}) "
            f"{clean_component(reg.get('registered_venue') or 'unknown')}; "
            f"{clean_component(reg.get('registered_title') or 'untitled')}")
    # ext4 allows 255 BYTES per component, and these titles are long.
    room = 250 - len(media.encode()) - 1
    while len(name.encode("utf-8")) > room:
        name = name[:-1].rstrip()
    return f"{name}.{media}"


def sidecar_id(name: str, year: int) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", clean_component(name).lower()).strip("-")
    return f"{year}-01-01_{slug[:40].rstrip('-')}"


TYPE_OF = {"journal-article": "paper", "posted-content": "preprint",
           "book": "review", "book-chapter": "review",
           "proceedings-article": "paper", "report": "note"}

PLACEHOLDER = ("_NOT YET WRITTEN._ This section is read off the paper by a person; "
               "`scripts/ingest_inbox.py` does not invent it. `status: prose-pending` "
               "in the frontmatter says so, and `make audit` reports it.")


def sidecar_text(rec: dict, prose: dict) -> str:
    def sec(key: str) -> str:
        v = (prose.get(key) or "").strip()
        return v if v else PLACEHOLDER
    kp = prose.get("key_points") or []
    kp_block = "\n".join(f"- {k}" for k in kp) if kp else PLACEHOLDER
    q = '"'
    return f"""---
# --- identity ------------------------------------------------
id: {rec['id']}
id_basis: filename-year
source: {rec['source']}
sha256: {rec['sha256']}
size_bytes: {rec['size_bytes']}
media: {rec['media']}

# --- ingest --------------------------------------------------
processed: '{rec['processed']}'
processor: {PROCESSOR}
status: {rec['status']}
extraction:
  method: pdftotext
  ocr: false
  chars: {rec['chars']}

# --- classification (LIH WI DC-909) --------------------------
type: {rec['type']}
classification: Public
classification_basis: {q}published literature — publicly available at its venue{q}

# --- bibliographic -------------------------------------------
doi: {q}{rec['doi']}{q}
year: {rec['year']}
title: {q}{rec['title'].replace(q, chr(92) + q)}{q}

# --- cross-area ----------------------------------------------
area: {AREA}
{rec['also_in_block']}
# --- provenance ----------------------------------------------
provenance: {q}{rec['provenance']}{q}
---

## Abstract

{sec('abstract')}

## Summary

{sec('summary')}

## Key points

{kp_block}

## Limitations

{sec('limitations')}

## Provenance

{rec['provenance_body']}

## Citation

{rec['citation']}
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write raw/ and meta/")
    ap.add_argument("--prose", default=None,
                    help="JSON keyed by sha256 with abstract/summary/key_points/limitations")
    ap.add_argument("--clear", action="store_true",
                    help="delete inbox files whose bytes are already in raw/ (re-hashed now)")
    ap.add_argument("--doi-map", default=None,
                    help="JSON {inbox filename or sha256: DOI} for papers whose DOI is "
                         "not on pages 1-3 (scans, older PDFs, some preprints). It "
                         "supplies the identifier ONLY -- title, venue, year and byline "
                         "still come from the registration, so a wrong DOI here is "
                         "caught by reading what comes back, not accepted.")
    ap.add_argument("--doi-override", default=None,
                    help="JSON {inbox filename or sha256: DOI} that BEATS the DOI "
                         "printed on the paper. Distinct from --doi-map, which is "
                         "only a fallback: use this when the paper prints a "
                         "REGISTERED but wrong identifier -- typically a published "
                         "article whose PDF still carries its preprint DOI, which "
                         "would otherwise be filed as `posted-content` with no "
                         "venue. Every use is printed and recorded in the sidecar.")
    ap.add_argument("--no-network", action="store_true")
    ap.add_argument("--approved", default=None,
                    help="the owner's words, recorded in the ledger; required with --apply")
    args = ap.parse_args()

    if not INBOX.is_dir():
        print(f"ingest_inbox: no {INBOX.relative_to(ROOT)}/ — nothing to do.")
        return 0
    files = sorted(p for p in INBOX.iterdir() if p.is_file() and not p.name.startswith("."))
    if not files:
        print("ingest_inbox: inbox/ is empty.")
        return 0

    # What the collection already holds. library.json is the convenient answer, but
    # it does NOT exist before the first build -- and "before the first build" is
    # exactly when a new collection is being filled, so reading only library.json
    # would turn the duplicate checks off during the one phase that needs them most.
    # meta/ is the ground truth and is always there.
    # ALWAYS meta/, never library.json. Upstream preferred library.json when it
    # existed and fell back to meta/ only before the first build -- but
    # library.json is a BUILD PRODUCT and is stale between an ingest and the next
    # `make build`. Measured 2026-09-05: ingesting 57 papers and then running
    # `--clear` in the same breath compared the inbox against a 60-paper
    # library.json, found none of the new bytes, and kept all 58 files. It reads
    # as "the copy failed" and invites a re-ingest of papers already in raw/.
    # meta/ is the ground truth, is always present, and is what `make verify`
    # re-proves against the bytes; parsing it costs milliseconds.
    held = []
    for side in sorted(META.glob("*.md")):
        fm = build.parse_frontmatter(side.read_text(encoding="utf-8"))
        if fm.get("sha256") and fm.get("source"):
            held.append(fm)
    have_sha = {p["sha256"]: p["source"] for p in held}
    # Every OTHER area's holdings, by bytes. Rescanned from meta/ rather than read
    # from index/registry.json, which is derived and may be stale.
    cross_area = paperlib.scan_all_areas(build.parse_frontmatter)
    have_doi = {build.normdoi(p["doi"]): p["source"] for p in held if p.get("doi")}
    prose_all = json.loads(Path(args.prose).read_text(encoding="utf-8")) if args.prose else {}
    doi_map = json.loads(Path(args.doi_map).read_text(encoding="utf-8")) if args.doi_map else {}
    doi_over = (json.loads(Path(args.doi_override).read_text(encoding="utf-8"))
                if args.doi_override else {})

    if args.clear:
        return clear_inbox(files, have_sha)

    fb = None
    if not args.no_network:
        import importlib.util as u
        sp = u.spec_from_file_location("fb", Path(__file__).parent / "fetch_bib.py")
        fb = u.module_from_spec(sp)
        sp.loader.exec_module(fb)

    # Whose collection this is -- project.json, so a retargeted copy does not credit
    # somebody else's owner in every sidecar it writes.
    owner = build.load_project().get("contact_name") or "the data owner"

    plans, refused = [], 0
    # What THIS RUN has already planned. Every check below compares against the
    # collection as it stands on disk, which is empty of anything planned a moment
    # ago -- so two inbox files that are the same paper both passed, both planned
    # the same raw/ name, and the apply loop copied the second over the first.
    # That is a silent add-only violation, and it takes the first paper's sidecar
    # with it. Found on the second real batch, 2026-09-05: `nature14426.pdf` and
    # `nature14426-1.pdf` are byte-identical.
    planned_sha: dict[str, str] = {}
    planned_doi: dict[str, str] = {}
    planned_dest: dict[str, str] = {}
    for f in files:
        print("=" * 78)
        print(f.name)
        media = f.suffix.lstrip(".").lower() or "bin"
        sha = sha256_of(f)
        if sha in have_sha:
            print(f"  REFUSED: identical bytes already in the corpus as "
                  f"{have_sha[sha]!r}")
            refused += 1
            continue
        if sha in planned_sha:
            print(f"  REFUSED: identical bytes to {planned_sha[sha]!r}, already "
                  f"planned earlier in this same run.")
            refused += 1
            continue
        txt = text_of(f)
        doi = find_doi(txt)
        # The map is a LAST resort, not an override: a DOI printed on the paper is
        # evidence, a DOI typed into a file is an assertion, and where both exist the
        # paper wins. It is here because extraction genuinely fails -- scanned pages,
        # older typesetting, some preprint servers -- and without it those papers
        # cannot enter the collection at all.
        over = doi_over.get(f.name) or doi_over.get(sha)
        if over and over != doi:
            # The ONE case that beats the paper, and it is never silent. The rule
            # that the printed DOI wins exists to stop a careless typed identifier
            # overriding evidence; it is not meant to file a published article as a
            # preprint because the publisher left the preprint DOI in the PDF.
            print(f"  DOI from --doi-override: {over}  (the paper prints {doi})")
            doi = over
        if not doi:
            doi = doi_map.get(f.name) or doi_map.get(sha)
            if doi:
                print(f"  DOI from --doi-map (not found in the text): {doi}")
        if not doi:
            print("  REFUSED: no DOI on pages 1-3. Supply it with --doi-map "
                  "(keyed by this filename or by its sha256); the collection keys "
                  "its bibliography on an identifier.")
            refused += 1
            continue
        if build.normdoi(doi) in have_doi:
            print(f"  REFUSED: DOI {doi} already in the corpus as "
                  f"{have_doi[build.normdoi(doi)]!r}")
            refused += 1
            continue
        if build.normdoi(doi) in planned_doi:
            print(f"  REFUSED: DOI {doi} is also {planned_doi[build.normdoi(doi)]!r}, "
                  f"already planned earlier in this same run.")
            refused += 1
            continue
        reg = fb.fetch_crossref(doi, None) if fb else None
        mapped = doi_map.get(f.name) or doi_map.get(sha)
        if (not reg or not reg.get("registered_title")) and mapped and mapped != doi:
            # A DOI read off the paper normally WINS over one typed into a file.
            # But an unregistered one is not evidence about the paper, it is
            # evidence that the extraction produced something that is not a DOI --
            # so here, and only here, the map is consulted. Printed loudly: the
            # whole point of the dry run is that a person sees which identifier
            # each record was built from.
            print(f"  the DOI read off the paper ({doi}) is NOT registered; "
                  f"falling back to --doi-map: {mapped}")
            doi = mapped
            if build.normdoi(doi) in have_doi:
                print(f"  REFUSED: DOI {doi} already in the corpus as "
                      f"{have_doi[build.normdoi(doi)]!r}")
                refused += 1
                continue
            reg = fb.fetch_crossref(doi, None) if fb else None
        if not reg or not reg.get("registered_title"):
            print(f"  REFUSED: {doi} is not registered at Crossref (or --no-network). "
                  f"Title, venue and year come from the registration.")
            refused += 1
            continue

        name = target_name(reg, media)
        dest = RAW / name
        if dest.exists():
            print(f"  REFUSED: raw/{name!r} already exists. raw/ is ADD-ONLY.")
            refused += 1
            continue
        if name in planned_dest:
            # The last line of defence: two different files, two different DOIs,
            # but a registration that yields the same surname, year, venue and
            # title. Writing both would still be one overwrite.
            print(f"  REFUSED: raw/{name!r} is already the target of "
                  f"{planned_dest[name]!r} in this same run. raw/ is ADD-ONLY.")
            refused += 1
            continue
        side = META / f"{name}.md"
        if side.exists():
            print(f"  REFUSED: meta/{name}.md already exists.")
            refused += 1
            continue

        # Held in ANOTHER area? Allowed, and recorded. Two areas are worked on
        # independently, so a paper can genuinely matter in both; what must not
        # happen is the second copy arriving with no trace of the first.
        elsewhere = paperlib.held_elsewhere(cross_area, sha, AREA)
        if elsewhere:
            print(f"  NOTE: these bytes are also held in: {', '.join(elsewhere)}. "
                  f"Ingesting anyway; the sidecar will record it.")

        prose = prose_all.get(sha, {})
        chars = len(text_of(f, pages=9999))
        au = reg.get("authors") or []
        rec = {
            "id": sidecar_id(name, reg["registered_year"]),
            "source": name, "sha256": sha, "size_bytes": f.stat().st_size,
            "media": media, "processed": date.today().isoformat(),
            "status": "ok" if prose else "prose-pending",
            "chars": chars,
            "type": prose.get("type") or TYPE_OF.get(reg.get("registered_type"), "paper"),
            "doi": doi, "year": reg["registered_year"],
            "title": clean_title(reg["registered_title"]),
            "also_in_block": also_in_block(elsewhere),
            "provenance": (f"located in the published literature and deposited by "
                           f"{owner} in inbox/ as {f.name}; ingested into area "
                           f"{AREA!r} by scripts/ingest_inbox.py on "
                           f"{date.today().isoformat()}"
                           + (f"; DOI supplied by --doi-override (the PDF prints a "
                              f"different registered identifier)" if over and over == doi
                              else "")),
            "provenance_body": (
                f"Located in the published literature, dropped into `inbox/` as "
                f"`{f.name}` and ingested into area **{AREA}** by "
                f"`scripts/ingest_inbox.py`. Title, venue, year and byline come from "
                f"the publisher's registration for `{doi}`; the prose sections were "
                f"written here from the paper itself."
                + (f" These same bytes are also held in: "
                   f"{', '.join(elsewhere)}." if elsewhere else "")),
            "citation": (f"{surname_key(au[0]) if au else 'Unknown'} et al. "
                         f"{reg.get('registered_venue') or 'unknown'} "
                         f"{reg['registered_year']}. {reg['registered_title']}. "
                         f"doi: {doi}"),
        }
        print(f"  -> raw/{name}")
        print(f"  -> meta/{name}.md   (id {rec['id']}, {chars} chars, "
              f"type {rec['type']}, status {rec['status']})")
        print(f"     {len(au)} registered author(s); first {au[0] if au else '?'!r}")
        if not prose:
            print("     NO PROSE for this sha256 — the four prose sections would be "
                  "placeholders and status would be `prose-pending`.")
        plans.append((f, dest, side, rec, prose))
        planned_sha[sha] = f.name
        planned_doi[build.normdoi(doi)] = f.name
        planned_dest[name] = f.name

    print("=" * 78)
    if not args.apply:
        print(f"ingest_inbox: DRY RUN · {len(plans)} would be ingested · {refused} refused")
        print("ingest_inbox: nothing written. inbox/ untouched. Re-run with --apply "
              "once the owner has seen this and said yes.")
        return 1 if refused else 0

    if not (args.approved or "").strip():
        print("ingest_inbox: --apply needs --approved '<the owner's words>'. Writing "
              "to raw/ and meta/ is an upstream write (D15), and the ledger records "
              "who approved it.", file=sys.stderr)
        return 2

    ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {"edits": []}
    seq = max([e.get("seq", 0) for e in ledger.get("edits", [])] or [0])
    entries = []
    for f, dest, side, rec, prose in plans:
        shutil.copy2(f, dest)                       # COPY: inbox/ is cleared separately
        got = sha256_of(dest)
        if got != rec["sha256"]:
            print(f"ingest_inbox: FATAL: {dest.name} copied but hashes differ "
                  f"({got[:12]} vs {rec['sha256'][:12]}). Removing.", file=sys.stderr)
            dest.unlink()
            return 3
        side.write_text(sidecar_text(rec, prose), encoding="utf-8")
        for rel, path in ((f"raw/{dest.name}", dest), (f"meta/{side.name}", side)):
            seq += 1
            entries.append({
                "seq": seq, "date": date.today().isoformat(), "file": rel,
                "keys": ["<new file>"], "before": {"<new file>": None},
                "after": {"<new file>": f"inbox/{f.name}"},
                "reason": "a paper the owner dropped in inbox/, ingested into the corpus",
                "evidence": (f"bytes copied from inbox/{f.name} and re-hashed after "
                             f"the copy; bibliography from the publisher's "
                             f"registration for {rec['doi']}"),
                "approved": args.approved,
                "sha256_before": None, "sha256_after": sha256_of(path),
            })
        print(f"  ADDED raw/{dest.name}")
        print(f"  ADDED meta/{side.name}")
    ledger["edits"] = ledger.get("edits", []) + entries
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    print(f"\ningest_inbox: {len(plans)} paper(s) ingested · {refused} refused · "
          f"ledger seq {entries[0]['seq']}–{entries[-1]['seq']}")
    print("ingest_inbox: next: `make bib` for the bylines, assign a topic in "
          "annotations/taxonomy.json, `make review`, install it, `make update`.")
    print("ingest_inbox: inbox/ is UNTOUCHED. Clear it with --clear once you have "
          "checked the build.")
    return 0


def clear_inbox(files: list, have_sha: dict) -> int:
    """Delete only what is provably already in raw/, re-hashed at this moment."""
    print("ingest_inbox: --clear re-hashes each inbox file and each raw/ candidate "
          "NOW; a file is removed only if its bytes are already in the corpus.\n")
    gone = kept = 0
    for f in files:
        sha = sha256_of(f)
        src = have_sha.get(sha)
        if not src:
            print(f"  KEPT   {f.name}  — its bytes are in no paper in library.json")
            kept += 1
            continue
        dest = RAW / src
        if not dest.exists() or sha256_of(dest) != sha:
            print(f"  KEPT   {f.name}  — {src!r} is missing from raw/ or differs")
            kept += 1
            continue
        f.unlink()
        print(f"  REMOVED {f.name}  — identical bytes served as raw/{src}")
        gone += 1
    print(f"\ningest_inbox: removed {gone} · kept {kept}")
    return 1 if kept else 0


if __name__ == "__main__":
    sys.exit(main())

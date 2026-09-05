#!/usr/bin/env python3
"""Emit a literature review covering EVERY paper, in the format build.py parses.

What this is, precisely, because the distinction matters:

    It CONSOLIDATES a taxonomy. It does not DECIDE one.

Every part, topic, description and assignment it writes already exists in
`data/library.json` — 234 of them read out of the 2026-08-06 review (D1), and 104
assigned in this project on 2026-09-03 on the owner's instruction (D9, §6.6). This
script invents nothing; it writes the merged tree back out as a single document so
that the review is once again the one place the taxonomy lives, and so
`annotations/topics.json` goes inert on the next build (which is exactly what §6.6
says should eventually happen to it).

**It is therefore NOT a substitute for a real regeneration in KBase.** A fresh pass
would re-read all 338 abstracts and might draw different lines; this reproduces the
lines already drawn. The document says so about itself, in the same words.

    python3 scripts/make_review.py                    # -> reports/<date>_literature_review.md
    python3 scripts/make_review.py --out outputs/     # the live location (D1, D15: ask first)

Standard library only, like build.py. Deterministic: same library.json -> byte-identical output.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit  # noqa: E402  -- reuses its CORPORATE test rather than a second copy
import build  # noqa: E402  -- one source of truth for folding and venue rules

ROOT = build.ROOT
PROSE = ROOT / "annotations" / "review_prose"

# The "How to read this" block is the one part of a review that makes a CLAIM
# ABOUT ITSELF -- how its clustering was arrived at, and by whom. That claim is
# true of one instance and one act, so it is data, not code: shipping it inside
# this script is how a retargeted copy would end up telling somebody else's
# story about somebody else's corpus. There is no default and no fallback; a
# missing file is fatal, because silently emitting generic prose would be the
# same failure one step quieter.
PROSE_FILES = {
    "first": "first.md",              # no --taxonomy, no prior taxonomy to keep
    "consolidate": "consolidate.md",  # no --taxonomy: the existing one, written out
    "recluster": "recluster.md",      # --taxonomy: the taxonomy was re-drawn
}


def load_prose(mode: str) -> str:
    path = PROSE / PROSE_FILES[mode]
    if not path.exists():
        print(f"make_review: FATAL: {path} not found. It is the review's account of "
              f"HOW ITS OWN CLUSTERING WAS MADE, which is true of this collection and "
              f"no other, so there is deliberately no default. Write it (see "
              f"RETARGETING.md step 5); the placeholders {{n}} {{t}} {{parts}} "
              f"{{moved}} {{reviewed}} {{curated}} {{with_authors}} are filled in.",
              file=sys.stderr)
        raise SystemExit(1)
    return path.read_text(encoding="utf-8")


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def anchor(name: str) -> str:
    """GitHub-style heading anchor: lowercase, punctuation dropped, spaces to hyphens."""
    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return re.sub(r"\s+", "-", s.strip())


def cite_author(p: dict) -> str:
    """`Rosen, Y. et al.` — the review's own citation convention, preserved.

    A paper that already came from a review has `first_author` in this form and is
    passed through untouched. For the rest the form has to be BUILT, and the
    surname is taken from the FILENAME rather than guessed out of the registered
    name — which is what makes it exact where a heuristic is not. An earlier audit
    of this corpus proved no particle list can do this job: the list that handles
    `de Groot` and `ter Huurne` also swallows the given name `Bin` in `Bin Duan`.

    Three cases needed handling beyond the obvious one, all found by checking the
    output against the corpus rather than by reasoning:

      * `HADACA consortium` deposited as the first author became `consortium, H.`
        — an organisation split as though it were a person. Corporate first
        authors now fall back to the filename's surname.
      * `Colliot(2023)`, an edited book, and `Chen(2025)`, an unsigned Nature
        Methods briefing, have NO known authors — so `et al.` asserted co-authors
        that may not exist. They get the bare surname.
      * `Patricia Martins Conde` with filename `Martins` matched no trailing run,
        fell back to the last token and became `Conde, P. M.`, dropping the half
        of the surname the filename names. The match is now made on the token
        INDEX, so it yields `Martins Conde, P.` — the whole surname.
    """
    fa = (p.get("first_author") or "").strip()
    if re.match(r"^[^,]+,\s*[A-Z]", fa):
        return fa                                  # already `Surname, I. ...`
    authors = p.get("authors") or []
    fnm = re.match(r"^([^(]+?)\s*\(", p["source"])
    fn_sur = fnm.group(1).strip() if fnm else ""

    # No byline at all: name the paper's surname and claim nothing more.
    if not authors:
        return fn_sur or fa

    # An organisation registered first is not a person to split.
    if audit.CORPORATE.search(authors[0]):
        return (fn_sur + " et al.") if fn_sur else authors[0]

    toks = authors[0].split()
    surname, given = None, []
    # 1. longest trailing run of tokens whose folded form IS the filename surname
    for i in range(len(toks)):
        if fold(" ".join(toks[i:])) == fold(fn_sur):
            surname, given = " ".join(toks[i:]), toks[:i]
            break
    # 2. otherwise the first token the filename surname begins with -- everything
    #    from there is the surname, which keeps a double surname whole.
    if surname is None and fn_sur:
        for i, t in enumerate(toks):
            if fold(t) and fold(fn_sur).startswith(fold(t)):
                surname, given = " ".join(toks[i:]), toks[:i]
                break
    if surname is None:
        surname, given = toks[-1], toks[:-1]
    inits = " ".join(t[0].upper() + "." for t in given if t and t[0].isalpha())
    head = f"{surname}, {inits}".strip().rstrip(",")
    return head + (" et al." if len(authors) > 1 else "")


def meta_line(p: dict) -> str:
    bits = []
    if p.get("doi"):
        bits.append(f"[doi:{p['doi']}](https://doi.org/{p['doi']})")
    elif p.get("arxiv"):
        bits.append(f"[arXiv:{p['arxiv']}](https://arxiv.org/abs/{p['arxiv']})")
    else:
        bits.append(build.NO_ID)
    if p.get("arxiv") and p.get("doi"):
        bits.append(f"[arXiv:{p['arxiv']}](https://arxiv.org/abs/{p['arxiv']})")
    bits.append(f"`{p['type']}`")
    if p.get("duplicate_of_area"):
        bits.append(f"also in **{p['duplicate_of_area']}**")
    return " · ".join(bits)


def entry(p: dict) -> str:
    # The venue goes in the italics and the arXiv ID does NOT: the 2026-08-06
    # review wrote `*arXiv:2506.03373.*` where the journal name belongs, which
    # made arXiv arrive as 19 distinct one-paper "venues" instead of one venue
    # with 19 papers (reported in reports/upstream_findings.md). `clean_venue`
    # patches over it downstream; writing it correctly here removes the need.
    venue = p.get("venue") or "venue not recorded"
    summary = re.sub(r"\s+", " ", p.get("abstract") or "").strip()
    return (
        f"### {cite_author(p)} ({p['year']}). *{venue}.* {p['title']}\n"
        f"{meta_line(p)}  \n"
        f"[src](<../raw/{p['source']}>)\n"
        f"\n{summary}\n"
    )


def papers_from_sidecars() -> list:
    """meta/*.md -> the minimum record set this script emits from.

    Deliberately NOT a second implementation of build.py's record builder: it reuses
    build's own frontmatter, section and filename parsers, and it fills only the
    fields an ENTRY needs. Topic and part are left absent on purpose -- they come
    from the --taxonomy spec, and a paper the spec misses must fail loudly at the
    coverage check rather than be quietly filed somewhere.
    """
    # data/bib_cache.json is `make bib`'s output and exists BEFORE any build: it is
    # keyed by the source file's sha256, which the sidecar declares. Reading it here
    # is not a nicety. In this collection upstream leaves `authors:` empty on all 340
    # sidecars (CLAUDE.md §3), so a review built from sidecars alone cited
    # `Avsec (2026)` where the corpus knows `Avsec, Ž. et al.` -- measured, on the
    # first run of this function against the real corpus. A newly ingested sidecar
    # DOES carry the registered byline, so both shapes have to work.
    cache = {}
    cache_path = build.DATA / "bib_cache.json"
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8")).get("by_sha256", {})

    out = []
    for path in sorted(build.META.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = build.parse_frontmatter(text)
        src = fm.get("source")
        if not src or fm.get("type") in build.NON_LITERATURE_TYPES:
            continue
        sections = build.body_sections(text)
        reg = cache.get(fm.get("sha256") or "", {})
        year = fm.get("year") or ""
        out.append({
            "source": src,
            "title": (fm.get("title") or reg.get("registered_title")
                      or build.title_from_filename(src)),
            # The filename is `Surname(YEAR) Venue; Title.ext`, so year and venue are
            # in it even for a paper that registers nowhere -- the sidecar's own
            # fields win where it has them.
            "year": int(year) if str(year).isdigit() else _year_from_filename(src),
            "venue": (build.clean_venue(fm.get("venue") or "")
                      or build.clean_venue(reg.get("registered_venue") or "")
                      or build.venue_from_filename(src)),
            "doi": fm.get("doi"),
            "arxiv": fm.get("arxiv"),
            "type": fm.get("type") or "paper",
            # parse_frontmatter already reads `authors` as a LIST (build.LIST_KEYS),
            # in both the block and the flow spelling
            "authors": fm.get("authors") or reg.get("authors") or [],
            "abstract": sections.get("Abstract") or sections.get("Summary") or "",
        })
    return out


def _year_from_filename(src: str) -> int:
    m = re.search(r"\((\d{4})\)", src)
    return int(m.group(1)) if m else 0


def sort_key(p: dict) -> tuple:
    """Newest first, then by the citation surname — the order the old review used."""
    return (-int(p["year"]), fold(cite_author(p)), p["source"])


def resolve_input(arg: str) -> Path:
    """A path argument, resolved the same way --out is: relative to the AREA.

    Falls back to the working directory so a path typed from the project root
    still works, and says which one it used -- silently reading a different file
    from the one the caller meant is worse than either.
    """
    p = Path(arg)
    if p.is_absolute():
        return p
    from_root = ROOT / p
    if from_root.exists():
        return from_root
    if p.exists():
        print(f"make_review: NOTE -- {arg!r} read relative to the working "
              f"directory ({p.resolve()}), not the area.", file=sys.stderr)
        return p
    print(f"make_review: FATAL: {arg!r} not found. Tried {from_root} and "
          f"{p.resolve()}.", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="reports",
                    help="directory to write into (default: reports/, a draft)")
    ap.add_argument("--taxonomy", default=None,
                    help="a re-clustering spec (annotations/taxonomy.json): parts, topics "
                         "with descriptions, and source -> topic. Without it the taxonomy "
                         "already in library.json is consolidated unchanged.")
    ap.add_argument("--date", default=date.today().isoformat(),
                    help="the date in the filename, which is what build.py orders on")
    ap.add_argument("--from-sidecars", action="store_true",
                    help="BOOTSTRAP: read the papers from meta/ instead of "
                         "data/library.json, which does not exist yet. Requires "
                         "--taxonomy, since there is no prior clustering to keep.")
    args = ap.parse_args()

    # The cold start. build.py needs a review (the taxonomy comes from it, D1) and
    # this script normally needs build.py's output -- so a NEW collection cannot
    # produce its first review at all without breaking that circle from one side.
    # It breaks here, because meta/ is the ground truth either way: library.json is
    # meta/ joined to a review, and the join is precisely what does not exist yet.
    if args.from_sidecars:
        if not args.taxonomy:
            print("make_review: FATAL: --from-sidecars needs --taxonomy. There is no "
                  "library.json to take a clustering from, so the clustering has to "
                  "come from the spec -- see RETARGETING.md step 5.", file=sys.stderr)
            return 1
        papers = papers_from_sidecars()
        if not papers:
            print(f"make_review: FATAL: no literature sidecars in {build.META}. "
                  f"Ingest some papers first (`make inbox`).", file=sys.stderr)
            return 1
        lib, tax = {"papers": papers}, []
    else:
        lib_path = build.DATA / "library.json"
        if not lib_path.exists():
            print(f"make_review: FATAL: {lib_path} not found. On a collection that has "
                  f"never been built, use --from-sidecars --taxonomy … (the first "
                  f"review has to come from meta/, because library.json is meta/ "
                  f"joined to a review that does not exist yet).", file=sys.stderr)
            return 1
        lib = json.loads(lib_path.read_text(encoding="utf-8"))
        papers, tax = lib["papers"], lib["taxonomy"]

    # A re-clustering spec REPLACES the taxonomy and every assignment. Applied to
    # copies of the paper records, so nothing else in this process sees the
    # override -- and it is fatal if the spec does not cover the corpus exactly,
    # because a partial re-clustering would silently leave papers in topics that
    # no longer exist.
    if args.taxonomy:
        spec = json.loads(resolve_input(args.taxonomy).read_text(encoding="utf-8"))
        A = spec["assignments"]
        srcs = {p["source"] for p in papers}
        if set(A) != srcs:
            print(f"make_review: FATAL: the spec covers {len(A)} papers, the corpus has "
                  f"{len(srcs)}. Missing: {sorted(srcs - set(A))[:3]}; unknown: "
                  f"{sorted(set(A) - srcs)[:3]}", file=sys.stderr)
            return 1
        part_of = {t["name"]: t["part"] for t in spec["topics"]}
        pname = {p["letter"]: p["name"] for p in spec["parts"]}
        # A letter is a POSITION; a name is a CLAIM. Checking one against the
        # other is what catches a renumbered part taking a topic with it --
        # which is exactly what happened on 2026-09-04: dropping one part and
        # renumbering the rest left three pure-mathematics papers filed under
        # cardiovascular medicine, because the maths topic kept its letter "H"
        # and that letter came to mean something else. The owner spotted it; the
        # build could not, because a letter cannot disagree with itself.
        drift = [(t["name"], t["part"], t.get("part_name"), pname.get(t["part"]))
                 for t in spec["topics"]
                 if t.get("part_name") and t.get("part_name") != pname.get(t["part"])]
        if drift:
            for name, letter, claimed, actual in drift:
                print(f"make_review: FATAL: topic {name!r} says part_name "
                      f"{claimed!r} but letter {letter!r} is {actual!r}",
                      file=sys.stderr)
            return 1
        missing = [t["name"] for t in spec["topics"] if not t.get("part_name")]
        if missing:
            print(f"make_review: FATAL: {len(missing)} topic(s) declare no "
                  f"`part_name`, so their part letter cannot be checked: "
                  f"{missing[:3]}", file=sys.stderr)
            return 1
        bad = sorted({t for t in set(A.values()) if t not in part_of})
        if bad:
            print(f"make_review: FATAL: {len(bad)} topic(s) assigned but not declared: "
                  f"{bad[:3]}", file=sys.stderr)
            return 1
        papers = [dict(p) for p in papers]
        for p in papers:
            p["topic"] = A[p["source"]]
            p["part_letter"] = part_of[p["topic"]]
            p["part"] = pname[p["part_letter"]]
        used = set(A.values())
        tax = [{"letter": q["letter"], "name": q["name"],
                "topics": [{"name": t["name"], "description": t.get("description")}
                           for t in spec["topics"]
                           if t["part"] == q["letter"] and t["name"] in used]}
               for q in spec["parts"]]
        tax = [q for q in tax if q["topics"]]

    by_topic: dict = {}
    unplaced = []
    for p in papers:
        if not p.get("topic") or not p.get("part_letter"):
            unplaced.append(p["source"])
            continue
        by_topic.setdefault((p["part_letter"], p["topic"]), []).append(p)
    if unplaced:
        print(f"make_review: FATAL: {len(unplaced)} paper(s) have no topic; the review "
              f"must cover every paper. First: {unplaced[:3]}", file=sys.stderr)
        return 1

    n_papers = len(papers)
    n_topics = sum(len(part["topics"]) for part in tax)
    curated = sum(1 for p in papers if p.get("topic_source") == "curated")

    name = build.load_project()["name"]

    out = []
    out.append(f"# {name} — literature review: {n_papers} papers by topic\n")
    out.append(f"> {args.date} · area: {name} · {n_papers} papers in {n_topics} "
               f"topics, each paper in exactly one\n")
    # The document must describe how ITS OWN clustering was arrived at. A first
    # clustering, a re-clustering and a consolidation are three different acts,
    # and the prose for one is FALSE about the other two.
    moved = 0
    if args.from_sidecars:
        mode = "first"
    elif args.taxonomy:
        mode = "recluster"
        orig = {p["source"]: p["topic"] for p in lib["papers"]}
        moved = sum(1 for p in papers if orig.get(p["source"]) != p["topic"])
    else:
        mode = "consolidate"
    out.append(load_prose(mode).format(
        n=n_papers, t=n_topics, parts=len(tax), moved=moved,
        reviewed=n_papers - curated, curated=curated,
        with_authors=sum(1 for p in papers if p.get("authors"))))

    # ---- Contents: the taxonomy's own checksum (build.py dies on a mismatch) ----
    out.append("## Contents\n")
    for part in tax:
        tot = sum(len(by_topic.get((part["letter"], t["name"]), [])) for t in part["topics"])
        out.append(f"**{part['letter']}. {part['name']}** — {tot} papers  ")
        for t in part["topics"]:
            n = len(by_topic.get((part["letter"], t["name"]), []))
            out.append(f"  · [{t['name']}](#{anchor(t['name'])}) ({n})  ")
        out.append("")
    out.append("---\n")

    # ---- body ----
    for part in tax:
        out.append(f"# {part['letter']}. {part['name']}\n")
        for t in part["topics"]:
            group = sorted(by_topic.get((part["letter"], t["name"]), []), key=sort_key)
            out.append(f"## {t['name']}\n")
            desc = re.sub(r"\s+", " ", t.get("description") or "").strip()
            lead = f"*{len(group)} paper{'' if len(group) == 1 else 's'}.*"
            out.append(f"{lead} {desc}\n" if desc else f"{lead}\n")
            for p in group:
                out.append(entry(p))
        out.append("")

    out.append(EPILOGUE)

    dest = Path(args.out)
    if not dest.is_absolute():
        dest = ROOT / dest
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / f"{args.date}_literature_review.md"
    path.write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8")

    print(f"make_review: wrote {path.relative_to(ROOT)}  "
          f"({path.stat().st_size / 1024:.0f} KB)")
    print(f"make_review: {n_papers} papers · {len(tax)} parts · {n_topics} topics · "
          f"{n_papers - curated} clustering(s) carried over, {curated} from "
          f"annotations/topics.json")
    if dest.name != "outputs":
        print("make_review: this is a DRAFT in reports/. Nothing reads it. Moving it "
              "into outputs/ is what makes it the taxonomy (D1) -- and under D15 that "
              "is an upstream write, so ask first.")
    return 0





EPILOGUE = """## What this document does not say

- **It does not rank or evaluate.** A paper's presence records that the team read or wrote it,
  nothing more.
- **It does not say who circulated what.** That is recorded per paper in the sidecars, and is
  deliberately not browsable.
- **It does not resolve disagreements between papers.** Two entries in one topic may contradict
  each other; the topic groups subjects, not conclusions.
- **The counts in `## Contents` are the checksum, not decoration.** `scripts/build.py` refuses to
  build if the body disagrees with them.
"""


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Self-test for build.py, against a synthetic fixture tree in a temp directory.

Why a fixture and not the real corpus: the behaviours that matter most --
`changed`, `gone`, `unfiled` -- can only be provoked by editing sidecars, and
editing the real meta/ is exactly the CLAUDE.md §2 violation the build exists to
detect. So the fixture is not a convenience, it is the only lawful way to test
these paths.

    python3 scripts/selftest.py

Standard library only. Exits non-zero on the first failed assertion.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import os
import subprocess
import sys
import tempfile
from pathlib import Path

BUILD = Path(__file__).resolve().parent / "build.py"
AREALIB = Path(__file__).resolve().parent / "paperlib.py"


def fixture_env(root: Path) -> dict:
    """Environment that pins a subprocess to the FIXTURE tree, not the real repo.

    build.py resolves its ROOT through paperlib.py, which looks for areas/ under
    the project. A fixture tree has no areas/, so without this the self-test
    either refuses to run or -- much worse -- resolves to the real collection and
    tests that instead. PAPERLIB_AREA_ROOT names the tree directly.
    """
    return {**os.environ, "PAPERLIB_AREA_ROOT": str(root)}
EDITTOOL = Path(__file__).resolve().parent / "edit_upstream.py"

PART_DEFS = [
    ("A", "Fixture foundations", [("Fixture topic one", 2), ("Fixture topic two", 1)]),
    ("B", "Fixture applications", [("Fixture topic three", 1)]),
]


def sidecar(source: str, *, typ="paper", year=2025, doi=None, prov=None,
            dup_area=None, body_extra="") -> str:
    sha = hashlib.sha256(source.encode()).hexdigest()
    doi_line = f'doi: "{doi}"\n' if doi else ""
    dup_line = f"duplicate_of_area: {dup_area}\n" if dup_area else ""
    if prov is None:
        prov_fm = ("circulated by Fixture Colleague in the BioAI/MoDaS Webex literature "
                   "thread, 2025-03-04; matched to the message by an exact DOI match")
        prov_body = ("- **Fixture Colleague**, 2025-03-04 09:10 — "
                     "[link](https://example.invalid/x)\n"
                     "  <!-- join: publisher article ID is the DOI suffix -->\n")
    elif prov == "untraced":
        prov_fm = ("deposited by the data owner; NOT traceable to a message in the "
                   "BioAI/MoDaS Webex literature thread")
        prov_body = "Not traceable to a message in the thread.\n"
    else:
        prov_fm, prov_body = prov
    return f"""---
# --- identity ------------------------------------------------
id: fixture_{sha[:12]}
source: {source}
sha256: {sha}
size_bytes: 1234
media: pdf

# --- ingest --------------------------------------------------
processor: 5
extraction:
  method: pymupdf
  chars: 4242

# --- classification ------------------------------------------
type: {typ}
classification: Public
{doi_line}year: {year}
{dup_line}
# --- provenance ----------------------------------------------
provenance: "{prov_fm}"
---
## Abstract

Fixture abstract for {source}.

## Summary

Fixture summary for {source}. Two sentences, so the section is non-trivial.

## Key points

- First fixture point.
- Second fixture point,
  wrapped onto a second line.

## Limitations

Fixture limitation.

## Provenance

{prov_body}{body_extra}"""


def review(entries: list[dict], date="2026-01-01") -> str:
    """entries: [{part, topic, head_author, year, venue, title, ident, type, src, also}]"""
    by = {}
    for e in entries:
        by.setdefault((e["part"], e["topic"]), []).append(e)

    toc = ["## Contents", ""]
    for letter, pname, topics in PART_DEFS:
        total = sum(len(by.get((letter, t), [])) for t, _ in topics)
        toc.append(f"**{letter}. {pname}** — {total} papers  ")
        for tname, _ in topics:
            n = len(by.get((letter, tname), []))
            anchor = tname.lower().replace(" ", "-")
            toc.append(f"  · [{tname}](#{anchor}) ({n})  ")
        toc.append("")

    out = ["# Fixture literature review", "", f"> {date} · fixture", "",
           "## How to read this", "",
           "Titles with no registered record are marked *[title from the filename; no "
           "registered record exists to check it against]* — this sentence must NOT be "
           "counted as an entry.", "", *toc, "---", ""]
    for letter, pname, topics in PART_DEFS:
        out += [f"# {letter}. {pname}", ""]
        for tname, _ in topics:
            es = by.get((letter, tname), [])
            out += [f"## {tname}", "", f"*{len(es)} papers.* Fixture description of {tname}.", ""]
            for e in es:
                label = ("  *[title from the filename; no registered record exists to "
                         "check it against]*" if e.get("filename_title") else "")
                out.append(f"### {e['author']} ({e['year']}). *{e['venue']}.* {e['title']}{label}")
                ident = e["ident"]
                also = f" · also in **{e['also']}**" if e.get("also") else ""
                out.append(f"{ident} · `{e['type']}`{also}  ")
                out.append(f"[src](<../raw/{e['src']}>)")
                out += ["", f"Fixture review summary for {e['src']}.", ""]
    out += ["---", "", "## What this document does not say", "",
            "- An epilogue heading that is not a topic and must not become one.", "",
            "## Sources", "", "- Fixture.", "", "## Related", "", "- Fixture."]
    return "\n".join(out) + "\n"


FIX = [
    dict(part="A", topic="Fixture topic one", author="Alpha, A. et al.", year=2025,
         venue="Nature", title="A fixture paper about foundations",
         ident="[doi:10.1000/aaa](https://doi.org/10.1000/aaa)", type="paper",
         src="Alpha(2025) Nature; A fixture paper about foundations.pdf"),
    dict(part="A", topic="Fixture topic one", author="Beta, B. et al.", year=2024,
         venue="arXiv", title="A fixture preprint", ident="[arXiv:2401.00001](https://arxiv.org/abs/2401.00001)",
         type="preprint", src="Beta(2024) arXiv; A fixture preprint.pdf"),
    dict(part="A", topic="Fixture topic two", author="Gamma, G. et al.", year=2023,
         venue="CVPR", title="Fixture_truncated_title_from_filen", ident="*no DOI or arXiv ID*",
         type="paper", filename_title=True,
         src="Gamma(2023) CVPR; Fixture_truncated_title_from_filen.pdf"),
    dict(part="B", topic="Fixture topic three", author="Delta, D. et al.", year=2026,
         venue="Cell", title="A fixture paper also held elsewhere",
         ident="[doi:10.1000/ddd](https://doi.org/10.1000/ddd)", type="review", also="Bioinformatics",
         src="Delta(2026) Cell; A fixture paper also held elsewhere.pdf"),
]

SIDECARS = {
    FIX[0]["src"]: dict(doi="10.1000/aaa", year=2025, typ="paper"),
    FIX[1]["src"]: dict(year=2024, typ="preprint", prov="untraced"),
    FIX[2]["src"]: dict(year=2023, typ="paper"),
    FIX[3]["src"]: dict(doi="10.1000/ddd", year=2026, typ="review", dup_area="Bioinformatics"),
    # the two non-literature artefacts, excluded by TYPE not by filename (§12)
    "LiteratureWebex_fixture.txt": dict(typ="other", year=2026),
    "shared_online_resources_fixture.md": dict(typ="synthesis", year=2026),
}

FAILURES: list[str] = []


def check(label: str, got, want) -> None:
    if got == want:
        print(f"  ok    {label}: {got!r}")
    else:
        print(f"  FAIL  {label}: got {got!r}, want {want!r}")
        FAILURES.append(label)


def build(root: Path, *args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(root / "scripts" / "build.py"), *args],
                       capture_output=True, text=True, env=fixture_env(root))
    return p.returncode, p.stdout + p.stderr


def make_tree(root: Path, entries: list[dict], sidecars: dict) -> None:
    for d in ("meta", "raw", "outputs", "data", "reports", "scripts"):
        (root / d).mkdir(parents=True, exist_ok=True)
    shutil.copy(BUILD, root / "scripts" / "build.py")
    # edit_upstream.py resolves ROOT from its own location, so copying it in is
    # what makes it operate on the FIXTURE rather than on the real repository.
    shutil.copy(EDITTOOL, root / "scripts" / "edit_upstream.py")
    # Both copied scripts import paperlib to resolve ROOT, so it has to be beside
    # them: sys.path[0] is the fixture's own scripts/, not the real one.
    shutil.copy(AREALIB, root / "scripts" / "paperlib.py")
    (root / "outputs" / "2026-01-01_literature_review.md").write_text(
        review(entries), encoding="utf-8")
    for src, kw in sidecars.items():
        (root / "meta" / f"{src}.md").write_text(sidecar(src, **kw), encoding="utf-8")
        (root / "raw" / src).write_bytes(b"fixture bytes")


def by9x(lib: dict, src: str) -> dict:
    return {p["source"]: p for p in lib["papers"]}[src]


def manifest(root: Path) -> dict:
    return json.loads((root / "data" / "manifest.json").read_text(encoding="utf-8"))


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="tlb-selftest-") as td:
        root = Path(td)
        make_tree(root, FIX, dict(SIDECARS))

        print("\n[1] first build on a clean tree")
        rc, out = build(root)
        check("exit code", rc, 0)
        m = manifest(root)
        c = m["counts"]
        check("papers", c["papers"], 4)
        check("non_literature (excluded by type)", c["non_literature"], 2)
        check("parts", c["parts"], 2)
        check("topics", c["topics"], 3)
        check("titles registered", c["title_registered"], 3)
        check("titles from filename", c["title_from_filename"], 1)
        check("with_doi", c["with_doi"], 2)
        check("with_arxiv", c["with_arxiv"], 1)
        check("traceable", c["traceable"], 3)
        check("untraceable", c["untraceable"], 1)
        check("also_in_topic_area", c["also_in_topic_area"], 1)
        check("new on first build", len(m["diff"]["new"]), 6)
        check("unfiled", m["diff"]["unfiled"], [])
        lib = json.loads((root / "data" / "library.json").read_text(encoding="utf-8"))
        check("taxonomy topic counts", [t["count"] for p in lib["taxonomy"] for t in p["topics"]],
              [2, 1, 1])
        check("every topic has a description",
              all(t["description"] for p in lib["taxonomy"] for t in p["topics"]), True)
        byname = {p["source"]: p for p in lib["papers"]}
        g = byname[FIX[2]["src"]]
        check("filename-title flag carried to the record", g["title_from_filename"], True)
        check("filename-title label stripped from the title",
              "title from the filename" in (g["title"] or ""), False)
        check("key points parsed (incl. wrapped line)",
              len(byname[FIX[0]["src"]]["key_points"]), 2)
        check("provenance sharer parsed",
              byname[FIX[0]["src"]]["provenance"]["sharers"], ["Fixture Colleague"])
        check("join strength parsed",
              byname[FIX[0]["src"]]["provenance"]["join"], "an exact DOI match")
        check("untraced paper has no sharers",
              byname[FIX[1]["src"]]["provenance"]["sharers"], [])
        check("arxiv id joined from review", byname[FIX[1]["src"]]["arxiv"], "2401.00001")
        check("also-in badge", byname[FIX[3]["src"]]["duplicate_of_area"], "Bioinformatics")

        print("\n[2] rebuild with nothing changed -- must be idempotent")
        before = (root / "data" / "library.json").read_bytes()
        rc, out = build(root)
        check("exit code", rc, 0)
        check("library.json byte-identical on rebuild (no wall clock in it)",
              (root / "data" / "library.json").read_bytes() == before, True)
        d = manifest(root)["diff"]
        check("new/changed/gone all empty",
              (d["new"], d["changed"], d["gone"]), ([], [], []))
        check("prints '0 new'", "new 0 · changed 0 · gone 0" in out, True)

        print("\n[3] a new paper arrives WITH a review entry -- filed")
        new_src = "Epsilon(2026) Science; A newly circulated fixture paper.pdf"
        entries = FIX + [dict(part="B", topic="Fixture topic three",
                              author="Epsilon, E. et al.", year=2026, venue="Science",
                              title="A newly circulated fixture paper",
                              ident="[doi:10.1000/eee](https://doi.org/10.1000/eee)",
                              type="paper", src=new_src)]
        (root / "outputs" / "2026-02-02_literature_review.md").write_text(
            review(entries, date="2026-02-02"), encoding="utf-8")
        (root / "meta" / f"{new_src}.md").write_text(
            sidecar(new_src, doi="10.1000/eee", year=2026), encoding="utf-8")
        (root / "raw" / new_src).write_bytes(b"fixture bytes")
        rc, out = build(root)
        check("exit code", rc, 0)
        m = manifest(root)
        check("newest review chosen by filename date", m["review_file"],
              "2026-02-02_literature_review.md")
        check("data_as_of follows the newest input", m["data_as_of"] >= "2026-02-02", True)
        check("new", m["diff"]["new"], [new_src])
        check("papers", m["counts"]["papers"], 5)
        check("unfiled", m["diff"]["unfiled"], [])

        print("\n[4] a new paper arrives WITHOUT a review entry -- unfiled, never guessed")
        orphan = "Zeta(2026) bioRxiv; A paper copied in before the next review.pdf"
        (root / "meta" / f"{orphan}.md").write_text(
            sidecar(orphan, doi="10.1000/zzz", year=2026), encoding="utf-8")
        (root / "raw" / orphan).write_bytes(b"fixture bytes")
        rc, out = build(root)
        check("exit code", rc, 0)
        m = manifest(root)
        check("unfiled", m["diff"]["unfiled"], [orphan])
        check("unfiled count", m["counts"]["unfiled"], 1)
        lib = json.loads((root / "data" / "library.json").read_text(encoding="utf-8"))
        z = {p["source"]: p for p in lib["papers"]}[orphan]
        check("unfiled topic is null, not guessed", z["topic"], None)
        check("unfiled flag set", z["unfiled"], True)
        check("unfiled paper still indexed with its summary", bool(z["summary"]), True)
        check("warns about the unfiled paper", "unfiled:" in out, True)

        print("\n[5] the PDF a sidecar POINTS AT changed -- `changed`, a D0 violation")
        # Not the same event as scenario 15's authorised sidecar edit, and D15 did
        # not license this one: `sha256:` is the byte chain `make verify` checks,
        # so a different value there means the PDF behind the sidecar was
        # replaced -- which add-only forbids however it happened.
        p = root / "meta" / f"{orphan}.md"
        p.write_text(p.read_text(encoding="utf-8").replace(
            "sha256: " + hashlib.sha256(orphan.encode()).hexdigest(),
            "sha256: " + "0" * 64), encoding="utf-8")
        rc, out = build(root)
        check("exit code (changed does not fail the build)", rc, 0)
        check("changed", manifest(root)["diff"]["changed"], [orphan])
        check("shouts about it", "CHANGED:" in out, True)
        check("names a rule", ("§2" in out or "add-only" in out.lower()), True)

        print("\n[6] a source deleted by hand -- `gone`, and the build FAILS")
        (root / "meta" / f"{orphan}.md").unlink()
        rc, out = build(root)
        check("exit code", rc, 1)
        check("gone", manifest(root)["diff"]["gone"], [orphan])
        check("says why it failed", "add-only" in out.lower(), True)

        print("\n[7] a raw file missing behind its sidecar -- reported, build survives")
        (root / "raw" / new_src).unlink()
        rc, out = build(root)
        check("exit code", rc, 0)
        check("reports the unresolved source", "does not resolve in raw/" in out, True)
        lib = json.loads((root / "data" / "library.json").read_text(encoding="utf-8"))
        check("file_ok false for it",
              {p["source"]: p for p in lib["papers"]}[new_src]["file_ok"], False)

        print("\n[8] a review whose body disagrees with its Contents table -- FATAL")
        bad = review(FIX)
        bad = bad.replace("· [Fixture topic one](#fixture-topic-one) (2)",
                          "· [Fixture topic one](#fixture-topic-one) (9)")
        (root / "outputs" / "2026-03-03_literature_review.md").write_text(bad, encoding="utf-8")
        rc, out = build(root)
        check("exit code", rc, 1)
        check("names the disagreement", "disagrees with its own" in out, True)
        check("reports declared vs parsed", "declared 9, parsed 2" in out, True)

        # ---------------------------------------------------------------- #
        print("\n[9] own vs shared, from a roster -- the surname trap")
        # A fresh tree, because this scenario needs its own author lists and a
        # roster. The cases below are the ones that actually go wrong: a surname
        # is not a person, and an initial is only an identifier where the surname
        # is one too.
        root9 = root / "own"
        def e9(author, title, src, doi):
            return dict(part="A", topic="Fixture topic one", author=author, year=2025,
                        venue="Journal", title=title, type="paper", src=src,
                        ident=(f"[doi:{doi}](https://doi.org/{doi})" if doi
                               else "*no DOI or arXiv ID*"))
        entries9 = [
            e9("Byron, P. et al.", "A paper the group wrote",
               "Byron(2025) Journal; A paper the group wrote.pdf", "10.1/own1"),
            e9("Stranger, J. et al.", "A paper by a different Hopper",
               "Stranger(2025) Journal; A paper by a different Hopper.pdf", "10.1/other"),
            e9("Rinaldetti, S. et al.", "Initials only, distinctive surname",
               "Rinaldetti(2025) Journal; Initials only distinctive surname.pdf",
               "10.1/init"),
            e9("Kovacs, T. et al.", "No author list, member surname in the filename",
               "Kovacs(2025) Journal; No author list member surname.pdf", None),
            e9("Allard Dohm-Hansen, S. et al.", "A two-token surname",
               "AllardDohmHansen(2025) Journal; A two-token surname.pdf", "10.1/two"),
        ]
        sc9 = {e["src"]: {"typ": "paper", "year": e["year"],
                          "doi": (e["ident"].split("doi:")[1].split("]")[0]
                                  if "doi:" in e["ident"] else None),
                          "prov": None} for e in entries9}
        make_tree(root9, entries9, sc9)
        (root9 / "wiki").mkdir(parents=True, exist_ok=True)
        (root9 / "wiki" / "group.md").write_text(
            "## Members and past members XX\n"
            "NN, ID, Full NAME, MESR effort, contract (:project)\n"
            "01, PN, Ada BYRON, 50/50%, CDI\n"
            "05, LZ, Grace HOPPER, 100%, CDI\n"
            "17, SA, Camille ALVAREZ BLOCH, 100%, CDD:HDS2\n"
            "xx, TL, Emil KOVACS, 100%, CDD\n", encoding="utf-8")
        # Author lists arrive only through the bib cache (D2), keyed by sha256.
        shas = {}
        for src in sc9:
            fm = (root9 / "meta" / f"{src}.md").read_text(encoding="utf-8")
            shas[src] = re.search(r"^sha256:\s*(\S+)", fm, re.M).group(1)
        cache = {
            # full given name -> own
            entries9[0]["src"]: ["Ada M. Byron", "Kwame Osei"],
            # real, different people who happen to share a member's surname ->
            # NOT own. `Lu` must never be inferred from `Hopper`.
            entries9[1]["src"]: ["Jeff Hopper", "Yun Hopper", "Ping Hopper"],
            # an initial on a distinctive surname -> own; an initial on a surname
            # worn by other people in the same corpus -> NOT own
            entries9[2]["src"]: ["S. Rinaldetti", "A. Byron", "G. Hopper"],
            # the surname is TWO tokens; taking only the last would miss it
            entries9[4]["src"]: ["Camille Alvarez Bloch", "Jane Doe"],
        }
        (root9 / "data").mkdir(parents=True, exist_ok=True)
        (root9 / "data" / "bib_cache.json").write_text(json.dumps(
            {"by_sha256": {shas[src]: {"authors": a, "source": "crossref"}
                           for src, a in cache.items()}}), encoding="utf-8")
        rc, out = build(root9)
        lib9 = json.loads((root9 / "data" / "library.json").read_text(encoding="utf-8"))
        by9 = {p["source"]: p for p in lib9["papers"]}
        check("exit code", rc, 0)
        check("full given name matches", by9[entries9[0]["src"]]["own"], True)
        check("  and names the member", by9[entries9[0]["src"]]["own_members"], ["PN"])
        check("three strangers who share a member's surname are NOT own",
              by9[entries9[1]["src"]]["own"], False)
        check("a two-token surname matches its member",
              by9[entries9[4]["src"]]["own_members"], ["SA"])
        check("initial on a DISTINCTIVE surname is own",
              sorted(by9[entries9[2]["src"]]["own_members"]), ["PN"])
        check("  initial on a surname others wear is NOT own (no LZ)",
              "LZ" in by9[entries9[2]["src"]]["own_members"], False)
        check("no author list: distinctive member surname in the filename",
              by9[entries9[3]["src"]]["own"], True)
        check("  and says the basis was the filename",
              by9[entries9[3]["src"]]["own_basis"], "filename")
        check("counts", (manifest(root9)["counts"]["own"],
                         manifest(root9)["counts"]["shared"]), (4, 1))
        check("only members who appear here are shipped",
              [(g["initials"], g["papers"]) for g in lib9["group"]],
              [("PN", 2), ("SA", 1), ("TL", 1)])

        # ---------------------------------------------------------------- #
        print("\n[10] one person, one name -- and strangers left alone")
        # Same tree, with the author lists rewritten to carry the variants that
        # Crossref actually deposits for this corpus.
        cache2 = {
            entries9[0]["src"]: ["Ada M. Byron", "A. Byron", "Jeff Hopper"],
            entries9[1]["src"]: ["Ada\u00a0M Byron", "Yun Hopper", "Grace Hopper"],
            entries9[2]["src"]: ["Ada Byron", "Marina Chepeleva"],
            entries9[4]["src"]: ["Camille Alvarez Bloch"],
        }
        (root9 / "wiki" / "group.md").write_text(
            "01, PN, Ada BYRON, 50/50%, CDI\n"
            "05, LZ, Grace HOPPER, 100%, CDI\n"
            "15, MC, Maryna CHEPELEVA, 100%, CDD:CANBIO2\n"
            "17, SA, Camille ALVAREZ BLOCH, 100%, CDD:HDS2\n"
            "xx, TL, Emil KOVACS, 100%, CDD\n", encoding="utf-8")
        (root9 / "data" / "bib_cache.json").write_text(json.dumps(
            {"by_sha256": {shas[src]: {"authors": a, "source": "crossref"}
                           for src, a in cache2.items()}}), encoding="utf-8")
        rc, out = build(root9)
        lib11 = json.loads((root9 / "data" / "library.json").read_text(encoding="utf-8"))
        names = sorted({a for p in lib11["papers"] for a in (p.get("authors") or [])})
        check("exit code", rc, 0)
        check("four Byron strings became one", [n for n in names if "Byron" in n],
              ["Ada M. Byron"])
        check("  the non-breaking space is gone",
              [n for n in names if "\u00a0" in n], [])
        check("the owner-confirmed misspelling is corrected",
              [n for n in names if "Chepeleva" in n], ["Maryna Chepeleva"])
        check("  so she is credited as a co-author",
              "MC" in by9x(lib11, entries9[2]["src"])["own_members"], True)
        check("strangers sharing a member's surname are NOT merged",
              sorted(n for n in names if "Hopper" in n),
              ["Grace Hopper", "Jeff Hopper", "Yun Hopper"])
        check("  and the build says why it declined", "someone else" in out, True)
        check("reports each merge", "one person:" in out, True)
        m11 = manifest(root9)["counts"]
        check("counts the merges", m11["author_names_merged"] >= 3, True)
        check("counts the confirmed correction", m11["author_names_confirmed_fixes"], 1)

        # ---------------------------------------------------------------- #
        print("\n[11] local topic annotation -- and the review overriding it")
        # The one property that matters: an annotation can fill a topic the
        # review is silent about, and can NEVER contradict the review.
        #
        # Its own tree: by this point `root` has had a source deleted by hand on
        # purpose (scenario 6), so a build there fails and the paper under test
        # is gone.
        root11 = root / "annot"
        e_filed = dict(
            part="A", topic="Fixture topic one", author="Filed, A. et al.", year=2025,
            venue="Journal", title="A paper the review covers",
            ident="[doi:10.1/filed](https://doi.org/10.1/filed)", type="paper",
            src="Filed(2025) Journal; A paper the review covers.pdf")
        unfiled_src = "Later(2026) bioRxiv; A paper the review has not reached.pdf"
        filed_src = e_filed["src"]
        make_tree(root11, [e_filed], {
            filed_src: {"typ": "paper", "year": 2025, "doi": "10.1/filed", "prov": None},
            unfiled_src: {"typ": "paper", "year": 2026, "doi": "10.1/later", "prov": None},
        })
        (root11 / "annotations").mkdir(parents=True, exist_ok=True)
        (root11 / "annotations" / "topics.json").write_text(json.dumps({
            "parts": [{"letter": "Z", "name": "A curated part"}],
            "topics": [{"name": "A curated topic", "part": "Z",
                        "description": "declared by the annotation"}],
            "assignments": {
                unfiled_src: "A curated topic",
                # an attempt to re-file a paper the REVIEW already covers
                filed_src: "A curated topic",
            },
        }), encoding="utf-8")
        rc, out = build(root11)
        lib12 = json.loads((root11 / "data" / "library.json").read_text(encoding="utf-8"))
        by12 = {p["source"]: p for p in lib12["papers"]}
        m12 = manifest(root11)["counts"]
        check("exit code", rc, 0)
        check("the unfiled paper gets the curated topic",
              by12[unfiled_src]["topic"], "A curated topic")
        check("  labelled as curated, not as reviewed",
              by12[unfiled_src]["topic_source"], "curated")
        check("  and is no longer unfiled", by12[unfiled_src]["unfiled"], False)
        check("  and gets its part, so the map can colour it",
              by12[unfiled_src]["part_letter"], "Z")
        check("THE REVIEW WINS: a filed paper is untouched",
              (by12[filed_src]["topic"], by12[filed_src]["topic_source"]),
              ("Fixture topic one", "review"))
        check("the curated part joins the taxonomy",
              [p["letter"] for p in lib12["taxonomy"]][-1], "Z")
        check("  with the curated topic and its count",
              [(t["name"], t["count"]) for p in lib12["taxonomy"]
               if p["letter"] == "Z" for t in p["topics"]],
              [("A curated topic", 1)])
        check("counts split review from curated",
              (m12["topic_from_review"], m12["topic_curated"]), (1, 1))
        check("reports it in the build output", "CURATED HERE" in out, True)

        # ---------------------------------------------------------------- #
        print("\n[12] an assignment to a topic nobody declared -- reported")
        (root11 / "annotations" / "topics.json").write_text(json.dumps({
            "assignments": {unfiled_src: "A topic that does not exist"},
        }), encoding="utf-8")
        rc, out = build(root11)
        check("exit code (reported, not fatal)", rc, 0)
        check("names the undeclared topic",
              "neither a review topic nor declared" in out, True)
        check("and says it would be uncoloured on the map",
              "uncoloured on the map" in out, True)
        (root11 / "annotations" / "topics.json").unlink()

        # ---------------------------------------------------------------- #
        print("\n[13] no roster at all -- the switch must simply not appear")
        (root9 / "wiki" / "group.md").unlink()
        rc, out = build(root9)
        lib10 = json.loads((root9 / "data" / "library.json").read_text(encoding="utf-8"))
        check("exit code (advisory, not fatal)", rc, 0)
        check("says the roster is missing", "group.md not found" in out, True)
        check("own left null, not guessed False",
              {p["own"] for p in lib10["papers"]}, {None})
        check("no roster shipped, so the page hides the switch", lib10["group"], [])

        # ---------------------------------------------------------------- #
        print("\n[14] local BIBLIOGRAPHY annotation -- and the registrar overriding it")
        # Same three properties as [11], applied to the bibliography. The one
        # with teeth is the third: ownership is decided from co-authorship, so a
        # byline that arrives from the annotation MUST reach the ownership pass.
        # Before this existed, both of the owner's own Kovacs papers had no
        # author list at all and credited `TL` alone.
        root14 = root / "annotbib"
        e_reg = dict(
            part="A", topic="Fixture topic one", author="Registered, R. et al.",
            year=2025, venue="Journal", title="A paper the registrar knows",
            ident="[doi:10.1/reg](https://doi.org/10.1/reg)", type="paper",
            src="Registered(2025) Journal; A paper the registrar knows.pdf")
        reg_src = e_reg["src"]
        # No sidecar DOI, no review entry, no registration: the shape of the
        # nine papers this feature was built for.
        bare_src = "Bare(2025) Mathematics; A paper with no identifier at all.pdf"
        make_tree(root14, [e_reg], {
            reg_src: {"typ": "paper", "year": 2025, "doi": "10.1/reg", "prov": None},
            bare_src: {"typ": "paper", "year": 2025, "doi": None, "prov": None},
        })
        (root14 / "wiki").mkdir(parents=True, exist_ok=True)
        (root14 / "wiki" / "group.md").write_text(
            "## Members and past members XX\n"
            "NN, ID, Full NAME, MESR effort, contract (:project)\n"
            "01, PN, Ada BYRON, 50/50%, CDI\n"
            "xx, TL, Emil KOVACS, 100%, CDD\n", encoding="utf-8")
        shas14 = {}
        for src in (reg_src, bare_src):
            fm = (root14 / "meta" / f"{src}.md").read_text(encoding="utf-8")
            shas14[src] = re.search(r"^sha256:\s*(\S+)", fm, re.M).group(1)
        (root14 / "data" / "bib_cache.json").write_text(json.dumps({"by_sha256": {
            shas14[reg_src]: {"authors": ["Rita Registered", "Ann Other"],
                              "source": "crossref"},
        }}), encoding="utf-8")
        (root14 / "annotations").mkdir(parents=True, exist_ok=True)
        annot14 = {"entries": {
            shas14[bare_src]: {
                "source": bare_src,
                "doi": "10.1/from-the-pdf",
                # a roster member sits mid-byline: only a full list can find him
                "authors": ["Emil Kovacs", "Ivan Novak", "Ada M. Byron"],
                "evidence": "page 1 byline",
            },
            shas14[reg_src]: {
                "source": reg_src,
                # DISAGREES with the registration on purpose
                "authors": ["Rita Registered", "Someone Else"],
                "evidence": "page 1 byline",
            },
            "0" * 64: {"source": "Gone(2020) Nowhere; not in the corpus.pdf",
                       "authors": ["A Name"], "evidence": "page 1"},
        }}
        bibp = root14 / "annotations" / "bibliography.json"
        bibp.write_text(json.dumps(annot14), encoding="utf-8")
        rc, out = build(root14)
        lib14 = json.loads((root14 / "data" / "library.json").read_text(encoding="utf-8"))
        by14 = {p["source"]: p for p in lib14["papers"]}
        m14 = manifest(root14)["counts"]
        check("exit code (all findings reported, none fatal)", rc, 0)
        check("the bare paper gets the PDF's byline",
              by14[bare_src]["authors"],
              ["Emil Kovacs", "Ivan Novak", "Ada M. Byron"])
        check("  labelled as read from the PDF, not as registered",
              by14[bare_src]["authors_source"], "pdf-byline")
        check("  and gets a first author it did not have",
              by14[bare_src]["first_author"], "Emil Kovacs")
        check("  and the DOI the PDF prints", by14[bare_src]["doi"], "10.1/from-the-pdf")
        check("  labelled as read from the PDF", by14[bare_src]["doi_source"], "pdf")
        check("OWNERSHIP READS THE ANNOTATED BYLINE: mid-list member found",
              (by14[bare_src]["own"], by14[bare_src]["own_members"],
               by14[bare_src]["own_basis"]),
              (True, ["PN", "TL"], "author"))
        check("THE REGISTRAR WINS: registered byline kept, not replaced",
              by14[reg_src]["authors"], ["Rita Registered", "Ann Other"])
        check("  and stays labelled as the registration",
              by14[reg_src]["authors_source"], "crossref")
        check("  the disagreement is REPORTED, not applied",
              "byline disagreement" in out, True)
        check("  naming the first differing surname",
              "other vs else" in out, True)
        check("an orphan sha256 is reported", "matches no paper" in out, True)
        check("counts split registration from PDF",
              (m14["authors_from_registration"], m14["authors_from_pdf"],
               m14["doi_from_pdf"]), (1, 1, 1))
        check("  and count the cross-check separately",
              (m14["bib_annot_crosschecked"], m14["bib_annot_disagree"]), (1, 1))

        # A partial list is not a partial answer, it is a false one (D2).
        bibp.write_text(json.dumps({"entries": {
            shas14[bare_src]: {"source": bare_src, "authors": ["", ""],
                               "evidence": "page 1"},
        }}), encoding="utf-8")
        rc, out = build(root14)
        lib14b = json.loads((root14 / "data" / "library.json").read_text(encoding="utf-8"))
        by14b = {p["source"]: p for p in lib14b["papers"]}
        check("a malformed `authors` value is refused", "not a non-empty list" in out, True)
        check("  and leaves the paper with NO byline rather than a bad one",
              by14b[bare_src]["authors"], None)

        # Upstream catching up must make the file inert, not fight it.
        bibp.write_text("{ this is not json", encoding="utf-8")
        rc, out = build(root14)
        check("invalid JSON is reported, not fatal", (rc, "not valid JSON" in out),
              (0, True))
        bibp.unlink()
        rc, out = build(root14)
        lib14c = json.loads((root14 / "data" / "library.json").read_text(encoding="utf-8"))
        by14c = {p["source"]: p for p in lib14c["papers"]}
        check("with the file gone the build still works",
              (rc, by14c[bare_src]["authors"], by14c[bare_src]["doi"]),
              (0, None, None))


        # ---------------------------------------------------------------- #
        print("\n[15] D15 -- an authorised sidecar edit, and drift that nobody recorded")
        # The property: a sidecar's bytes moving is VISIBLE, and the build can
        # tell our edit from a change nobody recorded. Before D15 neither was
        # true -- the manifest hashed the PDF a sidecar POINTS AT, so editing a
        # sidecar was invisible, and .gitignore claimed otherwise.
        root15 = root / "d15"
        e15 = dict(part="A", topic="Fixture topic one", author="Filed, A. et al.",
                   year=2025, venue="Journal", title="A filed paper",
                   ident="[doi:10.1/filed15](https://doi.org/10.1/filed15)",
                   type="paper", src="Filed(2025) Journal; A filed paper.pdf")
        tgt = "Bare(2025) Mathematics; A paper with no doi.pdf"
        make_tree(root15, [e15], {
            e15["src"]: {"typ": "paper", "year": 2025, "doi": "10.1/filed15",
                         "prov": None},
            tgt: {"typ": "paper", "year": 2025, "doi": None, "prov": None},
        })
        rc, out = build(root15)
        check("baseline builds", rc, 0)
        base = manifest(root15)
        check("the manifest now hashes each SIDECAR's own bytes",
              sorted(base["sidecars"]), sorted([e15["src"], tgt]))
        side_path = root15 / "meta" / f"{tgt}.md"
        pristine = side_path.read_text(encoding="utf-8")

        # (a) an edit with a ledger entry -> ours, and the authors are READ
        edited = pristine.replace(
            "year: 2025",
            'year: 2025\ndoi: "10.9/written-here"\nauthors:\n'
            '  - "Emil Kovacs"\n  - "Ada M. Byron"')
        side_path.write_text(edited, encoding="utf-8")
        import hashlib as _h
        after_sha = _h.sha256(edited.encode()).hexdigest()
        (root15 / "annotations").mkdir(parents=True, exist_ok=True)
        ledger_p = root15 / "annotations" / "upstream_edits.json"
        ledger_p.write_text(json.dumps({"edits": [{
            "seq": 1, "date": "2026-09-03", "file": f"meta/{tgt}.md",
            "keys": ["doi", "authors"],
            "after": {"doi": "10.9/written-here",
                      "authors": ["Emil Kovacs", "Ada M. Byron"]},
            "approved": "owner, fixture", "evidence": "page 1",
            "sha256_before": _h.sha256(pristine.encode()).hexdigest(),
            "sha256_after": after_sha,
        }]}), encoding="utf-8")
        (root15 / "wiki").mkdir(parents=True, exist_ok=True)
        (root15 / "wiki" / "group.md").write_text(
            "## Members and past members XX\n"
            "NN, ID, Full NAME, MESR effort, contract (:project)\n"
            "01, PN, Ada BYRON, 50/50%, CDI\n", encoding="utf-8")
        rc, out = build(root15)
        lib15 = json.loads((root15 / "data" / "library.json").read_text(encoding="utf-8"))
        by15 = {p["source"]: p for p in lib15["papers"]}
        check("exit code (an authorised edit is not a failure)", rc, 0)
        check("the edit is recognised as OURS",
              manifest(root15)["diff"]["sidecars_edited_here"], [tgt])
        check("  and nothing is reported as unexplained",
              manifest(root15)["diff"]["sidecars_changed_not_ours"], [])
        check("  it says so in the build output", "accounted for in" in out, True)
        check("the sidecar's doi is now read", by15[tgt]["doi"], "10.9/written-here")
        check("the sidecar's AUTHORS list is now parsed (it never could be before)",
              by15[tgt]["authors"], ["Emil Kovacs", "Ada M. Byron"])
        check("  and is labelled as OURS, not as upstream's",
              by15[tgt]["authors_source"], "sidecar-written-here")
        check("  so ownership can find the member in it",
              (by15[tgt]["own"], by15[tgt]["own_members"]), (True, ["PN"]))

        # (a2) D16: a registration appears LATER for a paper whose sidecar we
        # already gave a byline. The registration wins and the mismatch is
        # reported -- unreachable in real data today (the five sidecars with
        # `authors:` have no DOI between them), which is exactly why it needs a
        # fixture before the field became standing policy.
        (root15 / "data" / "bib_cache.json").write_text(json.dumps({"by_sha256": {
            hashlib.sha256(tgt.encode()).hexdigest(): {
                "authors": ["Emil Kovacs", "Ivan V. Novak", "Ada M. Byron"],
                "source": "crossref"},
        }}), encoding="utf-8")
        rc, out = build(root15)
        lib15b = json.loads((root15 / "data" / "library.json").read_text(encoding="utf-8"))
        by15b = {p["source"]: p for p in lib15b["papers"]}
        check("a later registration OUTRANKS the sidecar byline",
              (by15b[tgt]["authors"], by15b[tgt]["authors_source"]),
              (["Emil Kovacs", "Ivan V. Novak", "Ada M. Byron"], "crossref"))
        check("  and the disagreement is reported, not applied",
              "byline disagreement" in out, True)
        check("  saying we wrote the sidecar field, so a reading is wrong",
              "WE wrote that sidecar field" in out, True)
        check("  and naming where they diverge", "novak vs byron" in out, True)
        (root15 / "data" / "bib_cache.json").write_text(
            json.dumps({"by_sha256": {}}), encoding="utf-8")

        # (b) the same bytes moving with NO ledger entry -> loud
        # NOT the title or `source:` -- those are the join key, so changing one
        # reads as a rename (new + gone), which is a different event and fails
        # the build under add-only. `size_bytes` is what a re-export would move.
        side_path.write_text(edited.replace("size_bytes: 1234", "size_bytes: 9999"),
                             encoding="utf-8")
        rc, out = build(root15)
        check("an unrecorded change is reported", "NOT BY US" in out, True)
        check("  and listed in the manifest",
              manifest(root15)["diff"]["sidecars_changed_not_ours"], [tgt])
        check("  but does not fail the build (only a person can judge it)", rc, 0)

        # (c) our edit reverted by hand -> also loud, the other direction
        side_path.write_text(pristine, encoding="utf-8")
        rc, out = build(root15)
        check("a ledger entry whose file moved on is reported",
              "OUR EDIT IS GONE" in out, True)
        check("  and named in the manifest",
              manifest(root15)["diff"]["sidecars_no_longer_as_we_left_them"], [tgt])

        # ---------------------------------------------------------------- #
        print("\n[16] edit_upstream.py -- CRLF preserved, and what it refuses")
        # The CRLF check is here because the bug was real and shipped once: the
        # first version used read_text()/write_text(), whose universal-newline
        # handling rewrote all 64 line endings of every sidecar it touched. git
        # showed "663 insertions, 590 deletions" for 9 added fields -- a
        # whole-file reformat of upstream's bytes wearing an edit's clothes. The
        # 9 files were reverted from the baseline commit and the tool fixed.
        root16 = root / "edittool"
        e16 = dict(part="A", topic="Fixture topic one", author="Filed, A. et al.",
                   year=2025, venue="Journal", title="A filed paper",
                   ident="[doi:10.1/f16](https://doi.org/10.1/f16)", type="paper",
                   src="Filed(2025) Journal; A filed paper.pdf")
        t16 = "Crlf(2025) Mathematics; A sidecar with CRLF endings.pdf"
        make_tree(root16, [e16], {
            e16["src"]: {"typ": "paper", "year": 2025, "doi": "10.1/f16", "prov": None},
            t16: {"typ": "paper", "year": 2025, "doi": None, "prov": None},
        })
        side16 = root16 / "meta" / f"{t16}.md"
        # rewrite the fixture with CRLF, as KBase actually ships them
        side16.write_bytes(side16.read_bytes().replace(b"\n", b"\r\n"))
        pristine16 = side16.read_bytes()
        check("fixture really is CRLF",
              (pristine16.count(b"\r\n") > 0,
               pristine16.count(b"\n") - pristine16.count(b"\r\n")),
              (True, 0))

        planp = root16 / "plan.json"
        planp.write_text(json.dumps({
            "approved": "owner, fixture: yes",
            "edits": [{"file": f"meta/{t16}.md",
                       "set": {"doi": "10.9/read-off-the-pdf"},
                       "set_list": {"authors": ["A. One", "B. Two"]},
                       "reason": "fixture", "evidence": "page 1"}],
        }), encoding="utf-8")

        def edit16(*extra):
            r = subprocess.run(
                [sys.executable, str(root16 / "scripts" / "edit_upstream.py"),
                 "--plan", str(planp), *extra],
                capture_output=True, text=True, env=fixture_env(root16))
            return r.returncode, r.stdout + r.stderr

        rc, out = edit16()
        check("DRY RUN writes nothing at all", side16.read_bytes(), pristine16)
        check("  and says so", "nothing was written" in out, True)
        check("  and reports the line ending it found", "CRLF" in out, True)

        rc, out = edit16("--apply")
        after16 = side16.read_bytes()
        check("APPLY preserves CRLF exactly",
              (after16.count(b"\r\n") > 0,
               after16.count(b"\n") - after16.count(b"\r\n")),
              (True, 0))
        check("  and only ADDS lines",
              after16.count(b"\r\n") - pristine16.count(b"\r\n"), 4)
        check("  the fields land WITH the bibliographic ones, not in provenance",
              after16.split(b"provenance:")[0].count(b'doi: "10.9/read-off-the-pdf"'),
              1)
        check("  every pristine line survives",
              all(l in after16.split(b"\r\n") for l in pristine16.split(b"\r\n")),
              True)
        led16 = json.loads((root16 / "annotations" / "upstream_edits.json")
                           .read_text(encoding="utf-8"))
        check("  the ledger records it with the approval",
              (len(led16["edits"]), led16["edits"][0]["approved"]),
              (1, "owner, fixture: yes"))
        check("  and the hash it records is the file as written",
              led16["edits"][0]["sha256_after"],
              hashlib.sha256(after16).hexdigest())
        check("  re-running is a no-op, not a second edit",
              (edit16("--apply")[1].count("nothing to do"), side16.read_bytes()),
              (1, after16))

        # --- the refusals ---
        def refuse16(spec, *extra):
            planp.write_text(json.dumps(
                {"approved": "owner, fixture: yes", "edits": [spec]}), encoding="utf-8")
            return edit16("--apply", *extra)[1]

        # A name containing a double quote. Real: `Xuhai "Orson" Xu` on the
        # Heydari paper. quote() escaped it and the readers did not un-escape,
        # so the value read back as `Xuhai \\"Orson\\" Xu` -- visible backslashes
        # on the page, AND a value that failed its own round-trip, so re-running
        # the same plan reported a conflicting overwrite on a field we had just
        # written ourselves.
        nick = 'Xuhai "Orson" Xu'
        planp.write_text(json.dumps({
            "approved": "owner, fixture: yes",
            "edits": [{"file": f"meta/{t16}.md", "set_list": {"authors": [nick]},
                       "reason": "fixture", "evidence": "page 1"}],
        }), encoding="utf-8")
        edit16("--apply", "--allow-overwrite")
        rc, out = build(root16)
        lib16 = json.loads((root16 / "data" / "library.json").read_text(encoding="utf-8"))
        check("a name with a double quote survives the write/read round trip",
              {p["source"]: p for p in lib16["papers"]}[t16]["authors"], [nick])
        check("  and re-running that edit is a no-op, not a conflict",
              "nothing to do" in edit16("--apply", "--allow-overwrite")[1], True)
        planp.write_text(json.dumps({
            "approved": "owner, fixture: yes",
            "edits": [{"file": f"meta/{t16}.md",
                       "set": {"doi": "10.9/read-off-the-pdf"},
                       "set_list": {"authors": ["A. One", "B. Two"]},
                       "reason": "fixture", "evidence": "page 1"}],
        }), encoding="utf-8")
        edit16("--apply", "--allow-overwrite")

        check("raw/ is refused by name, D15 or not",
              "raw/ holds publisher PDFs" in refuse16(
                  {"file": f"raw/{t16}", "set": {"doi": "10.9/x"}}), True)
        check("a directory outside D15's scope is refused",
              "not one of" in refuse16({"file": "src/app.js", "set": {"doi": "10.9/x"}}),
              True)
        for key in ("sha256", "source", "id"):
            check(f"the identity field {key!r} is refused",
                  "identifies the record" in refuse16(
                      {"file": f"meta/{t16}.md", "set": {key: "tampered"}}), True)
        # `classification`, because the fixture actually carries it -- setting a
        # field the file does NOT have is an addition, which is the permitted act.
        check("overwriting a field upstream filled in is refused by default",
              "different acts" in refuse16(
                  {"file": f"meta/{t16}.md",
                   "set": {"classification": "Internal"}}), True)
        check("  the value is untouched by that refusal",
              b'classification: Public' in side16.read_bytes(), True)
        check("  and permitted only with --allow-overwrite",
              "different acts" in refuse16(
                  {"file": f"meta/{t16}.md", "set": {"classification": "Internal"}},
                  "--allow-overwrite"), False)
        check("  which then really does change it",
              b'classification: "Internal"' in side16.read_bytes(), True)
        check("  and is recorded with the value it replaced",
              [(e["keys"], e["before"]) for e in json.loads(
                  (root16 / "annotations" / "upstream_edits.json")
                  .read_text(encoding="utf-8"))["edits"]][-1],
              (["classification"], {"classification": "Public"}))

        planp.write_text(json.dumps({"edits": []}), encoding="utf-8")
        rc, out = edit16("--apply")
        check("a plan with no recorded approval cannot run at all",
              (rc, "always ask" in out or "asking the owner" in out), (2, True))

    print()
    if FAILURES:
        print(f"selftest: {len(FAILURES)} FAILURE(S): " + ", ".join(FAILURES))
        return 1
    print("selftest: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

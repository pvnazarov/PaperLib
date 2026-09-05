#!/usr/bin/env python3
"""Write a small synthetic collection into raw/ + meta/, so the pipeline can be
run end to end before any real paper exists.

    python3 scripts/make_example.py            # dry run: says what it would write
    python3 scripts/make_example.py --apply

WHY: every other script in here assumes a collection. A new instance of this
toolkit has none, so the first honest question -- "does any of this work?" --
cannot be answered without inventing one. This invents one: 12 papers, 6 topics,
3 parts, with vocabularies distinct enough that the similarity map is meaningful
rather than a single blob.

WHAT IT DOES NOT PROVE: `make inbox`. Ingestion refuses any paper whose DOI is
not registered at Crossref, and a synthetic paper is registered nowhere -- by
design, since that check is what stops a typo becoming a citation. So the example
starts one step downstream, at sidecars that already exist, and the ingest path is
exercised the first time real papers are dropped in `inbox/`.

It REFUSES to write into a collection that already holds anything. Removing the
example again is `rm` on the twelve names it prints -- they all begin `Example`.

Standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paperlib  # noqa: E402

# PAPERLIB: ROOT is the AREA being worked on (scripts/paperlib.py).
ROOT = paperlib.resolve_root()
RAW, META, ANNOT = ROOT / "raw", ROOT / "meta", ROOT / "annotations"

# (surname, year, venue, title, topic, part_letter, keywords, authors)
# The keywords are what the source text is built from, and they are deliberately
# separated by topic: a map whose points all sit on top of each other teaches a
# reader nothing about whether the map works.
PAPERS = [
    ("Alvarez", 2024, "Journal of Example Methods",
     "Distributional models of meaning in small annotated corpora",
     "Distributional semantics", "A",
     "distributional semantics word vectors cosine similarity corpus token "
     "embedding lexical co-occurrence window frequency",
     ["Rosa Alvarez", "Ken Ito", "Mira Osei"]),
    ("Bianchi", 2023, "Journal of Example Methods",
     "Contextual embeddings compared with count-based vectors",
     "Distributional semantics", "A",
     "contextual embedding count vector comparison lexical semantics cosine "
     "corpus token frequency window similarity benchmark",
     ["Luca Bianchi", "Rosa Alvarez"]),
    ("Chowdhury", 2025, "Example Review of Linguistics",
     "What annotation guidelines do and do not fix",
     "Annotation and corpora", "A",
     "annotation guideline inter-annotator agreement kappa corpus construction "
     "labelling disagreement adjudication schema",
     ["Nadia Chowdhury"]),
    ("Delgado", 2022, "Example Review of Linguistics",
     "Building a balanced corpus without a balanced population",
     "Annotation and corpora", "A",
     "corpus balance sampling register genre representativeness annotation "
     "metadata documentation collection design",
     ["Pilar Delgado", "Nadia Chowdhury", "Ken Ito"]),

    ("Eriksson", 2024, "Example Transactions on Sensing",
     "Low-cost sensor networks in urban field deployments",
     "Sensor networks", "B",
     "sensor network deployment node battery telemetry urban field measurement "
     "packet loss gateway humidity temperature",
     ["Anders Eriksson", "Wei Sun"]),
    ("Farah", 2025, "Example Transactions on Sensing",
     "Node failure and gap-filling in long field campaigns",
     "Sensor networks", "B",
     "node failure gap filling imputation field campaign telemetry sensor "
     "downtime network maintenance deployment",
     ["Layla Farah", "Anders Eriksson"]),
    ("Grigoryan", 2023, "Example Journal of Instrumentation",
     "Drift correction for inexpensive gas sensors",
     "Calibration and drift", "B",
     "calibration drift reference instrument co-location gas sensor correction "
     "baseline response temperature dependence recalibration",
     ["Ani Grigoryan"]),
    ("Haddad", 2026, "Example Journal of Instrumentation",
     "How often does a field instrument need recalibrating?",
     "Calibration and drift", "B",
     "recalibration interval drift rate reference instrument calibration "
     "schedule field instrument accuracy bias correction",
     ["Omar Haddad", "Ani Grigoryan", "Wei Sun"]),

    ("Ivanova", 2024, "Example Statistical Review",
     "Reporting uncertainty when the model is the least of your problems",
     "Uncertainty quantification", "C",
     "uncertainty interval coverage propagation measurement error bootstrap "
     "confidence prediction interval calibration of probabilities",
     ["Nina Ivanova", "Tomas Klein"]),
    ("Klein", 2022, "Example Statistical Review",
     "Interval coverage under misspecification",
     "Uncertainty quantification", "C",
     "coverage misspecification interval bootstrap simulation nominal level "
     "confidence estimator bias variance",
     ["Tomas Klein"]),
    ("Lindqvist", 2025, "Example Journal of Research Practice",
     "What a reproduction package has to contain to be usable",
     "Reproducibility", "C",
     "reproduction package code data availability environment pinning container "
     "reproducibility replication archive documentation",
     ["Sara Lindqvist", "Nina Ivanova"]),
    ("Mbeki", 2026, "Example Journal of Research Practice",
     "Reanalysis without the original analyst",
     "Reproducibility", "C",
     "reanalysis independent replication archive code availability documentation "
     "provenance audit trail reproducibility",
     ["Thabo Mbeki-Ndlovu", "Sara Lindqvist"]),
]

PARTS = [
    ("A", "Language and corpora"),
    ("B", "Field measurement"),
    ("C", "Statistical and research practice"),
]

TOPIC_DESC = {
    "Distributional semantics":
        "Meaning represented as position in a vector space, and what that does and "
        "does not capture.",
    "Annotation and corpora":
        "How a collection of text is assembled, labelled and documented, and where "
        "those choices leak into results.",
    "Sensor networks":
        "Deployments of many cheap instruments, and the failure modes that come with "
        "the count rather than the instrument.",
    "Calibration and drift":
        "Keeping an instrument's readings tied to a reference over time.",
    "Uncertainty quantification":
        "Saying how wrong a number might be, in a form somebody else can use.",
    "Reproducibility":
        "What has to travel with a result for another person to obtain it again.",
}


def source_text(p) -> str:
    """The `raw/` file. Plain text, not PDF: this exists so the sha256 and the byte
    count are real and so the `[src]` link resolves to something. Nothing in the
    pipeline parses it -- the prose in the sidecar is what is read."""
    sur, year, venue, title, topic, part, kw, authors = p
    return (
        f"{title}\n{', '.join(authors)}\n{venue}, {year}\n\n"
        f"THIS IS A SYNTHETIC EXAMPLE FILE written by scripts/make_example.py.\n"
        f"It is not a paper. It exists so that the collection has real bytes to hash\n"
        f"and a real file to link to while the pipeline is being tried out.\n\n"
        f"Keywords: {kw}\n"
    )


def sidecar(p, src_name: str, sha: str, size: int) -> str:
    sur, year, venue, title, topic, part, kw, authors = p
    alist = "\n".join(f"  - {a}" for a in authors)
    words = kw.split()
    # Two different sentences out of the same words, so Abstract and Summary are
    # not identical text, and so the shared scaffolding is a small fraction of
    # each record rather than most of it.
    kw_sentence = (f"Concerns {' '.join(words[:4])}, and the relation between "
                   f"{' '.join(words[4:7])} and {' '.join(words[7:10])}.")
    kw_para = (f"Discusses {', '.join(words[:6])}. Treats {' '.join(words[6:11])} "
               f"as the central difficulty, and reports on "
               f"{' '.join(words[11:])} as well.")
    return f"""---
# --- identity ------------------------------------------------
id: {year}-01-01_example-{sur.lower()}-{year}
id_basis: example
source: {src_name}
sha256: {sha}
size_bytes: {size}
media: txt

# --- ingest --------------------------------------------------
processed: '{year}-01-01'
processor: make_example.py
status: ok

# --- classification ------------------------------------------
type: paper
classification: Public
classification_basis: "synthetic example, not a real document"

# --- bibliographic -------------------------------------------
year: {year}
title: "{title}"
venue: "{venue}"
authors:
{alist}

# --- provenance ----------------------------------------------
provenance: "synthetic example written by scripts/make_example.py; NOT traceable to any source"
---
## Abstract

{kw_sentence} The record is synthetic — see Provenance — and its wording is chosen so that
papers on one topic share vocabulary with each other and not with the rest.

## Summary

{title}. {kw_para}

This record is not a paper and makes no claim about the world. It exists so that the build,
the map and the browser have something with the shape of a real record: a title, a byline, a
year, a venue, prose of a realistic length, and a source file in `raw/` with a real sha256.
Delete the twelve `Example…` files from `raw/` and `meta/` once real papers are in place.

## Key points

- Synthetic. Written by `scripts/make_example.py`, not read off any document.
- Topic: {topic}, in part {part}.
- Keywords: {kw}.
- Present so that `make build`, `make embed`, `make render` have something to work on.

## Limitations

- It is not evidence of anything. Nothing here was measured, read or reviewed.
- The similarity map built from twelve records is a demonstration of the mechanism, not
  a meaningful picture of a field.

## Provenance

Synthetic. Written by `scripts/make_example.py`. **NOT traceable** to any source.

## Citation

{sur} et al. {venue}. {year}. {title}. (synthetic example, no DOI)
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean", action="store_true",
                    help="remove exactly the files this script generates, and the "
                         "generated taxonomy/bibliography if they are still the "
                         "generated ones")
    ap.add_argument("--apply", action="store_true", help="write the files")
    args = ap.parse_args()

    # Dotfiles do not count as content. A freshly unpacked archive ships a
    # `.gitkeep` in every directory the pipeline expects to exist, and treating
    # those as a collection made this script refuse on the very first command of
    # the runbook -- found by unpacking the archive and following it.
    def real(d: Path, pat: str) -> list:
        return [p for p in d.glob(pat)
                if p.is_file() and not p.name.startswith(".")] if d.is_dir() else []

    existing_raw = real(RAW, "*")
    existing_meta = real(META, "*.md")
    # --clean is the one mode that NEEDS a non-empty collection: it removes what a
    # previous run wrote. The guard below protects against WRITING an example into
    # a real collection, which is the opposite operation.
    if (existing_raw or existing_meta) and not args.clean:
        print(f"make_example: REFUSED. raw/ holds {len(existing_raw)} file(s) and meta/ "
              f"{len(existing_meta)} sidecar(s). This writes an EXAMPLE collection and "
              f"must never be mixed into a real one.", file=sys.stderr)
        return 1

    plan = []
    for p in PAPERS:
        sur, year, venue, title, topic, part, kw, authors = p
        src_name = f"{sur}({year}) {venue}; {title}.txt"
        body = source_text(p).encode("utf-8")
        plan.append((p, src_name, body, hashlib.sha256(body).hexdigest()))

    tax = {
        "_comment": "Written by scripts/make_example.py. The shape a real taxonomy takes.",
        "parts": [{"letter": l, "name": n} for l, n in PARTS],
        "topics": [
            {"name": t, "part": next(p[5] for p in PAPERS if p[4] == t),
             "part_name": dict(PARTS)[next(p[5] for p in PAPERS if p[4] == t)],
             "description": TOPIC_DESC[t]}
            for t in dict.fromkeys(p[4] for p in PAPERS)
        ],
        "assignments": {src: p[4] for p, src, _, _ in plan},
    }

    # `make audit` requires that a paper with no DOI has been LOOKED AT -- an entry
    # in annotations/bibliography.json recording that the document itself prints no
    # identifier. These twelve genuinely have none, so the entry is true, and
    # writing it is what makes `make audit` pass on a fresh collection instead of
    # greeting a new operator with twelve red lines that are not their fault. The
    # rule is not weakened: it still demands the check, and the check is recorded.
    bib = {
        "_about": [
            "Written by scripts/make_example.py for the synthetic example collection.",
            "Each entry records that the document prints no identifier -- which is",
            "true: these are text files, not publications. Delete this file along",
            "with the Example* files.",
        ],
        # `evidence` is required by `make audit`, and rightly: a bibliographic
        # claim with no stated source is not a record. For these the evidence is
        # that the file was generated with a known byline and no identifier.
        "entries": {sha: {
            "source": src, "doi": None, "authors": list(p[7]),
            "evidence": ("synthetic example generated by scripts/make_example.py; "
                         "the byline is in the file's first two lines and the file "
                         "carries no DOI or arXiv ID because it is not a publication"),
        } for p, src, _, sha in plan},
    }

    # PAPERLIB: removing the example has to be driven by the GENERATOR, because
    # only it knows what it wrote. Upstream's documented cleanup was
    # `rm raw/Example*`, which removes nothing: the synthetic filenames start with
    # the author's surname and carry "Example" inside the VENUE
    # (`Alvarez(2024) Journal of Example Methods; ...`). Reported in
    # docs/PROVENANCE.md rather than left as a shell glob that silently no-ops and
    # leaves 12 synthetic papers in a real collection.
    if args.clean:
        removed = 0
        for _, src, _, _ in plan:
            for f in (RAW / src, META / f"{src}.md"):
                if f.exists():
                    if args.apply:
                        f.unlink()
                    removed += 1
                    print(f"  {'removed' if args.apply else 'would remove'} "
                          f"{f.relative_to(ROOT)}")
        for f in (ANNOT / "taxonomy.json", ANNOT / "bibliography.json"):
            # Only if it is still the generated one: a hand-written taxonomy must
            # never be deleted by a cleanup aimed at synthetic data.
            # Both generated files name this script in their own text —
            # taxonomy.json in its `_comment`, bibliography.json in each
            # `evidence`. That is the marker; matching only bibliography.json's
            # longer phrase left taxonomy.json behind, and a stale taxonomy is
            # exactly the thing a real collection must not inherit.
            if f.exists() and "scripts/make_example.py" in f.read_text(
                    encoding="utf-8", errors="replace"):
                if args.apply:
                    f.unlink()
                removed += 1
                print(f"  {'removed' if args.apply else 'would remove'} "
                      f"{f.relative_to(ROOT)}")
            elif f.exists():
                print(f"  KEPT {f.relative_to(ROOT)} — not the generated one")
        print(f"make_example: {removed} example file(s) "
              f"{'removed' if args.apply else 'would be removed'}"
              f"{'' if args.apply else '; re-run with --apply'}")
        return 0

    if not args.apply:
        print(f"make_example: DRY RUN — would write {len(plan)} source files to raw/, "
              f"{len(plan)} sidecars to meta/, annotations/taxonomy.json "
              f"({len(tax['parts'])} parts, {len(tax['topics'])} topics) and "
              f"annotations/bibliography.json ({len(plan)} 'no identifier' entries).")
        for _, src, body, _ in plan:
            print(f"  raw/{src}  ({len(body)} bytes)")
        print("make_example: nothing written. Re-run with --apply.")
        return 0

    RAW.mkdir(exist_ok=True)
    META.mkdir(exist_ok=True)
    ANNOT.mkdir(exist_ok=True)
    for p, src, body, sha in plan:
        (RAW / src).write_bytes(body)
        (META / f"{src}.md").write_text(
            sidecar(p, src, sha, len(body)), encoding="utf-8")
    (ANNOT / "taxonomy.json").write_text(
        json.dumps(tax, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ANNOT / "bibliography.json").write_text(
        json.dumps(bib, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"make_example: wrote {len(plan)} sources, {len(plan)} sidecars, "
          f"annotations/taxonomy.json and annotations/bibliography.json")
    print("\nNext, in order:")
    print("  python3 scripts/make_review.py --from-sidecars \\")
    print("      --taxonomy annotations/taxonomy.json --out outputs")
    print("  make build && make render        # a browsable page, no numpy needed")
    print("  make venv && make embed && make render   # adds the similarity map")
    return 0


if __name__ == "__main__":
    sys.exit(main())

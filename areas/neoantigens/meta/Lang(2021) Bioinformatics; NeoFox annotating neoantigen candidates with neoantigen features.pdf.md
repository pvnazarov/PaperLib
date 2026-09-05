---
# --- identity ------------------------------------------------
id: 2021-01-01_lang-2021-bioinformatics-neofox-annotati
id_basis: filename-year
source: Lang(2021) Bioinformatics; NeoFox annotating neoantigen candidates with neoantigen features.pdf
sha256: e33ba6adddc751cfca74d73f42fe1e1dd16c429cdde1888bd76a5952b2be72f9
size_bytes: 341067
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 16283

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btab344"
year: 2021
title: "NeoFox: annotating neoantigen candidates with neoantigen features"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as btab344.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoFox is an open-source Python package that annotates neoantigen candidates with 16 neoantigen features gathered from the literature, bringing scattered published metrics into one toolbox.

## Summary

The contribution is consolidation rather than a new predictor. Published neoantigen features - differential agretopicity, dissimilarity to self, expression, clonality, hydrophobicity and the rest - live in separate papers with separate implementations, and reproducing them all is a substantial effort before any ranking can even be attempted.

Having them computed uniformly in one place is what makes comparing or combining them tractable, and makes a ranking reproducible by someone else.

## Key points

- 16 published neoantigen features in a single package with consistent implementations.
- Open source under GPL v3, so the feature definitions are inspectable rather than described.
- Annotates candidates rather than ranking them - the judgement stays with the user.
- Makes cross-study comparison of feature-based rankings practical.

## Limitations

A feature toolbox does not say which features to trust, and this collection contains direct evidence that several of them generalise poorly - Wan (2024) found optimal features differ substantially between datasets. Uniform implementation can also diverge subtly from each feature's original definition, so a NeoFox value and a published value are not guaranteed identical. It computes; it does not validate.

## Provenance

Located in the published literature, dropped into `inbox/` as `btab344.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btab344`; the prose sections were written here from the paper itself.

## Citation

Lang et al. Bioinformatics 2021. NeoFox: annotating neoantigen candidates with neoantigen features. doi: 10.1093/bioinformatics/btab344

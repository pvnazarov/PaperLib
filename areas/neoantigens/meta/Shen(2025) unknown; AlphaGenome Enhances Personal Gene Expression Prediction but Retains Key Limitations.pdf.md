---
# --- identity ------------------------------------------------
id: 2025-01-01_shen-2025-unknown-alphagenome-enhances-p
id_basis: filename-year
source: Shen(2025) unknown; AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations.pdf
sha256: 5620b8f724ee4b987ce6ecb52ebe4c6543dbe2851bb09428f273df86b402da2d
size_bytes: 5051234
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 32393

# --- classification (LIH WI DC-909) --------------------------
type: preprint
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1101/2025.08.05.668750"
year: 2025
title: "AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025.08.05.668750v1.full.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

An evaluation of AlphaGenome for predicting individual-specific gene expression, comparing it against Enformer, Elastic Net and Random Forest on GTEx data. It improves prediction of expression direction over Enformer with an odds ratio of 3.0 and in some cases reverses previously negative correlations to positive, while retaining key limitations.

## Summary

Genome AI models have been criticised for poor accuracy on personal, individual-specific expression even while excelling at general sequence-to-function tasks, and this asks whether the current state of the art has closed that gap.

It is in this collection because expression is a filter in every neoantigen pipeline - a mutation in an unexpressed gene yields nothing - and the Ma (2026) paper here argues transcript abundance is the wrong proxy anyway. How well personal expression can be predicted from sequence bounds what those filters can do.

## Key points

- Evaluates personal, individual-specific expression prediction, not the general sequence-to-expression task where these models already do well.
- Odds ratio of 3.0 for expression direction over Enformer, on GTEx.
- Compared against classical baselines (Elastic Net, Random Forest), not only against its predecessor.
- Finds AlphaGenome exploits mechanisms distinct from those tree-based models identify on nonlinear genes.

## Limitations

A preprint, not peer reviewed, and it carries no journal venue in its registration. It is a single-author evaluation on GTEx, so the tissues and populations GTEx covers bound the conclusions. The title concedes the point: improvement over a predecessor is not the same as usable personal prediction, and the paper reports the gap rather than closing it. Its relevance to neoantigens is indirect.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025.08.05.668750v1.full.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1101/2025.08.05.668750`; the prose sections were written here from the paper itself.

## Citation

Shen et al. unknown 2025. AlphaGenome Enhances Personal Gene Expression Prediction but Retains Key Limitations. doi: 10.1101/2025.08.05.668750

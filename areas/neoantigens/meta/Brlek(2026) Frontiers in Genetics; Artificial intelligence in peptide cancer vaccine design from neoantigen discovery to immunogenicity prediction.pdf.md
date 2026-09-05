---
# --- identity ------------------------------------------------
id: 2026-01-01_brlek-2026-frontiers-in-genetics-artific
id_basis: filename-year
source: Brlek(2026) Frontiers in Genetics; Artificial intelligence in peptide cancer vaccine design from neoantigen discovery to immunogenicity prediction.pdf
sha256: ca4c719074d0df86c79d21b6d826ffd2646e765c5346b098e72459eb201b4d7a
size_bytes: 3248078
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 100998

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3389/fgene.2026.1875066"
year: 2026
title: "Artificial intelligence in peptide cancer vaccine design: from neoantigen discovery to immunogenicity prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as fgene-17-1875066.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A mini-review of AI across the peptide cancer vaccine pipeline: neoantigen discovery, epitope prioritisation, peptide-HLA binding, antigen presentation and TCR recognition, including modern pan-allele computational frameworks.

## Summary

Shorter and more focused than the other AI reviews here, and its value is that it keeps the vaccine platform in view rather than treating prediction as the whole problem.

It is unusually direct about the constraints that are not computational: short peptides are often weakly immunogenic and need adjuvants or delivery systems, tumour heterogeneity means a genetically diverse tumour may not uniformly express the target, and HLA polymorphism complicates design regardless of how good the predictor is.

## Key points

- Scoped to peptide vaccines specifically, so the design constraints stay visible alongside the prediction methods.
- Names three non-computational limits: weak peptide immunogenicity, tumour heterogeneity, HLA polymorphism.
- Covers pan-allele frameworks, the approach that makes rare alleles addressable at all.
- A compact entry point where the Bakhshian and Hu reviews here are exhaustive.

## Limitations

A mini-review: brief by design, so coverage is selective and every number belongs to a cited study. It describes the pipeline without evaluating any part of it. Where it and the other two AI reviews in this batch disagree in emphasis, none of them provides the measurement that would settle it.

## Provenance

Located in the published literature, dropped into `inbox/` as `fgene-17-1875066.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3389/fgene.2026.1875066`; the prose sections were written here from the paper itself.

## Citation

Brlek et al. Frontiers in Genetics 2026. Artificial intelligence in peptide cancer vaccine design: from neoantigen discovery to immunogenicity prediction. doi: 10.3389/fgene.2026.1875066

---
# --- identity ------------------------------------------------
id: 2026-01-01_bakhshian-2026-journal-of-translational
id_basis: filename-year
source: Bakhshian(2026) Journal of Translational Medicine; AI-driven neoantigen identification a comprehensive review from somatic variant calling to T cell recognition.pdf
sha256: a8b1281beb869861953d2b2b12444d1ff2b0c910e3a0c408ad0b71aff3c8ead2
size_bytes: 7927228
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 399207

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12967-026-08535-x"
year: 2026
title: "AI-driven neoantigen identification: a comprehensive review from somatic variant calling to T cell recognition"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s12967-026-08535-x.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review of how AI has reshaped neoantigen discovery across the whole pipeline: somatic variant calling, HLA typing, peptide processing, peptide-MHC binding, presentation, and T cell recognition. It reports that models trained on eluted ligand datasets substantially outperform affinity-only predictors across diverse HLA alleles and populations.

## Summary

The organising claim is that the bottleneck has not moved: high-throughput sequencing, immunopeptidomics and AI turned neoantigen discovery from bespoke experiments into scalable pipelines, but identifying the small subset of mutations that yield processed, presented and immunogenic epitopes remains where the process fails.

At 47 pages it is the most complete map in this collection of how the stages connect, and it catalogues tools stage by stage rather than surveying a single step.

## Key points

- Covers the pipeline end to end, from variant calling through to TCR recognition, rather than one stage.
- States plainly that eluted-ligand-trained models beat affinity-only predictors for presentation, across alleles and populations.
- Cites consortium-scale benchmarking as the evidence for integrating features rather than relying on any single one.
- Catalogues named tools with repositories per stage, which makes it usable as an index into the rest of this collection.

## Limitations

A review, so every quantitative claim belongs to a cited study and must be traced before use. It surveys methods largely on their authors' reported terms and runs no independent benchmark, so the comparisons it relays inherit whatever train-test leakage those papers carry - a problem this collection documents in detail elsewhere. Tool catalogues date quickly.

## Provenance

Located in the published literature, dropped into `inbox/` as `s12967-026-08535-x.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12967-026-08535-x`; the prose sections were written here from the paper itself.

## Citation

Bakhshian et al. Journal of Translational Medicine 2026. AI-driven neoantigen identification: a comprehensive review from somatic variant calling to T cell recognition. doi: 10.1186/s12967-026-08535-x

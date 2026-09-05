---
# --- identity ------------------------------------------------
id: 2023-01-01_racle-2023-unknown-how-to-predict-bindin
id_basis: filename-year
source: Racle(2023) unknown; How to predict binding specificity and ligands for new MHC-II alleles with MixMHC2pred.pdf
sha256: 0275eb139b272541984d12cd6b27f0ed91df4e526e8e167147aa6acfd0dd8668
size_bytes: 4125410
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 80203

# --- classification (LIH WI DC-909) --------------------------
type: preprint
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1101/2023.12.18.572125"
year: 2023
title: "How to predict binding specificity and ligands for new MHC-II alleles with MixMHC2pred"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023.12.18.572125v1.full.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A practical guide to using MixMHC2pred to predict the binding specificity of any MHC-II allele directly from its amino acid sequence, and to predict MHC-II ligands and CD4+ T cell epitopes across species. Available as a web server and as precompiled executables.

## Summary

A protocol chapter rather than a research paper, and it is here for the problem it addresses: MHC-II genes are extremely polymorphic and fast-evolving, with tens of thousands of alleles across vertebrates and hundreds more found every year through sequencing projects.

No method that requires per-allele training data can keep up with that. Predicting specificity from the allele's amino acid sequence alone is the only approach that scales, and this documents how to do it.

## Key points

- Predicts binding specificity from an allele's amino acid sequence, so newly discovered alleles need no training data of their own.
- Covers the cross-species case, where allele discovery outpaces experimental characterisation most severely.
- Web server plus precompiled standalone executables for Windows, macOS and Linux.
- The practical companion to the Racle (2023) Immunity paper's method.

## Limitations

A protocol, not an evaluation: it documents usage and does not independently establish accuracy, which rests on the underlying method paper. That paper's own finding applies here - pan-allele accuracy falls for species distant from the training data, so the cross-species use this chapter describes is exactly where the predictions are weakest. Venue metadata is incomplete in this record ('unknown'), a defect noted rather than patched.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023.12.18.572125v1.full.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1101/2023.12.18.572125`; the prose sections were written here from the paper itself.

## Citation

Racle et al. unknown 2023. How to predict binding specificity and ligands for new MHC-II alleles with MixMHC2pred. doi: 10.1101/2023.12.18.572125

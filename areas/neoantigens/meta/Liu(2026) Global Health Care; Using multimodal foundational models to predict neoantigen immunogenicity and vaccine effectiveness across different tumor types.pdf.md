---
# --- identity ------------------------------------------------
id: 2026-01-01_liu-2026-global-health-care-using-multim
id_basis: filename-year
source: Liu(2026) Global Health Care; Using multimodal foundational models to predict neoantigen immunogenicity and vaccine effectiveness across different tumor types.pdf
sha256: 2443495a9d48279a7b4fc321f62139be8d7880ce1b3080c6634e897764d94e1a
size_bytes: 880068
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 65757

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.63808/ghc.v2i3.498"
year: 2026
title: "Using multimodal foundational models to predict neoantigen immunogenicity and vaccine effectiveness across different tumor types"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as GHC-498.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoVAX-FM is a multi-modal foundation model embedding peptide sequences, pHLA 3D structures and gene expression into one semantic space via a contrastive pretraining paradigm, then fine-tuned to score immunogenicity and predict progression-free survival. Trained on paired data from 15 solid tumour types, it reports an average cross-tumour AUC of 0.94 in melanoma, NSCLC and microsatellite-stable colorectal cancer.

## Summary

The problem it targets is one this collection documents repeatedly: prediction models are trained and validated on a single tumour type and are rarely tested across cancers that differ in immune milieu, mutation burden and MHC genotype.

The design response is to fuse modalities - sequence, structure and expression - into a shared space, and to predict a clinical endpoint alongside immunogenicity rather than treating them as separate tasks.

## Key points

- Explicitly targets cross-tumour generalisation, tested on 15 solid tumour types.
- Fuses peptide sequence, pHLA structure and transcriptome in one contrastively pretrained space.
- Predicts progression-free survival jointly with immunogenicity, not as a downstream afterthought.
- Evaluated on one prospective trial and three external validation cohorts.

## Limitations

An average AUC of 0.94 for immunogenicity is far above anything else measured in this collection - the Wells consortium found 37 immunogenic of 608 tested peptide-MHCs - and a result that large invites the leakage and evaluation-design questions that Zhang (2026) and Graber (2025) here show are pervasive. The venue is outside the mainstream of this literature and the paper reports no bias control. Treat the headline number as unverified until an independent group reproduces it.

## Provenance

Located in the published literature, dropped into `inbox/` as `GHC-498.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.63808/ghc.v2i3.498`; the prose sections were written here from the paper itself.

## Citation

Liu et al. Global Health Care 2026. Using multimodal foundational models to predict neoantigen immunogenicity and vaccine effectiveness across different tumor types. doi: 10.63808/ghc.v2i3.498

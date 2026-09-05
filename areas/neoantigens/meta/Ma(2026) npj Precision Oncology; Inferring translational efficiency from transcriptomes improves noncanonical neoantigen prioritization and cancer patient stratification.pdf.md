---
# --- identity ------------------------------------------------
id: 2026-01-01_ma-2026-npj-precision-oncology-inferring
id_basis: filename-year
source: Ma(2026) npj Precision Oncology; Inferring translational efficiency from transcriptomes improves noncanonical neoantigen prioritization and cancer patient stratification.pdf
sha256: 9ec1fb6d301dec77e57d0f8b52f90416f2a238092c72a6b579a8be6399e3add6
size_bytes: 26265961
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 109781

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41698-026-01567-y"
year: 2026
title: "Inferring translational efficiency from transcriptomes improves noncanonical neoantigen prioritization and cancer patient stratification"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41698-026-01567-y_reference.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A framework evaluating inferred translational profiles across 15 independent datasets shows they outperform conventional RNA-seq proxies at recapitulating ribosome occupancy, and reveal lncRNA translational potential. Integrated into a translation-aware neoantigen pipeline, this identifies high-confidence noncanonical neoantigens missed by expression-based filtering, and corrects high-risk misclassification in glioma stratification.

## Summary

The premise is a mismatch every neoantigen pipeline quietly assumes away: transcript abundance is used as the filter for whether a neoantigen is actually made, but mRNA and protein levels diverge. Ribosome profiling measures translation directly but is too costly and complex for clinical use.

Inferring translation efficiency from RNA-seq is the compromise, and the paper's contribution is testing whether the inferred signal is actually better than the RNA-seq proxy it replaces rather than assuming it.

## Key points

- Directly tests whether inferred translatomes beat RNA-seq expression as a neoantigen filter, across 15 datasets.
- Surfaces the 'dark proteome' by predicting lncRNA translational potential - a source expression filters discard.
- A translation effect score replaces transcript abundance as the prioritisation criterion.
- Glioma stratification changes: some patients classed high-risk by expression-based methods are reclassified, with survival validation.

## Limitations

Inferred translation is a model output, not a measurement - the paper improves on a proxy with a better proxy, and the authors note existing models like RiboNN and Riboformer capture only parts of translational regulation. Reclassifying patients on a survival endpoint in retrospective cohorts is hypothesis-generating, not validated stratification. Noncanonical neoantigens identified this way remain predictions with no immunogenicity testing here.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41698-026-01567-y_reference.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41698-026-01567-y`; the prose sections were written here from the paper itself.

## Citation

Ma et al. npj Precision Oncology 2026. Inferring translational efficiency from transcriptomes improves noncanonical neoantigen prioritization and cancer patient stratification. doi: 10.1038/s41698-026-01567-y

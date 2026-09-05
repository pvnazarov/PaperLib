---
# --- identity ------------------------------------------------
id: 2022-01-01_ko-alo-lu-yal-n-2022-nucleic-acids-resea
id_basis: filename-year
source: Koşaloğlu-Yalçın(2022) Nucleic Acids Research; The Cancer Epitope Database and Analysis Resource (CEDAR).pdf
sha256: 9150c2b433e7d221511819d7d9971bb3993022482e4e8f141edaccbabcfb81f8
size_bytes: 3166356
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 40569

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gkac902"
year: 2022
title: "The Cancer Epitope Database and Analysis Resource (CEDAR)"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Ko_alo_lu_Yal_n_Nucleic_Acids_Res_The_Cancer_Epitope_Database_and_Analysis_Resou_PMID36250634.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

CEDAR is a freely accessible database cataloguing cancer epitope and immune receptor data curated from the literature, built as a companion to the IEDB, which covers infectious, autoimmune and allergic disease. It provides molecular characteristics and associated metadata for epitopes recognised by anti-cancer immune cells.

## Summary

The separation from IEDB is deliberate rather than administrative: cancer epitopes are mostly patient-private neoantigens with different provenance, different assay types and different metadata needs from pathogen epitopes, and pooling them obscures both.

For anyone training an immunogenicity model, this is one of the few curated sources of cancer-specific positives with the experimental context attached, which is what makes negatives and assay bias assessable rather than invisible.

## Key points

- Companion to IEDB, scoped specifically to cancer epitopes and receptors.
- Curated from literature with metadata about how each response was measured.
- Covers both T cell and B cell epitopes, and the receptors recognising them.
- Freely accessible at cedar.iedb.org; a standard training and benchmarking source for the predictors in this collection.

## Limitations

It is a literature curation, so it inherits publication bias: epitopes that were looked for, found and reported. It records positives far more reliably than negatives, which is precisely the gap that makes immunogenicity model training difficult. Coverage across HLA alleles and cancer types follows research attention rather than clinical prevalence. As a snapshot resource, any count taken from it is dated.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Ko_alo_lu_Yal_n_Nucleic_Acids_Res_The_Cancer_Epitope_Database_and_Analysis_Resou_PMID36250634.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gkac902`; the prose sections were written here from the paper itself.

## Citation

Koşaloğlu-Yalçın et al. Nucleic Acids Research 2022. The Cancer Epitope Database and Analysis Resource (CEDAR). doi: 10.1093/nar/gkac902

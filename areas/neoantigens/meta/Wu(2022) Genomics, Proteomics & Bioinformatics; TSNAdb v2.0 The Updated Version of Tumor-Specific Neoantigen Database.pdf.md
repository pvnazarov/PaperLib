---
# --- identity ------------------------------------------------
id: 2022-01-01_wu-2022-genomics-proteomics-bioinformati
id_basis: filename-year
source: Wu(2022) Genomics, Proteomics & Bioinformatics; TSNAdb v2.0 The Updated Version of Tumor-Specific Neoantigen Database.pdf
sha256: c20cd0bac7530808907906b54d2428b9d44b1ced2c890ad4691e9ec5e4189cf6
size_bytes: 1473852
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 48378

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.gpb.2022.09.012"
year: 2022
title: "TSNAdb v2.0: The Updated Version of Tumor-Specific Neoantigen Database"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Wu_Genomics_Proteomics_Bi_TSNAdb_v2_0_The_Updated_Version_of_Tumor_speci_PMID36209954.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

TSNAdb v2.0 updates the tumour-specific neoantigen database with stricter neoantigen identification criteria, predicted neoantigens from three types of somatic mutation, and a collection of experimentally validated neoantigens stratified by the level of experimental evidence supporting each.

## Summary

The stratification by experimental level is the feature that makes this useful rather than merely large. A neoantigen supported by a tetramer-positive T cell clone and one supported by a single ELISpot well are different kinds of evidence, and a database that records which is which lets a modeller choose a defensible positive set.

The rest is coverage: three mutation classes rather than missense alone, under tightened identification criteria relative to v1.

## Key points

- Experimentally validated neoantigens are divided by level of experimental evidence, not pooled into one 'validated' label.
- Predicted neoantigens from three somatic mutation types, broadening beyond missense.
- Stricter identification criteria than v1.0.
- Freely available; one of the few cancer-specific neoantigen resources alongside CEDAR and TumorAgDB.

## Limitations

The bulk of the content is predicted rather than validated, and predictions inherit the error rates of whichever tools produced them - a database of predictions is not evidence. Validated entries are drawn from published studies and carry that publication bias. Because prediction pipelines and their versions change, a stored prediction ages in a way a stored measurement does not.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Wu_Genomics_Proteomics_Bi_TSNAdb_v2_0_The_Updated_Version_of_Tumor_speci_PMID36209954.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.gpb.2022.09.012`; the prose sections were written here from the paper itself.

## Citation

Wu et al. Genomics, Proteomics &amp; Bioinformatics 2022. TSNAdb v2.0: The Updated Version of Tumor-Specific Neoantigen Database. doi: 10.1016/j.gpb.2022.09.012

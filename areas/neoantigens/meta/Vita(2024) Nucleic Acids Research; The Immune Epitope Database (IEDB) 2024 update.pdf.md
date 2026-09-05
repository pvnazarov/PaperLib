---
# --- identity ------------------------------------------------
id: 2024-01-01_vita-2024-nucleic-acids-research-the-imm
id_basis: filename-year
source: Vita(2024) Nucleic Acids Research; The Immune Epitope Database (IEDB) 2024 update.pdf
sha256: 7aa0de8b1bcc67781917f64add701e97d3cb249973fa62ebae6b81d334acca47
size_bytes: 1627480
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 41733

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gkae1092"
year: 2024
title: "The Immune Epitope Database (IEDB): 2024 update"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Vita_Nucleic_Acids_Res_The_Immune_Epitope_Database_IEDB_2024_update_PMID39558162.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The twenty-year update to the IEDB, now holding 6.8 million assays and 1.6 million immune epitopes extracted from over 25,000 publications. Changes since 2018 cover a user-directed search interface, advanced data exports, data quality improvements and better interoperability with related resources.

## Summary

The interoperability work is the substantive change for anyone building models: CEDAR, the cancer-specific companion also in this collection, is one of the resources it now aligns with, and consistent identifiers across them is what makes combined training sets defensible.

The growth from 1.6 million experiments in 2018 to 6.8 million assays here also means any model trained before this release was fitted on a substantially smaller corpus, which matters when comparing published performance figures across years.

## Key points

- 6.8 million assays and 1.6 million epitopes from >25,000 publications; twenty years of continuous curation.
- Improved interoperability across related resources, including the cancer-focused CEDAR.
- Advanced data exports make reproducible dataset construction practical.
- Emphasis on data standardisation, which is what makes cross-study benchmarks comparable at all.

## Limitations

The curation model and its biases are unchanged from earlier releases: published positives are captured far better than negatives, and assay heterogeneity persists across two decades of source literature. Cancer epitope coverage is deliberately delegated to CEDAR, so IEDB alone is not the right source for neoantigen work. Any count quoted from it is a snapshot that ages.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Vita_Nucleic_Acids_Res_The_Immune_Epitope_Database_IEDB_2024_update_PMID39558162.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gkae1092`; the prose sections were written here from the paper itself.

## Citation

Vita et al. Nucleic Acids Research 2024. The Immune Epitope Database (IEDB): 2024 update. doi: 10.1093/nar/gkae1092

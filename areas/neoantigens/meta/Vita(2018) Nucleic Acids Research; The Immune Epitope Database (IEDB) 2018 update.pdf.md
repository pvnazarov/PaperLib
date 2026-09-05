---
# --- identity ------------------------------------------------
id: 2018-01-01_vita-2018-nucleic-acids-research-the-imm
id_basis: filename-year
source: Vita(2018) Nucleic Acids Research; The Immune Epitope Database (IEDB) 2018 update.pdf
sha256: 9a3b980a02a94382a7721637b9a352c08d2b5ba54b9379f1d1442e1d17087166
size_bytes: 1338853
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 33385

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gky1006"
year: 2018
title: "The Immune Epitope Database (IEDB): 2018 update"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2019_Vita_Nucleic_Acids_Res_The_Immune_Epitope_Database_IEDB_2018_update_PMID30357391.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The 2018 update to the Immune Epitope Database, which manually curates experimental epitope data from the literature into a free, searchable resource covering antibody, T cell and MHC binding contexts across infectious, allergic, autoimmune and transplant disease. At this point it held more than 1.6 million experiments from 19,500 publications.

## Summary

IEDB is the training and benchmarking substrate for most of the predictors in this collection, so its curation policy is upstream of their reported performance.

Worth noting how the corpus was built: historical curation back to 1952 was completed in 2011, and PubMed is queried every two weeks since. The database is therefore comprehensive over published epitopes, with all the selection that 'published' implies.

## Key points

- More than 1.6 million experiments curated from 19,500 publications, structured by manual curation guidelines.
- Spans antibody, T cell and MHC binding contexts, not just T cell epitopes.
- Historical curation back to 1952 completed in 2011; biweekly PubMed queries since.
- The 2018 update focuses on query and reporting functionality rather than new data types.

## Limitations

A literature curation inherits publication bias: epitopes that were sought, found and reported. Negative results are recorded far less reliably than positive ones, which is the root cause of the unreliable negative class that limits every immunogenicity model here. Assays differ in sensitivity and threshold across decades of curated papers, so a single 'immunogenic' label spans heterogeneous evidence. Superseded by the 2024 update, also in this collection.

## Provenance

Located in the published literature, dropped into `inbox/` as `2019_Vita_Nucleic_Acids_Res_The_Immune_Epitope_Database_IEDB_2018_update_PMID30357391.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gky1006`; the prose sections were written here from the paper itself.

## Citation

Vita et al. Nucleic Acids Research 2018. The Immune Epitope Database (IEDB): 2018 update. doi: 10.1093/nar/gky1006

---
# --- identity ------------------------------------------------
id: 2022-01-01_zheng-2022-cancer-cell-transcriptomic-pr
id_basis: filename-year
source: Zheng(2022) Cancer Cell; Transcriptomic profiles of neoantigen-reactive T cells in human gastrointestinal cancers.pdf
sha256: e4616eaa5b997df5df63e41b350bd63f0ad1f5593809ec2f5ee9fee5439fd143
size_bytes: 2481046
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 118950

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2022.03.005"
year: 2022
title: "Transcriptomic profiles of neoantigen-reactive T cells in human gastrointestinal cancers"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS1535610822001209.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Single-cell RNA-seq with in vitro immunological screening identifies neoantigen-reactive T cells infiltrating cholangiocarcinoma and pancreatic cancer. Most CD8+ and CD4+ neoantigen-reactive TILs are in an exhausted state, with CD8+ cells enriched for CXCL13 and GZMA co-expression and CD4+ cells for HOPX or ADGRG1.

## Summary

This is the low-mutation-burden counterpart to the NSCLC and melanoma signature papers in this collection, and it does not simply confirm them. The distinct CD4 and CD8 markers found here are only partly the same, which suggests the phenotype of a neoantigen-reactive T cell depends on tumour type.

The most useful result is negative and practical: PD-1-high and CD39+CD103+ populations, widely used to enrich for tumour-reactive T cells, largely did not contain neoantigen-reactive cells in these cancers.

## Key points

- Covers cholangiocarcinoma and PDAC - low-mutation cancers where neoantigen-reactive cells are rare and hardest to find.
- Most neoantigen-reactive TILs, CD4 and CD8 alike, are exhausted.
- Distinct markers per compartment: CXCL13 with GZMA for CD8, HOPX or ADGRG1 for CD4.
- PD-1-high and CD39+CD103+ enrichment strategies largely failed here - a directly actionable negative result.

## Limitations

The authors note the CD8+CD39+CD103+ population was not captured in the single-cell data, likely because too few such cells were sequenced, so that arm of the comparison is weak. Reactive T cells were not detected at all in several patients, so the signature is derived from those where they were found. Numbers are small throughout - one of seven TCRs reactive in one patient, one of ten in another - so the transcriptomic profiles rest on few cells.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS1535610822001209.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2022.03.005`; the prose sections were written here from the paper itself.

## Citation

Zheng et al. Cancer Cell 2022. Transcriptomic profiles of neoantigen-reactive T cells in human gastrointestinal cancers. doi: 10.1016/j.ccell.2022.03.005

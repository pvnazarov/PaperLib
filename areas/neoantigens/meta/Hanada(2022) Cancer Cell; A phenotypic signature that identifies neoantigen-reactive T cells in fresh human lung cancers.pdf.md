---
# --- identity ------------------------------------------------
id: 2022-01-01_hanada-2022-cancer-cell-a-phenotypic-sig
id_basis: filename-year
source: Hanada(2022) Cancer Cell; A phenotypic signature that identifies neoantigen-reactive T cells in fresh human lung cancers.pdf
sha256: 2b78d6efb0264609542e7dd7b65fad8bd6786378953cf9298dc4ab99c0b196b1
size_bytes: 8094636
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 114328

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2022.03.012"
year: 2022
title: "A phenotypic signature that identifies neoantigen-reactive T cells in fresh human lung cancers"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS1535610822001271.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

CITE-seq with paired TCR-seq on T cells from fresh non-small-cell lung tumours identifies neoantigen-reactive T cells by phenotype: CD39 protein-positive, CXCL13-positive, and belonging to a high-frequency clonotype. The signature finds both CD4 and CD8 neoantigen-reactive TCRs.

## Summary

This inverts the usual direction of work. Rather than predicting which mutations produce neoantigens and then hunting for T cells that see them, it identifies the reactive T cells directly by surface and transcriptional phenotype and reads their receptors off.

For adoptive therapy that is the operationally useful direction, because the deliverable is a TCR, and it sidesteps the prediction accuracy problem entirely.

## Key points

- A three-part phenotype - CD39+, CXCL13+, high-frequency clonotype - marks neoantigen reactivity without needing to know the antigen.
- Works for both CD4 and CD8 reactive T cells, where most approaches are CD8-only.
- Uses fresh human tumours rather than expanded cultures, avoiding culture-driven selection.
- Provides an independent ground truth against which neoantigen predictions could be scored.

## Limitations

The signature is correlative: CD39 and CXCL13 mark chronic antigen exposure generally, so non-neoantigen-reactive tumour-resident cells can carry it and specificity is not perfect. Developed in NSCLC, a high-mutation tumour type where neoantigen-reactive cells are relatively abundant; transfer to low-mutation cancers is untested here. It identifies reactive T cells without identifying what they recognise.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS1535610822001271.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2022.03.012`; the prose sections were written here from the paper itself.

## Citation

Hanada et al. Cancer Cell 2022. A phenotypic signature that identifies neoantigen-reactive T cells in fresh human lung cancers. doi: 10.1016/j.ccell.2022.03.012

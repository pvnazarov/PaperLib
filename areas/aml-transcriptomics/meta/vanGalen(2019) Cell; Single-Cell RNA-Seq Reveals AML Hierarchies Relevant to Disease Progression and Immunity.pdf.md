---
# --- identity ------------------------------------------------
id: 2019-01-01_vangalen-2019-cell-single-cell-rna-seq-r
id_basis: filename-year
source: vanGalen(2019) Cell; Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.pdf
sha256: e23297e7f0210a43f53ee4b1907eed39c5de01955d3cb71338b62fe1c4a4a002
size_bytes: 10316478
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 520527

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2019.01.031"
year: 2019
title: "Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as vanGalen(2019) Cell; Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Combining single-cell RNA sequencing with genotyping, 38,410 cells were profiled from 40 bone marrow aspirates including 16 AML patients and five healthy donors, and a machine learning classifier applied to distinguish malignant cell types whose abundances varied between patients and over disease progression. Six malignant cell types along the HSC-to-myeloid axis were identified; primitive AML cells aberrantly co-express stemness and myeloid priming genes; and differentiated AML cells express immunomodulatory factors and suppress T cells. Unsupervised clustering of TCGA bulk profiles by the derived signatures yielded seven AML groups with distinct cell-type compositions, each strongly enriched for characteristic genetic lesions.

## Summary

The reference single-cell dataset for AML, used by several other papers in this collection as a source of cell-type signatures. Its foundational contribution is methodological - combining transcriptome and genotype in the same cells so malignant and normal can be distinguished, which expression alone cannot do reliably in a disease that partly recapitulates normal hematopoiesis.

Two biological findings have shaped the field since. Primitive AML cells co-express stemness and myeloid priming genes, an aberrant combination that normal cells do not display. And differentiated AML cells - the monocyte-like population usually treated as inert bystanders - express immunomodulatory factors and actively suppress T cells, with immunohistochemistry confirming fewer T cells and cytotoxic lymphocytes but more regulatory T cells in AML marrow. That gives the differentiated compartment a functional role rather than a passive one.

## Key points

- Paired single-cell transcriptomes and genotypes in 38,410 cells allow malignant and normal cells to be distinguished reliably.
- Six malignant cell types are defined along the HSC-to-myeloid axis, with abundances varying by patient and over progression.
- Primitive AML cells aberrantly co-express stemness and myeloid priming genes.
- AML-derived monocyte-like cells express immunomodulatory factors and suppress T cells, confirmed by immunohistochemistry showing fewer CTLs and more regulatory T cells.
- Applying the signatures to TCGA bulk data yields seven AML groups by cell-type composition, each enriched for characteristic genetic lesions.

## Limitations

Sixteen AML patients and five healthy donors is small for the cell-type composition claims, and the TCGA extension depends on deconvolution against signatures derived from those few patients. Cell-type assignment uses a machine learning classifier trained on this data, so the categories are defined by the method as much as discovered by it. The T cell suppression result is supported by an in vitro CD4+ T cell activation assay with a reporter readout, which demonstrates capacity rather than the effect in patients. Genotyping captures only selected mutations in cells where the transcript is sampled, so many cells remain unassigned. As a 2019 dataset it predates the deeper and longer-read methods used elsewhere in this collection.

## Provenance

Located in the published literature, dropped into `inbox/` as `vanGalen(2019) Cell; Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2019.01.031`; the prose sections were written here from the paper itself.

## Citation

vanGalen et al. Cell 2019. Single-Cell RNA-Seq Reveals AML Hierarchies Relevant to Disease Progression and Immunity. doi: 10.1016/j.cell.2019.01.031

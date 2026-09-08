---
# --- identity ------------------------------------------------
id: 2016-01-01_corces-2016-nature-genetics-lineage-spec
id_basis: filename-year
source: Corces(2016) Nature Genetics; Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution.pdf
sha256: 075272a3fb1c9145671cf1089dedcd6c2904383789f53ed364a5ef4db486010a
size_bytes: 10740257
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 260327

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/ng.3646"
year: 2016
title: "Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Corces(2016) Nat Genet; Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Chromatin accessibility and transcriptional landscapes are defined in 13 human primary blood cell types spanning the hematopoietic hierarchy, using Fast-ATAC, an ATAC-seq protocol optimised for blood cells: 137 samples from 9 healthy donors and 12 AML patients covering 16 cell types, with paired transcriptomes for 96. Distal enhancer landscapes reflect cell identity better than mRNA (91% cluster purity versus 78%), enabling 'enhancer cytometry' to enumerate pure cell types from mixtures. In AML, chromatin accessibility reveals regulatory evolution tracking mutation burden, single cells show mixed regulome profiles corresponding to disparate developmental stages, and accounting for that heterogeneity implicates HOX factors as regulators of preleukemic HSC characteristics.

## Summary

A foundational resource, and the measurement it justifies is the part worth remembering: distal regulatory elements classify blood cell identity better than expression does. That is not a small technical remark - it means the enhancer landscape, not the transcriptome, is the more reliable coordinate system for saying what a cell is, which underwrites everything built on it here.

The leukemia analysis uses that to construct synthetic normal analogs and ask what in an AML cell is genuinely cancer-specific rather than simply a reflection of the developmental stage it is stuck at - a confound that has muddied a great deal of AML profiling. Single-cell ATAC showing individual AML cells with mixed regulomes spanning several developmental stages is the observation that makes the correction necessary in the first place.

## Key points

- Fast-ATAC makes chromatin accessibility measurable in rare primary human blood populations, including progenitors not previously profiled.
- Distal regulatory elements define cell identity better than mRNA - 91% versus 78% cluster purity - which is the basis for enhancer cytometry.
- Enhancer cytometry enumerates pure cell types within complex mixtures, and builds synthetic normal analogs for comparison against cancer.
- Single AML cells carry mixed regulome profiles from disparate developmental stages; correcting for this isolates cancer-specific deviations.
- HOX factors are implicated as regulators of preleukemic HSC characteristics; disease-linked GWAS variants are assigned to the cell types where their elements are open.

## Limitations

Nine healthy donors and twelve AML patients is a small foundation for a reference atlas, and inter-individual variation in human hematopoiesis is substantial. Cell types are defined by surface-marker sorting, so each 'pure' population is as pure as its gating strategy - a circularity for a paper arguing that surface phenotype and regulatory identity can diverge. Single-cell ATAC-seq of this era is extremely sparse per cell, so 'mixed regulome profiles' rests on aggregating over cells and models rather than on confident per-cell measurement. Enhancer cytometry is validated computationally rather than against an orthogonal ground truth. The leukemia conclusions are correlative: regulatory evolution is inferred from cross-sectional samples of different patients with different mutation burdens, not from following a clone, and the HOX implication comes from motif enrichment rather than perturbation.

## Provenance

Located in the published literature, dropped into `inbox/` as `Corces(2016) Nat Genet; Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/ng.3646`; the prose sections were written here from the paper itself.

## Citation

RyanCorces et al. Nature Genetics 2016. Lineage-specific and single-cell chromatin accessibility charts human hematopoiesis and leukemia evolution. doi: 10.1038/ng.3646

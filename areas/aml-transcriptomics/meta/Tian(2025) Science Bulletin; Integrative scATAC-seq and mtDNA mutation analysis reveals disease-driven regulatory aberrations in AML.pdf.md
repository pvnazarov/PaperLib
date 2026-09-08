---
# --- identity ------------------------------------------------
id: 2025-01-01_tian-2025-science-bulletin-integrative-s
id_basis: filename-year
source: Tian(2025) Science Bulletin; Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML.pdf
sha256: df292c304716be54f5c1405328c7bb2055598247ecafd1f0505c9b918b9ec791
size_bytes: 8589350
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 115063

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.scib.2025.07.009"
year: 2025
title: "Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tian(2025) Sci Bull (Beijing); Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Mitochondrial single-cell ATAC-seq with single-cell RNA-seq was used to characterise AML cells, mapping them onto a constructed single-cell hematopoiesis reference to identify altered chromatin accessibility at cis-regulatory elements. Using an in-house algorithm, cisGRN, the authors found that mutations in the WT1 zinc finger domain associate with decreased accessibility and hypermethylation at target gene regulatory regions, validating five mutations (R467Q, R467L, R467W, H470Y, H470R). They identified a cis-regulatory element mutation arising early in hematopoiesis that creates a new CEBPB binding motif, activating enhancer activity and GATA4 expression to promote proliferation, confirmed by luciferase reporter and prime editing. Mitochondrial DNA lineage tracing with machine learning identified relapse-associated clones resembling leukemia stem cells and 27 marker genes predicting relapse.

## Summary

Combines three things that are usually done separately - chromatin accessibility, native lineage tracing through mitochondrial mutations, and regulatory network inference - so that clones can be followed without engineered barcodes and their regulatory states characterised at the same time.

The non-coding mutation is the standout finding. A single change creates a CEBPB binding site where none existed, activating an enhancer and driving GATA4, and the authors validate it by prime editing rather than by reporter assay alone - which is the appropriate standard for a claim about a single base in its native context. Identifying it as arising early in hematopoiesis places it before the recognised drivers.

## Key points

- Combines mtscATAC-seq, scRNA-seq and native mitochondrial lineage tracing, avoiding the need for engineered barcodes.
- WT1 zinc finger mutations reduce accessibility and increase methylation at target regulatory regions; five specific mutations were functionally validated.
- A non-coding cis-regulatory mutation creates a new CEBPB motif, activating an enhancer and GATA4 expression to promote proliferation.
- That mutation was validated by prime editing in its native context, not only by reporter assay, and arises early in hematopoiesis.
- Relapse-associated clones resembling leukemia stem cells were identified, yielding 27 marker genes for relapse prediction.

## Limitations

The relapse marker analysis rests on three patients for clone identification, with the 27-gene predictor then trained and tested on a public TARGET dataset split 70/30 - so the derivation cohort is very small and the validation is on different data with a different measurement platform. The authors state that the mechanisms by which these relapse genes act need further investigation, and the regulatory network linking them is predicted by their own algorithm rather than tested. Mitochondrial lineage tracing resolves clones only as coarsely as mtDNA mutation diversity allows, and scATAC-seq is sparse per cell, so clonal and regulatory assignments carry substantial uncertainty. The cisGRN algorithm is in-house and its predictions are validated at selected loci rather than systematically.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tian(2025) Sci Bull (Beijing); Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.scib.2025.07.009`; the prose sections were written here from the paper itself.

## Citation

Tian et al. Science Bulletin 2025. Integrative scATAC-seq and mtDNA mutation analysis reveals disease-driven regulatory aberrations in AML. doi: 10.1016/j.scib.2025.07.009

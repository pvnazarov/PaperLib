---
# --- identity ------------------------------------------------
id: 2023-01-01_lambo-2023-cancer-cell-a-longitudinal-si
id_basis: filename-year
source: Lambo(2023) Cancer Cell; A longitudinal single-cell atlas of treatment response in pediatric AML.pdf
sha256: 522e4836fd8ae82ff9627270b75ac2ed6d8f8a71dda01a7011a7d09b117cc9f1
size_bytes: 16426555
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 183250

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2023.10.008"
year: 2023
title: "A longitudinal single-cell atlas of treatment response in pediatric AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lambo(2023) Cancer Cell; A longitudinal single-cell atlas of treatment response in pediatric AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Single-cell RNA and ATAC sequencing of 28 pediatric AML patients from the AAML1031 trial, representing different subtypes, profiled at diagnosis, remission and relapse. Cellular composition differed between genetic subgroups at diagnosis; upon relapse, cellular hierarchies transitioned toward a more primitive state regardless of subtype. Primitive cells at relapse were distinct from those at diagnosis, with under-representation of myeloid transcriptional programs and over-representation of other lineage programs, in some patients including the appearance of a B-lymphoid-like hierarchy.

## Summary

A longitudinal design applied to a disease where it is rarely possible - matched diagnosis, remission and relapse samples in children, from a trial cohort. Pediatric AML lacks the targetable driver mutations that adult disease offers and its overall survival has not improved, so the question of what actually changes at relapse matters more than usual.

The answer is a shift in cellular hierarchy rather than genetics. Current therapy eradicates myeloid-primed cells - CMP-like, GMP-like, early monocyte - but not multipotent HSPC-like cells, which then dominate and show reduced myeloid priming with activation of other lineage programs, occasionally including a B-lymphoid-like hierarchy. The therapeutic inference the authors draw is specific and non-obvious: differentiation therapy might work better at relapse than at diagnosis, because that is when primitive cells are enriched.

## Key points

- 28 pediatric AML patients profiled by single-cell RNA and ATAC sequencing at diagnosis, remission and relapse.
- Relapse involves a shift toward a more primitive hierarchy regardless of subtype, and abundance of primitive cells at diagnosis may predict outcome.
- Therapy eradicates myeloid-primed populations but not multipotent HSPC-like cells.
- Relapse-associated primitive cells lose myeloid priming and gain other lineage programs, sometimes producing a B-lymphoid-like hierarchy.
- Suggests targeting MEF2C in MLL-rearranged cases and AP-1 in others, and that differentiation therapy may work better at relapse than at diagnosis.

## Limitations

28 patients across multiple genetic subtypes leaves very few per subgroup, so subtype-specific conclusions rest on small numbers. Cell-type assignment in single-cell AML data depends on reference-based classification against normal hematopoiesis, which is circular in a disease that partially recapitulates that hierarchy - a difficulty the authors name. The relapse hierarchy shift is observational and cannot distinguish selection of a pre-existing primitive population from plasticity of surviving cells, which matters for whether differentiation therapy would help. Targeting MEF2C and AP-1, and the proposal about timing differentiation therapy, are inferences from expression data with no functional or therapeutic test. The prognostic value of primitive-cell abundance at diagnosis is a correlation in this cohort, not a validated marker.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lambo(2023) Cancer Cell; A longitudinal single-cell atlas of treatment response in pediatric AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2023.10.008`; the prose sections were written here from the paper itself.

## Citation

Lambo et al. Cancer Cell 2023. A longitudinal single-cell atlas of treatment response in pediatric AML. doi: 10.1016/j.ccell.2023.10.008

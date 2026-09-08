---
# --- identity ------------------------------------------------
id: 2019-01-01_adelman-2019-cancer-discovery-aging-huma
id_basis: filename-year
source: Adelman(2019) Cancer Discovery; Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia.pdf
sha256: f0b4b7cc7a1528506cf10dff8b43097956a53d8d011bfe63dfd0dd0e3575910a
size_bytes: 5450238
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 197121

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-18-1474"
year: 2019
title: "Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Adelman(2019) Cancer Discov; Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An integrative epigenomic and transcriptomic characterisation of normal human ageing in Lineage-CD34+CD38- HSC-enriched cells, combining histone marks, DNA methylation and single-cell RNA sequencing. Aged cells show redistributed DNA methylation and reduced H3K27ac, H3K4me1 and H3K4me3, losing 4646 active enhancers and 3091 bivalent promoters at developmental and cancer pathways that are comparably altered in AML of all ages. Downregulating KLF6 in vitro impairs differentiation, increases colony-forming potential, and reproduces both ageing and leukemia expression signatures.

## Summary

This is the paper that makes 'AML is a disease of the elderly' a statement about chromatin rather than only about accumulated mutations. The argument is that normal ageing already moves the human HSC epigenome in the direction AML occupies, so the aged stem cell is a partly prepared substrate before any leukemic driver arrives.

What lifts it above a correlation is the KLF6 experiment. Having found that the pathways lost with age overlap those deregulated in AML, they take one transcription factor down in vitro and recover impaired differentiation with increased self-renewal - the phenotype the correlation predicted. It is one factor out of many and the effect is partial, which the authors say.

## Key points

- Human HSC ageing involves loss of active enhancers and bivalent promoters, not merely global drift in DNA methylation.
- The pathways affected by ageing overlap those deregulated in AML across all ages, which is the basis of the predisposition claim.
- KLF6, BCL6 and RUNX3 are among the hematopoietic transcription factors deregulated.
- KLF6 knockdown alone impairs differentiation and raises colony-forming potential, partially recapitulating the aged and leukemic signature.
- Works on sorted human HSC-enriched cells rather than peripheral blood or unfractionated CD34+, which earlier human studies had used.

## Limitations

Cross-sectional comparison of young and aged donors, so 'reprogramming' is inferred from a contrast between people, not followed within anyone; donor numbers for the chromatin assays are small and inter-individual variation in human marrow is large. The link to leukemia is an overlap of pathway annotations between two datasets, which is a weak form of evidence for causation - and the title's 'may predispose' is doing real work. The functional test is a single factor knocked down in vitro, recapitulating signatures rather than producing leukemia, and colony-forming potential is a surrogate for self-renewal. Clonal hematopoiesis is discussed but the aged samples are not shown to be free of it, so some of the aged signature could come from expanded mutant clones rather than from ageing itself.

## Provenance

Located in the published literature, dropped into `inbox/` as `Adelman(2019) Cancer Discov; Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-18-1474`; the prose sections were written here from the paper itself.

## Citation

Adelman et al. Cancer Discovery 2019. Aging Human Hematopoietic Stem Cells Manifest Profound Epigenetic Reprogramming of Enhancers That May Predispose to Leukemia. doi: 10.1158/2159-8290.CD-18-1474

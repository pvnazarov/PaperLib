---
# --- identity ------------------------------------------------
id: 2025-01-01_shi-2025-cell-reports-transcript-isoform
id_basis: filename-year
source: Shi(2025) Cell Reports; Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing.pdf
sha256: a701ef885637fb36baa6af8d4afa6436b80f4843cf80e7fbbb45d49c3ec46b69
size_bytes: 6106514
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 140051

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2025.116216"
year: 2025
title: "Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Shi(2025) Cell Rep; Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Long-read Oxford Nanopore transcriptome sequencing of 60 primary AML bone marrow samples gives isoform-level resolution of splicing abnormalities, detecting extensive AML-specific anomalies and 119,278 previously unannotated transcript isoforms, of which 80,294 (67.31%) contain complete open reading frames and 9,812 (12.22%) were validated by mass spectrometry. Quantifying these across 175 RNA-seq samples and clustering by non-negative matrix factorisation defines isoform-based molecular subtypes that correlate with prognosis, and a 10-transcript prognostic model predicts outcome within the internal cohort.

## Summary

Argues that isoform structure, not gene-level expression, is the right resolution for classifying AML - and supports it by deriving subtypes from isoform quantification that separate on prognosis. The immunological characterisation of two of them is the most substantive biology: C6 and C8 both have high immune infiltration, exhaustion and poor outcome, but by different routes - C8 shows classical antigen-overload exhaustion with high HLA class I and regulatory T cell expansion, while C6 shows intrinsic dysregulation with absent inhibitory signalling and compensatory checkpoint activation. That distinction would matter for choosing immunotherapy.

The paper carries an explicit limitations section that is unusually informative about its own negative results.

## Key points

- Long-read sequencing of 60 primary AML samples identifies 119,278 unannotated isoforms, two thirds with complete open reading frames.
- Isoform-level clustering defines molecular subtypes that correlate with prognosis, distinct from gene-expression classification.
- Two poor-prognosis subtypes show immune exhaustion by different mechanisms - antigen overload versus intrinsic dysregulation.
- A 10-transcript prognostic model predicts outcome in the internal cohort.
- Fewer than 14% of novel transcripts have NMD-associated features, so translational deficiency likely arises by other mechanisms such as ribosome occupancy.

## Limitations

The authors state theirs directly: the annotation pipeline prioritised coding potential and therefore omits lncRNAs, miRNAs and circRNAs, so the catalogue is not a complete isoform landscape; and only 12.22% of unannotated transcripts were confirmed as translated, leaving the great majority unvalidated - a rate they note is consistent with other large proteogenomic studies but which still means most of the 119,278 isoforms have no protein evidence. The prognostic model is developed and evaluated within the internal cohort with no external validation described. Sixty samples for discovery is modest for defining subtypes, and non-negative matrix factorisation will return clusters from any dataset. Long-read isoform calls remain sensitive to library preparation artefacts and assembly parameters.

## Provenance

Located in the published literature, dropped into `inbox/` as `Shi(2025) Cell Rep; Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2025.116216`; the prose sections were written here from the paper itself.

## Citation

Shi et al. Cell Reports 2025. Transcript isoform diversity defines molecular subtypes and prognosis in acute myeloid leukemia through long-read sequencing. doi: 10.1016/j.celrep.2025.116216

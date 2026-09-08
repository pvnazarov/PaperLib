---
# --- identity ------------------------------------------------
id: 2022-01-01_zhai-2022-molecular-cancer-longitudinal
id_basis: filename-year
source: Zhai(2022) Molecular Cancer; Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia.pdf
sha256: cbb5489e65d881a5bb086605f385f306c0c99e6a4201df00d4ee29867a149a4f
size_bytes: 4483053
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 73710

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12943-022-01635-4"
year: 2022
title: "Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zhai(2022) Mol Cancer; Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Whole-exome sequencing for somatic mutations and copy number variations was combined with single-cell RNA-seq to investigate clonal heterogeneity in diagnosis-relapse pairs. Extensive expression differences were found between patients and between paired samples, even for those with the same presumed initiating events, and the differences were associated with clonal composition and evolution - most strikingly in patients acquiring large-scale copy number variations at relapse. In a DNMT3A/FLT3-ITD patient the leukemia switched from an AP-1-regulated clone at diagnosis to an mTOR signalling-driven clone at relapse, while two AML1-ETO pairs shared genes related to hematopoietic stem cell maintenance and cell migration, suggesting relapse LSC-like cells evolved from diagnosis cells.

## Summary

The useful observation is a dissociation between genetic and transcriptional change. Pathway switches occurred with few differential somatic mutations - AP-1 to mTOR in one patient - and conversely samples could differ genetically without corresponding transcriptional divergence, though samples with extensive copy number variation did show the largest transcriptional differences.

That argues relapse is not reliably predicted by mutation, and that following patients transcriptionally captures something mutation profiling misses. The two AML1-ETO pairs behaving similarly, sharing stem cell maintenance and migration genes, suggests some relapse routes are subtype-determined while others, like the DNMT3A/FLT3-ITD case, are individual.

## Key points

- Paired diagnosis-relapse single-cell profiling combined with exome sequencing links clonal and transcriptional change.
- Samples with extensive copy number variation showed the largest transcriptional differences between diagnosis and relapse.
- Pathway switches can occur with few differential somatic mutations - AP-1 to mTOR in one DNMT3A/FLT3-ITD patient.
- Two AML1-ETO pairs shared stem cell maintenance and migration genes, suggesting relapse LSC-like cells evolved from diagnosis cells.
- Transcriptional heterogeneity exists between patients with the same presumed initiating event.

## Limitations

A small number of diagnosis-relapse pairs, with the principal findings presented as individual patient vignettes - the AP-1 to mTOR switch rests on one patient and the AML1-ETO observation on two - so these illustrate possible mechanisms rather than establishing their frequency. No functional validation of any pathway switch or of the LSC-like populations. The conclusion that relapse LSC-like cells evolved from diagnosis cells is inferred from shared gene expression rather than from lineage tracing. Quality control in one sample required discarding a cluster as doublets or ambient RNA contamination, which illustrates the interpretive difficulty of these data. Descriptive throughout, with no therapeutic implication tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zhai(2022) Mol Cancer; Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12943-022-01635-4`; the prose sections were written here from the paper itself.

## Citation

Zhai et al. Molecular Cancer 2022. Longitudinal single-cell transcriptomics reveals distinct patterns of recurrence in acute myeloid leukemia. doi: 10.1186/s12943-022-01635-4

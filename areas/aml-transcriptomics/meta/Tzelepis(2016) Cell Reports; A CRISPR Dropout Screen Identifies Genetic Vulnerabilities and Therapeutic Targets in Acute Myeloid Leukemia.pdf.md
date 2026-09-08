---
# --- identity ------------------------------------------------
id: 2016-01-01_tzelepis-2016-cell-reports-a-crispr-drop
id_basis: filename-year
source: Tzelepis(2016) Cell Reports; A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia.pdf
sha256: a3fb5caf6cecf67643d7b8d1a3451235417fe4c917ff79e5314b8a01ab8d0593
size_bytes: 3799538
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 190885

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2016.09.079"
year: 2016
title: "A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tzelepis(2016) Cell Rep; A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An optimised genome-wide CRISPR-Cas9 screening platform for recessive genetic screens is applied to human AML cell lines, producing a catalogue of genetic vulnerabilities. It recovers known therapeutic targets including BRD4, DOT1L and MEN1 alongside numerous additional candidates. KAT2A is proposed as a therapeutic target: its inhibition induces myeloid differentiation and apoptosis and arrests growth of primary AML cells while sparing normal progenitors.

## Summary

The resource that much subsequent AML target discovery in this collection draws on, including the dependency-screen mining that identifies ACSL4 and other subtype-selective vulnerabilities. Its validity check is that it recovers BRD4, DOT1L and MEN1 - targets found independently by mechanistic and RNAi approaches - which is what licenses attention to the novel hits alongside them.

The KAT2A nomination has the property that matters most: growth arrest in primary AML cells but not normal progenitors. The authors are careful about mechanism, saying the molecular basis will need future study while noting that the transcriptional changes suggest an effect secondary to inhibiting leukemogenic transcriptional programmes, comparable to BRD4 and DOT1L inhibition. KAT2A acts within the SAGA and ATAC coactivator complexes at distinct sets of promoters and enhancers, which is offered as why it influences such diverse programmes.

## Key points

- An optimised genome-wide CRISPR-Cas9 dropout platform produces a catalogue of AML genetic vulnerabilities.
- Recovery of BRD4, DOT1L and MEN1 validates the screen against targets identified by independent approaches.
- KAT2A inhibition induces myeloid differentiation and apoptosis in AML cells.
- It arrests growth of primary AML cells while sparing normal progenitors - the selectivity a target requires.
- KAT2A functions within the SAGA and ATAC coactivator complexes at distinct promoters and enhancers, explaining its broad transcriptional influence.

## Limitations

The authors flag limitations in predicting clinical toxicity, and their mechanistic account of KAT2A is explicitly provisional - the molecular basis of differentiation and apoptosis is left to future work, with the transcriptional-programme explanation offered as a hypothesis. Screens are in AML cell lines, which under-represent primary disease and its microenvironment; primary cell work is limited to growth arrest assays. Dropout screens identify genes required for proliferation in culture over weeks, biasing toward strong fast phenotypes and against dependencies that matter in vivo. KAT2A has no clinical-grade selective inhibitor, and subsequent work in this collection shows its loss acts through increased transcriptional noise rather than through a conventional target relationship.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tzelepis(2016) Cell Rep; A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2016.09.079`; the prose sections were written here from the paper itself.

## Citation

Tzelepis et al. Cell Reports 2016. A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia. doi: 10.1016/j.celrep.2016.09.079

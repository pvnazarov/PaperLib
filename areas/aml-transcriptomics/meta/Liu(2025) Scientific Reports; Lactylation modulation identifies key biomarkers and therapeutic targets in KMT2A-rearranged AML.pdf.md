---
# --- identity ------------------------------------------------
id: 2025-01-01_liu-2025-scientific-reports-lactylation
id_basis: filename-year
source: Liu(2025) Scientific Reports; Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML.pdf
sha256: 46550fdc1590c9ec4f9851ebdf03e2902d27bbd3060b470fbc8f3447cea1ced6
size_bytes: 6446922
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 66986

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41598-025-86136-2"
year: 2025
title: "Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Liu(2025) Sci Rep; Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A computational study of lactylation-related gene expression in KMT2A-rearranged AML, using microarray data from CN-AML (n = 70) and KMT2Ar-AML (n = 52) cohorts. Twelve lactylation-dependent differentially expressed genes were identified, from which machine learning selected six (PFN1, S100A6, CBR1, LDHB, LGALS1, PRDX1) as prognostically relevant and linked to disease pathways. Unsupervised clustering distinguished two lactylation subtypes with differing pathway enrichment and immune cell infiltration, and the analysis suggested PI3K inhibitors and pevonedistat as candidate agents.

## Summary

Applies the lactylation framework - lysine modification by lactate, a recent addition to the epigenetic repertoire - to KMT2A-rearranged AML, on the reasonable premise that a highly glycolytic malignancy should produce the substrate for it. The six genes selected are individually plausible in AML: LDHB in glycolysis and chemoresistance, S100A6 in MDS-to-AML progression, LGALS1 in immunosuppression, PRDX1 in leukemic stem cells and redox handling.

The paper is best read as a hypothesis-generating survey of a metabolic-epigenetic axis rather than as evidence about it, and the authors themselves close by noting the need for clinical validation.

## Key points

- Applies the lactylation concept - lactate-driven lysine modification - to KMT2A-rearranged AML.
- Six lactylation-associated genes selected by machine learning: PFN1, S100A6, CBR1, LDHB, LGALS1, PRDX1.
- Unsupervised clustering identifies two lactylation subtypes with distinct pathway and immune infiltration profiles.
- Links the genes to myeloid-derived suppressor cells and the immunosuppressive microenvironment.
- Nominates PI3K inhibitors and pevonedistat as candidate agents from the expression analysis.

## Limitations

Entirely computational, with no experimental work at all: no lactylation is measured anywhere in the study. The genes are 'lactylation-related' by annotation and differential expression, not because any lactylation event was detected, so the central premise is assumed rather than demonstrated - a substantial gap for a paper whose claim is about a specific post-translational modification. Analysis rests on public microarray data from 52 KMT2Ar cases with no independent validation cohort, and six genes selected from twelve by machine learning in a cohort of this size is a setting prone to overfitting. Immune infiltration is inferred by deconvolution rather than measured. The drug nominations come from expression-signature matching, with no test in any model. The authors acknowledge that clinical validation is needed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Liu(2025) Sci Rep; Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41598-025-86136-2`; the prose sections were written here from the paper itself.

## Citation

Liu et al. Scientific Reports 2025. Lactylation modulation identifies key biomarkers and therapeutic targets in KMT2A-rearranged AML. doi: 10.1038/s41598-025-86136-2

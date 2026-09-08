---
# --- identity ------------------------------------------------
id: 2025-01-01_richard-carpentier-2025-biomarker-resear
id_basis: filename-year
source: Richard-Carpentier(2025) Biomarker Research; High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the Leucegene cohort.pdf
sha256: dd16ab812583129a563240fca381d956a4a620f027ef445971a5fe9b8e223e8b
size_bytes: 5571132
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 84427

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s40364-025-00827-6"
year: 2025
title: "High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the Leucegene cohort"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Richard-Carpentier(2025) Biomark Res; High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the L.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Transcriptomic analysis of 316 Leucegene patients with intermediate-risk cytogenetic AML treated with intensive chemotherapy identified high IL1R1 expression as both prognostic and predictive. IL1R1-high was associated with older age, monocytic differentiation, more FLT3-ITD and RUNX1 mutations and fewer IDH1/2 and bZIP CEBPA mutations, and with lower 5-year overall survival (10% versus 38%) and higher relapse incidence (76% versus 59%), independently in multivariable analysis (HR 1.78). In landmark analysis, transplant in first remission significantly improved 5-year survival in IL1R1-high patients (67% versus 27%, HR 0.33) but not in IL1R1-low patients (62% versus 54%, HR 0.72), and the poor prognosis of IL1R1-high was abrogated by transplant.

## Summary

A predictive rather than merely prognostic biomarker, which is the harder and more useful thing. Intermediate-risk cytogenetic AML without FLT3-ITD is precisely the group where the decision to transplant in first remission is genuinely uncertain, and a marker that identifies who benefits addresses a real clinical question rather than restating known risk.

The interaction analysis is what supports the predictive claim: transplant helps IL1R1-high patients substantially and IL1R1-low patients not detectably, including among those without FLT3-ITD where the hazard ratio is essentially 1. After transplant, survival is equivalent between the two groups, so the disadvantage is abolished rather than merely reduced. The authors also developed and validated an RT-qPCR assay against the sequencing data, which is the step that makes a transcriptomic marker deployable.

## Key points

- IL1R1-high is independently prognostic in intermediate-risk AML (HR 1.78) with 5-year survival of 10% versus 38%.
- It is also predictive: transplant in first remission improves survival in IL1R1-high (HR 0.33) but not IL1R1-low patients.
- The benefit distinction holds among FLT3-ITD-negative patients, the group where the transplant decision is least clear.
- After transplant, survival is comparable between IL1R1-high and IL1R1-low, so the poor prognosis is abrogated.
- An RT-qPCR test was developed and correlated against RNA sequencing, making the marker clinically deployable.

## Limitations

The authors state that external validation is needed - this is a single cohort, and the predictive claim rests on a landmark analysis in which transplant was not randomised, so patients who received it differ systematically from those who did not in ways that residual confounding cannot fully address. Subgroup analyses, particularly the FLT3-ITD-negative comparison, involve small numbers. IL1R1-high correlates with monocytic differentiation, older age and specific mutations, so the marker may be partly a composite of features already known to matter. A dichotomising threshold of 2.0 transcripts per million chosen within the same cohort will perform optimistically. No functional work tests whether IL1R1 or inflammatory signalling causes the resistance to chemotherapy that the transplant benefit implies.

## Provenance

Located in the published literature, dropped into `inbox/` as `Richard-Carpentier(2025) Biomark Res; High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the L.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s40364-025-00827-6`; the prose sections were written here from the paper itself.

## Citation

Richard-Carpentier et al. Biomarker Research 2025. High IL1R1 expression predicts poor survival and benefit from stem cell transplant in intermediate-risk acute myeloid leukemia from the Leucegene cohort. doi: 10.1186/s40364-025-00827-6

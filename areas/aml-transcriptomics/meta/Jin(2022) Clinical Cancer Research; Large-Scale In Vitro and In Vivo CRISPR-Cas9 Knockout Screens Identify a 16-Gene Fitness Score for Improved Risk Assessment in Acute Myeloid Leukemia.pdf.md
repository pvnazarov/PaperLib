---
# --- identity ------------------------------------------------
id: 2022-01-01_jin-2022-clinical-cancer-research-large
id_basis: filename-year
source: Jin(2022) Clinical Cancer Research; Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemia.pdf
sha256: 015306c1a0e809bfb87124fd2e1ddbc771cbfb14ec7eb399fee6a12eec990a79
size_bytes: 1677736
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 189884

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/1078-0432.CCR-22-1618"
year: 2022
title: "Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Jin(2022) Clin Cancer Res; Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemi.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Integrating genome-wide CRISPR-Cas9 data from more than 1000 in vitro and in vivo knockout screens, the authors identify 280 AML-specific fitness genes and derive a 16-gene fitness score (AFG16) by sparse regression in a training cohort of 618 cases, validated in five public cohorts (n = 1570) and their own RJAML cohort (n = 157) with matched RNA and targeted sequencing - more than 2300 patients in total. AFG16 distils the downstream consequences of several genetic abnormalities and substantially improves ELN classification; high scores predicted poor response to induction chemotherapy, and ex vivo drug screening showed high-AFG16 patients were more sensitive to the cell-cycle inhibitors flavopiridol and SNS-032, with strongly activated cell-cycle signalling.

## Summary

A methodologically distinctive way to build a prognostic signature. Rather than mining expression for correlates of survival, it starts from functional genomics - which genes AML cells actually need - and then asks whether their expression predicts outcome. That grounding gives a reason why the genes should matter, which most signatures lack, and supports the authors' framing that a common signature can be derived regardless of the underlying genetic lesion.

Validation is unusually broad: six independent cohorts across different platforms, more than 2300 patients. And the score is not only prognostic but predictive in two directions - poor response to induction chemotherapy, and greater ex vivo sensitivity to CDK inhibitors - which is what would make it clinically useful rather than merely informative.

## Key points

- Built from functional genomics: 280 AML fitness genes from over 1000 CRISPR knockout screens, in vitro and in vivo.
- The 16-gene AFG16 score validated across six independent cohorts and more than 2300 patients on different platforms.
- Substantially improves ELN risk classification and captures downstream consequences shared across different genetic lesions.
- High AFG16 predicts poor response to induction chemotherapy.
- High-AFG16 patients show activated cell-cycle signalling and greater ex vivo sensitivity to flavopiridol and SNS-032.

## Limitations

All cohorts are retrospective, with heterogeneous treatments across eras, so 'improves risk stratification' means better separation of observed outcomes rather than demonstrated benefit from acting on the score. The fitness genes come from cell-line screens, which under-represent the primary disease and its microenvironment, and gene expression in patients is used as a proxy for a dependency measured in lines. The drug sensitivity result is ex vivo on isolated mononuclear cells, an assay that correlates only moderately with clinical response, and flavopiridol has a long history of preclinical promise and clinical disappointment in AML. A 16-gene expression score requires standardised quantitative RNA measurement across laboratories, which is a harder deployment problem than the cytogenetic and mutational testing it would supplement.

## Provenance

Located in the published literature, dropped into `inbox/` as `Jin(2022) Clin Cancer Res; Large-Scale In Vitro and In Vivo CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemi.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/1078-0432.CCR-22-1618`; the prose sections were written here from the paper itself.

## Citation

Jin et al. Clinical Cancer Research 2022. Large-Scale
                    <i>In Vitro</i>
                    and
                    <i>In Vivo</i>
                    CRISPR-Cas9 Knockout Screens Identify a 16-Gene Fitness Score for Improved Risk Assessment in Acute Myeloid Leukemia. doi: 10.1158/1078-0432.CCR-22-1618

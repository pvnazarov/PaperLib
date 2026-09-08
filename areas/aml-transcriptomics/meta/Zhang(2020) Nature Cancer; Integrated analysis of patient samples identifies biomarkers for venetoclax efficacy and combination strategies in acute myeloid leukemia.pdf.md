---
# --- identity ------------------------------------------------
id: 2020-01-01_zhang-2020-nature-cancer-integrated-anal
id_basis: filename-year
source: Zhang(2020) Nature Cancer; Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia.pdf
sha256: ad47c867e5603a3268f5650aecebdd318a894bcde255bf7eceaed010b4186812
size_bytes: 13806642
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 327867

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s43018-020-0103-x"
year: 2020
title: "Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zhang(2020) Nat Cancer; Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Integrating clinical characteristics, exome and RNA sequencing, and inhibitor data from primary AML patient samples in the Beat AML cohort, the authors determined that myelomonocytic leukemia, upregulation of BCL2A1 and CLEC7A, and mutations of PTPN11 and KRAS conferred resistance to venetoclax and to multiple venetoclax combinations. Venetoclax combined with the MCL1 inhibitor AZD5991 induced synthetic lethality and circumvented that resistance, shown in cell line models engineered for each resistance factor, in xenografts, and in a KRAS-mutant primary AML model with survival benefit.

## Summary

Its methodological argument is that most venetoclax resistance work has been done in cell lines that do not reproduce the clinical and genetic diversity of primary AML - so the biomarkers derived from them may not transfer. Working from primary patient samples with matched sequencing and drug response data addresses that directly.

The biomarkers found span three kinds: a morphological phenotype (myelomonocytic), expression changes (BCL2A1, CLEC7A) and mutations (PTPN11, KRAS), which together predict resistance not only to venetoclax but to multiple venetoclax combinations - a more demanding and more useful endpoint. BCL2A1 is the mechanistically central one, since it is an anti-apoptotic BCL2 family member with no available inhibitor, and MCL1 inhibition is the workable route around it.

## Key points

- Derived from primary patient samples with matched exome, RNA-seq and drug response, rather than from cell lines.
- Myelomonocytic phenotype, BCL2A1 and CLEC7A upregulation, and PTPN11 and KRAS mutations confer venetoclax resistance.
- Resistance extends to multiple venetoclax combinations, not just the single agent.
- Venetoclax with the MCL1 inhibitor AZD5991 is synthetically lethal and circumvents each resistance factor.
- Validated across engineered cell lines, xenografts and a KRAS-mutant primary AML model with survival benefit.

## Limitations

MCL1 inhibitors including AZD5991 have encountered cardiac toxicity in clinical development, since MCL1 is required in cardiomyocytes - a serious obstacle the preclinical combination data do not address. The authors note there is no pharmacologic way to target BCL2A1 directly, so MCL1 inhibition is a workaround rather than a solution to the identified mechanism. Biomarkers are derived retrospectively from ex vivo drug sensitivity in Beat AML, which correlates imperfectly with clinical response, and are not validated prospectively. The myelomonocytic association is contested by other work in this collection reporting that monocytic differentiation predicts resistance in culture but not in patients. In vivo experiments use small groups of 3 to 5 mice per arm.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zhang(2020) Nat Cancer; Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s43018-020-0103-x`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Nature Cancer 2020. Integrated analysis of patient samples identifies biomarkers for venetoclax efficacy and combination strategies in acute myeloid leukemia. doi: 10.1038/s43018-020-0103-x

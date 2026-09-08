---
# --- identity ------------------------------------------------
id: 2024-01-01_ma-2024-leukemia-genomic-and-global-gene
id_basis: filename-year
source: Ma(2024) Leukemia; Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALMMLLT10 Fusion.pdf
sha256: db56561df3309c5c96931ab178a78b6f230860bcc5a1c220e8a815cb89bf472e
size_bytes: 1442490
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 81669

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-024-02194-x"
year: 2024
title: "Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALM::MLLT10 Fusion"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ma(2024) Leukemia; Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALM MLLT10 Fusion.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genomic and gene expression profiling of 20 PICALM::MLLT10-positive acute leukemias - 10 AML, 8 T-ALL/LLy, 1 mixed-phenotype and 1 acute undifferentiated. Beyond confirming HOXA activation, differential expression against hematopoietic stem cells showed enrichment of proliferation pathways and relatively high XPO1 expression in both PM-AML and PM-T-ALL/LLy. PHF6 disruption emerged as a key cooperating event across immunophenotypes. The two groups form distinct transcriptomic classes with markedly different co-mutation spectra: TP53 and NF1 alterations characterise PM-AML and associate with progression and relapse, while EZH2 alterations are enriched in PM-T-ALL/LLy.

## Summary

A rare-entity study whose value is in showing that one fusion produces two diseases. PICALM::MLLT10 occurs across lineages, and the question is whether the resulting leukemias are variants of one thing; the answer here is no - the transcriptomes separate and the co-mutation spectra barely overlap, with TP53, NF1 and SUZ12 almost exclusive to the AML side and EZH2, NOTCH, JAK-STAT and CDKN2A to the T-ALL side.

That matters clinically because the outcomes diverge sharply: in the international cohort the authors cite, five-year survival was 76% for ALL and 26% for AML, and their own cohort matches (7 of 8 versus 2 of 10 alive). What the two share is HOXA activation and PHF6 disruption, the most frequently mutated gene here regardless of immunophenotype. The observation of high XPO1 expression connects to the XPO1-dependency work elsewhere in this collection.

## Key points

- One fusion, two diseases: PM-AML and PM-T-ALL/LLy form distinct transcriptomic groups with near-disjoint co-mutation spectra.
- Shared features are HOXA activation, PHF6 disruption - the most frequently mutated gene in the cohort - and relatively high XPO1 expression.
- TP53, NF1 and SUZ12 alterations are essentially confined to PM-AML and associate with progression and relapse.
- EZH2, NOTCH, JAK-STAT and CDKN2A alterations are enriched in PM-T-ALL/LLy and rare in PM-AML.
- Outcomes diverge sharply: 7 of 8 T-ALL/LLy patients alive versus 2 of 10 AML patients, consistent with a larger international series.

## Limitations

Twenty patients across four disease categories, so each subgroup is very small and the co-mutation associations rest on a handful of cases each; the near-exclusivity of TP53/NF1 to AML and EZH2 to T-ALL could shift substantially with more patients. Retrospective and descriptive, with no functional work: PHF6 disruption is nominated as a key cooperating event from mutation frequency, not tested. The cohort differs notably from the international series in extramedullary disease (7 of 10 versus 2 of 35 AML patients), suggesting referral or ascertainment bias at this single centre. Their gamma-delta T-ALL cases did not show the poor outcome prior work predicted, which the authors attribute to genetic heterogeneity - a plausible but untested explanation for a discrepancy in five patients.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ma(2024) Leukemia; Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALM MLLT10 Fusion.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-024-02194-x`; the prose sections were written here from the paper itself.

## Citation

Ma et al. Leukemia 2024. Genomic and global gene expression profiling in pediatric and young adult acute leukemia with PICALM::MLLT10 Fusion. doi: 10.1038/s41375-024-02194-x

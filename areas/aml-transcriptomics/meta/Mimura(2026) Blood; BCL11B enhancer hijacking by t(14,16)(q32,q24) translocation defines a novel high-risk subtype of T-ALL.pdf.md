---
# --- identity ------------------------------------------------
id: 2026-01-01_mimura-2026-blood-bcl11b-enhancer-hijack
id_basis: filename-year
source: Mimura(2026) Blood; BCL11B enhancer hijacking by t(14,16)(q32,q24) translocation defines a novel high-risk subtype of T-ALL.pdf
sha256: 6b5aebd339f60e616de52dfe70089276609d0443696a6d410fee7753618a56b9
size_bytes: 382697
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 15909

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025031466"
year: 2026
title: "BCL11B enhancer hijacking by t(14;16)(q32;q24) translocation defines a novel high-risk subtype of T-ALL"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Mimura(2026) Blood; BCL11B enhancer hijacking by t(14 16)(q32 q24) translocation defines a novel high-risk subtype of T-ALL.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Integrated whole-genome and whole-transcriptome analysis of pediatric and adult T-ALL and mixed-phenotype acute leukemias identified 14 patients with predominantly T-lineage disease driven by a t(14;16)(q32;q24) translocation, with universal GATA3 mutations and CDKN2A/B deletions. The translocation repositions the ThymoD locus downstream of BCL11B, causing monoallelic ectopic overexpression of FENDRR and the mesenchymal transcription factors FOXF1 and FOXC2 and activating epithelial-mesenchymal transition signatures. Immunophenotyping and single-cell RNA sequencing show marked lineage ambiguity with myeloid and B-cell differentiation potential, and FOXF1 overexpression in CD34+ cord blood cells promotes myeloid while suppressing T-cell differentiation. The subtype occurs in 0.15% to 4.0% of cases, median age 15, with extremely poor prognosis.

## Summary

A new leukemia subtype defined by enhancer hijacking rather than by a fusion gene - the translocation moves a T-cell regulatory region so that it drives genes it should never touch. What it drives is unexpected: FOXF1 and FOXC2 are mesenchymal transcription factors not previously implicated in leukemia, and they impose an EMT-like program on a blood cancer.

The functional experiment is what elevates this above a descriptive genomics finding. Overexpressing FOXF1 in normal CD34+ cord blood cells promotes myeloid and suppresses T-cell differentiation, which explains the lineage ambiguity observed in patients rather than merely reporting it. The clinical case is that these patients do worse than the recognised high-risk groups, and at a median age of 15 they concentrate in adolescents and young adults.

## Key points

- A new T-ALL/MPAL subtype defined by t(14;16)(q32;q24) enhancer hijacking, with universal GATA3 mutation and CDKN2A/B deletion.
- The ThymoD locus is repositioned downstream of BCL11B, driving monoallelic overexpression of FENDRR, FOXF1 and FOXC2.
- FOXF1 and FOXC2 are mesenchymal factors not previously implicated in leukemia; they activate EMT transcriptional signatures.
- FOXF1 overexpression in CD34+ cord blood cells promotes myeloid and suppresses T-cell differentiation, explaining the lineage ambiguity.
- Prognosis trends worse than KMT2A-rearranged ETP-like, SPI1-rearranged and LMO2 gamma-delta-like T-ALL; median age 15 years.

## Limitations

Fourteen patients, assembled across multiple cohorts, and the reported frequency spans 0.15% to 4.0% depending on cohort - a 27-fold range that reflects how differently these cases are ascertained and makes the true prevalence unclear. The prognostic claim is a trend toward worse outcomes than other high-risk groups, not a significant difference, in a sample this size. The functional work establishes that FOXF1 can redirect differentiation in cord blood progenitors, not that it is required for the leukemia or sufficient to cause it. This record's text was captured through a publisher proxy and is partially garbled, with the discussion truncated mid-sentence. The subtype is predominantly T-lineage, so its direct relevance to the AML focus of this collection is as a lineage-ambiguity and enhancer-hijacking case rather than as AML.

## Provenance

Located in the published literature, dropped into `inbox/` as `Mimura(2026) Blood; BCL11B enhancer hijacking by t(14 16)(q32 q24) translocation defines a novel high-risk subtype of T-ALL.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025031466`; the prose sections were written here from the paper itself.

## Citation

Mimura et al. Blood 2026. <i>BCL11B</i>
                    enhancer hijacking by t(14;16)(q32;q24) translocation defines a novel high-risk subtype of T-ALL. doi: 10.1182/blood.2025031466

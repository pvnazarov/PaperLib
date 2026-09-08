---
# --- identity ------------------------------------------------
id: 2026-01-01_salah-2026-european-journal-of-haematolo
id_basis: filename-year
source: Salah(2026) European Journal of Haematology; Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia.pdf
sha256: 8dd161e42220cced56804cd54060640ff320618471875a10186e1d4d97e4cec8
size_bytes: 2206612
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 131273

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1111/ejh.70230"
year: 2026
title: "Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Salah(2026) Eur J Haematol; Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of the molecular and epigenetic landscape of pediatric AML, which accounts for 15-20% of childhood leukemias and where survival for high-risk patients remains below 60%. It covers the distinct genetic profile of pediatric relative to adult disease - FLT3-ITD, NPM1, KMT2A rearrangements and core-binding factor fusions - alongside aberrant DNA methylation, histone modifications and non-coding RNA expression. It surveys how computational RNA-seq pipelines and pathway analyses have highlighted DNMT3A, TET2 and HDACs as candidate targets, and how multi-omics combining transcriptomic, methylomic and chromatin accessibility data is being used to define biomarkers.

## Summary

A survey of the in silico literature on pediatric AML, and its most valuable section is the one criticising that literature. The authors set out the methodological problems plainly: sequencing depth and normalisation differ between studies so cross-study comparison and meta-analysis are compromised; low-abundance transcripts and non-coding RNAs are captured inconsistently; and pediatric AML cohorts are small while the transcriptomic differences being sought are subtle.

The sharpest point is about validation. Many studies report differentially expressed genes, fusion signatures and candidate targets from computation alone, without RT-qPCR, western blotting, proteomics or functional assay - and since transcript abundance does not track protein abundance, it remains unknown whether the reported alterations are biologically real. That caution applies directly to several computational papers elsewhere in this collection.

## Key points

- Pediatric AML is genetically distinct from adult disease, so adult findings and risk models do not transfer directly.
- Surveys epigenetic dysregulation - DNA methylation, histone marks, non-coding RNA - alongside the recurrent genetic lesions.
- Names DNMT3A, TET2 and HDACs as the epigenetic targets most often nominated by computational analyses.
- States the methodological problems of the in silico literature: batch, depth and normalisation differences, small cohorts, subtle effects.
- Emphasises that most transcriptomic findings lack orthogonal experimental validation, and that transcript level does not imply protein level or function.

## Limitations

A narrative review with no systematic search or evidence appraisal, and it reviews computational studies rather than generating or validating anything. Its therapeutic section is a survey of rationales - DNMT, HDAC, BET and EZH2 inhibitors are said to hold promise for reprogramming malignant cells - which is optimistic given that HDAC and DNMT inhibitors have a long record of modest results in AML. The criticisms it makes of the field apply to much of what it summarises, so the reader is left with a literature the review itself describes as inadequately validated. Coverage of pediatric-specific work is thinner than the framing implies, since much of the underlying data comes from general AML resources.

## Provenance

Located in the published literature, dropped into `inbox/` as `Salah(2026) Eur J Haematol; Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1111/ejh.70230`; the prose sections were written here from the paper itself.

## Citation

Salah et al. European Journal of Haematology 2026. Epigenetics and In Silico Transcriptome Analysis of Pediatric Acute Myeloid Leukemia. doi: 10.1111/ejh.70230

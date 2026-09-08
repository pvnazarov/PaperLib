---
# --- identity ------------------------------------------------
id: 2025-01-01_zhou-2025-data-in-brief-iso-seq-and-rna
id_basis: filename-year
source: Zhou(2025) Data in Brief; Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene.pdf
sha256: 5eb68beff6a950b4373f4daa9dd24b100ae61aec3e14ea4db2810fa3912602fc
size_bytes: 295755
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 20421

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.dib.2025.112048"
year: 2025
title: "Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zhou(2025) Data Brief; Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A data article describing PacBio single-molecule long-read isoform sequencing and Illumina short-read RNA sequencing of ML-2 AML cells stably overexpressing ZCCHC10, a zinc finger CCHC-type protein reported to act as a tumour suppressor in AML, against cells overexpressing an empty vector. The Iso-seq data provide full-length transcripts allowing identification of mRNA isoforms and of alternative transcription initiation, alternative splicing and alternative polyadenylation; the RNA-seq data provide transcript profiles showing the effects of ZCCHC10 overexpression on gene expression. Both datasets are deposited in the SRA.

## Summary

A dataset description rather than a research paper - the Data in Brief format exists to make data reusable and citable, and this one supplies paired long-read and short-read transcriptomes from an isogenic pair differing only in ZCCHC10 expression.

Its value in this collection is as a resource for the alternative-processing questions that several primary papers here pursue. Pairing Iso-seq with RNA-seq is the right combination: long reads resolve complete transcript structures while short reads give the quantification depth those structures need to be measured. The premise is that ZCCHC10 is a tumour suppressor in AML whose mechanism is unknown, and that many ZCCHC proteins act in RNA metabolism - so its overexpression is used to expose whatever processing changes it causes.

## Key points

- Paired PacBio Iso-seq and Illumina RNA-seq from ML-2 AML cells overexpressing ZCCHC10 versus empty vector.
- Long reads resolve full transcript structures, permitting analysis of alternative initiation, splicing and polyadenylation.
- Short reads supply the quantification depth needed to measure those structures.
- Premised on ZCCHC10 acting as an AML tumour suppressor by an unknown mechanism, with related ZCCHC proteins acting in RNA metabolism.
- Both datasets deposited in the SRA for reuse.

## Limitations

A data article, not a study: it reports no biological finding, tests no hypothesis, and draws no conclusion about ZCCHC10's mechanism - the analyses it enables are left to whoever reuses the data. The system is a single AML cell line with stable overexpression from a vector, so any processing changes observed reflect supraphysiological ZCCHC10 rather than its endogenous function, and there is no knockdown or knockout arm. No primary patient material. The article states 'Limitations: None', which is a convention of the format rather than an accurate statement about what these data can support.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zhou(2025) Data Brief; Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.dib.2025.112048`; the prose sections were written here from the paper itself.

## Citation

Zhou et al. Data in Brief 2025. Iso-seq and RNA-seq data from ML-2 acute myeloid leukemia cells overexpressing the ZCCHC10 gene. doi: 10.1016/j.dib.2025.112048

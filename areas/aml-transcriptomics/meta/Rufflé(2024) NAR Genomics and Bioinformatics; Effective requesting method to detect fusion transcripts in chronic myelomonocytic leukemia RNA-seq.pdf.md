---
# --- identity ------------------------------------------------
id: 2024-01-01_ruffl-2024-nar-genomics-and-bioinformati
id_basis: filename-year
source: Rufflé(2024) NAR Genomics and Bioinformatics; Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq.pdf
sha256: 1cceb2c2519aaf15280267c1a941a4dc16423ea43237be93314f0b99d9eafa51
size_bytes: 1724570
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 65794

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nargab/lqae117"
year: 2024
title: "Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Rufflé(2024) NAR Genom Bioinform; Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An integrated k-mer approach querying indexed RNA-seq datasets, combining short- and long-read analysis, is used to detect chimeric RNAs in chronic myelomonocytic leukemia. Applying CRAC tools with basic filters identified 1787 chimeric RNAs in four classes, from which four were selected and validated in CMML cells. The authors focus on NRIP1-MIR99AHG, also recently detected in AML, showing it encodes three isoforms including a novel one. Stringency is placed on tissue specificity of expression rather than on initial filters, using chimeric k-mer counts compared quantitatively across indexed datasets via the transipedia interface.

## Summary

A methodological inversion worth noting: rather than filter candidates stringently at detection, they keep a large permissive set and impose stringency through tumour specificity, comparing chimeric k-mer presence across many indexed datasets. That turns the selection criterion from 'does this look like a real junction' into 'does this occur in tumour and not elsewhere', which is closer to what a biomarker actually needs.

The clinical motivation is specific to CMML: driver mutations are found in essentially every patient, but cytogenetic abnormalities in only about a third, so the stratification tools are unbalanced - and predicting transformation to AML remains difficult. Chimeric transcripts are proposed as an additional class of molecular abnormality that might fill that gap. NRIP1-MIR99AHG being found in AML as well is what makes it the candidate they pursue.

## Key points

- k-mer querying of indexed RNA-seq datasets allows chimeric transcripts to be compared quantitatively across many samples at once.
- Stringency is applied through tumour specificity of expression rather than through restrictive initial filters.
- 1787 chimeric RNAs in four classes were identified in CMML; four were validated.
- NRIP1-MIR99AHG, also reported in AML, encodes three isoforms including one novel.
- Addresses a real gap in CMML, where driver mutations are near-universal but cytogenetic abnormalities are found in only a third of cases.

## Limitations

Four validated chimeras from 1787 candidates, and no attempt to estimate the false discovery rate across the remainder - so the catalogue's reliability is unknown. The biological significance of NRIP1-MIR99AHG is explicitly left for future work; nothing here shows it is expressed at functional levels, translated, or associated with outcome or transformation. Sample numbers are small and the tumour-specificity criterion depends on which datasets happen to be indexed, so a chimera present in an untested tissue would appear specific. The approach detects transcripts but does not establish whether they arise from genomic rearrangement or from transcriptional mechanisms, which matters for their use as clonal markers. No clinical stratification is tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Rufflé(2024) NAR Genom Bioinform; Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nargab/lqae117`; the prose sections were written here from the paper itself.

## Citation

Rufflé et al. NAR Genomics and Bioinformatics 2024. Effective requesting method to detect fusion transcripts in chronic myelomonocytic leukemia RNA-seq. doi: 10.1093/nargab/lqae117

---
# --- identity ------------------------------------------------
id: 2025-01-01_khan-2025-scientific-reports-revealing-t
id_basis: filename-year
source: Khan(2025) Scientific Reports; Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics.pdf
sha256: 8e53b755f97581541609281077b0f10229ec59e053fc32d33559899cda6baca0
size_bytes: 5769334
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 74058

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41598-025-99865-1"
year: 2025
title: "Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Khan(2025) Sci Rep; Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

U2AF1, the splicing factor that recognises 3' splice sites and is recurrently mutated in MDS and AML, is examined for its role in chimeric RNA formation. Using knockdown and overexpression in leukemia and esophageal cancer cell lines with paired-end RNA sequencing and the SOAPfuse algorithm, the authors report significant changes in the chimeric RNA landscape following U2AF1 knockdown, concluding that U2AF1 has a critical role in the formation and regulation of distinct categories of chimeric RNA.

## Summary

Extends the question about splicing factor mutations from ordinary alternative splicing to chimeric RNAs - transcripts joining sequence from two genes without an underlying DNA rearrangement, including cis-splicing between adjacent genes. That matters practically for AML transcriptomics, where a chimeric read is normally interpreted as evidence of a fusion gene: if a splicing factor perturbation can generate chimeric transcripts without any translocation, some detected fusions may not correspond to genomic events.

The study is a straightforward perturbation-and-sequence design, and its contribution is the observation that the chimeric landscape moves substantially with U2AF1 levels.

## Key points

- Connects a recurrently mutated splicing factor to chimeric RNA formation, not only to conventional alternative splicing.
- Knockdown and overexpression in leukemia and esophageal cancer cell lines, with paired-end RNA-seq and SOAPfuse detection.
- Different categories of chimeric RNA respond differently to U2AF1 perturbation.
- Relevant to fusion detection in AML transcriptomics, where chimeric reads are usually taken to imply a genomic rearrangement.
- Proposed as a source of candidate biomarkers, though the paper stops short of nominating any.

## Limitations

Cell lines only, with no primary patient material and no in vivo work, so nothing establishes relevance to human MDS or AML. The experiments manipulate U2AF1 levels by knockdown and overexpression rather than modelling the recurrent hotspot mutations (S34F, Q157) that actually occur in patients - and those are neomorphic, so altering abundance is not the same perturbation. Chimeric RNA detection from short reads is notoriously prone to false positives, and no orthogonal validation of the detected chimeras is described; a single caller, SOAPfuse, is used. No chimeric RNA is shown to be translated or to have any function, so the biomarker and therapeutic framing in the conclusion is aspiration rather than result. Raw data are available only on request from the corresponding author.

## Provenance

Located in the published literature, dropped into `inbox/` as `Khan(2025) Sci Rep; Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41598-025-99865-1`; the prose sections were written here from the paper itself.

## Citation

Khan et al. Scientific Reports 2025. Revealing the role of U2AF1 in splicing regulation and chimeric RNA dynamics. doi: 10.1038/s41598-025-99865-1

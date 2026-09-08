---
# --- identity ------------------------------------------------
id: 2017-01-01_ruffl-2017-f1000research-new-chimeric-rn
id_basis: filename-year
source: Rufflé(2017) F1000Research; New chimeric RNAs in acute myeloid leukemia.pdf
sha256: ea634e50679cc080c9bd00c61f851fecb984f045b65ad3097fb3796cc47d02b7
size_bytes: 5203569
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 106788

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.12688/f1000research.11352.1"
year: 2017
title: "New chimeric RNAs in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Rufflé(2017) F1000Res; New chimeric RNAs in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using Crac, a tool that infers splice and chimeric junctions within a single read from genomic locations and local coverage, with CracTools to aggregate, annotate and filter, the authors detect chimeric RNAs in AML RNA-seq irrespective of annotation. Seventeen chimeric RNAs were identified and validated by real-time PCR and sequencing across three AML patients: ten from a t(15;17) patient, four from a normal-karyotype patient and three from an inv(16) patient. The new fusion transcripts fall into four groups by exon organisation, suggesting distinct synthesis mechanisms, and tumour-specific expression was checked against a public dataset using a tag search approach.

## Summary

Broadens what counts as a fusion transcript. Chimeric RNAs used diagnostically are almost all products of chromosomal translocation, but transcripts joining two genes also arise from read-through, cis- and trans-splicing, and other mechanisms - and this classifies detected chimeras into categories tied to their likely biogenesis rather than treating them as one class.

The authors are appropriately preoccupied with the central methodological problem, which is that false positives dominate this field: reverse transcription and PCR artefacts during library preparation, plus mapping artefacts against a repetitive reference. Their response is to validate every reported candidate by PCR and sequencing, and to build a benchmarking system for calibrating detection pipelines - a more honest engagement with the error mode than simply reporting a long candidate list.

## Key points

- Detects chimeric RNAs from single reads without relying on annotation, using Crac and CracTools.
- Seventeen chimeras identified and experimentally validated across three AML patients with different karyotypes.
- Classifies chimeras into four groups by exon organisation, linked to distinct biogenesis mechanisms.
- Extends the diagnostic concept beyond translocation-derived fusions to read-through, cis- and trans-splicing products.
- Addresses the false-positive problem directly, with PCR validation and a benchmarking system for pipeline selection.

## Limitations

Three patients, so this is a methods demonstration rather than a survey of chimeric RNA in AML, and no frequency or clinical association can be drawn from it. None of the seventeen validated chimeras is shown to be functional, translated or clinically informative - the diagnostic potential is argued, not demonstrated. Validation confirms that a chimeric junction exists in the RNA, which does not exclude that it arose during library preparation in a reproducible way. The benchmarking system and machine learning model are described as personal data submitted elsewhere, so they cannot be assessed here. Published in an F1000Research post-publication review format at version 2, with two approving referees.

## Provenance

Located in the published literature, dropped into `inbox/` as `Rufflé(2017) F1000Res; New chimeric RNAs in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.12688/f1000research.11352.1`; the prose sections were written here from the paper itself.

## Citation

Rufflé et al. F1000Research 2017. New chimeric RNAs in acute myeloid leukemia. doi: 10.12688/f1000research.11352.1

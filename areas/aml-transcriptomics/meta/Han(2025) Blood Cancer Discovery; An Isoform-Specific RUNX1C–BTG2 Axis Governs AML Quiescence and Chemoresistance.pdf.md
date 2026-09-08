---
# --- identity ------------------------------------------------
id: 2025-01-01_han-2025-blood-cancer-discovery-an-isofo
id_basis: filename-year
source: Han(2025) Blood Cancer Discovery; An Isoform-Specific RUNX1C–BTG2 Axis Governs AML Quiescence and Chemoresistance.pdf
sha256: fc5c4a672001f5be369a2fee68f573511665664ea5660ae6fbfed458b740f3d6
size_bytes: 9920260
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 222549

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2643-3230.BCD-24-0327"
year: 2025
title: "An Isoform-Specific RUNX1C–BTG2 Axis Governs AML Quiescence and Chemoresistance"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Han(2025) Blood Cancer Discov; An Isoform-Specific RUNX1C-BTG2 Axis Governs AML Quiescence and Chemoresistance.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A paired analysis of RNA isoform changes in AML patients before therapy and at relapse identifies intragenic DNA methylation at the proximal RUNX1 promoter, driving elevated expression of the long isoform RUNX1C from its alternative distal promoter. The unique N-terminal region of RUNX1C directs an isoform-specific transcriptional program promoting chemoresistance, with the direct target BTG2 implicated: BTG2 promotes rRNA deadenylation, decreasing mRNA expression and stability, and increasing cellular quiescence. RNA-based targeting of RUNX1C reactivates quiescent leukemia cells and enhances chemotherapy efficacy.

## Summary

Addresses the awkward fact that relapsed AML is genomically rather quiet - few new mutations - which implies non-genetic mechanisms of resistance. Here the mechanism is isoform choice at a single locus: the same gene, a different promoter, a different N-terminus, and a different transcriptional program.

The therapeutic logic is inverted from the usual and worth noting. Rather than killing the resistant cells directly, targeting RUNX1C pushes them out of quiescence, which restores their sensitivity to chemotherapy that only works on cycling cells. That makes it a sensitiser rather than a cytotoxic. The paired before/after patient design is the right way to find something that only appears under treatment pressure.

## Key points

- Paired pre-treatment and relapse patient samples identify isoform switching, not mutation, as a resistance mechanism.
- Intragenic methylation at the proximal RUNX1 promoter shifts expression to the long RUNX1C isoform via its distal promoter.
- The RUNX1C-specific N-terminus drives a distinct program including BTG2, which is not engaged by other RUNX1 isoforms.
- BTG2 promotes rRNA deadenylation and reduced protein synthesis, producing a quiescent, chemoresistant state.
- RNA-based targeting of RUNX1C forces cells out of quiescence and resensitises them to chemotherapy.

## Limitations

The therapeutic route is antisense oligonucleotide targeting, and the authors are candid that RNA therapeutics remain limited by poor stability and inefficient delivery to tumour cells in vivo - so the strategy's feasibility is the main open question. Their own data show RUNX1C also upregulates interferon-gamma signalling including IFITM1/2/3, genes independently linked to drug resistance, so the BTG2 axis is one of several possible mechanisms and its relative contribution is not quantified; the authors say this needs future study. Waking quiescent leukemia cells is a strategy with an obvious risk if chemotherapy does not then eliminate them. The paired relapse cohort size is not large, and isoform quantification from short-read RNA-seq is error-prone for distinguishing promoter-driven isoforms.

## Provenance

Located in the published literature, dropped into `inbox/` as `Han(2025) Blood Cancer Discov; An Isoform-Specific RUNX1C-BTG2 Axis Governs AML Quiescence and Chemoresistance.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2643-3230.BCD-24-0327`; the prose sections were written here from the paper itself.

## Citation

Han et al. Blood Cancer Discovery 2025. An Isoform-Specific RUNX1C–BTG2 Axis Governs AML Quiescence and Chemoresistance. doi: 10.1158/2643-3230.BCD-24-0327

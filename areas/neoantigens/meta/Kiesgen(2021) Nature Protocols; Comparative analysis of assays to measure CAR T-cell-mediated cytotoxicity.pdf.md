---
# --- identity ------------------------------------------------
id: 2021-01-01_kiesgen-2021-nature-protocols-comparativ
id_basis: filename-year
source: Kiesgen(2021) Nature Protocols; Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity.pdf
sha256: 96571453692d9135631a6243353fc56217ce369310184381567a9dd42abd1252
size_bytes: 641939
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 122760

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41596-020-00467-0"
year: 2021
title: "Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41596-020-00467-0.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A comparative review of in vitro cytotoxicity assays for engineered T cells - chromium release, bioluminescence, impedance and flow cytometry - covering experimental setup, appropriate uses, advantages, disadvantages and ways to compensate for each one's limitations, together with FDA directives for a potency assay for clinical cell therapy release.

## Summary

This is a measurement-methods paper, and it is in the collection because nearly every immunogenicity claim elsewhere here ultimately rests on a cytotoxicity or cytokine readout. Which assay was used, at what effector-to-target ratio and over what time, changes the number that gets reported as 'immunogenic'.

It also covers advanced designs - repeated antigen exposure, heterogeneous targets with variable antigen expression - that are closer to what a T cell meets in a tumour than a single-timepoint killing assay.

## Key points

- Compares four assay families on setup, endpoint, throughput, automatability and ability to measure killing of heterogeneous targets.
- Covers FDA requirements for a potency assay for clinical release, which constrains what is usable in translation.
- Discusses repeated antigen exposure assays, which reveal exhaustion that single-exposure assays miss.
- Supplies the measurement context for the immunogenicity labels the predictors in this collection are trained on.

## Limitations

A review of methods: it compares assays rather than validating any, and every quantitative claim belongs to a cited study. It is written for CAR and TCR T-cell products, so its emphasis differs from the ELISpot and multimer readouts most neoantigen work uses. In vitro cytotoxicity of any kind is a proxy for tumour control in a patient, which is the comparison that matters and the one it cannot make.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41596-020-00467-0.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41596-020-00467-0`; the prose sections were written here from the paper itself.

## Citation

Kiesgen et al. Nature Protocols 2021. Comparative analysis of assays to measure CAR T-cell-mediated cytotoxicity. doi: 10.1038/s41596-020-00467-0

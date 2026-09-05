---
# --- identity ------------------------------------------------
id: 2020-01-01_ott-2020-cell-a-phase-ib-trial-of-person
id_basis: filename-year
source: Ott(2020) Cell; A Phase Ib Trial of Personalized Neoantigen Therapy Plus Anti-PD-1 in Patients with Advanced Melanoma, Non-small Cell Lung Cancer, or Bladder Cancer.pdf
sha256: cdca65d3c0f73678dab1a0f94669e0ffa50b6e069fa0948f0e7b67cec38d1bc4
size_bytes: 7968539
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 169559

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2020.08.053"
year: 2020
title: "A Phase Ib Trial of Personalized Neoantigen Therapy Plus Anti-PD-1 in Patients with Advanced Melanoma, Non-small Cell Lung Cancer, or Bladder Cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS0092867420311417.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A phase Ib trial of the personalised neoantigen vaccine NEO-PV-01 plus nivolumab in advanced melanoma, NSCLC and bladder cancer. The combination was feasible and safe, induced durable neoantigen-specific T cell reactivity with cytotoxic potential, and produced T cells that trafficked to tumours; epitope spread and major pathologic responses were observed.

## Summary

This extends personal neoantigen vaccination from the adjuvant setting into advanced disease and combines it with checkpoint blockade, which is the pairing most likely to be used clinically.

Three things are shown that the earlier trials could not: vaccine-induced T cells persist, they have cytotoxic potential rather than merely being detectable, and they can be found in the tumour. Epitope spread is also reported, consistent with vaccine-driven tumour killing releasing further antigens.

## Key points

- Three tumour types, combined with anti-PD-1 rather than given alone.
- Vaccine-induced T cells persist, show cytotoxic potential, and traffic to the tumour.
- Epitope spreading observed, consistent with vaccine-mediated tumour cytotoxicity - agreeing with Hu (2021) and contrasting with Sethna (2025) in PDAC.
- Major pathologic tumour responses detected after vaccination.

## Limitations

The authors state the central one: the trial is single-arm with no nivolumab monotherapy comparator, so deepening radiographic responses, epitope spread and major pathologic responses cannot definitively be attributed to the vaccine rather than to anti-PD-1. They note randomised trials against anti-PD-1 monotherapy will be necessary - which KEYNOTE-942, also in this collection, later provided for melanoma.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS0092867420311417.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2020.08.053`; the prose sections were written here from the paper itself.

## Citation

Ott et al. Cell 2020. A Phase Ib Trial of Personalized Neoantigen Therapy Plus Anti-PD-1 in Patients with Advanced Melanoma, Non-small Cell Lung Cancer, or Bladder Cancer. doi: 10.1016/j.cell.2020.08.053

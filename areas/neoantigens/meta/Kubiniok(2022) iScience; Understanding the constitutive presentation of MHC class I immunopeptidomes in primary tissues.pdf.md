---
# --- identity ------------------------------------------------
id: 2022-01-01_kubiniok-2022-iscience-understanding-the
id_basis: filename-year
source: Kubiniok(2022) iScience; Understanding the constitutive presentation of MHC class I immunopeptidomes in primary tissues.pdf
sha256: cf79d5407117a25f6107827aeffb94836b6e7f33f9cd7b2d4422242f57af7f8c
size_bytes: 3611520
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 123542

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.isci.2022.103768"
year: 2022
title: "Understanding the constitutive presentation of MHC class I immunopeptidomes in primary tissues"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS2589004222000384.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A global analysis of MHC-I immunopeptidomes across 29 human and 19 mouse primary tissues. HLA-A, -B and -C allotypes contribute unevenly to the immunopeptidome; tissue-specific and housekeeping peptides have distinct properties; evolutionarily hyperconserved proteins are the primary source at organism scale; and new antigen-processing components are identified, including carboxypeptidases CPE, CNDP1/2 and CPVL.

## Summary

The organism-wide framing is what distinguishes this. Most immunopeptidomics is one tissue or one cell line; sampling dozens of tissues in two species allows statements about which peptides are shared and which are local, and shows most are tissue-specific with a smaller shared core.

Shared peptides turn out to be highly abundant and strong MHC-I binders, which is a warning for target selection: peptides that are easiest to detect and best predicted are also the ones most likely to be presented on healthy tissue somewhere.

## Key points

- 29 human and 19 mouse primary tissues - the first organism-level estimate of tissue-specific versus shared MHC-I peptides.
- HLA-A, -B and -C do not contribute evenly to the immunopeptidome, so per-locus prediction quality has uneven consequences.
- Peptides shared across tissues are abundant, strong binders - the profile of an attractive but unsafe target.
- Identifies new antigen-processing components (CPE, CNDP1/2, CPVL) beyond the canonical pathway.

## Limitations

The authors give an explicit limitations section: bulk tissues were used, so contributions of stromal versus resident cells cannot be separated, and a peptide attributed to a tissue may come from any cell type in it. Mass-spectrometry detection bias applies throughout. Being cross-sectional it describes constitutive presentation, not how the immunopeptidome changes under inflammation or interferon - the state that matters for tumours.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS2589004222000384.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.isci.2022.103768`; the prose sections were written here from the paper itself.

## Citation

Kubiniok et al. iScience 2022. Understanding the constitutive presentation of MHC class I immunopeptidomes in primary tissues. doi: 10.1016/j.isci.2022.103768

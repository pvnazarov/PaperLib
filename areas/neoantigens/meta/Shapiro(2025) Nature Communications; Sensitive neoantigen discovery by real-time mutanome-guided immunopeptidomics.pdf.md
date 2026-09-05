---
# --- identity ------------------------------------------------
id: 2025-01-01_shapiro-2025-nature-communications-sensi
id_basis: filename-year
source: Shapiro(2025) Nature Communications; Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics.pdf
sha256: 2ea452a32150685f95f96e61dbf82bc5ce916c00a02cd2bc31ce043be6ebf44b
size_bytes: 1844696
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 177735

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-025-62647-4"
year: 2025
title: "Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41467-025-62647-4.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoDiscMS extends NeoDisc to personalised immunopeptidomics, using next-generation-sequencing-guided real-time spectral acquisition to maximise sensitivity with minimal loss of global depth. It improves detection of tumour-associated-antigen-derived peptides by up to 20% and increases confidence in neoantigen identifications.

## Summary

The instrument decides what it fragments while the sample is running, guided by the patient's own mutanome from sequencing - so the mass spectrometer is told in advance which masses matter rather than selecting by abundance alone.

That matters because neoantigens are low-abundance by nature, and conventional data-dependent acquisition preferentially fragments what is plentiful. The trade the paper optimises explicitly is target sensitivity against global coverage, which most targeted methods sacrifice entirely.

## Key points

- Real-time, sequencing-guided acquisition: the mutanome steers the instrument during the run.
- Up to 20% better detection of tumour-associated-antigen peptides, without abandoning global depth.
- Spike-in free, unlike targeted approaches that need heavy-labelled standards.
- Designed for clinical constraints - scarce sample input, short turnaround, minimal manual data processing.

## Limitations

The authors survey why previous sensitivity approaches fall short and their own inherits some of the same ceiling: co-isolated precursors limit sensitivity for low-abundance targets even in narrow-window acquisition, and they note chimeric spectrum deconvolution, used in low-input proteomics, has not yet been implemented for immunopeptidomics. Detecting a presented peptide is not showing it is immunogenic. Sample input remains the binding constraint for clinical use.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41467-025-62647-4.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-025-62647-4`; the prose sections were written here from the paper itself.

## Citation

Shapiro et al. Nature Communications 2025. Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics. doi: 10.1038/s41467-025-62647-4

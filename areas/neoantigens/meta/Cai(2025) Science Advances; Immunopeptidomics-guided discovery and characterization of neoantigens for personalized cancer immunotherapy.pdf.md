---
# --- identity ------------------------------------------------
id: 2025-01-01_cai-2025-science-advances-immunopeptidom
id_basis: filename-year
source: Cai(2025) Science Advances; Immunopeptidomics-guided discovery and characterization of neoantigens for personalized cancer immunotherapy.pdf
sha256: f3b0628204fdf303525eae837be5d3ffea5345b36d8dabcac9198a7f703ad8ad
size_bytes: 6060776
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 101434

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/sciadv.adv6445"
year: 2025
title: "Immunopeptidomics-guided discovery and characterization of neoantigens for personalized cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Cai_Sci_Adv_Immunopeptidomics_guided_discovery_and_charact_PMID40397742.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A pan-cancer peptide atlas assembled from immunopeptidomics of 531 samples across 14 cancer and 29 normal tissue types yields 389,165 canonical and 70,270 noncanonical peptides. The authors build MaNeo, a machine-learning screening pipeline over this atlas, and validate three predicted neo-peptides that induce T cell proliferation and killing of cancer cells but not healthy cells.

## Summary

The motivating gap is 'cold' tumours with too few nonsynonymous mutations to yield conventional neoepitopes. Noncanonical peptides - from UTRs, noncoding genes and alternative translation - are a second source of targets, and the atlas is built to make them findable.

Noncanonical peptides are reported at presentation levels comparable to canonical ones, and tumour-specific peptides differ in biochemical character from normal-tissue peptides, which is what MaNeo exploits to prioritise candidates.

## Key points

- 531 samples across 14 cancer and 29 normal tissue types; 389,165 canonical and 70,270 noncanonical peptides.
- Noncanonical peptides show presentation levels comparable to canonical peptides across cancer types.
- The normal-tissue arm is what allows tumour specificity to be asserted rather than assumed - the usual weak point in neoantigen screens.
- Three predicted neo-peptides were validated functionally in cell lines, including a healthy-cell control.

## Limitations

Functional validation is three peptides in cancer cell lines, which is a demonstration rather than an estimate of the pipeline's precision. The authors note that transcriptome-based approaches cannot directly establish presentation, but mass spectrometry has its own detection bias against low-abundance and hydrophobic peptides, and that bias propagates into the atlas. Nothing here is tested in patients.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Cai_Sci_Adv_Immunopeptidomics_guided_discovery_and_charact_PMID40397742.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/sciadv.adv6445`; the prose sections were written here from the paper itself.

## Citation

Cai et al. Science Advances 2025. Immunopeptidomics-guided discovery and characterization of neoantigens for personalized cancer immunotherapy. doi: 10.1126/sciadv.adv6445

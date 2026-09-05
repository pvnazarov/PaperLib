---
# --- identity ------------------------------------------------
id: 2021-01-01_marcu-2021-journal-for-immunotherapy-of
id_basis: filename-year
source: Marcu(2021) Journal for ImmunoTherapy of Cancer; HLA Ligand Atlas a benign reference of HLA-presented peptides to improve T-cell-based cancer immunotherapy.pdf
sha256: 3135b9be29dbf79f094047774c9fab9e225d3b219846d6423b36a13edc698934
size_bytes: 3847745
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 130731

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1136/jitc-2020-002071"
year: 2021
title: "HLA Ligand Atlas: a benign reference of HLA-presented peptides to improve T-cell-based cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2021_Marcu_J_Immunother_Cancer_HLA_Ligand_Atlas_a_benign_reference_of_HLA_pre_PMID33858848.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The HLA Ligand Atlas is the first large paired HLA-I and HLA-II immunopeptidome collection from benign human tissue: 227 samples from 16 autopsy subjects plus thymus and ovary donors, over 1200 LC-MS runs, yielding 90,428 HLA-I and 142,625 HLA-II ligands across 51 HLA-I and 86 HLA-II allotypes.

## Summary

The motivation is a safety problem with a body count. Defining a tumour-associated antigen requires knowing what benign tissue presents, and because benign tissue is hard to obtain, tumour-adjacent normal tissue has been used as the surrogate - a substitution the authors note has proven insufficient and has resulted in lethal outcomes.

The atlas replaces that surrogate with an actual benign reference spanning many tissues, and finds immunopeptidomes differ considerably between tissues and between individuals at both source-protein and ligand level, which is precisely why a single adjacent-tissue comparison fails.

## Key points

- 227 benign tissue samples with paired HLA-I and HLA-II immunopeptidomes; allotypes representative of the world population.
- Directly motivated by lethal off-target outcomes from inadequate benign references.
- Immunopeptidomes vary substantially between tissues and between individuals - a single normal-tissue comparison is not enough.
- 1407 HLA-I ligands identified from non-canonical genomic regions, expanding the target space beyond the canonical proteome.

## Limitations

Autopsy tissue dominates the collection, and post-mortem interval affects the immunopeptidome in ways not fully characterised. Mass spectrometry detects what ionises well and misses low-abundance ligands, so absence from the atlas is weak evidence of absence in the tissue - the direction that matters most for a safety reference. The authors note they did not perform a large-scale statistical analysis to validate the observed HLA-I/HLA-II hotspot co-location.

## Provenance

Located in the published literature, dropped into `inbox/` as `2021_Marcu_J_Immunother_Cancer_HLA_Ligand_Atlas_a_benign_reference_of_HLA_pre_PMID33858848.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1136/jitc-2020-002071`; the prose sections were written here from the paper itself.

## Citation

Marcu et al. Journal for ImmunoTherapy of Cancer 2021. HLA Ligand Atlas: a benign reference of HLA-presented peptides to improve T-cell-based cancer immunotherapy. doi: 10.1136/jitc-2020-002071

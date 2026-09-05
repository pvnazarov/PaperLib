---
# --- identity ------------------------------------------------
id: 2026-01-01_yuan-2026-research-epimii-structure-awar
id_basis: filename-year
source: Yuan(2026) Research; EpiMII Structure-Aware Graph Neural Networks for MHC-II Epitope Generation.pdf
sha256: f175daa3b3c9e0707d0fc6bd7dbc227dce86f2ac030e42a174a47ae4c059ebdf
size_bytes: 28284769
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 185680

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.34133/research.1311"
year: 2026
title: "EpiMII: Structure-Aware Graph Neural Networks for MHC-II Epitope Generation"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2026_Yuan_Research_Wash_D_C_EpiMII_Structure_Aware_Graph_Neural_Networks_f_PMID42306778.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

EpiMII applies structure-aware graph neural networks to MHC-II epitope generation, using an inverse-folding formulation: rather than predicting structure from sequence, it starts from a fixed 3D backbone and searches sequence space for residues compatible with that geometry, using atomic-level features such as hydrogen bonding, side-chain packing and electrostatics.

## Summary

The motivation is generalisation failure. The authors note that sparse coverage of MHC-II alleles in training data causes substantial performance drops on unseen HLA types, and argue that structural information is what could carry a model across alleles it has not seen, because the physics does not change.

Inverting the usual sequence-to-structure direction is what makes generation rather than ranking possible: given a groove geometry, propose peptides that fit it.

## Key points

- Inverse folding: fixed 3D backbone, search sequence space - the reverse of conventional structure prediction.
- Uses atomic-level detail (hydrogen bonds, side-chain packing, electrostatics) rather than sequence features.
- Motivated explicitly by generalisation collapse on unseen HLA-II alleles.
- Generative rather than discriminative: it proposes epitopes instead of scoring given ones.

## Limitations

Generated epitopes are compatible with a groove geometry, which is a claim about binding and not about presentation, processing or immunogenicity - the gap the rest of this collection documents repeatedly. The approach depends on the quality of the MHC-II backbone structures it starts from, and class II structural coverage is thinner than class I. No experimental validation of generated epitopes is reported.

## Provenance

Located in the published literature, dropped into `inbox/` as `2026_Yuan_Research_Wash_D_C_EpiMII_Structure_Aware_Graph_Neural_Networks_f_PMID42306778.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.34133/research.1311`; the prose sections were written here from the paper itself.

## Citation

Yuan et al. Research 2026. EpiMII: Structure-Aware Graph Neural Networks for MHC-II Epitope Generation. doi: 10.34133/research.1311

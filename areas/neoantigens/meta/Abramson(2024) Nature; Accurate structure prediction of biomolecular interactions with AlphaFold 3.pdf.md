---
# --- identity ------------------------------------------------
id: 2024-01-01_abramson-2024-nature-accurate-structure
id_basis: filename-year
source: Abramson(2024) Nature; Accurate structure prediction of biomolecular interactions with AlphaFold 3.pdf
sha256: aba3109f2892454c9512570001598a069aaf422adb5aa0f3879414cb29a258fb
size_bytes: 8602339
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 118692

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-024-07487-w"
year: 2024
title: "Accurate structure prediction of biomolecular interactions with AlphaFold 3"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Abramson_Nature_Accurate_structure_prediction_of_biomolecular_PMID38718835.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

AlphaFold 3 replaces the AlphaFold 2 architecture with a diffusion-based one that predicts the joint structure of complexes containing proteins, nucleic acids, small molecules, ions and modified residues in a single unified framework. It reports substantially higher accuracy than specialised tools for protein-ligand docking, protein-nucleic acid complexes and antibody-antigen prediction.

## Summary

The model drops AF2's rigid separation between protein-only structure prediction and everything else, and predicts raw atom coordinates through a diffusion module rather than assembling residue frames. This lets one network cover nearly every molecular type present in the PDB, and in all but one benchmark category it beats methods specialised for that category alone.

For this collection the relevance is indirect but load-bearing: several TCR:pMHC structure-based predictors here are built on AlphaFold, and its accuracy ceiling on antibody-antigen-like interfaces is the ceiling those methods inherit.

## Key points

- One diffusion-based network predicts protein, nucleic acid, ligand, ion and modified-residue complexes without task-specific architectures.
- Reports higher accuracy than state-of-the-art docking tools on protein-ligand interfaces and than AlphaFold-Multimer v2.3 on antibody-antigen.
- Antibody-antigen accuracy improves with the number of seeds sampled, which means single-seed predictions understate what the model can do and also cost more compute.
- The authors document a 4.4% chirality violation rate on the PoseBusters benchmark despite an explicit ranking penalty.

## Limitations

The authors state the model's own limitations plainly: stereochemistry violations including chirality, hallucinated structure in disordered regions, no representation of dynamics, and reduced accuracy on specific target classes. It did not reach the best human-expert-aided CASP15 RNA submission, and dataset sizes were too small to report significance tests there. Accuracy on antibody-antigen-like interfaces is not the same as accuracy on TCR:pMHC, and nothing here measures the latter.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Abramson_Nature_Accurate_structure_prediction_of_biomolecular_PMID38718835.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-024-07487-w`; the prose sections were written here from the paper itself.

## Citation

Abramson et al. Nature 2024. Accurate structure prediction of biomolecular interactions with AlphaFold 3. doi: 10.1038/s41586-024-07487-w

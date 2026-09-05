---
# --- identity ------------------------------------------------
id: 2023-01-01_bradley-2023-elife-structure-based-predi
id_basis: filename-year
source: Bradley(2023) eLife; Structure-based prediction of T cell receptorpeptide-MHC interactions.pdf
sha256: 4cce84957ded06f5c0e257327e3ec5f07646e2f741908b6502dfb15d8cec95db
size_bytes: 4316934
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 100027

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.7554/eLife.82813"
year: 2023
title: "Structure-based prediction of T cell receptor:peptide-MHC interactions"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Bradley_Elife_Structure_based_prediction_of_T_cell_receptor_PMID36661395.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A specialised, template-guided version of AlphaFold is used to model TCR:peptide-MHC complexes, and the resulting models discriminate correct from incorrect peptide epitopes with substantial accuracy. The paper argues that structural modelling is a viable route to generalisable TCR specificity prediction in a regime where training data are scarce.

## Summary

The two obstacles the paper names are the diversity of TCR docking modes and the small number of validated TCR:pMHC pairs. Sequence-based predictors learn new TCRs against epitopes already in their training set but do not generalise to unseen epitopes; structure, being biophysical, ought to.

The pipeline supplies multi-chain template information that AlphaFold-Multimer cannot use on its own, which both constrains the docking geometry to the observed range and cuts runtime enough to make the approach usable.

## Key points

- Off-the-shelf AlphaFold-Multimer produced displaced peptides and docking modes outside the native range, and took hours per target.
- Supplying multi-chain templates for the constrained TCR:pMHC binding mode is what makes the predictions consistent.
- Discrimination works by molecular specificity determinants in the model, not by memorised sequence pairs.
- Accuracy varies by epitope: those with more sequence-diverse TCR repertoires are harder to model.

## Limitations

The author states directly that overall accuracy falls short of what most practical applications of TCR:pMHC prediction would require. Performance is uneven across epitopes and the paper cannot yet predict which systems will be modelled reliably. It is a single-author proof of direction rather than a deployable tool.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Bradley_Elife_Structure_based_prediction_of_T_cell_receptor_PMID36661395.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.7554/eLife.82813`; the prose sections were written here from the paper itself.

## Citation

Bradley et al. eLife 2023. Structure-based prediction of T cell receptor:peptide-MHC interactions. doi: 10.7554/eLife.82813

---
# --- identity ------------------------------------------------
id: 2023-01-01_gfeller-2023-cell-systems-improved-predi
id_basis: filename-year
source: Gfeller(2023) Cell Systems; Improved predictions of antigen presentation and TCR recognition with MixMHCpred2.2 and PRIME2.0 reveal potent SARS-CoV-2 CD8+ T-cell epitopes.pdf
sha256: d0adbe0d50e0d6d28117e7467af3c49942d80ba8cca3e1fdc826924ea7d0ec6a
size_bytes: 2948416
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 106408

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cels.2022.12.002"
year: 2023
title: "Improved predictions of antigen presentation and TCR recognition with MixMHCpred2.2 and PRIME2.0 reveal potent SARS-CoV-2 CD8+ T-cell epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Gfeller_Cell_Syst_Improved_predictions_of_antigen_presentation_a_PMID36603583.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Large curated datasets of HLA-I ligands and neo-epitopes are used to train two tools: MixMHCpred2.2 for antigen presentation and PRIME2.0 for TCR recognition. Applied to SARS-CoV-2, they identify potent CD8+ T-cell epitopes, several cross-reactive with other coronaviruses.

## Summary

The two-stage split is the point: presentation and recognition are different questions with different training data, and modelling them separately lets each use the evidence appropriate to it. Presentation is learnt from mass-spectrometry HLA-I peptidomics rather than binding assays.

The reason that matters is stated plainly in the paper - peptides in historical binding assays were often pre-selected using earlier versions of the same predictors, so training on them partly measures agreement with the previous model. Naturally presented ligands identified by MS do not have that circularity.

## Key points

- Separates antigen presentation (MixMHCpred2.2) from TCR recognition (PRIME2.0) as distinct trained models.
- Names the circularity in binding-assay training sets: peptides pre-selected by earlier predictors.
- Confirms enrichment of aromatic and hydrophobic residues at TCR-facing positions among epitopes, consistent with Calis and Chowell.
- Prospective application to SARS-CoV-2 yielded validated CD8+ epitopes with cross-coronavirus reactivity.

## Limitations

When the test set was restricted to experimentally validated peptides with similar predicted HLA-I binding, the authors did not observe significant differences - so part of the apparent gain reflects binding differences the model already captures. Mass-spectrometry ligand data carry their own detection biases towards abundant, well-ionising peptides. The SARS-CoV-2 application is a demonstration in a pathogen system, not evidence about neoantigen ranking.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Gfeller_Cell_Syst_Improved_predictions_of_antigen_presentation_a_PMID36603583.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cels.2022.12.002`; the prose sections were written here from the paper itself.

## Citation

Gfeller et al. Cell Systems 2023. Improved predictions of antigen presentation and TCR recognition with MixMHCpred2.2 and PRIME2.0 reveal potent SARS-CoV-2 CD8+ T-cell epitopes. doi: 10.1016/j.cels.2022.12.002

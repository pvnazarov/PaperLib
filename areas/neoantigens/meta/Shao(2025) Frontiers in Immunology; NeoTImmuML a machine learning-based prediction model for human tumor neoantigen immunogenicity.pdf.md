---
# --- identity ------------------------------------------------
id: 2025-01-01_shao-2025-frontiers-in-immunology-neotim
id_basis: filename-year
source: Shao(2025) Frontiers in Immunology; NeoTImmuML a machine learning-based prediction model for human tumor neoantigen immunogenicity.pdf
sha256: 602f826676fe8e26233cd973defc5e42bb97668803662d725dc0da11a01aa44d
size_bytes: 5101201
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 66744

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3389/fimmu.2025.1681396"
year: 2025
title: "NeoTImmuML: a machine learning-based prediction model for human tumor neoantigen immunogenicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Shao_Front_Immunol_NeoTImmuML_a_machine_learning_based_prediction_PMID41200173.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoTImmuML is a weighted ensemble of LightGBM, XGBoost and Random Forest trained on physicochemical peptide features computed from TumorAgDB2.0, a consolidated tumour antigen database built by the same authors. Eight algorithms were compared by five-fold cross-validation, SHAP was used for interpretability, and the ensemble outperformed single models on an external dataset.

## Summary

The paper pairs a resource with a model: TumorAgDB2.0 addresses scattered, small, single-function earlier databases, and NeoTImmuML is the demonstration of what the consolidated data supports.

Methodologically it is conventional - physicochemical features, gradient-boosted trees, ensemble weighting, SHAP for explanation - which makes it a reasonable baseline rather than a novel approach.

## Key points

- Consolidates fragmented tumour antigen data into TumorAgDB2.0, then models on top of it.
- Eight algorithm families compared under five-fold cross-validation before the ensemble was constructed.
- SHAP used to identify which physicochemical features drive the immunogenicity call.
- Tested on an external independent dataset, not only cross-validation.

## Limitations

The authors state two limitations that matter more than the headline result. The model uses peptide-level and public biological information only, with no representation of tumour microenvironment immune dynamics. More seriously, dataset splitting is by sequence uniqueness rather than sequence similarity, so near-identical peptides can appear in both train and test - a known source of inflated performance that they flag as future work. Features are physicochemical, so this is closer to the Calis/Chowell tradition than to the presentation-aware models here.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Shao_Front_Immunol_NeoTImmuML_a_machine_learning_based_prediction_PMID41200173.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3389/fimmu.2025.1681396`; the prose sections were written here from the paper itself.

## Citation

Shao et al. Frontiers in Immunology 2025. NeoTImmuML: a machine learning-based prediction model for human tumor neoantigen immunogenicity. doi: 10.3389/fimmu.2025.1681396

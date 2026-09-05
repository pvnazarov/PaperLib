---
# --- identity ------------------------------------------------
id: 2023-01-01_bravi-2023-elife-a-transfer-learning-app
id_basis: filename-year
source: Bravi(2023) eLife; A transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity.pdf
sha256: 0c5bf2daba2f9d3538c3c5e70be6275cb69866ffee3737c78e536f75e1a8d1e2
size_bytes: 3002280
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 223166

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.7554/eLife.85126"
year: 2023
title: "A transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Bravi_Elife_A_transfer_learning_approach_to_predict_antige_PMID37681658.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

diffRBM applies transfer learning to Restricted Boltzmann Machines to model two properties separately: what makes an antigen immunogenic, and what makes a TCR specific for a given antigen. The learnt patterns predict putative contact sites of the antigen-receptor complex and discriminate immunogenic from non-immunogenic antigens at performance comparable to existing sequence-based predictors.

## Summary

The design idea is that a background model of generic sequences can be subtracted from a model of the property-bearing sequences, leaving the distinctive amino-acid composition that carries the signal. This is trained twice, once on antigens and once on receptors.

Because the residual model is interpretable at the position level, it yields contact-site predictions as a by-product rather than requiring a separate structural step - which is the main thing distinguishing it from black-box sequence predictors.

## Key points

- Separates a generic background from the property-specific signal, so what the model learnt can be read off per position.
- Predicts putative contact sites in the antigen-receptor complex from sequence alone.
- Handles both immunogenic-vs-non-immunogenic antigens and antigen-specific-vs-generic receptors within one framework.
- Performance is reported as comparable to, not clearly better than, existing sequence-based predictors.

## Limitations

Performance is described as comparing favourably rather than as a decisive improvement, so the case rests substantially on interpretability. Contact sites are 'putative' - inferred from learnt sequence patterns, not validated against structures at scale. Like every immunogenicity model trained on curated epitope sets, it inherits whatever assay and reporting biases those sets carry.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Bravi_Elife_A_transfer_learning_approach_to_predict_antige_PMID37681658.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.7554/eLife.85126`; the prose sections were written here from the paper itself.

## Citation

Bravi et al. eLife 2023. A transfer-learning approach to predict antigen immunogenicity and T-cell receptor specificity. doi: 10.7554/eLife.85126

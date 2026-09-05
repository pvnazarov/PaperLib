---
# --- identity ------------------------------------------------
id: 2026-01-01_culka-2026-cell-systems-predicting-speci
id_basis: filename-year
source: Culka(2026) Cell Systems; Predicting specificity of TCR-pMHC interactions using machine-learning and biophysical models.pdf
sha256: 4e86bfc86dcd5627f63f91743c3ed13f80a0952a69ba37b486a56d3d94dda53a
size_bytes: 2890600
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 76390

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cels.2026.101700"
year: 2026
title: "Predicting specificity of TCR-pMHC interactions using machine-learning and biophysical models"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2026_Culka_Cell_Syst_Predicting_specificity_of_TCR_pMHC_interaction_PMID42594866.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05; DOI supplied by --doi-override (the PDF prints a different registered identifier)"
---

## Abstract

Using a proprietary cancer-patient dataset that profiles TCR binding in previously unexplored regions of peptide space, the authors show that machine-learning TCR specificity models fail to generalise to novel peptides, while physics-based methods using classical energy functions do better on novel peptides and worse on known ones. They then build a model on protein foundation-model representations that matches or beats both, in and out of distribution.

## Summary

This is the paper in the collection that tests the assumption the others rest on. Most TCR specificity models are trained directly on TCR-pMHC pairs using CDR3-beta and peptide sequence alone, and their reported performance is measured on peptides that appear in training.

The contribution beyond the negative result is a way to quantify it: performance is analysed as a function of sequence distance between training and test TCRs, which turns 'does it generalise' into a measurable property of any given model rather than a claim.

## Key points

- ML models have demonstrable utility on known peptides and fail on novel ones - the two regimes must be reported separately.
- Classical biophysical energy functions outperform ML on novel peptides, the exact case where ML is weakest.
- Leveraging protein foundation models recovers performance in both regimes.
- Introduces performance-versus-training-distance as a generalisation metric applicable to any TCR-pMHC model.

## Limitations

The central dataset is proprietary, so the headline generalisation result cannot be independently reproduced. Distance in TCR sequence space is a proxy for novelty and does not capture structural or functional similarity. The comparison covers particular ML and biophysical methods at one point in time; it bounds current practice rather than the approaches in principle.

## Provenance

Located in the published literature, dropped into `inbox/` as `2026_Culka_Cell_Syst_Predicting_specificity_of_TCR_pMHC_interaction_PMID42594866.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cels.2026.101700`; the prose sections were written here from the paper itself.

## Citation

Culka et al. Cell Systems 2026. Predicting specificity of TCR-pMHC interactions using machine-learning and biophysical models. doi: 10.1016/j.cels.2026.101700

---
# --- identity ------------------------------------------------
id: 2004-01-01_bhasin-2004-vaccine-prediction-of-ctl-ep
id_basis: filename-year
source: Bhasin(2004) Vaccine; Prediction of CTL epitopes using QM, SVM and ANN techniques.pdf
sha256: 2d9a75ce70c77751bce8d509faa50b0fc6dc115e8b4f472f6a2a3caf62841019
size_bytes: 238541
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 65389

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.vaccine.2004.02.005"
year: 2004
title: "Prediction of CTL epitopes using QM, SVM and ANN techniques"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-S0264410X04001409-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A direct CTL epitope predictor built from quantitative matrices, support vector machines and neural networks, trained on a non-redundant set including 1,137 experimentally proven MHC class I restricted T cell epitopes. Accuracies were 70.0% (QM), 72.2% (ANN) and 75.2% (SVM), with machine learning ahead of the matrix method on a blind set.

## Summary

The paper's argument is the one the field would keep rediscovering: most epitope prediction methods are indirect, predicting MHC binders rather than T cell epitopes, and their central limitation is that they cannot separate a true epitope from a non-epitope binder.

A subgroup analysis is offered as the key evidence - the trained models discriminate epitopes from MHC binders that are not epitopes, which a binding predictor by construction cannot do.

## Key points

- States the presentation-versus-immunogenicity distinction explicitly in 2004, and builds directly for the second.
- 1,137 experimentally proven class I restricted epitopes, from MHCBN, with a non-redundant negative set.
- SVM 75.2% > ANN 72.2% > quantitative matrix 70.0%, evaluated by leave-one-out at the equal-sensitivity-and-specificity point.
- Demonstrates discrimination between T cell epitopes and non-epitope MHC binders in a subgroup analysis.

## Limitations

Accuracy is reported at the cutoff where sensitivity and specificity are roughly equal, which flatters a task whose real operating point is extreme precision at the top of a ranking. The non-epitope class comes from a 2004 database and carries the usual problem that 'not reported as an epitope' is not 'not an epitope'. Twenty years of subsequent data and methods have superseded the numbers; the framing is what remains valuable.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-S0264410X04001409-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.vaccine.2004.02.005`; the prose sections were written here from the paper itself.

## Citation

Bhasin et al. Vaccine 2004. Prediction of CTL epitopes using QM, SVM and ANN techniques. doi: 10.1016/j.vaccine.2004.02.005

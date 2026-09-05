---
# --- identity ------------------------------------------------
id: 2021-01-01_schmidt-2021-cell-reports-medicine-predi
id_basis: filename-year
source: Schmidt(2021) Cell Reports Medicine; Prediction of neo-epitope immunogenicity reveals TCR recognition determinants and provides insight into immunoediting.pdf
sha256: 3b9e83522cd02285ef18eb104831db8c03f3b1d4c9a6cd3841c62e978c29fea3
size_bytes: 3272277
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 147963

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.xcrm.2021.100194"
year: 2021
title: "Prediction of neo-epitope immunogenicity reveals TCR recognition determinants and provides insight into immunoediting"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2021_Schmidt_Cell_Rep_Med_Prediction_of_neo_epitope_immunogenicity_revea_PMID33665637.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

PRIME predicts immunogenic CD8+ T cell epitopes by combining HLA presentation with a learnt model of TCR recognition, improving accuracy on neoepitopes over presentation-only predictors. The learnt determinants of TCR recognition are then used to argue that immunoediting acts on recurrent cancer mutations.

## Summary

The design separates the two steps that most tools conflate. Presentation is predicted from HLA binding models; recognition is learnt separately from what T cells actually responded to, and the combination is what PRIME scores.

The immunoediting argument is the more interesting use: if recurrent cancer mutations are systematically depleted of predicted-immunogenic epitopes, that depletion is a footprint of the immune system having removed the tumours that carried them.

## Key points

- Explicitly models TCR recognition on top of presentation, rather than treating binding as a proxy for immunogenicity.
- Improved accuracy specifically on neoepitopes, which is where presentation-only predictors degrade.
- Recovers interpretable molecular determinants of TCR recognition at the peptide positions facing the receptor.
- Provides population-level evidence for immunoediting acting on recurrent mutations.

## Limitations

The authors are explicit: immunogenic peptides are defined as those recognised by some T cells in assays such as IFN-gamma ELISpot, so PRIME captures propensity to be physically recognised - antigenicity - and does not demonstrate that these peptides elicit a stronger response on vaccination. They also flag that recurrent mutations are under-represented in the analysed set, that expression can be biased by non-malignant cells, that clonality is hard to estimate from single biopsies, and that in vivo responses depend on coreceptors, cytokines, T cell fitness and microenvironment - none of which are modelled.

## Provenance

Located in the published literature, dropped into `inbox/` as `2021_Schmidt_Cell_Rep_Med_Prediction_of_neo_epitope_immunogenicity_revea_PMID33665637.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.xcrm.2021.100194`; the prose sections were written here from the paper itself.

## Citation

Schmidt et al. Cell Reports Medicine 2021. Prediction of neo-epitope immunogenicity reveals TCR recognition determinants and provides insight into immunoediting. doi: 10.1016/j.xcrm.2021.100194

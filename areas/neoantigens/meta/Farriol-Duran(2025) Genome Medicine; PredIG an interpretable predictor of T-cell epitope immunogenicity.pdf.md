---
# --- identity ------------------------------------------------
id: 2025-01-01_farriol-duran-2025-genome-medicine-predi
id_basis: filename-year
source: Farriol-Duran(2025) Genome Medicine; PredIG an interpretable predictor of T-cell epitope immunogenicity.pdf
sha256: 201bf20708acea5aac6ce2bba2f7560d54df19ab78a0c9f1a945791af9820be5
size_bytes: 4920737
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 148511

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13073-025-01569-8"
year: 2025
title: "PredIG: an interpretable predictor of T-cell epitope immunogenicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Farriol_Duran_Genome_Med_PredIG_an_interpretable_predictor_of_T_cell_ep_PMID41225487.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

PredIG predicts T-cell epitope immunogenicity from 17,448 peptide-HLA-I pairs with reported immunogenicity, combining in silico antigen-processing features (proteasomal cleavage, TAP translocation, binding affinity, presentation) with physicochemical descriptors focused on TCR-facing positions. Three antigen-specific XGBoost models cover neoantigens, non-canonical antigens and pathogens, and SHAP analysis is used to make the predictions interpretable.

## Summary

The metric the paper optimises is the immunogenicity screening success rate - how many truly immunogenic epitopes appear among the top-ranked candidates sent for experimental validation - rather than a global AUC. That is the quantity that decides whether a screen is affordable.

SHAP analysis shows importance balanced between antigenic processing likelihood and physicochemical character, with processing contributing more than is usual in epitope predictors, which mostly stop at binding.

## Key points

- Optimises screening success rate at the top of the ranking, not overall discrimination - the quantity that matters when validation is the bottleneck.
- Separate models for neoantigens, non-canonical antigens and pathogen epitopes rather than one model assumed to transfer.
- SHAP attributes substantial weight to antigen processing likelihood, often omitted from immunogenicity models.
- Reported to generalise to non-canonical antigens not seen during training.

## Limitations

The authors state the field-wide constraint that immunogenicity models are hindered by low epitope diversity in T-cell assay databases, which are biased towards strong HLA binders because validation is expensive - PredIG is trained on those same databases. Some training sources contain only positive cases, so negatives are constructed rather than observed. Data from several studies had to be discarded for insufficient HLA resolution, which narrows allele coverage.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Farriol_Duran_Genome_Med_PredIG_an_interpretable_predictor_of_T_cell_ep_PMID41225487.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13073-025-01569-8`; the prose sections were written here from the paper itself.

## Citation

Farriol-Duran et al. Genome Medicine 2025. PredIG: an interpretable predictor of T-cell epitope immunogenicity. doi: 10.1186/s13073-025-01569-8

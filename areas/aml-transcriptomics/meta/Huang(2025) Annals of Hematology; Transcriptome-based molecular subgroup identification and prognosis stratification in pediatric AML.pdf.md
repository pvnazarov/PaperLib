---
# --- identity ------------------------------------------------
id: 2025-01-01_huang-2025-annals-of-hematology-transcri
id_basis: filename-year
source: Huang(2025) Annals of Hematology; Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML.pdf
sha256: cd3f3ba7b5c2c3c9c3e4a5875fc88a18242b9c0a4ff3c1529467edfbcbdb93a4
size_bytes: 18149700
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 84762

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1007/s00277-025-06634-1"
year: 2025
title: "Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Huang(2025) Ann Hematol; Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A computational analysis of public AML transcriptome data from the GDC Data Portal with MSigDB gene sets, reclassifying AML into 8 molecular subgroups and characterising their expression profiles, immune microenvironment, biological pathways and clinical features. Four machine learning algorithms (random forest, SVM, XGBoost, decision tree) were compared for classification, with XGBoost performing best; HSD17B10, NDUFS8, ASCL5, FADS2 and COX8A emerged as important features, of which only NDUFS8 and FADS2 had been previously reported in AML. A 62-gene prognostic model is proposed with retrospective validation.

## Summary

A bioinformatics reanalysis addressing a real gap - pediatric AML is genetically distinct from adult disease and adult risk models are not simply transferable - by deriving subgroups from expression rather than from cytogenetics and mutations.

The candidate genes point at oxidative metabolism (NDUFS8 and COX8A are respiratory chain components, HSD17B10 is mitochondrial) and lipid metabolism (FADS2), which is at least consistent with the mitochondrial dependency running through this collection, though the paper reaches them by feature importance rather than by biology. The authors state their own principal caveat plainly in the abstract: the work is retrospective and needs prospective confirmation.

## Key points

- Reclassifies AML into 8 transcriptome-defined molecular subgroups, characterised by expression, immune microenvironment and pathway differences.
- Motivated by substantial heterogeneity in survival within existing cytogenetic and molecular risk subgroups.
- XGBoost outperformed random forest, SVM and decision tree for subgroup classification.
- Highlights HSD17B10, ASCL5 and COX8A as prognostic candidates not previously reported in AML, alongside NDUFS8 and FADS2.
- Proposes a 62-gene prognostic model with retrospective validation.

## Limitations

Entirely computational on public data, with no experimental validation of any gene and no independent patient cohort collected by the authors. Subgroups are derived by unsupervised clustering, which will produce clusters from any dataset - eight is a choice, and the paper does not establish that these are more useful than existing classifications on a held-out basis. A 62-gene model built and evaluated on overlapping public data risks optimistic performance, and the abstract does not describe a fully external validation. Despite the pediatric framing, the discovery data are drawn from general AML resources, so how much is genuinely pediatric-specific is unclear. Feature importance in XGBoost identifies genes useful for prediction in this dataset, not genes with a biological role, and the authors' own note that three of five are unreported in AML is presented as novelty when it is equally a reason for caution. Retrospective throughout, as the authors state.

## Provenance

Located in the published literature, dropped into `inbox/` as `Huang(2025) Ann Hematol; Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1007/s00277-025-06634-1`; the prose sections were written here from the paper itself.

## Citation

Huang et al. Annals of Hematology 2025. Transcriptome-based molecular subgroup identification and prognosis stratification in pediatric AML. doi: 10.1007/s00277-025-06634-1

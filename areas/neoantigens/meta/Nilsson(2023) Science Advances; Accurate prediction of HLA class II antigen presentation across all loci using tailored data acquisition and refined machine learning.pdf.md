---
# --- identity ------------------------------------------------
id: 2023-01-01_nilsson-2023-science-advances-accurate-p
id_basis: filename-year
source: Nilsson(2023) Science Advances; Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning.pdf
sha256: 688e44b112767b90626950c647a2828ffe2115047cc5892b2e40782789db5300
size_bytes: 2797045
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 120266

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/sciadv.adj6367"
year: 2023
title: "Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Nilsson_Sci_Adv_Accurate_prediction_of_HLA_class_II_antigen_pr_PMID38000035.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NetMHCIIpan-4.3 closes the performance gap between HLA-DR, -DQ and -DP by combining a refined machine learning framework that accommodates inverted peptide binders with targeted immunopeptidomics assays generating new HLA-DP data. The result is high accuracy and molecular coverage across all class II allotypes.

## Summary

Class II prediction had been effectively DR-only, because pan-class-II antibodies pull down DR far more efficiently than DQ or DP, so immunopeptidomics for the other two loci was scarce. The authors solve the data problem experimentally with three locus-specific antibodies rather than modelling around it.

The modelling refinement is accommodating inverted binders - peptides that sit in the groove in the reverse orientation - which earlier frameworks could not represent and therefore learnt as noise.

## Key points

- The DR/DQ/DP gap was a data-acquisition artefact: pan-class-II antibody yield for DP and DQ was very low, and locus-specific antibodies fix it.
- The learning framework explicitly handles inverted peptide binding modes.
- Built on NNAlign_MA, so multi-allele elution data from heterozygous samples are usable.
- Matters for neoantigens because CD4+ responses are increasingly implicated in tumour control.

## Limitations

Coverage is much improved but still uneven: alleles without immunopeptidomics rely on pan-specific extrapolation, and DP/DQ data remain thinner than DR. Predicting presentation is not predicting CD4+ immunogenicity. Mass-spectrometry elution bias towards abundant, well-ionising peptides applies here as elsewhere, and the targeted assays inherit whatever specificity the locus-specific antibodies have.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Nilsson_Sci_Adv_Accurate_prediction_of_HLA_class_II_antigen_pr_PMID38000035.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/sciadv.adj6367`; the prose sections were written here from the paper itself.

## Citation

Nilsson et al. Science Advances 2023. Accurate prediction of HLA class II antigen presentation across all loci using tailored data acquisition and refined machine learning. doi: 10.1126/sciadv.adj6367

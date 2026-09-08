---
# --- identity ------------------------------------------------
id: 2026-01-01_whittle-2026-elife-single-cell-atlas-of
id_basis: filename-year
source: Whittle(2026) eLife; Single-cell atlas of AML reveals age-related gene regulatory networks in t(8,21) AML.pdf
sha256: 92398767e81e7a0afdeaacacb02a1e2fdb68863e6ac5951d0da55d208d54d2e0
size_bytes: 9155643
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 127168

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.7554/eLife.104978"
year: 2026
title: "Single-cell atlas of AML reveals age-related gene regulatory networks in t(8;21) AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Whittle(2026) Elife; Single-cell atlas of AML reveals age-related gene regulatory networks in t(8 21) AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Large-scale integration of published single-cell RNA-seq datasets creates an AML single-cell atlas of 748,679 cells from 159 AML patients and 51 healthy donors across 20 studies, publicly available through cellxgene. Applying it to 20 patients with t(8;21) AML, the authors explored the clinical importance of age given the in-utero origin of pediatric disease, uncovering age-associated gene regulatory network signatures validated in bulk RNA-seq data to delineate groups with divergent biological characteristics. Using an additional multiomic dataset combining scRNA-seq and scATAC-seq, they validated the findings and constructed a de-noised enhancer-driven gene regulatory network reflecting the age-related signatures.

## Summary

Solves a statistical problem rather than a biological one, and thereby enables a biological question. Individual single-cell studies have too few patients to compare subgroups, so integrating twenty of them into the largest human AML single-cell resource makes it possible to isolate 20 t(8;21) patients and analyse them properly.

The question chosen is well motivated: pediatric t(8;21) AML originates in utero while adult disease does not, so age at onset may mark genuinely different biology rather than only different tolerance of treatment. Finding age-associated regulatory network signatures, then validating them in bulk RNA-seq and in an independent multiomic dataset with matched accessibility, is a three-stage confirmation that most integration studies do not attempt. Releasing the atlas publicly with the full analysis code is the lasting contribution.

## Key points

- Integrates 20 published studies into an AML single-cell atlas of 748,679 cells from 159 patients and 51 healthy donors - the largest such human resource.
- Makes subgroup comparison possible where individual studies are too small, demonstrated on 20 t(8;21) patients.
- Age at onset is a biologically motivated variable in t(8;21), since pediatric disease originates in utero.
- Age-associated gene regulatory network signatures were validated in bulk RNA-seq and in an independent scRNA/scATAC multiomic dataset.
- The atlas and analysis code are publicly released, with candidate targets more relevant to pediatric than adult t(8;21) AML.

## Limitations

Integration of 20 studies means combining data generated with different protocols, platforms, tissue sources and processing pipelines, and batch correction can both remove and create biological signal - the authors apply quality filtering and standard best practice, but the atlas remains a reconstruction rather than a uniform dataset. Twenty t(8;21) patients is still a small subgroup for age stratification, and age is confounded with treatment era and clinical management across contributing studies. The regulatory networks are computationally inferred, and the candidate therapeutic targets identified are nominated rather than functionally tested. This record's file corresponds to the eLife reviewed-preprint publishing model, in which assessment accompanies rather than gates the article.

## Provenance

Located in the published literature, dropped into `inbox/` as `Whittle(2026) Elife; Single-cell atlas of AML reveals age-related gene regulatory networks in t(8 21) AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.7554/eLife.104978`; the prose sections were written here from the paper itself.

## Citation

Whittle et al. eLife 2026. Single-cell atlas of AML reveals age-related gene regulatory networks in t(8;21) AML. doi: 10.7554/eLife.104978

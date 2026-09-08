---
# --- identity ------------------------------------------------
id: 2020-01-01_je-ek-2020-antioxidants-redox-signaling
id_basis: filename-year
source: Ježek(2020) Antioxidants & Redox Signaling; 2-Hydroxyglutarate in Cancer Cells.pdf
sha256: a3ff5c36a626318dda764828bd5387d16ded5527a8d7f38e23cb6395d1f687fe
size_bytes: 1739016
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 161195

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1089/ars.2019.7902"
year: 2020
title: "2-Hydroxyglutarate in Cancer Cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ježek(2020) Antioxid Redox Signal; 2-Hydroxyglutarate in Cancer Cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of 2-hydroxyglutarate as an oncometabolite across cancers including AML. Heterozygous mutations at the active sites of IDH1 (R132H) and mitochondrial IDH2 (R140Q) give cells millimolar R-2HG, while side activities of lactate and malate dehydrogenase produce submillimolar S-2HG; even wild-type IDH1/2, under reductive carboxylation glutaminolysis, yields intermediate 0.01-0.1 mM levels against 10^-8 M in non-cancer cells. 2HG inhibits 2-oxoglutarate-dependent dioxygenases, blocking DNA and histone demethylation, interferes with HIF transcriptome reprogramming and mTOR signalling, contributes to oxidative stress, and acts in tumour-immune crosstalk, including directing differentiation of naive T lymphocytes.

## Summary

Useful in this collection for two things beyond the standard IDH-mutant account. The first is quantitative: the concentration ranges are laid out explicitly, from 10^-8 M in normal cells through 0.01-0.1 mM in wild-type-IDH cancers to millimolar in IDH-mutant cells, which makes the point that 2HG is not simply present or absent and that wild-type IDH tumours occupy a middle ground usually ignored.

The second is the immunological arm. R-2HG produced by Th17 cells hypermethylates the Foxp3 locus and blocks induced regulatory T cell differentiation, and activated CD8+ T cells generate S-2HG - so 2HG in a tumour is not necessarily tumour-derived, which complicates its use as a marker and adds a mechanism by which it shapes the immune microenvironment.

## Key points

- Distinguishes the two enantiomers throughout: R-2HG from mutant IDH1/2, S-2HG from lactate and malate dehydrogenase side activities.
- Gives explicit concentration ranges - 10^-8 M normal, 0.01-0.1 mM in wild-type-IDH cancers, millimolar in IDH-mutant cells.
- 2HG inhibits 2-oxoglutarate-dependent dioxygenases, blocking DNA and histone demethylation, and perturbs HIF and mTOR signalling.
- Immune cells themselves produce both enantiomers: Th17-derived R-2HG blocks iTreg differentiation via Foxp3 hypermethylation.
- Proposes 2HG, and enantiomer discrimination in particular, as a diagnostic metabolic marker in body fluids.

## Limitations

A narrative review, not systematic, and broad across cancer types rather than focused on AML, so its leukemia content is a subset of a wider survey. The diagnostic proposal is speculative: the authors write that one 'may speculate' that immune-derived R-2HG diffuses into the microenvironment and might subsequently be found in plasma, urine or lymph, which is a hypothesis rather than a validated assay, and enantiomer-resolving measurement in body fluids is not demonstrated here. Published 2020, so it predates later clinical experience with IDH inhibitors. Cross-species and cross-cancer-type evidence is combined throughout, and the concentration figures come from disparate studies with different measurement methods, so the ranges are indicative rather than directly comparable.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ježek(2020) Antioxid Redox Signal; 2-Hydroxyglutarate in Cancer Cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1089/ars.2019.7902`; the prose sections were written here from the paper itself.

## Citation

Ježek et al. Antioxidants &amp; Redox Signaling 2020. 2-Hydroxyglutarate in Cancer Cells. doi: 10.1089/ars.2019.7902

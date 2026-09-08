---
# --- identity ------------------------------------------------
id: 2016-01-01_li-2016-blood-genome-wide-studies-identi
id_basis: filename-year
source: Li(2016) Blood; Genome-wide studies identify a novel interplay between AML1 and AML1 ETO in t(8,21) acute myeloid leukemia.pdf
sha256: f858343d059056376a94bed9b79c589578a5bfee5fd50a69256354043eb0bf00
size_bytes: 2077008
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 76699

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood-2015-03-626671"
year: 2016
title: "Genome-wide studies identify a novel interplay between AML1 and AML1/ETO in t(8;21) acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Li(2016) Blood; Genome-wide studies identify a novel interplay between AML1 and AML1 ETO in t(8 21) acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Chromatin immunoprecipitation sequencing with computational analysis and experimental validation shows that wild-type AML1 orchestrates the expression of AML1/ETO targets whether they are activated or repressed, by forming a complex with AML1/ETO on chromatin and recruiting the cofactor AP-1. The two proteins largely overlap in occupancy and preferentially bind adjacent, distinct short and long AML1 motifs respectively; they interact through the runt homology domain of both proteins. The relative binding signals of AML1 and AML1/ETO determine whether a target is repressed or activated, with transactivation proceeding through AP-1 recruitment to the complex.

## Summary

Refines a long-standing simplification. AML1/ETO was described as a dominant-negative inhibitor of wild-type AML1, which implies displacement; here the two proteins occupy the same regions together, bound to adjacent motifs of different length, physically joined through the runt homology domain.

The consequence is quantitative rather than categorical. Whether a target is activated or repressed depends on the ratio of the two proteins at that site: where AML1/ETO is abundant enough to reduce AML1 binding, the gene is repressed; where it is not, AML1 keeps transactivating and the fusion serves as a platform for cofactor recruitment - AP-1 in particular. The supporting observation is neat, since depleting AML1/ETO increases AML1 binding at repressed genes but not at activated ones.

## Key points

- Wild-type AML1 and AML1/ETO form a complex on chromatin rather than the fusion simply displacing the wild-type protein.
- The two bind adjacent, distinct short and long AML1 motifs at colocalised regions, interacting via the runt homology domain of both.
- The relative binding signal of the two proteins determines whether a target is repressed or activated.
- AML1/ETO transactivates by recruiting AP-1 into the AML1/ETO-AML1 complex.
- Depleting AML1/ETO increases AML1 binding at repressed genes but not activated ones, supporting the ratio model.

## Limitations

Work is in t(8;21) cell lines - Kasumi-1 and SKNO-1 - with U937 used for ectopic expression, so nothing is established in primary patient blasts beyond re-used expression data. The ratio model is inferred from correlating ChIP-seq signal with expression changes rather than from manipulating the ratio directly and observing the predicted switch. ChIP-seq signal is not a straightforward measure of protein amount at a site, so 'relative binding signals' is a proxy for the quantity the model needs. The AP-1 mechanism rests on co-occupancy and cofactor analysis, without a functional test that removing AP-1 abolishes transactivation of these targets. No in vivo or therapeutic implication is tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Li(2016) Blood; Genome-wide studies identify a novel interplay between AML1 and AML1 ETO in t(8 21) acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood-2015-03-626671`; the prose sections were written here from the paper itself.

## Citation

Li et al. Blood 2016. Genome-wide studies identify a novel interplay between AML1 and AML1/ETO in t(8;21) acute myeloid leukemia. doi: 10.1182/blood-2015-03-626671

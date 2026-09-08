---
# --- identity ------------------------------------------------
id: 2022-01-01_zeng-2022-nature-medicine-a-cellular-hie
id_basis: filename-year
source: Zeng(2022) Nature Medicine; A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia.pdf
sha256: 318192b289d5191b13898d710dc05ba0e765d3380819135fb565acdd1ef26919
size_bytes: 27383334
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 415019

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41591-022-01819-x"
year: 2022
title: "A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zeng(2022) Nat Med; A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Leukemia cell hierarchy composition was determined from bulk transcriptomes of more than 1000 patients by deconvolution using single-cell reference profiles of leukemia stem, progenitor and mature cell types. Hierarchy composition was associated with functional, genomic and clinical properties and converged into four classes - Primitive, Mature, GMP and Intermediate. Variation along the Primitive versus GMP axis was associated with chemotherapy response, and along the Primitive versus Mature axis with drug sensitivity profiles of targeted therapies; a seven-gene biomarker derived from the latter axis was associated with response to 105 investigational drugs.

## Summary

Reconciles the two frameworks that have organised AML thinking separately - the genomic model and the stem cell model - by measuring something neither captures alone. Hierarchy composition integrates genomic profile, functional stem cell properties and clinical outcome in one classification, and the authors state plainly that this could not be achieved by either model alone.

The methodological trick is practical: deconvolving bulk transcriptomes against single-cell references means the framework applies to the thousands of patients with bulk data rather than only to the few with single-cell profiling. The trial-design warning is the most consequential point - relapsed AML is depleted of Mature and GMP-dominant hierarchies, and relapsed patients are usually where new drugs are tested first, so agents effective in those hierarchies risk being discarded on the wrong population.

## Key points

- Deconvolution of bulk transcriptomes against single-cell references makes hierarchy composition measurable in over 1000 patients.
- Four hierarchy classes - Primitive, Mature, GMP, Intermediate - integrate genomic, functional and clinical information.
- The Primitive versus GMP axis tracks chemotherapy response; the Primitive versus Mature axis tracks targeted therapy sensitivity.
- A seven-gene biomarker from the Primitive-Mature axis associates with response to 105 investigational drugs.
- Relapsed AML is depleted of Mature and GMP hierarchies, so testing new drugs first in relapse risks discarding effective agents.

## Limitations

Deconvolution infers composition rather than measuring it, so accuracy depends on the single-cell reference being representative - and cells in states absent from the reference will be misassigned. Associations with drug response come from ex vivo sensitivity data and retrospective cohorts, not from prospective assignment. The authors raise an unresolved question their own framework does not answer: emerging data after venetoclax and azacitidine show loss of phenotypic LSCs and emergence of a promonocytic population that may carry leukemic propagating potential, so which blast populations actually bear stemness is undetermined. The seven-gene biomarker is derived and evaluated within the same data resources.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zeng(2022) Nat Med; A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41591-022-01819-x`; the prose sections were written here from the paper itself.

## Citation

Zeng et al. Nature Medicine 2022. A cellular hierarchy framework for understanding heterogeneity and predicting drug response in acute myeloid leukemia. doi: 10.1038/s41591-022-01819-x

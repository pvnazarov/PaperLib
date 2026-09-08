---
# --- identity ------------------------------------------------
id: 2023-01-01_rodriguez-meira-2023-nature-genetics-sin
id_basis: filename-year
source: Rodriguez-Meira(2023) Nature Genetics; Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution.pdf
sha256: 08ab44ebbe6aec2c8b2af9e8647da6fd47bdd5571641f6ebfb040f799ccb93c3
size_bytes: 15527075
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 538927

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41588-023-01480-1"
year: 2023
title: "Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Rodriguez-Meira(2023) Nat Genet; Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Allelic-resolution single-cell multi-omic analysis of hematopoietic stem and progenitor cells from myeloproliferative neoplasm patients who transformed to TP53-mutant secondary AML. All patients showed dominant TP53 'multihit' HSPC clones at transformation, carrying a leukemia stem cell transcriptional signature strongly predictive of adverse outcomes in independent cohorts across both TP53-mutant and wild-type AML. Through serial samples, antecedent TP53-heterozygous clones and in vivo perturbation, the authors demonstrate that chronic inflammation suppresses TP53 wild-type HSPCs while enhancing the fitness advantage of TP53-mutant cells and promoting genetic evolution.

## Summary

Identifies a non-genetic force shaping genetic evolution. TP53-mutant transformation is usually framed as an accumulation of lesions; here the environment does the selecting - chronic inflammation, which is intrinsic to myeloproliferative neoplasms, handicaps the wild-type competitors and lets the mutant clone expand.

That is a mechanistically satisfying explanation for why myeloproliferative neoplasms transform to TP53-mutant secondary AML specifically, and it has an unusual therapeutic implication: reducing inflammation might slow clonal evolution, which is prevention rather than treatment. The methodological achievement is allelic resolution at single-cell level, which is what allows the 'multihit' state - point mutation on one allele plus loss of the other - to be established per cell rather than inferred from bulk allele frequencies. The leukemia stem cell signature predicting outcome in TP53 wild-type AML as well suggests the transcriptional state matters beyond the genotype that produced it.

## Key points

- Allelic-resolution single-cell multi-omics establishes the TP53 'multihit' state per cell rather than inferring it from bulk data.
- Dominant TP53 multihit HSPC clones are present in all patients at transformation, carrying an LSC transcriptional signature.
- That signature predicts adverse outcomes in independent cohorts, in TP53 wild-type as well as TP53-mutant AML.
- Chronic inflammation suppresses TP53 wild-type HSPCs while enhancing the fitness of TP53-mutant cells.
- Inflammation therefore promotes genetic evolution - a non-genetic driver of a genetic process, with implications for prevention.

## Limitations

The patient cohort is small, as serial samples spanning myeloproliferative neoplasm through transformation are rare, and the analysis requires stringent cell-number thresholds - patients needed at least 300 cells including more than 50 preleukemic and more than 50 TP53 multihit cells - which further restricts the sample. The inflammation mechanism is supported by in vivo perturbation in mice plus inference from serial human samples, so the causal step is murine. Survival validation involved 132 patients of whom only 8 were TP53-mutant, so the signature's prognostic value is established mainly in TP53 wild-type disease. Single-cell genotyping suffers allelic dropout, which is a particular concern when the classification depends on detecting loss of one allele. The therapeutic implication - that reducing inflammation would slow evolution - is not tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Rodriguez-Meira(2023) Nat Genet; Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41588-023-01480-1`; the prose sections were written here from the paper itself.

## Citation

Rodriguez-Meira et al. Nature Genetics 2023. Single-cell multi-omics identifies chronic inflammation as a driver of TP53-mutant leukemic evolution. doi: 10.1038/s41588-023-01480-1

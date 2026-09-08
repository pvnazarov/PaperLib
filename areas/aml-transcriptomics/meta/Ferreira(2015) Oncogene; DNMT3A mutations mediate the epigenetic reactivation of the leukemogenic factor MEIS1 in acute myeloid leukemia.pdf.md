---
# --- identity ------------------------------------------------
id: 2015-01-01_ferreira-2015-oncogene-dnmt3a-mutations
id_basis: filename-year
source: Ferreira(2015) Oncogene; DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia.pdf
sha256: c38b687abb6c01f4f7a34be8f9409a0752ec1c76c38a282cc681468b0f189ed4
size_bytes: 1478578
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 47881

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/onc.2015.359"
year: 2015
title: "DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ferreira(2016) Oncogene; DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Whole-genome bisulfite sequencing and DNA methylation microarrays of a DNMT3A-mutant AML line (OCI-AML3, R882C) against a wild-type line identify MEIS1, the leukemogenic HOX cofactor, as undergoing promoter hypomethylation-associated transcriptional reactivation. Screening 68 AML patients and validating in an independent cohort of 194, the authors define a 12-gene hypomethylation signature enriched in DNMT3A-mutant cases and associated with shorter overall survival. The conclusion is that in the absence of MLL fusions, DNMT3A mutations provide an alternative route to an oncogenic MEIS1-dependent transcriptional program.

## Summary

A short communication that supplies a missing link. DNMT3A is mutated in roughly 20% of AML, but no downstream gene had been identified that explained what the mutation does; naming MEIS1 connects the most common epigenetic-modifier mutation to the HOX/MEIS program that KMT2A rearrangements and NPM1 mutations already converge on.

The convergence is the point worth holding: three genetically unrelated lesions - MLL fusion, NPM1 mutation, DNMT3A mutation - all end at the same transcriptional output, by different routes. The 12-gene hypomethylation signature is validated in a second cohort and carries independent prognostic weight, which is more than most signature papers of this length attempt.

## Key points

- MEIS1 undergoes promoter hypomethylation and transcriptional reactivation in DNMT3A-mutant AML.
- Supplies a downstream effector for DNMT3A mutation, which had lacked one despite occurring in ~20% of AML.
- Provides an MLL-fusion-independent route into the oncogenic MEIS1/HOX program.
- A 12-gene hypomethylation signature is enriched in DNMT3A-mutant cases and associated with worse overall survival.
- The signature is validated in an independent cohort of 194 primary AML samples.

## Limitations

The discovery rests on a comparison of two cell lines, OCI-AML3 versus AML5, which differ in far more than DNMT3A status - so the 292 hypomethylated-activated genes are a list from an n-of-1 contrast, and no isogenic model or DNMT3A restoration experiment is presented. Everything downstream is association: MEIS1 reactivation is correlated with the mutation, not shown to be caused by it, and no functional experiment tests whether MEIS1 is required for the phenotype in DNMT3A-mutant cells. The survival associations are borderline (P = 0.046 and P = 0.037 in the discovery set) in cohorts of 68 and 194 with no multivariable adjustment against established risk factors. A short communication, so the mechanism by which a hypomorphic methyltransferase produces focal hypomethylation at specific promoters is not addressed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ferreira(2016) Oncogene; DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/onc.2015.359`; the prose sections were written here from the paper itself.

## Citation

Ferreira et al. Oncogene 2015. DNMT3A mutations mediate the epigenetic reactivation of the leukemogenic factor MEIS1 in acute myeloid leukemia. doi: 10.1038/onc.2015.359

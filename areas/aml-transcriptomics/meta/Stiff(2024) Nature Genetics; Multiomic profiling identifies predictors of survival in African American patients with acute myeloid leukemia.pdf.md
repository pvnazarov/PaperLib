---
# --- identity ------------------------------------------------
id: 2024-01-01_stiff-2024-nature-genetics-multiomic-pro
id_basis: filename-year
source: Stiff(2024) Nature Genetics; Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia.pdf
sha256: caf1faee2586efe0a7c1f801002d5cde98eb8edcc0908920265e13b0df1ae56a
size_bytes: 12558797
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 204663

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41588-024-01929-x"
year: 2024
title: "Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Stiff(2024) Nat Genet; Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Exomes and transcriptomes of 100 AML patients with genomically confirmed African ancestry were compared with 323 self-reported white patients. Of 162 gene mutations recurrent in Black patients, 73% - including a previously unreported PHIP alteration in 7% - were found in one white patient or not at all. Black patients with myelodysplasia-related AML were younger. On multivariable analysis, NPM1 and NRAS mutations were associated with inferior disease-free survival and IDH1 and IDH2 with reduced overall survival. Inflammatory profiles, cell type distributions and transcriptional profiles differed between Black and white patients with NPM1 mutations, and incorporating ancestry-specific risk markers into ELN 2022 stratification changed risk group for one-third of Black patients and improved outcome prediction.

## Summary

Addresses a structural gap rather than a biological curiosity. Black patients are about 9% of AML cases and under 2% of patients in the landmark genomics studies that current risk stratification is built on - so the panels and classifications in clinical use were derived from a population that largely excludes them. The finding that a third of Black patients change risk group when ancestry-specific markers are added, with improved prediction, is a direct measure of what that exclusion costs.

The most striking result is that 73% of mutations recurrent in Black patients were essentially absent from the comparison cohort - which is only discoverable because the authors sequenced exomes rather than the established AML gene panels that prior work relied on. NPM1 associating with inferior disease-free survival in this cohort inverts its usual favourable prognostic meaning, and the transcriptional and inflammatory differences within NPM1-mutant cases suggest the same mutation sits in a different biological context.

## Key points

- Black patients are 9% of AML cases but under 2% of patients in the studies underlying current risk stratification.
- 73% of 162 mutations recurrent in Black patients were absent or nearly absent from the white comparison cohort, including a novel PHIP alteration in 7%.
- Unbiased exome sequencing was necessary - prior work analysed only established AML gene panels and could not have found these.
- NPM1 and NRAS associated with inferior disease-free survival, and IDH1/IDH2 with reduced overall survival, in Black patients.
- Adding ancestry-specific markers to ELN 2022 changed risk group for one-third of Black patients and improved outcome prediction.

## Limitations

The authors state their own principal limitation: outcome analyses were restricted to fit patients under 60 receiving intensive induction, and none received allogeneic transplant in first complete remission, so the survival associations do not describe contemporary practice for most patients. The comparison cohorts differ in more than ancestry - 100 Alliance trial patients against 323 BeatAML patients, only 55% with confirmed European ancestry - so cohort, treatment and ascertainment differences are confounded with ancestry throughout. Genetic ancestry is not the only or main driver of the outcome disparity the paper opens with; the authors note structural racism and socioeconomic factors, which genomic analysis cannot address. The revised risk stratification is derived and evaluated in the same cohort with no external validation.

## Provenance

Located in the published literature, dropped into `inbox/` as `Stiff(2024) Nat Genet; Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41588-024-01929-x`; the prose sections were written here from the paper itself.

## Citation

Stiff et al. Nature Genetics 2024. Multiomic profiling identifies predictors of survival in African American patients with acute myeloid leukemia. doi: 10.1038/s41588-024-01929-x

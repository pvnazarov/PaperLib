---
# --- identity ------------------------------------------------
id: 2025-01-01_arellano-2025-blood-menin-inhibition-wit
id_basis: filename-year
source: Arellano(2025) Blood; Menin inhibition with revumenib for NPM1-mutated relapsed or refractory acute myeloid leukemia the AUGMENT-101 study.pdf
sha256: a3d6c7bc0933970500b54f7924b1bf703d8c5f4b510e085903f446ce332e0395
size_bytes: 1150705
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 109824

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025028357"
year: 2025
title: "Menin inhibition with revumenib for NPM1-mutated relapsed or refractory acute myeloid leukemia: the AUGMENT-101 study"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Arellano(2025) Blood; Menin inhibition with revumenib for NPM1-mutated relapsed or refractory acute myeloid leukemia the AUGMENT-101 study.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The phase 2 NPM1-mutated cohort of AUGMENT-101 (NCT04065399), testing the oral menin inhibitor revumenib in relapsed or refractory NPM1m AML. 84 patients received at least one dose; the protocol-defined efficacy population was 64 adults, heavily pretreated (35.9% with three or more prior lines, 75.0% with previous venetoclax). The CR + CRh rate was 23.4% (1-sided P = .0014) and overall response rate 46.9%, with median duration of CR + CRh of 4.7 months; 5 of 30 responders proceeded to transplant, and treatment-related adverse events caused discontinuation in 4 patients (4.8%).

## Summary

The clinical anchor of the menin-inhibitor story in this collection. Revumenib blocks the KMT2A-menin interaction, collapsing the MEIS1 and HOX program that mutant NPM1 depends on, and this is the trial showing that the mechanism converts into remissions in patients who have already failed everything, including venetoclax.

Read the two response numbers as different claims. CR + CRh of 23.4% is the registrational endpoint and is modest; ORR of 46.9% says that roughly half the patients respond by some measure. Median duration of 4.7 months places this as a bridge rather than a cure, and the five patients who reached transplant are the concrete version of that argument. Responses occurred regardless of comutations, prior transplant or number of prior lines.

## Key points

- First efficacy report of menin inhibition in NPM1-mutant relapsed/refractory AML, a group with no standard option after venetoclax failure.
- CR + CRh 23.4% and ORR 46.9% in 64 heavily pretreated adults; median age 63.
- Median duration of CR + CRh 4.7 months, with 5 of 30 responders bridged to allogeneic transplant and 3 resuming revumenib afterwards.
- Responses were seen across subgroups regardless of comutations, prior HSCT or number of prior lines.
- Discontinuation for treatment-related adverse events in 4.8%; the safety profile matched the earlier KMT2A-rearranged experience.

## Limitations

Single-arm and open-label, so the response rate has no randomised comparator and the survival figures cannot be attributed to the drug. Investigator-assessed responses, in a trial sponsored by the drug's manufacturer, with several company employees among the authors. The efficacy population is a protocol-defined subset of 64 from 84 dosed, which inflates the rate relative to all-comers. Median duration of response is short and follow-up is limited, so durability is unestablished; the transplant subgroup is 5 patients and cannot support a claim about bridging. Only one patient was under 18, so the pediatric label extrapolates from almost no data here, and the paper does not resolve which comutations, if any, predict resistance.

## Provenance

Located in the published literature, dropped into `inbox/` as `Arellano(2025) Blood; Menin inhibition with revumenib for NPM1-mutated relapsed or refractory acute myeloid leukemia the AUGMENT-101 study.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025028357`; the prose sections were written here from the paper itself.

## Citation

Arellano et al. Blood 2025. Menin inhibition with revumenib for
                    <i>NPM1</i>
                    -mutated relapsed or refractory acute myeloid leukemia: the AUGMENT-101 study. doi: 10.1182/blood.2025028357

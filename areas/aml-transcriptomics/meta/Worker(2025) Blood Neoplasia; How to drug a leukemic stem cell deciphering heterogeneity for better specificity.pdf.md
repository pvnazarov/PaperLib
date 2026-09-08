---
# --- identity ------------------------------------------------
id: 2025-01-01_worker-2025-blood-neoplasia-how-to-drug
id_basis: filename-year
source: Worker(2025) Blood Neoplasia; How to drug a leukemic stem cell deciphering heterogeneity for better specificity.pdf
sha256: f93ea5f7afc01b6fdb42319108fc929d1011ccba2f997995ddbb35bcbfe97115
size_bytes: 1329319
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 75800

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.bneo.2025.100146"
year: 2025
title: "How to drug a leukemic stem cell: deciphering heterogeneity for better specificity"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Worker(2025) Blood Neoplasia; How to drug a leukemic stem cell deciphering heterogeneity for better specificity.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of leukemic stem cell biology framed around the problem of therapeutic specificity. It sets out that relapse is the single most important cause of treatment failure in AML, with more than half of intensively treated patients relapsing within a year, and that relapse originates from quiescent LSCs sheltering in the marrow that escape chemotherapy aimed at proliferating blasts. It surveys global and subtype-specific LSC traits, how heterogeneity between AML subtypes and within the LSC compartment has frustrated target discovery, how single-cell sequencing is resolving that, and which aspects of LSC biology admit targeted treatment.

## Summary

Organised around a specific difficulty rather than around a survey: LSCs resemble hematopoietic stem cells closely enough that most candidate targets are shared, so the question is which of the variable and unique differences can be exploited.

The conclusion is the most useful part, and it is a warning as much as a summary. The facets of LSC biology - quiescence, self-renewal, growth, survival - do not operate in isolation, and there is extensive cross-regulation between growth factor signalling, metabolism and proteostasis. That means combination targeting may be synergistic, as with the unfolded protein response and oxidative stress converging on cell death, or may simply be defeated by compensation when one arm is hit alone. That framing explains a good deal of the single-agent disappointment recorded across this collection.

## Key points

- Relapse is the leading cause of treatment failure, with over half of intensively treated patients relapsing within a year.
- LSCs escape chemotherapy through quiescence and re-enter cycle later to regenerate the leukemia.
- Similarity to normal hematopoietic stem cells is the central obstacle to specificity; the variable differences are where targets must be found.
- Heterogeneity between subtypes and within the LSC compartment has frustrated target discovery, and single-cell methods are addressing it.
- Growth factor signalling, metabolism and proteostasis cross-regulate extensively, so single-pathway targeting invites compensation.

## Limitations

A narrative review with no systematic search or evidence grading, covering a large and contested field selectively. It advocates the cancer stem cell model of relapse, which primary work in this collection challenges - notably the finding that chemotherapy-resistant cells are not enriched for LSCs but are defined by oxidative metabolism, and that a transient senescence-like state confers relapse capacity independent of stem cell status. Its therapeutic content is largely prospective, describing progress toward therapies rather than results. The cross-regulation argument, while well made, is illustrated rather than quantified.

## Provenance

Located in the published literature, dropped into `inbox/` as `Worker(2025) Blood Neoplasia; How to drug a leukemic stem cell deciphering heterogeneity for better specificity.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.bneo.2025.100146`; the prose sections were written here from the paper itself.

## Citation

Worker et al. Blood Neoplasia 2025. How to drug a leukemic stem cell: deciphering heterogeneity for better specificity. doi: 10.1016/j.bneo.2025.100146

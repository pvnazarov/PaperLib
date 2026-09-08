---
# --- identity ------------------------------------------------
id: 2018-01-01_martinez-soria-2018-cancer-cell-the-onco
id_basis: filename-year
source: Martinez-Soria(2018) Cancer Cell; The Oncogenic Transcription Factor RUNX1 ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation.pdf
sha256: e48dcffab6663800b84a11dcad5265cb3cabcba9a1e86e64863623795be3cc06
size_bytes: 5804210
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 125044

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2018.08.015"
year: 2018
title: "The Oncogenic Transcription Factor RUNX1/ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Martinez-Soria(2018) Cancer Cell; The Oncogenic Transcription Factor RUNX1 ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using epigenomic profiling data to direct an RNAi screen against the transcriptional network maintaining t(8;21) AML, the authors identify Cyclin D2 (CCND2) as a crucial transmitter of RUNX1/ETO-driven leukemic propagation. RUNX1/ETO cooperates with AP-1 to drive CCND2 expression, acting both directly - including by interfering with an intergenic negative regulatory element 30 kb from the gene - and indirectly through AP-1 family member expression. Knockdown or pharmacological inhibition of CCND2 with the approved CDK4/6 inhibitor palbociclib significantly impairs expansion of patient-derived AML cells and engraftment in immunodeficient mice.

## Summary

A strategy for drugging an undruggable target by going one step downstream. RUNX1/ETO is a transcription factor fusion with no binding pocket; rather than attack it, the screen asks which of its target genes actually transmits the leukemic phenotype, on the reasoning that a network component may be pharmacologically accessible even when the driver is not.

CCND2 is a good answer because palbociclib already exists and is approved. The mechanism is also more interesting than simple transactivation - RUNX1/ETO activates CCND2 partly by interfering with a negative regulatory element 30 kb away, so an oncogenic transcription factor raises expression by disabling a silencer, which is a mode RUNX family proteins are known for. That 10-15% of t(8;21) AMLs carry CCND2 mutations independently supports the axis mattering in patients.

## Key points

- Epigenomics-instructed RNAi screening identifies CCND2 as the transmitter of RUNX1/ETO function most worth targeting.
- The strategy is to drug a network component downstream of an undruggable transcription factor fusion.
- RUNX1/ETO activates CCND2 both directly - by interfering with an intergenic negative regulatory element - and indirectly via AP-1.
- Palbociclib, an approved CDK4/6 inhibitor, impairs expansion of patient-derived cells and engraftment in mice.
- 10-15% of t(8;21) AMLs carry CCND2 mutations independently, supporting the axis's relevance in patients.

## Limitations

Preclinical: efficacy is impaired expansion and engraftment in immunodeficient mice, not survival benefit or cure, and CDK4/6 inhibitors are cytostatic rather than cytotoxic, so single-agent durability is the obvious concern - the authors' own conclusion is that combinations will be needed and that identifying them is ongoing work. CCND-CDK4/6 activity is required in normal proliferating tissue, and palbociclib's dose-limiting neutropenia is precisely the toxicity that matters when treating a marrow disease. The mechanism is partly indirect through AP-1, so CCND2 is a node rather than the sole effector. Screening was done in t(8;21) cell lines with validation in patient-derived cells, and t(8;21) is a favourable-risk subtype where the unmet need is relapse rather than initial response.

## Provenance

Located in the published literature, dropped into `inbox/` as `Martinez-Soria(2018) Cancer Cell; The Oncogenic Transcription Factor RUNX1 ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2018.08.015`; the prose sections were written here from the paper itself.

## Citation

Martinez-Soria et al. Cancer Cell 2018. The Oncogenic Transcription Factor RUNX1/ETO Corrupts Cell Cycle Regulation to Drive Leukemic Transformation. doi: 10.1016/j.ccell.2018.08.015

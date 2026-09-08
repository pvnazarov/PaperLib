---
# --- identity ------------------------------------------------
id: 2022-01-01_uckelmann-2022-cancer-discovery-mutant-n
id_basis: filename-year
source: Uckelmann(2022) Cancer Discovery; Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia.pdf
sha256: a768e1eed03f53b7d71b23fcaa592e2a57e2435b0852bfe2e65150028f52fda6
size_bytes: 2982076
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 140022

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-22-0366"
year: 2022
title: "Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Uckelmann(2023) Cancer Discov; Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

NPM1c is shown to bind directly to specific chromatin targets co-occupied by the histone methyltransferase KMT2A (MLL1). Targeted degradation of NPM1c causes rapid decrease in gene expression with loss of RNA polymerase II and of activating histone modifications at those targets. The work demonstrates that NPM1c directly regulates oncogenic gene expression in collaboration with the MLL1 complex, and defines the mechanism by which MLL1-menin inhibitors produce clinical responses in NPM1-mutated AML.

## Summary

Resolves the paradox that has defined NPM1-mutant AML since its discovery. The mutation is characterised by cytoplasmic mislocalisation, and most mechanistic work has followed the loss-of-function logic - asking which nuclear proteins are dragged out with it. This shows the opposite: NPM1c binds chromatin directly and activates transcription there, so the oncogene has a gain-of-function role at the very locus its name suggests it has left.

The practical contribution is explaining a drug that already works. Menin inhibitors produce clinical responses in NPM1-mutant AML, a subtype with no MLL rearrangement, and the mechanism had been inferred rather than shown; establishing that NPM1c co-occupies chromatin with MLL1 and requires it supplies that. The authors also note the parallel with their own MLL-AF9 degradation work - similar locus-specific disruption of transcriptional machinery - suggesting a shared oncogenic mechanism.

## Key points

- NPM1c binds chromatin directly at specific targets co-occupied by MLL1, despite its defining cytoplasmic mislocalisation.
- Targeted degradation causes rapid loss of expression, RNA polymerase II and activating histone marks at those targets.
- Reframes NPM1c from a loss-of-function model - proteins evicted to the cytoplasm - to direct transcriptional activation.
- Explains mechanistically why MLL1-menin inhibitors work in NPM1-mutated AML, which carries no MLL rearrangement.
- The pattern parallels MLL-AF9 degradation, suggesting a shared mechanism among oncoproteins driving aberrant transcription.

## Limitations

Degradation requires an engineered degron, so experiments are in modified cell lines rather than patient blasts. Wild-type NPM1 also interacts with chromatin transiently - during late S phase, at DNA damage sites, at rDNA repeats - which the authors discuss, and distinguishing mutant-specific from shared chromatin binding is difficult. They note that NPM1c chromatin recruitment by itself does not appear sufficient, so what determines target specificity is unresolved. The relationship to the condensate model proposed elsewhere in this collection, in which NPM1c acts through nuclear phase-separated bodies, is not addressed and the two accounts of where NPM1c acts have yet to be reconciled.

## Provenance

Located in the published literature, dropped into `inbox/` as `Uckelmann(2023) Cancer Discov; Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-22-0366`; the prose sections were written here from the paper itself.

## Citation

Uckelmann et al. Cancer Discovery 2022. Mutant NPM1 Directly Regulates Oncogenic Transcription in Acute Myeloid Leukemia. doi: 10.1158/2159-8290.CD-22-0366

---
# --- identity ------------------------------------------------
id: 2020-01-01_falini-2020-blood-npm1-mutated-acute-mye
id_basis: filename-year
source: Falini(2020) Blood; NPM1-mutated acute myeloid leukemia from bench to bedside.pdf
sha256: 431a881da39a7f61bad5c0713e717c21a0b5b715984150fe587238f38f37398b
size_bytes: 2227645
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 125662

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2019004226"
year: 2020
title: "NPM1-mutated acute myeloid leukemia: from bench to bedside"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Falini(2020) Blood; NPM1-mutated acute myeloid leukemia from bench to bedside.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of NPM1-mutated AML by the group that discovered the mutation, covering newly identified functions of wild-type NPM1 in the nucleolus - including its role in liquid-liquid phase separation with R-motif proteins and nascent rRNA - and the biology and clinical management of the mutant entity. It addresses cooperation between NPM1 and other mutations in producing different outcomes, the need to eradicate NPM1-mutated clones for cure, the role of persisting preleukemic clonal hematopoiesis in predisposing to second AML, the contribution of HOX gene expression, unresolved diagnostic issues in the 2017 WHO classification, the place of NPM1 in European LeukemiaNet risk stratification, the value and limits of NPM1-based measurable residual disease assessment, and preclinical results with XPO1 and menin-MLL inhibitors.

## Summary

The authoritative review of the entity, written by Falini, who discovered cytoplasmic nucleophosmin in AML by immunohistochemistry before next-generation sequencing existed. It is the right place to see why NPM1-mutated AML became one of only two WHO leukemia entities defined by a single gene mutation.

Its most useful feature for this collection is that it is candid about what is unresolved rather than tidy. Whether the diagnosis should hold irrespective of blast percentage is open; MRD measurement is not standardised and its impact at different timepoints is not well defined; and the distinction between eradicating the NPM1-mutant clone and leaving preleukemic clonal hematopoiesis behind - which predisposes to a second AML - is drawn clearly. The nucleolar phase-separation section anticipates the condensate work that follows later in this collection.

## Key points

- NPM1 mutations are the most common lesion in adult AML (about one third) and define a distinct WHO entity.
- Wild-type NPM1 organises the nucleolus through liquid-liquid phase separation with R-motif proteins and nascent rRNA.
- HOX gene expression is central to the leukemic phenotype; XPO1 and menin-MLL inhibitors are the preclinical therapeutic leads.
- Curing the disease requires eradicating the NPM1-mutant clone; persisting preleukemic clonal hematopoiesis predisposes to a second, distinct AML.
- NPM1-based measurable residual disease is valuable but not standardised, and its impact at different timepoints needs better definition.

## Limitations

A narrative review with no stated search strategy or evidence appraisal, written by the group that discovered the mutation - authoritative, and also invested in the entity's significance. Published 2020, so the clinical menin inhibitor results reported elsewhere in this collection postdate it, and its treatment sections are correspondingly out of date. The corresponding author holds a patent on NPM1 mutants, which is disclosed. Several of the most important questions it raises - blast percentage in the diagnostic definition, MRD standardisation and timing - are posed rather than answered, which is honest but means the review states the state of uncertainty rather than resolving it.

## Provenance

Located in the published literature, dropped into `inbox/` as `Falini(2020) Blood; NPM1-mutated acute myeloid leukemia from bench to bedside.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2019004226`; the prose sections were written here from the paper itself.

## Citation

Falini et al. Blood 2020. NPM1-mutated acute myeloid leukemia: from bench to bedside. doi: 10.1182/blood.2019004226

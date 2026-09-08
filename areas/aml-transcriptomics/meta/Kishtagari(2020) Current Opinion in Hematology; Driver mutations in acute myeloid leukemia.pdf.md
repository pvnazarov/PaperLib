---
# --- identity ------------------------------------------------
id: 2020-01-01_kishtagari-2020-current-opinion-in-hemat
id_basis: filename-year
source: Kishtagari(2020) Current Opinion in Hematology; Driver mutations in acute myeloid leukemia.pdf
sha256: a80a618202d4ad1897cb96036fe9c24c9356e913fe72fd887a56e5aa29212208
size_bytes: 651911
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 74694

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1097/MOH.0000000000000567"
year: 2020
title: "Driver mutations in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kishtagari(2020) Curr Opin Hematol; Driver mutations in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of recurrently mutated genes in AML and their functional consequences beyond conventional oncogene activation and tumour suppressor loss. It covers the 40-50 genes carrying recurrent somatic mutations, organised around DNA methylation effectors, chromatin modifiers, spliceosomal machinery and transcription factors, and notes that many of these mutations are found across a spectrum from clonal hematopoiesis through myelodysplasia to overt AML. Mutation-based targeted therapy has produced several FDA-approved drugs, and the review argues that understanding the pathophysiologic functions of these genes is what will translate genomics into treatment.

## Summary

A compact orientation to the AML mutational landscape, with two arguments that carry beyond a catalogue. The first is about the shape of the disease: AML is constituted either by a few strong drivers such as NPM1 or by serial acquisition of individually weaker lesions, and co-mutational interaction dominates outcome in ways that resist decoding - DNMT3A and NPM1 co-occur commonly, yet adding NRAS versus FLT3-ITD gives dramatically different prognosis and chemosensitivity.

The second is a candid comparison the field tends to avoid: FLT3 and IDH1/2 inhibitors have improved outcomes but nothing like imatinib in BCR-ABL, and the reason is the multigenic nature of AML. The review's closing suggestion - that because many disease alleles appear in clonal hematopoiesis, the intervention point might be earlier, in clonal cytopenia of undetermined significance - is the more interesting proposal.

## Key points

- Organises 40-50 recurrently mutated AML genes by function: methylation, chromatin, splicing, transcription factors.
- NPM1 mutation (~30% of AML) is explained mechanistically: NPM1c chaperones PU.1 to the cytoplasm, releasing its repression of HOX/MEIS1.
- Disease constitution reflects either few strong drivers or serial accumulation of weaker ones; co-mutation dominates prognosis.
- Targeted FLT3 and IDH1/2 inhibitors have improved outcomes but not to the degree seen with imatinib in BCR-ABL.
- Suggests earlier intervention in clonal hematopoiesis and clonal cytopenia of undetermined significance.

## Limitations

A short opinion-format review from 2020 with no systematic search, so coverage is selective and shaped by the authors' interests; it predates the menin inhibitor clinical data and much else in this collection. It surveys mechanism rather than evaluating evidence quality, and prognostic statements reflect the ELN framework as it then stood. The proposal to intervene in clonal hematopoiesis is offered as a question rather than supported by data, and would require evidence that early treatment prevents progression - which does not exist. One senior author declares extensive industry relationships including supervisory board, advisory and consulting roles across numerous companies.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kishtagari(2020) Curr Opin Hematol; Driver mutations in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1097/MOH.0000000000000567`; the prose sections were written here from the paper itself.

## Citation

Kishtagari et al. Current Opinion in Hematology 2020. Driver mutations in acute myeloid leukemia. doi: 10.1097/MOH.0000000000000567

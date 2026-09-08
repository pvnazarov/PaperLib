---
# --- identity ------------------------------------------------
id: 2025-01-01_venkatasubramanian-2025-science-translat
id_basis: filename-year
source: Venkatasubramanian(2025) Science Translational Medicine; Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias.pdf
sha256: 1dc5ae6a299176e98c2a8a838defdbe3b3d6004355d74af5190a07c1dd64c799
size_bytes: 1725284
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 151091

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/scitranslmed.adr1471"
year: 2025
title: "Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Venkatasubramanian(2025) Sci Transl Med; Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

OncoSplice, an unsupervised computational workflow, defines tumour molecular landscapes from splicing profiles. In adult and pediatric AML it identified the spectrum of driver genetics from splicing alone, defined over a dozen new recurrent molecular subtypes, and discovered a dominant subtype partially phenocopying U2AF1-mutant splicing. This U2AF1-like subtype spans pediatric and adult AML genetics despite pediatric leukemias lacking splicing factor mutations, and consistently predicts poor prognosis. Long-read single-cell RNA-seq confirmed the splicing programme is shared across cell states, co-opts a healthy circadian gene programme, is stable through relapse, and induces a leukemia stem cell programme. PRMT5 inhibition rescued the mis-splicing and inhibited growth, and deleting IRAK4 blocked leukemia development in xenografts and induced differentiation.

## Summary

Establishes that the splicing consequences of splicing factor mutations can occur without the mutations - U2AF1-like and SRSF2-like programmes together describe close to 80% of adult and pediatric AML, while splicing factor mutations are present in 10-15% of adults and are rare in children. That converts splicing dysregulation from a subtype-specific problem into a general one, and the pediatric finding is the cleanest evidence, since those patients cannot have acquired the phenotype from the mutation.

The therapeutic chain is complete in a way most such papers are not: a subtype, an implicated regulator whose inhibition rescues the splicing, and a downstream target, IRAK4, whose deletion blocks leukemia in xenografts and induces differentiation. IRAK4 is a well-chosen endpoint because hypermorphic IRAK4 isoform inclusion is already established in MDS and AML.

## Key points

- Splicing profiles alone recover the spectrum of AML driver genetics and define over a dozen new recurrent subtypes.
- U2AF1-like and SRSF2-like splicing programmes describe close to 80% of adult and pediatric AML without requiring the mutations.
- The U2AF1-like programme predicts poor prognosis, is stable through relapse, and induces a leukemia stem cell programme.
- It co-opts a healthy circadian gene regulatory programme - supported by circadian transcription factor regulation and CYCLOPS ordering.
- PRMT5 inhibition rescues the mis-splicing; deleting the shared target IRAK4 blocks leukemia in xenografts and induces differentiation.

## Limitations

The authors state their limitations clearly. Culturing SRSF2-like primary cells resets splicing to a high U2AF1-like state, which prevents modelling SRSF2-like splicing in conventional xenografts - so half the framework cannot currently be tested therapeutically. The circadian hypothesis predicts that U2AF1-like splicing oscillates through the day in healthy but not leukemic marrow, and confirming it requires temporal single-cell analysis of healthy bone from the same donors, which was not done. And although the programmes are attributed to U2AF1 and SRSF2 dysregulation, knockdown analyses indicate they may arise from coordinated dysregulation of multiple interacting splicing factors, so the naming may overstate the specificity.

## Provenance

Located in the published literature, dropped into `inbox/` as `Venkatasubramanian(2025) Sci Transl Med; Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/scitranslmed.adr1471`; the prose sections were written here from the paper itself.

## Citation

Venkatasubramanian et al. Science Translational Medicine 2025. Splicing regulatory dynamics for precision analysis and treatment of heterogeneous leukemias. doi: 10.1126/scitranslmed.adr1471

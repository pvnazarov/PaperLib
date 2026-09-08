---
# --- identity ------------------------------------------------
id: 2023-01-01_dimambro-2023-oncogene-set-pp2a-complex
id_basis: filename-year
source: DiMambro(2023) Oncogene; SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML.pdf
sha256: 81be11a39b32978c36c51c6a2a07358de32b7fe2557f3cfc8a6b4ff822016ba3
size_bytes: 3463882
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 97314

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41388-023-02840-1"
year: 2023
title: "SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as DiMambro(2023) Oncogene; SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

SET, the endogenous inhibitor of the Ser/Thr phosphatase PP2A, is shown to be overexpressed in AML, with elevated expression correlating with poor prognosis and with MEIS and HOXA expression. Silencing SET specifically abolished clonogenic ability of KMT2A-rearranged leukemic cells and transcription of the KMT2A targets HOXA9 and HOXA10. SET interacts with both wild-type KMT2A and the fusion proteins and is recruited to the HOXA10 promoter. Pharmacological inhibition by FTY720 disrupted the SET-PP2A interaction, causing cell cycle arrest and increased chemosensitivity; phosphoproteomics showed reduced activity of PP2A-regulated kinases ERK1, GSK3beta, AURB and PLK1 and suppression of MYC.

## Summary

A deliberate move against the grain of the KMT2A-rearranged literature, which has been overwhelmingly about kinases. Here the argument is that the phosphatase side has been ignored, and that PP2A is held down in these cells by an overexpressed inhibitor - so the intervention is to release a brake rather than block an accelerator.

The mechanistic reach is what makes it more than a phosphatase story: SET is found physically at the HOXA10 promoter and interacting with KMT2A itself, which places it inside the transcriptional machinery rather than merely downstream in signalling. The proposed feedback loop among PP2A, AURB, PLK1, MYC and SET is presented as a hypothesis, which is the right register for it.

## Key points

- SET, a PP2A inhibitor, is overexpressed in AML and its expression correlates with poor prognosis and with MEIS/HOXA expression.
- Silencing SET abolishes clonogenicity specifically in KMT2A-rearranged cells and shuts down HOXA9 and HOXA10 transcription.
- SET binds both wild-type KMT2A and the fusion proteins and is recruited to the HOXA10 promoter.
- FTY720 disrupts SET-PP2A, causing cell cycle arrest and increasing chemosensitivity; phosphoproteomics shows reduced ERK1, GSK3beta, AURB, PLK1 activity and MYC suppression.
- Shifts attention in KMT2A-r leukemia from kinases, where the field has concentrated, to phosphatase regulation.

## Limitations

FTY720 (fingolimod) is an approved immunosuppressant, and the paper reports that in their in vivo models it caused immunosuppression, lymphopenia and severe weight loss - reported as 'data not shown', which is a weak way to present the finding that most constrains translation. The therapeutic proposal therefore rests on non-immunosuppressive analogues that the authors have not tested here, saying only that further studies are needed. FTY720 is also pleiotropic beyond SET-PP2A, so attributing the phenotype to that interaction is not airtight. The prognostic correlations come from re-used public expression datasets. Efficacy is clonogenic and cell cycle readouts in cell lines and models, without in vivo anti-leukemic benefit at a tolerated dose.

## Provenance

Located in the published literature, dropped into `inbox/` as `DiMambro(2023) Oncogene; SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41388-023-02840-1`; the prose sections were written here from the paper itself.

## Citation

DiMambro et al. Oncogene 2023. SET-PP2A complex as a new therapeutic target in KMT2A (MLL) rearranged AML. doi: 10.1038/s41388-023-02840-1

---
# --- identity ------------------------------------------------
id: 2022-01-01_wang-2022-cancer-discovery-mutant-npm1-h
id_basis: filename-year
source: Wang(2022) Cancer Discovery; Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia.pdf
sha256: 0241ca76e254479488ce9d57cadedc020ab3b0d51cfc734acc9c2ed5ceb8264b
size_bytes: 16785785
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 219930

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-22-0424"
year: 2022
title: "Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wang(2023) Cancer Discov; Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

NPM1c is shown to bind a subset of active gene promoters in NPM1c AML, including HOXA/B cluster genes and MEIS1. It sustains active transcription of these targets by orchestrating a transcription hub and maintains the active chromatin landscape by inhibiting histone deacetylase activity, thereby preventing the silencing that normally accompanies myeloid differentiation. The authors observe that NPM1c forms condensates significantly smaller than those of wild-type NPM1, and propose that NPM1c acts as a transcriptional amplifier rather than forming mesoscale phase-separated puncta that would exclude transcriptional machinery.

## Summary

Published alongside Uckelmann's paper in the same issue and reaching the same central conclusion by independent means - that NPM1c binds chromatin directly and activates transcription - which is unusually strong corroboration for a claim that overturns the prevailing loss-of-function model.

This version adds two things. The mechanism includes active inhibition of HDACs, so NPM1c does not merely activate but blocks the silencing that would normally occur as myeloid cells differentiate - which is a specific account of the differentiation block. And it engages the condensate question directly: NPM1c condensates are smaller than the wild-type nucleolar ones, which the authors read as a transcription hub incorporating Pol II rather than a large phase-separated body that would exclude it. That is a substantive alternative to the C-body model proposed elsewhere in this collection. They also address the paradox of a cytoplasmic protein regulating transcription by noting NPM1c retains two nuclear localisation signals and shuttles.

## Key points

- NPM1c binds active promoters including HOXA/B and MEIS1, corroborating the direct-regulation model published simultaneously by an independent group.
- It maintains the active chromatin landscape by inhibiting HDACs, blocking the silencing that accompanies normal myeloid differentiation.
- NPM1c retains two nuclear localisation signals and shuttles, resolving how a cytoplasmic protein acts on chromatin.
- NPM1c condensates are smaller than wild-type nucleolar ones, consistent with a Pol II-containing transcription hub rather than exclusionary phase separation.
- Combining menin inhibition (MI-3454) with XPO1 inhibition (eltanexor) suppresses HOXA/B expression cooperatively in vitro and in vivo.

## Limitations

The transcription hub model and the C-body phase-separation model proposed elsewhere in this collection give different accounts of the same protein, and this paper argues against mesoscale phase separation on the basis of condensate size - an indirect argument that the two groups have not yet reconciled experimentally. HDAC inhibition by NPM1c is inferred from chromatin state changes rather than from a direct enzymatic assay in the summary evidence. The combination therapy data are preclinical, in cell lines and xenografts. The claim that NPM1c needs to be at 'the right concentration' in the nucleus to form hubs is stated as a requirement without being quantified.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wang(2023) Cancer Discov; Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-22-0424`; the prose sections were written here from the paper itself.

## Citation

QingDavidWang et al. Cancer Discovery 2022. Mutant NPM1 Hijacks Transcriptional Hubs to Maintain Pathogenic Gene Programs in Acute Myeloid Leukemia. doi: 10.1158/2159-8290.CD-22-0424

---
# --- identity ------------------------------------------------
id: 2023-01-01_radzisheuskaya-2023-the-embo-journal-an
id_basis: filename-year
source: Radzisheuskaya(2023) The EMBO Journal; An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions.pdf
sha256: f84895d978577f1c8c9c02ed337a1d52876ff7f21858f42a88f8e8be6d755865
size_bytes: 2576164
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 309270

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.15252/embj.2023114221"
year: 2023
title: "An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Radzisheuskaya(2023) EMBO J; An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A CRISPRi screen against chromatin factors identified the NURF subunit BPTF as essential for AML cell survival. BPTF forms an alternative NURF complex with SMARCA5 and BAP18 that regulates accessibility at a large set of insulator regions, ensuring efficient CTCF binding and boundary formation between topologically associated domains, which maintains the leukemic transcriptional program - including the interaction between the BENC enhancer and the MYC promoter. The well-studied PHD2-BROMO chromatin reader domains of BPTF contribute to recruitment but are dispensable for leukemic growth.

## Summary

Two findings that cut against expectation. The first is domain-level: the PHD and bromodomain reader modules of BPTF, which are the parts anyone would try to drug and the parts the literature has concentrated on, are not required for leukemic growth - so a reader-domain inhibitor would miss the essential function.

The second concerns MYC. NURF loss reduces MYC expression only 30-40%, and MYC overexpression does not rescue the phenotype - so unlike SWI/SNF loss in AML, this is not a MYC story. The authors take that as evidence for a global role in TAD insulation rather than a single-target one, and note that TAD structure modulates transcriptional output rather than determining it. The therapeutic angle is a clean piece of reasoning from public data: the canonical NURF ATPase SMARCA1 is not expressed in AML lines, and across DepMap, SMARCA1 expression predicts SMARCA5 sensitivity - so lacking the paralog is what makes these cells vulnerable.

## Key points

- BPTF, with SMARCA5 and BAP18, forms an alternative NURF complex essential for AML survival in vitro and in vivo.
- The complex maintains accessibility at insulator regions, supporting CTCF binding and TAD boundary formation.
- The PHD2-BROMO reader domains of BPTF aid recruitment but are dispensable for leukemic growth - a warning for reader-domain drug design.
- MYC falls only 30-40% and MYC overexpression does not rescue, so the mechanism is global chromatin architecture rather than a single target.
- SMARCA1 is not expressed in AML lines, and SMARCA1 expression predicts SMARCA5 sensitivity across DepMap - the basis for selectivity.

## Limitations

The alternative BPTF/SMARCA5 complex is not leukemia-specific - the authors note BPTF interacts with SMARCA5 in HeLa and HEK293T cells - so selectivity depends on the absence of SMARCA1 rather than on the complex itself, and how broadly that absence holds across normal tissues is not established. With the reader domains dispensable, there is no obvious druggable module: targeting the SMARCA5 ATPase would hit a broadly required remodeller. The mechanism is global chromatin architecture, which is harder to attribute causally than a single-gene effect, and the authors themselves cannot point to the specific target genes that matter. Work is in MLL-rearranged AML cell lines with in vivo validation in models rather than in primary patient material.

## Provenance

Located in the published literature, dropped into `inbox/` as `Radzisheuskaya(2023) EMBO J; An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.15252/embj.2023114221`; the prose sections were written here from the paper itself.

## Citation

Radzisheuskaya et al. The EMBO Journal 2023. An alternative NURF complex sustains acute myeloid leukemia by regulating the accessibility of insulator regions. doi: 10.15252/embj.2023114221

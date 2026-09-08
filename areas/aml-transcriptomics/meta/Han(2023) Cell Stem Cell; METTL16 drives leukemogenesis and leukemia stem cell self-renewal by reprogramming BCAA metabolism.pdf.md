---
# --- identity ------------------------------------------------
id: 2023-01-01_han-2023-cell-stem-cell-mettl16-drives-l
id_basis: filename-year
source: Han(2023) Cell Stem Cell; METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism.pdf
sha256: b17354c9c9dd2df2e43a9c345e7946cdc7c3ee86df487cc3358b31e4fe118919
size_bytes: 8507967
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 162780

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.stem.2022.12.006"
year: 2023
title: "METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Han(2023) Cell Stem Cell; METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

CRISPR-Cas9 screening and validation identify METTL16, an m6A methyltransferase, as highly essential for AML cell survival, aberrantly overexpressed in human AML and especially in leukemia stem and initiating cells. Genetic depletion suppresses AML initiation, development and maintenance and attenuates LSC/LIC self-renewal while only moderately affecting normal hematopoiesis in mice. Mechanistically METTL16 promotes expression of the branched-chain amino acid transaminases BCAT1 and BCAT2 in an m6A-dependent manner, reprogramming BCAA metabolism.

## Summary

Extends the m6A story in AML in two directions at once - to a second methyltransferase beyond METTL3, and to amino acid metabolism, where m6A's role had not been examined. The BCAA connection is mechanistically satisfying because BCAT1/2 feed the TCA cycle and nucleotide biosynthesis, tying an RNA modification to the oxidative metabolism that recurs throughout this collection as the leukemic vulnerability.

The therapeutic argument is explicitly comparative: METTL16 is less required than METTL3 for normal human HSPC proliferation and repopulation, yet more essential for AML development and LSC self-renewal, so the authors argue it is the better target of the two. The paper carries a formal Limitations section, unusually, and states what it has not done.

## Key points

- METTL16 is an AML-selective dependency, overexpressed in AML and enriched in leukemia stem and initiating cells.
- Depletion suppresses AML initiation, development and maintenance and LSC/LIC self-renewal with only moderate effect on normal hematopoiesis.
- The mechanism is m6A-dependent upregulation of BCAT1 and BCAT2, reprogramming branched-chain amino acid metabolism.
- First demonstration of m6A regulating tumour amino acid metabolism, as opposed to glycolysis or glutamine metabolism.
- Argued to be a safer target than METTL3 - less required by normal HSPCs, more required by AML.

## Limitations

No METTL16 inhibitor exists, which the authors state as their first listed limitation: whether a small molecule could kill LSCs while sparing normal HSPCs is untested. Constitutive homozygous Mettl16 knockout is embryonically lethal, so safety in non-hematopoietic tissues is a live concern that the authors flag as needing systematic study. The claim that METTL16 is a safer target than METTL3 is partly extrapolated from published data on the METTL3 inhibitor STM2457 rather than from a head-to-head comparison, and the authors concede systematic comparative studies are warranted. 'Moderately influencing normal hematopoiesis' is a real effect, not none. Much of the dependency evidence comes from CERES scores in cell-line panels plus knockdown, and the m6A-dependence of BCAT1/2 regulation relies on antibody-based m6A mapping.

## Provenance

Located in the published literature, dropped into `inbox/` as `Han(2023) Cell Stem Cell; METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.stem.2022.12.006`; the prose sections were written here from the paper itself.

## Citation

Han et al. Cell Stem Cell 2023. METTL16 drives leukemogenesis and leukemia stem cell self-renewal by reprogramming BCAA metabolism. doi: 10.1016/j.stem.2022.12.006

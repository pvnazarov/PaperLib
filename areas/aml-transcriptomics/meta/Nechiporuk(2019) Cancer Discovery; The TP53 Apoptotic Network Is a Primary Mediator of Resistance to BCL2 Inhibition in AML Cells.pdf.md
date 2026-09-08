---
# --- identity ------------------------------------------------
id: 2019-01-01_nechiporuk-2019-cancer-discovery-the-tp5
id_basis: filename-year
source: Nechiporuk(2019) Cancer Discovery; The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells.pdf
sha256: 8b61e3f3fc87e136c517b81cdd2ff27a764eaddcc8270eb3e4ab531fccbd23a1
size_bytes: 3993520
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 201222

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-19-0125"
year: 2019
title: "The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Nechiporuk(2019) Cancer Discov; The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A genome-wide CRISPR/Cas9 screen for gene knockouts conferring venetoclax resistance in AML validated TP53, BAX and PMAIP1. Resistance arose from inability to execute apoptosis after BAX loss, decreased BCL2 expression, and reliance on alternative family members such as BCL2L1, accompanied by changes in mitochondrial homeostasis and cellular metabolism. Screening TP53 knockout cells against a panel of small-molecule inhibitors revealed gained sensitivity to TRK inhibitors, associated with increased NTRK3 and decreased NTRK1 expression. Findings were related to patient drug responses and expression in the Beat AML dataset.

## Summary

Explains why venetoclax underperforms in AML relative to CLL, and quantifies the gap using the Beat AML ex vivo data - median IC50 of 1.4 micromolar for AML against 0.1 for CLL. The mechanism is that BCL2 inhibition only kills if the downstream apoptotic machinery is intact, so TP53, BAX or PMAIP1 loss makes the drug irrelevant regardless of target engagement.

That has a direct clinical correlate the authors point to: in the venetoclax-azacitidine experience, the TP53-mutant subset had the worst response of any group. What makes the paper more than a resistance catalogue is the collateral sensitivity - TP53 knockout cells gain sensitivity to TRK inhibitors, with an NTRK3-up, NTRK1-down expression switch, which turns a resistance mechanism into a candidate second-line strategy for the group that needs one most.

## Key points

- TP53, BAX and PMAIP1 loss confer venetoclax resistance - the drug fails when the downstream apoptotic machinery is broken, not when the target is unengaged.
- Resistance also involves lower BCL2 expression and switching to alternative family members such as BCL2L1.
- Quantifies the AML/CLL gap in the Beat AML data: median venetoclax IC50 1.4 micromolar versus 0.1 micromolar.
- TP53 knockout cells gain sensitivity to TRK inhibitors, with increased NTRK3 and decreased NTRK1.
- Matches the clinical observation that TP53-mutant patients respond worst to venetoclax-azacitidine.

## Limitations

The collateral TRK sensitivity is derived from TP53 knockout cell lines, not from TP53-mutant primary AML - and knockout is not equivalent to the missense mutations that predominate in patients, which often have gain-of-function properties. NTRK-driven cancers are rare (under 1%), and TRK inhibitor efficacy is established for fusion-positive disease, so extending it to TP53-altered AML on the basis of an expression shift is a substantial leap. The screen is in cell lines; the patient link is correlative association with Beat AML drug response and expression. Multiple resistance mechanisms are identified without establishing their relative frequency in patients, and the metabolic and mitochondrial changes are described as accompanying resistance rather than causing it.

## Provenance

Located in the published literature, dropped into `inbox/` as `Nechiporuk(2019) Cancer Discov; The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-19-0125`; the prose sections were written here from the paper itself.

## Citation

Nechiporuk et al. Cancer Discovery 2019. The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells. doi: 10.1158/2159-8290.CD-19-0125

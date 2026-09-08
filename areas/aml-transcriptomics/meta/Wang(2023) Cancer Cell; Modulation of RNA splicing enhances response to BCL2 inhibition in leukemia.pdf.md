---
# --- identity ------------------------------------------------
id: 2023-01-01_wang-2023-cancer-cell-modulation-of-rna
id_basis: filename-year
source: Wang(2023) Cancer Cell; Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia.pdf
sha256: 23257cac7df2eeee4051097878f3fb50f5d69bb297c62fe5c58d233303b185ee
size_bytes: 6438795
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 148099

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2022.12.002"
year: 2023
title: "Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wang(2023) Cancer Cell; Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

CRISPR-Cas9 screens across a range of AML therapies identified a selective dependency on RNA splicing factors whose loss preferentially enhances venetoclax response. Loss of the splicing factor RBM10 augments venetoclax response while being completely dispensable for normal hematopoiesis; combined RBM10 and BCL2 inhibition causes mis-splicing and inactivation of the apoptosis inhibitor XIAP and downregulation of BCL2A1, an anti-apoptotic protein implicated in venetoclax resistance. Inhibiting the CLK and DYRK splicing kinase families produces aberrant splicing of key splicing and apoptotic factors that synergises with venetoclax and overcomes resistance.

## Summary

Turns splicing modulation into a sensitiser rather than a cytotoxic. The screen is designed the right way round - across multiple AML therapies, so the splicing dependency emerges as specific to venetoclax rather than as a general fitness effect - and RBM10 loss being completely dispensable for normal hematopoiesis is the property that makes it worth pursuing.

The mechanism is doubly apt: mis-splicing inactivates XIAP, removing a brake on apoptosis, and downregulates BCL2A1, which is a known route to venetoclax resistance. So the intervention both enhances the drug and closes an escape. The CLK/DYRK kinase inhibitor extends this to a druggable approach, and the authors are appropriately measured about the early clinical data, noting only that hematologic recovery is required for complete remission in AML and that the toxicity therefore appears manageable.

## Key points

- Screening across multiple AML therapies identifies splicing factor loss as selectively enhancing venetoclax, not as a general fitness effect.
- RBM10 loss augments venetoclax response and is completely dispensable for normal hematopoiesis.
- The mechanism is mis-splicing that inactivates XIAP and downregulates BCL2A1, a known venetoclax resistance factor.
- CLK and DYRK kinase inhibition reproduces the effect pharmacologically and overcomes established resistance.
- Addresses the central clinical problem that venetoclax plus hypomethylating agent is effective but not curative.

## Limitations

The clinical data on the CLK/DYRK inhibitor SM09419 are early, and the authors' own conclusion is cautious - feasibility is inferred from manageable hematologic toxicity rather than from efficacy. They note it remains to be tested whether particular genetic alterations are more susceptible, so patient selection is unresolved. CLK and DYRK are families with broad substrate ranges, so the inhibitor is not a precise tool. RBM10 itself has no inhibitor. Six authors are employees of Biosplice Therapeutics, which develops the compound, and the senior author declares extensive consulting and advisory relationships including several companies in the splicing therapeutics space.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wang(2023) Cancer Cell; Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2022.12.002`; the prose sections were written here from the paper itself.

## Citation

Wang et al. Cancer Cell 2023. Modulation of RNA splicing enhances response to BCL2 inhibition in leukemia. doi: 10.1016/j.ccell.2022.12.002

---
# --- identity ------------------------------------------------
id: 2017-01-01_zaidi-2017-oncotarget-an-aml1-eto-mir-29
id_basis: filename-year
source: Zaidi(2017) Oncotarget; An AML1-ETO miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells.pdf
sha256: 72c88dc12a93f2180527a2c3ce4fc6d176ec0a4a098b8a89a65f7b74c8d9d663
size_bytes: 2150357
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 55906

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.18632/oncotarget.18127"
year: 2017
title: "An AML1-ETO/miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zaidi(2017) Oncotarget; An AML1-ETO miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

AML1-ETO and the corepressor NCoR co-occupy the miR-29a/b-1 locus and downregulate its expression in leukemia cells. Conversely, reintroducing miR-29b-1 into AML1-ETO-expressing cells causes significant downregulation of the fusion protein by directly targeting the 3' untranslated region of the chimeric transcript. Restoring miR-29b-1 decreases cell growth, increases apoptosis, and partially reverses the AML1-ETO-dependent differentiation block and transcriptional program, establishing a regulatory circuit between the tumour-suppressive microRNA and the oncogenic fusion.

## Summary

A mutually antagonistic loop: the fusion protein represses the microRNA, and the microRNA degrades the fusion transcript - so each suppresses the other, and the leukemic state depends on which direction the balance has settled. That makes it in principle a switch that could be flipped, which is the therapeutic appeal.

The mechanism is direct on both arms - AML1-ETO with NCoR occupying the miR-29a/b-1 locus, and miR-29b-1 targeting the 3'UTR of the chimeric transcript - and restoring the microRNA reverses the phenotype partially, with reduced growth, increased apoptosis and some recovery of differentiation as measured by myeloperoxidase activity.

## Key points

- AML1-ETO with NCoR occupies and represses the miR-29a/b-1 locus.
- miR-29b-1 directly targets the 3'UTR of the AML1-ETO chimeric transcript, lowering fusion protein levels.
- The two form a mutually antagonistic circuit whose balance determines the leukemic phenotype.
- Restoring miR-29b-1 reduces growth, increases apoptosis and partially reverses the differentiation block.
- Adds a non-coding RNA layer to t(8;21) biology, which had been studied almost entirely at the protein and chromatin level.

## Limitations

Effects are modest and the authors describe them as such - the increase in myeloperoxidase activity is 'modest but significant', reversal of the differentiation block is partial, and the control microRNA miR-15 produced some of the same directional effects, which weakens the specificity. Work is confined to the SKNO-1 cell line with no primary patient samples or in vivo models. Restoring a microRNA is not a therapeutic strategy with current delivery technology. The colony-forming results are difficult to reconcile with the growth suppression, since colony numbers continued to increase for both miR-15 and miR-29b-1 infected cells. Published in a journal whose editorial standing has been questioned.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zaidi(2017) Oncotarget; An AML1-ETO miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.18632/oncotarget.18127`; the prose sections were written here from the paper itself.

## Citation

Zaidi et al. Oncotarget 2017. An AML1-ETO/miR-29b-1 regulatory circuit modulates phenotypic properties of acute myeloid leukemia cells. doi: 10.18632/oncotarget.18127

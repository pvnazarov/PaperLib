---
# --- identity ------------------------------------------------
id: 2016-01-01_wang-2016-current-opinion-in-genetics-de
id_basis: filename-year
source: Wang(2016) Current Opinion in Genetics & Development; The role of DOT1L in the maintenance of leukemia gene expression.pdf
sha256: 1b119f2baf6f4487edd5fed4bd2759bb2c6c3905bad046ec6bbbbee8dbd73b57
size_bytes: 419926
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 33323

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.gde.2016.03.015"
year: 2016
title: "The role of DOT1L in the maintenance of leukemia gene expression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wang(2016) Curr Opin Genet Dev; The role of DOT1L in the maintenance of leukemia gene expression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of DOT1L, the H3K79 methyltransferase required for maintenance of MLL-rearranged leukemia. It covers the structural basis of chromatin targeting through cofactors AF9 and AF10, proposed as readers of histone modifications that recruit the DOT1L complex to open chromatin; the role of DOT1L in preventing SIRT1-mediated gene silencing in MLL-rearranged cells; and H3K79 methylation as a mechanism of selective gene regulation. No demethylase for H3K79 has been identified, so regulation of DOT1L activity is likely the dominant determinant of the mark.

## Summary

A compact account of why DOT1L became a therapeutic target and what remains unexplained about it. The most useful point is the selectivity puzzle: global loss of H3K79 methylation arrests transcription of only a subset of genes, housekeeping genes are largely unaffected, and MLL-AF9-bound genes are specifically downregulated - so the mark's presence does not determine dependence on it, and something else selects which genes need DOT1L.

The review also corrects a common assumption about complex membership. DOT1L is often placed with the super elongation complex, but several studies indicate it is not in the same complex as AF4 family proteins and in fact competes with AFF4 for the AHD domain of ENL and AF9 - so the link between DOT1L and active transcriptional machinery is described as inconclusive. That framing anticipates the later finding elsewhere in this collection that menin and DOT1L inhibition act on different timescales.

## Key points

- No H3K79 demethylase has been identified, so regulation of DOT1L activity is likely the dominant determinant of the mark.
- AF9 and AF10 are proposed as readers recruiting DOT1L to open chromatin - the structural basis of its targeting.
- DOT1L prevents SIRT1-mediated silencing in MLL-rearranged cells, framing it as repelling repression rather than only activating.
- Losing H3K79 methylation arrests only a subset of genes - housekeeping genes are spared, MLL-AF9 targets are not - which is the basis of therapeutic selectivity.
- DOT1L competes with AFF4 for the ENL/AF9 AHD domain, so it is likely not part of the super elongation complex.

## Limitations

A short opinion-format review from 2016 with no systematic search, and it states directly that the molecular mechanism underlying the epigenetic dependency is not well understood and that the link between DOT1L and active transcription remains inconclusive. It predates the clinical outcome for this target: DOT1L inhibitors subsequently showed only modest activity in adult acute leukemia trials, which the enthusiasm here does not anticipate. Coverage is mechanism-focused and selective, and the recruitment model via AF9 and AF10 readers is presented as proposed rather than established.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wang(2016) Curr Opin Genet Dev; The role of DOT1L in the maintenance of leukemia gene expression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.gde.2016.03.015`; the prose sections were written here from the paper itself.

## Citation

Wang et al. Current Opinion in Genetics &amp; Development 2016. The role of DOT1L in the maintenance of leukemia gene expression. doi: 10.1016/j.gde.2016.03.015

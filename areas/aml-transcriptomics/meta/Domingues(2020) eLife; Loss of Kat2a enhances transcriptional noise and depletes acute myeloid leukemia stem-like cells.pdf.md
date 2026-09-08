---
# --- identity ------------------------------------------------
id: 2020-01-01_domingues-2020-elife-loss-of-kat2a-enhan
id_basis: filename-year
source: Domingues(2020) eLife; Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells.pdf
sha256: 2facd8854eff5ebc423ae1b60ce82696275c4f3ff232053578caa85168e62a0c
size_bytes: 3857561
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 183885

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.7554/eLife.51754"
year: 2020
title: "Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Domingues(2020) Elife; Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Combining chromatin profiling with single-cell transcriptomics in a conditional knockout mouse, the authors show that the histone acetyltransferase Kat2a supports leukemia propagation by preserving leukemia stem-like cells in MLL-AF9 AML. Kat2a loss alters transcription factor binding and reduces transcriptional burst frequency at a subset of promoters, increasing variability in transcript levels; the resulting destabilisation of target programs shifts leukemia cells out of self-renewal into differentiation. The authors propose that control of transcriptional variability is central to leukemia stem-like cell propagation.

## Summary

An unusual and conceptually interesting claim: that what a leukemia stem cell needs is not a particular expression level but low variance around it. Kat2a loss does not simply turn target genes down - it reduces burst frequency so that the same average expression is achieved less reliably, and the resulting noise dissolves the coordinated programs that hold the self-renewal state together.

The therapeutic window arrives almost as a bonus: normal hematopoietic stem and progenitors are unaffected, which the authors find surprising and corroborate against an independent Vav-Cre knockout, reasoning that normal developmental systems are robust to noise in a way the leukemic state is not. They are also careful to record that the differentiation Kat2a loss produces is aberrant, following multiple dead ends rather than the normal path.

## Key points

- Kat2a is required to sustain leukemia stem-like cells in MLL-AF9 AML, but is dispensable for normal HSPCs.
- The mechanism is transcriptional variability: reduced burst frequency at a subset of promoters raises cell-to-cell variance in transcript levels.
- Increased noise destabilises coordinated gene expression programs, pushing cells out of self-renewal into differentiation.
- Differentiation following Kat2a loss is aberrant, following multiple alternative dead ends rather than the normal trajectory.
- Proposes noise control, rather than expression level, as the property that maintains a leukemic stem state - a paradigm the authors suggest generalises.

## Limitations

Single mouse model, MLL-AF9-initiated AML, with no primary human validation beyond a Kat2a inhibitor (MB-3) in MOLM-13; MB-3 is a weak and non-selective tool compound. Transcriptional burst frequency is inferred from single-cell RNA-seq distributions by model fitting, not measured directly, and scRNA-seq technical noise is difficult to separate from biological variability - which is the paper's central quantity. The causal chain from noise to loss of self-renewal is argued from association between the two rather than demonstrated by manipulating variability independently of Kat2a. Absence of an effect on normal HSPCs is a negative result in a specific assay set. The proposed generalisation to other tumours and stages of cancer evolution is a suggestion, not a result.

## Provenance

Located in the published literature, dropped into `inbox/` as `Domingues(2020) Elife; Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.7554/eLife.51754`; the prose sections were written here from the paper itself.

## Citation

FilipaDomingues et al. eLife 2020. Loss of Kat2a enhances transcriptional noise and depletes acute myeloid leukemia stem-like cells. doi: 10.7554/eLife.51754

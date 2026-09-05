---
# --- identity ------------------------------------------------
id: 2024-01-01_xia-2024-genome-medicine-pvacview-an-int
id_basis: filename-year
source: Xia(2024) Genome Medicine; pVACview an interactive visualization tool for efficient neoantigen prioritization and selection.pdf
sha256: 4e81d231db38f08920912724e4b0e2045efbd47c8431430f84ffa3f656ba057a
size_bytes: 1650960
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 67055

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13073-024-01384-7"
year: 2024
title: "pVACview: an interactive visualization tool for efficient neoantigen prioritization and selection"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Xia_Genome_Med_pVACview_an_interactive_visualization_tool_for_PMID39538339.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

pVACview is an interactive visualisation interface for neoantigen prioritisation, presenting variant, transcript, peptide and algorithm-level data together. It is designed to replace tabular pipeline reports that are hard to navigate and are commonly over-simplified - for example by restricting consideration to a single RNA isoform.

## Summary

The problem it addresses is real and rarely written about: neoantigen pipelines emit predictions across alternative transcripts, multiple peptide lengths, multiple registers and an ensemble of algorithms, and the usual coping strategy is to collapse all of that into one row per variant, discarding the information a human would need to judge the call.

With at least 100 clinical trials of neoantigen-targeting therapies initiated globally, the selection step is a clinical decision, and this makes it inspectable rather than automatic.

## Key points

- Keeps transcript, peptide, register, length and algorithm-ensemble detail visible instead of collapsing it into a single row.
- Shows candidates in the context of transcript expression, tumour clonality and HLA-specific anchor information.
- Directly targets a documented failure mode: over-simplifying pipeline output to make it tractable.
- Aimed at a setting where the selection is a clinical decision, not a benchmark score.

## Limitations

A visualisation layer: it improves what a human can see about predictions but does not improve the predictions, and confident presentation of uncertain calls carries its own risk. It presupposes the pVACtools ecosystem. No evaluation is offered of whether analysts using it select better neoantigens - the claim is tractability, not accuracy.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Xia_Genome_Med_pVACview_an_interactive_visualization_tool_for_PMID39538339.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13073-024-01384-7`; the prose sections were written here from the paper itself.

## Citation

Xia et al. Genome Medicine 2024. pVACview: an interactive visualization tool for efficient neoantigen prioritization and selection. doi: 10.1186/s13073-024-01384-7

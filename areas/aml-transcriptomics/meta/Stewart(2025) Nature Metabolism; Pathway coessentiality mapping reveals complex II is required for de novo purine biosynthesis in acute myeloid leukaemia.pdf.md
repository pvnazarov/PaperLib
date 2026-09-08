---
# --- identity ------------------------------------------------
id: 2025-01-01_stewart-2025-nature-metabolism-pathway-c
id_basis: filename-year
source: Stewart(2025) Nature Metabolism; Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia.pdf
sha256: a68e9a18548e0bc440e6156f9bb587c3b7581df31306de3fc85a59c3a2c98f2c
size_bytes: 20191250
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 301968

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s42255-025-01410-x"
year: 2025
title: "Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Stewart(2025) Nat Metab; Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A multi-gene pathway coessentiality mapping approach, developed to move beyond gene-gene interaction analysis, reveals that AML depends on a link between electron transport chain complex II and purine metabolism. Stable-isotope metabolomic tracing shows complex II directly supports de novo purine biosynthesis, and exogenous purines rescue AML cells from complex II inhibition. The circuit is that glutamine provides nitrogen for the purine ring, producing glutamate that complex II metabolises to sustain purine synthesis; raising intracellular glutamate suppresses purine production and sensitises cells to complex II inhibition. Targeting complex II caused rapid disease regression and extended survival in a syngeneic AML model, and higher complex II gene expression correlates with BCL-2 inhibitor resistance and worse survival in patients.

## Summary

The methodological move is scaling coessentiality analysis from genes to pathways, which sidesteps the roughly 200 million pairwise comparisons a genome-wide gene-gene analysis would require and surfaces relationships that single-gene queries miss.

What it finds is a non-canonical role for a respiratory complex, consistent with a line of work showing that complex I matters for proliferation through aspartate synthesis rather than ATP. Here complex II sustains purine synthesis by metabolising the glutamate left over when glutamine donates nitrogen to the purine ring - a circuit rather than a linear pathway. The purine rescue experiment is the control that makes the mechanism rather than the correlation, and the clinical correlation with venetoclax resistance connects it to the collection's recurring resistance problem.

## Key points

- Pathway-level coessentiality mapping makes genome-scale interaction analysis tractable where gene-gene comparison does not.
- Complex II directly supports de novo purine biosynthesis, established by isotope tracing and by purine rescue of complex II inhibition.
- The circuit: glutamine donates nitrogen to the purine ring, and complex II metabolises the resulting glutamate to sustain synthesis.
- Raising intracellular glutamate suppresses purine production and sensitises AML cells to complex II inhibition.
- Higher complex II expression correlates with BCL-2 inhibitor resistance and worse survival in patients; targeting it caused regression in a syngeneic model.

## Limitations

The authors identify neurotoxicity as the primary concern with complex II inhibition and cite direct evidence for it - 3-NP and malonate cause striatal defects analogous to Huntington's disease with long-term use - proposing a brain-impermeant inhibitor as a hypothetical solution rather than testing one. Complex II is part of both the TCA cycle and the respiratory chain and is required in normal tissue, so selectivity is unresolved. The clinical evidence is expression correlation with outcome and venetoclax resistance, not a tested intervention. They also note that OGDH ablation produces similar effects on purine synthesis by a different proposed mechanism, so complex II may be one node in a broader dependency rather than the specific one. In vivo evidence is a syngeneic mouse model.

## Provenance

Located in the published literature, dropped into `inbox/` as `Stewart(2025) Nat Metab; Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s42255-025-01410-x`; the prose sections were written here from the paper itself.

## Citation

Stewart et al. Nature Metabolism 2025. Pathway coessentiality mapping reveals complex II is required for de novo purine biosynthesis in acute myeloid leukaemia. doi: 10.1038/s42255-025-01410-x

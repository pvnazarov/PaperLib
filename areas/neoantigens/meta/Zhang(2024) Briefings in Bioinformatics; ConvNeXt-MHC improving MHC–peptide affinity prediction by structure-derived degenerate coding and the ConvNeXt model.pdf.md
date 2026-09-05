---
# --- identity ------------------------------------------------
id: 2024-01-01_zhang-2024-briefings-in-bioinformatics-c
id_basis: filename-year
source: Zhang(2024) Briefings in Bioinformatics; ConvNeXt-MHC improving MHC–peptide affinity prediction by structure-derived degenerate coding and the ConvNeXt model.pdf
sha256: fd6c104a432b389893462ed0029f078a04afafb7834611426b0693df6041a05f
size_bytes: 1441601
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 55631

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbae133"
year: 2024
title: "ConvNeXt-MHC: improving MHC–peptide affinity prediction by structure-derived degenerate coding and the ConvNeXt model"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Zhang_Brief_Bioinform_ConvNeXt_MHC_improving_MHC_peptide_affinity_pr_PMID38561979.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ConvNeXt-MHC predicts MHC-I peptide binding affinity using a structure-derived degenerate encoding of amino acids combined with transfer and semi-supervised learning in the ConvNeXt architecture. Benchmarks report accuracy above state-of-the-art methods.

## Summary

The substantive idea is the degenerate coding: amino acids are grouped by structurally derived equivalence rather than treated as 20 unrelated symbols or embedded freely, which injects prior knowledge and reduces what has to be learnt from scarce data.

The rest is a careful application of a modern convolutional architecture with transfer learning from larger related datasets and semi-supervised use of unlabelled peptides.

## Key points

- Structure-derived degenerate encoding groups amino acids by physical equivalence instead of learning all 20 independently.
- Combines transfer learning and semi-supervised learning to exploit unlabelled data.
- Built on ConvNeXt, adapting a general-purpose vision architecture to the sequence-pair problem.
- A public web server is provided alongside the model.

## Limitations

This is binding affinity prediction, the furthest upstream and least informative of the three tasks - the Zhang 2026 paper in this collection shows models across all three inherit shortcut biases from the same training corpora. Benchmark gains are reported against methods trained on overlapping data with known circularity in peptide selection. No prospective or experimental validation is presented.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Zhang_Brief_Bioinform_ConvNeXt_MHC_improving_MHC_peptide_affinity_pr_PMID38561979.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbae133`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Briefings in Bioinformatics 2024. ConvNeXt-MHC: improving MHC–peptide affinity prediction by structure-derived degenerate coding and the ConvNeXt model. doi: 10.1093/bib/bbae133

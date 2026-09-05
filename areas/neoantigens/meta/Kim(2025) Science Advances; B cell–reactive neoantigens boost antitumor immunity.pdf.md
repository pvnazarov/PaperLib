---
# --- identity ------------------------------------------------
id: 2025-01-01_kim-2025-science-advances-b-cell-reactiv
id_basis: filename-year
source: Kim(2025) Science Advances; B cell–reactive neoantigens boost antitumor immunity.pdf
sha256: dc0f42dffd6f17029ab648854396e3fed2afc1b7d2914527b4e0ba2042c46c4d
size_bytes: 3189048
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 257642

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/sciadv.adx8303"
year: 2025
title: "B cell–reactive neoantigens boost antitumor immunity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as sciadv.adx8303.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

DeepNeo-BCR, a CNN-based model, predicts B cell reactivity to neoantigens, extending neoantigen selection beyond the T cell focus that dominates the field. Validated across large-scale cancer genome data, animal experiments and cancer vaccine clinical trial data.

## Summary

The motivating observation is that antitumor immunity work has been almost entirely T cell centred, while B cells contribute through tertiary lymphoid structures - lymph-node-like aggregates where B cells help reinvigorate T cells by antigen recognition and costimulation.

Selecting neoantigens for B cell reactivity as well as T cell reactivity is therefore a different objective, not a refinement of the same one, and the authors argue it is what would let a vaccine produce durable memory rather than a single wave of killing.

## Key points

- First model reported to quantitatively predict B cell reactivity to neoantigens, alongside T cell reactivity.
- Motivated by tertiary lymphoid structures, where B cells sustain local T cell responses.
- Validated on three independent kinds of evidence: cancer genomes, mouse experiments, and vaccine trial data.
- Complements Jardine (2016) in this collection, the other paper here concerned with B cell rather than T cell recognition.

## Limitations

The authors state theirs directly: DeepNeo-BCR's ROC-AUC on the test set was below 0.9; in the clinical trial analysis they could only select B cell epitopes from sequences already preselected for MHC binding, rather than identifying B-cell-engaging neoepitopes ab initio from the full mutation pool; and unlike the mouse data, the human wild-type sequence comparison was constrained. So the model is demonstrated within a T-cell-shaped candidate set, which is the very framing it argues against.

## Provenance

Located in the published literature, dropped into `inbox/` as `sciadv.adx8303.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/sciadv.adx8303`; the prose sections were written here from the paper itself.

## Citation

YeonKim et al. Science Advances 2025. B cell–reactive neoantigens boost antitumor immunity. doi: 10.1126/sciadv.adx8303

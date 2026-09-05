---
# --- identity ------------------------------------------------
id: 2026-01-01_zhang-2026-scientific-reports-multi-stra
id_basis: filename-year
source: Zhang(2026) Scientific Reports; Multi-strategy embedded framework for neoantigen vaccine maturation.pdf
sha256: 4ae15009e006333f00a406f847f84009262430731c2c0bceaf34e309355666f1
size_bytes: 6726383
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 88344

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41598-025-34618-8"
year: 2026
title: "Multi-strategy embedded framework for neoantigen vaccine maturation"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41598-025-34618-8-1.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NEOM evolves a single input peptide into diverse higher-affinity candidates by combining adaptive Markov chain Monte Carlo sampling with explicit pHLA structural modelling, in five modules: policy, structure, evaluation, selection and filter. Free energy perturbation narrowed 38 candidates to six, and MHC tetramer exchange assays with flow cytometry validated five.

## Summary

This is affinity maturation for neoantigens: rather than choosing among the peptides a tumour produced, it modifies one into variants that bind HLA better, which is the generative approach the Hu review in this batch describes.

What distinguishes it from sequence-only generative methods is that the three-dimensional dynamics of pHLA binding are modelled explicitly at each step, and the funnel ends in physical experiment rather than in a predicted score.

## Key points

- Generative rather than discriminative: designs improved peptides instead of ranking existing ones.
- Explicit pHLA structural modelling inside the sampling loop, not as a post hoc filter.
- A real validation funnel: in silico filtering, then free energy perturbation to 6 of 38, then tetramer exchange assays confirming 5.
- Modular design makes each stage - policy, structure, evaluation, selection, filter - separately inspectable.

## Limitations

The objective optimised is HLA class I binding, and this collection's central lesson is that binding is necessary but far from sufficient - a matured peptide binding better may be no more immunogenic, and a peptide altered away from the tumour's actual mutation may not match what the tumour presents at all. Validation is tetramer binding, which measures pMHC formation rather than T cell response. Free energy perturbation is computationally expensive, limiting how many candidates can pass that stage.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41598-025-34618-8-1.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41598-025-34618-8`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Scientific Reports 2026. Multi-strategy embedded framework for neoantigen vaccine maturation. doi: 10.1038/s41598-025-34618-8

---
# --- identity ------------------------------------------------
id: 2018-01-01_assi-2018-nature-genetics-subtype-specif
id_basis: filename-year
source: Assi(2018) Nature Genetics; Subtype-specific regulatory network rewiring in acute myeloid leukemia.pdf
sha256: 3cdacabbbc1f13f276556d3baf9bdea9f82145274a5533c4c26488253091e145
size_bytes: 3983111
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 132197

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41588-018-0270-1"
year: 2018
title: "Subtype-specific regulatory network rewiring in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Assi(2019) Nat Genet; Subtype-specific regulatory network rewiring in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A global analysis of cis-regulatory element activity and interaction, transcription factor occupancy and gene expression in purified leukemic blasts from AML patients grouped by mutation - RUNX1, CEBPA, FLT3-ITD, RAS and NPM1. Combining DNaseI footprinting, capture Hi-C promoter interaction mapping and expression profiling, the authors show that each mutant regulator establishes a specific transcriptional and signaling network unrelated to that of normal cells, and that AP-1 activity is a shared growth dependency across multiple subtypes.

## Summary

The paper that replaces 'AML subtypes differ in expression' with 'AML subtypes differ in the wiring that produces the expression'. Working on purified primary blasts rather than cell lines, it reads transcription factor occupancy directly off DNaseI footprints and assigns distal elements to their promoters by capture Hi-C, so subtype identity is described at the level of the regulatory circuit.

Two results carry weight beyond the atlas. AP-1 emerges as a common dependency in several subtypes, tying signaling mutations to a shared transcriptional output. And knocking out NFIX and FOXC1 - factors with subtype-specific activity, not classical drivers - reduces growth and colony formation in AML but not normal cells, which is the evidence that the aberrant network is load-bearing rather than incidental.

## Key points

- Each classifier mutation establishes its own transcription factor and signaling network, distinct from normal cells and from other subtypes.
- DNaseI footprinting on purified primary blasts gives factor occupancy without antibodies, across many factors at once.
- Capture Hi-C assigns most distal cis-elements to their correct promoters, which is what makes the networks interpretable.
- AP-1 activity is a shared growth dependency across multiple AML subtypes, linking signaling mutations to transcriptional output.
- NFIX and FOXC1 elimination reduces growth and colony-forming ability in AML but not normal cells.

## Limitations

Patient numbers per mutational subgroup are small, and primary AML samples vary in blast purity and cellular composition, so subtype-specific footprints could partly reflect differences in the cells present rather than in regulation. Footprinting infers occupancy from cleavage patterns and motif matches, which conflates factors sharing a motif - AP-1 is a family, and the assay cannot say which member. The networks are correlative reconstructions; only two factors are functionally tested, in cell lines and colony assays rather than in vivo. Comparison is against normal blasts, and the normal counterpart of a leukemic blast is itself a contested choice.

## Provenance

Located in the published literature, dropped into `inbox/` as `Assi(2019) Nat Genet; Subtype-specific regulatory network rewiring in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41588-018-0270-1`; the prose sections were written here from the paper itself.

## Citation

Assi et al. Nature Genetics 2018. Subtype-specific regulatory network rewiring in acute myeloid leukemia. doi: 10.1038/s41588-018-0270-1

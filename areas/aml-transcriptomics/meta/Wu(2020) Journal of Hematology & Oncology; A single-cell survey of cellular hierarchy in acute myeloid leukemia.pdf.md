---
# --- identity ------------------------------------------------
id: 2020-01-01_wu-2020-journal-of-hematology-oncology-a
id_basis: filename-year
source: Wu(2020) Journal of Hematology & Oncology; A single-cell survey of cellular hierarchy in acute myeloid leukemia.pdf
sha256: aaffd215869dc464fab283d99887bf78bcb7554b67e02fbf2e2a2ada55fbd875
size_bytes: 10990552
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 98040

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13045-020-00941-y"
year: 2020
title: "A single-cell survey of cellular hierarchy in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wu(2020) J Hematol Oncol; A single-cell survey of cellular hierarchy in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using Microwell-seq, 191,727 cells from bone marrow of 40 AML patients and 3 healthy donors were analysed, with single-molecule real-time sequencing used to investigate clonal heterogeneity. The authors established a single-cell AML landscape, identified an AML progenitor cell cluster with novel markers, and found that patients with ribosomal protein-high progenitor cells had a low remission rate, deducing two types of AML with diverse clinical outcomes. Combining Microwell-seq with SMRT sequencing to trace mitochondrial mutations showed a lack of association between AML clones and transcriptomic phenotypes, prompting the proposal of a phenotypic 'cancer attractor' defining a common AML progenitor phenotype.

## Summary

The genotype-phenotype dissociation is the interesting result. Tracing mitochondrial mutations to define clones and then asking whether clones correspond to transcriptomic states, the answer is that they do not - genetically distinct clones converge on similar phenotypes.

The authors' interpretation is a 'cancer attractor': a stable phenotypic state that different genetic routes converge on, borrowed from dynamical systems thinking about cell fate. That would explain why AML progenitor cells look similar across genetically heterogeneous disease, and it has a practical corollary - a therapy aimed at the attractor state might work across genotypes where mutation-directed therapy cannot. The ribosomal protein finding connects to the ribosome biogenesis dependencies reported independently elsewhere in this collection.

## Key points

- 191,727 cells from 40 AML patients profiled by Microwell-seq, with an AML progenitor cluster and novel markers identified.
- Ribosomal protein-high progenitor cells associate with low remission rate, distinguishing two AML types with different outcomes.
- Mitochondrial mutation tracing shows genetically distinct clones do not correspond to distinct transcriptomic phenotypes.
- Proposes a phenotypic 'cancer attractor' that different genetic routes converge on - implying genotype-agnostic targeting may be possible.
- Potential drug targets explored by comparing the AML landscape against the Human Cell Landscape.

## Limitations

The cancer attractor is a conceptual proposal supported by an absence of association, which is weaker evidence than a positive demonstration - and mitochondrial mutation tracing resolves clones only as coarsely as mtDNA diversity allows, so failure to link clone and phenotype may partly reflect limited clonal resolution. Three healthy donors is a thin normal reference for a 40-patient comparison. The prognostic association between ribosomal protein-high progenitors and remission is observational in a single cohort without multivariable adjustment. Drug targets are nominated by comparing expression landscapes, with no functional testing. Microwell-seq captures fewer genes per cell than droplet platforms, which limits resolution of subtle states.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wu(2020) J Hematol Oncol; A single-cell survey of cellular hierarchy in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13045-020-00941-y`; the prose sections were written here from the paper itself.

## Citation

Wu et al. Journal of Hematology &amp; Oncology 2020. A single-cell survey of cellular hierarchy in acute myeloid leukemia. doi: 10.1186/s13045-020-00941-y

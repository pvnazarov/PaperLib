---
# --- identity ------------------------------------------------
id: 2023-01-01_wu-2023-plos-biology-single-cell-transcr
id_basis: filename-year
source: Wu(2023) PLOS Biology; Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression.pdf
sha256: e158cf3e1bc89e76ccf70674cceff572c811af79228d329e9bce21688df563c1
size_bytes: 3409122
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 124613

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1371/journal.pbio.3002088"
year: 2023
title: "Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wu(2023) PLoS Biol; Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Serial single-cell transcriptome analyses of preleukemic and leukemic cells construct the cellular and molecular transformation trajectory in a Myc-driven AML mouse model. Myc targets were gradually upregulated along the trajectory, including splicing factors whose expression showed stage-specific prognostic value in patients. The authors dissect a tipping point at which hematopoietic stem and progenitor cells generate initiating preleukemic cells, characterised by dramatically increased splicing factors and unusual RNA velocity, and show that late-stage cells acquire explosive heterogeneity through alternative splicing. An Hsp90aa1-high subpopulation conserved between human and mouse AML associates with poor prognosis, and exon skipping in Tmem134 produces isoforms with opposite effects - the skipped product promotes the cell cycle while the full-length form delays tumorigenesis.

## Summary

Follows leukemogenesis as a process rather than comparing endpoints, and the striking observation is that splicing factor expression rises progressively along the trajectory while Myc, the driver, stays constant - so the transformation is not simply a matter of more oncogene.

Two structural features of tumorigenesis emerge. There is a tipping point where progenitors make an irreversible choice between normal differentiation and transformation, marked by a sharp increase in splicing factors and anomalous RNA velocity. And heterogeneity, usually treated as a background property of cancer, is acquired late rather than present throughout. The TMEM134 isoform pair is the functional validation: exon skipping removes one of two transmembrane domains, and the two products have opposite effects on malignancy.

## Key points

- Serial single-cell profiling constructs a continuous trajectory from preleukemic to leukemic cells in a Myc-driven model.
- Splicing factors rise progressively along the trajectory even though Myc expression stays constant.
- A tipping point marks the irreversible choice between normal differentiation and transformation, with sharply increased splicing factors and unusual RNA velocity.
- Heterogeneity is acquired late in tumorigenesis rather than being present throughout.
- TMEM134 exon skipping is conserved in human AML and associates with poor prognosis; the two isoforms have opposite effects on malignancy.

## Limitations

A single Myc-overexpression mouse model, and the authors ask directly whether the tipping point and explosive heterogeneity generalise to AML driven by other mutations or to other MYC-driven cancers - a question the study cannot answer. They also state that how splicing genes are progressively upregulated without any change in Myc level requires future investigation, so the central observation is unexplained. Human relevance rests on conservation of signatures and of the TMEM134 event rather than on patient trajectories, which cannot be sampled this way. Note a discrepancy in the record: the abstract refers to exon 4 skipping of Tmem134 while the discussion describes exon 6 skipping of TMEM134.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wu(2023) PLoS Biol; Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1371/journal.pbio.3002088`; the prose sections were written here from the paper itself.

## Citation

Wu et al. PLOS Biology 2023. Single-cell transcriptome analyses reveal critical roles of RNA splicing during leukemia progression. doi: 10.1371/journal.pbio.3002088

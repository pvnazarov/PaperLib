---
# --- identity ------------------------------------------------
id: 2025-01-01_baronas-2025-unknown-high-throughput-sin
id_basis: filename-year
source: Baronas(2025) unknown; High-throughput single cell -omics using semi-permeable capsules.pdf
sha256: fad95c52d5daef6216b9ae74adeac1e5c40bd09e5aa8c3d0ab84df262c6a6e83
size_bytes: 2531380
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 69475

# --- classification (LIH WI DC-909) --------------------------
type: preprint
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1101/2025.03.14.642805"
year: 2025
title: "High-throughput single cell -omics using semi-permeable capsules"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Baronas(2025) bioRxiv; High-throughput single cell -omics using semi-permeable capsules.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A technology based on semi-permeable capsules (SPCs) - uniform compartments with a liquid core inside a thin, tunable semi-permeable shell - for high-throughput nucleic acid assays including digital PCR, genome sequencing, single-cell RNA-seq and FACS-based isolation of transcriptomes by nucleic acid marker. SPCs retain nucleic acid fragments longer than 300 bp while admitting enzymes up to 160 kDa, are biocompatible enough to support single-cell cultivation and clonal expansion, and survive freezing, thawing, thermocycling and FACS. Applied as CapSeq to white blood cells from patients with hematopoietic disorders, they give superior transcript capture, and in AML samples reveal changes in mature granulocyte and monocyte transcriptomes associated with blast and progenitor phenotypes.

## Summary

A platform paper whose relevance to this collection is what it does to the cells droplet methods handle worst. Granulocytes are RNA-poor, RNase-rich and routinely lost or filtered out of scRNA-seq of blood, which quietly removes a large part of the innate immune compartment from AML single-cell studies; CapSeq claims to retain them.

The engineering argument is about multi-step chemistry. Droplet microfluidics is a one-pot reaction - reagents go in at droplet formation and cannot be changed - whereas once SPCs exist all subsequent steps are pipette work. Retention in a free liquid core rather than by hybridisation to a solid support is the stated reason capture efficiency is higher.

## Key points

- Semi-permeable capsules retain nucleic acids over 300 bp while admitting enzymes up to 160 kDa, enabling multi-step assays after encapsulation.
- Microfluidics is needed only to make the capsules; every later step uses standard pipettes and tubes.
- Capsules support long-term single-cell cultivation and clonal expansion, which droplet systems cannot.
- CapSeq reports superior transcript capture on difficult cell types, including granulocytes usually lost in blood scRNA-seq.
- In AML samples, mature granulocytes and monocytes show transcriptome changes associated with blast and progenitor phenotypes.

## Limitations

A bioRxiv preprint, not certified by peer review at the time of this record. The comparative claim of superior transcript capture is made by the developers of the method against other platforms, which is the configuration in which method comparisons are least reliable; benchmarking conditions favour the new method unless deliberately guarded against, and no independent replication is offered. The AML biology is a demonstration application on a small number of patient samples, so the granulocyte and monocyte findings are observations to follow up rather than established results. The permeability cut-off at 300 bp constrains which assays are possible, and long-term clonal expansion is shown as feasible rather than characterised for how faithfully expanded cells represent their founders.

## Provenance

Located in the published literature, dropped into `inbox/` as `Baronas(2025) bioRxiv; High-throughput single cell -omics using semi-permeable capsules.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1101/2025.03.14.642805`; the prose sections were written here from the paper itself.

## Citation

Baronas et al. unknown 2025. High-throughput single cell -omics using semi-permeable capsules. doi: 10.1101/2025.03.14.642805

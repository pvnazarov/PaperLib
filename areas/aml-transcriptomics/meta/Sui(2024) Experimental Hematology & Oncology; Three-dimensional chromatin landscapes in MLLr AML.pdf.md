---
# --- identity ------------------------------------------------
id: 2024-01-01_sui-2024-experimental-hematology-oncolog
id_basis: filename-year
source: Sui(2024) Experimental Hematology & Oncology; Three-dimensional chromatin landscapes in MLLr AML.pdf
sha256: 847f7d31ae7c33d50a6a302ee5c812335b7f1aee38f86114d420ab86e015229a
size_bytes: 5246921
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 18417

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s40164-024-00523-5"
year: 2024
title: "Three-dimensional chromatin landscapes in MLLr AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Sui(2024) Exp Hematol Oncol; Three-dimensional chromatin landscapes in MLLr AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An integrative analysis of 3D genome structure, chromatin accessibility and gene expression in gene-edited MLL-AF9 AML cells against normal cord blood CD34+ controls, combining ATAC-seq and RNA-seq with Micro-C at around 800 million paired-end reads per library. The data reveal MLL-rearrangement-specific alterations of chromatin accessibility, A/B compartments, topologically associating domains and chromatin loops, with 5731 healthy donor-specific and 2679 AML-specific loops. Local 3D configuration is rewired at loci associated with AML-specific expression, including inter-chromosomal enhancer- and silencer-hijacking events.

## Summary

Uses CRISPR-generated MLL-AF9 in human hematopoietic stem and progenitor cells, which addresses a real gap - the field has lacked an accurate human model - and compares against the cord blood CD34+ cells considered the healthy cell of origin, so the contrast isolates the rearrangement rather than confounding it with donor or lineage differences.

The negative result is the more interesting one. HOXA9 and MEIS1, the canonical MLL-AF9 signature genes, showed no significant loop alterations, which the authors read as evidence that 3D genome dynamics in this disease may be more complex than assumed and potentially independent of the HOXA9/MEIS1 axis. Given how much of the MLL-rearranged literature runs through that axis, a structural reorganisation that bypasses it is worth noting.

## Key points

- Uses CRISPR-generated MLL-AF9 in human HSPCs with cord blood CD34+ controls, addressing the lack of an accurate human model.
- Micro-C at high depth reveals AML-specific changes in accessibility, A/B compartments, TAD number and strength, and loops.
- 2679 AML-specific and 5731 donor-specific loops identified; AML-specific loops contain known MLL targets such as UBE2J1, PARP8 and PHC2.
- No significant loop alterations at HOXA9 or MEIS1, suggesting structural reorganisation partly independent of that axis.
- Inter-chromosomal enhancer-hijacking (ATP5L) and silencer-hijacking (UBE4A) events were identified.

## Limitations

The authors state their limitations directly: sample size is small and the loops were not validated - they propose that incorporating CTCF, H3K27ac and H3K27me3 ChIP-seq would be needed to separate loop-associated enhancers from silencers and to confirm the AML-specific loops identified. Published as a letter to the editor, so the analysis is compressed and the supporting data limited. The enhancer- and silencer-hijacking claims rest on individual loci with correlated expression change. Gene-edited cells are a model of the initiating lesion rather than of established patient disease, which carries additional cooperating mutations. No functional experiment tests whether any identified loop matters for the leukemic phenotype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Sui(2024) Exp Hematol Oncol; Three-dimensional chromatin landscapes in MLLr AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s40164-024-00523-5`; the prose sections were written here from the paper itself.

## Citation

Sui et al. Experimental Hematology &amp; Oncology 2024. Three-dimensional chromatin landscapes in MLLr AML. doi: 10.1186/s40164-024-00523-5

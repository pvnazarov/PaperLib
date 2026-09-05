---
# --- identity ------------------------------------------------
id: 2022-01-01_ragone-2022-journal-of-translational-med
id_basis: filename-year
source: Ragone(2022) Journal of Translational Medicine; Molecular mimicry between tumor associated antigens and microbiota-derived epitopes.pdf
sha256: 17e3aa3edc06b8a287495dcba37fc7d630938c4733142a78a16c2d7b3ac461c2
size_bytes: 2701421
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 93944

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12967-022-03512-6"
year: 2022
title: "Molecular mimicry between tumor associated antigens and microbiota-derived epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2022_Ragone_J_Transl_Med_Molecular_mimicry_between_tumor_associated_ant_PMID35836198.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A BLAST-plus-bioinformatics search for homology between published tumour-associated antigens and microbiota-derived epitopes finds numerous homologous pairs, including three at 100% sequence identity. Predicted HLA affinity of the microbiota-derived antigens is high (< 100 nM), and structural conformation - including TCR-facing residue geometry - is in some cases indistinguishable from the paired TAA.

## Summary

The proposal is that the microbiome influences anti-tumour immunity partly through molecular mimicry: exposure to bacterial epitopes resembling tumour antigens could prime or tolerise T cells that later meet the tumour.

The structural analysis goes beyond sequence identity to planar and dihedral angles of TCR-facing residues, arguing that some pairs are not merely similar but conformationally identical at the surface a T cell reads.

## Key points

- Three TAA/microbiota pairs at 100% sequence identity, with many more partial homologies.
- Predicted HLA affinities of microbiota-derived epitopes are high (< 100 nM).
- Structural comparison extends to TCR-facing residue angles, not just sequence.
- Offers a mechanistic hypothesis for the observed microbiome-immunotherapy association.

## Limitations

Entirely computational: homology, affinity and conformation are all predicted, with no T cell tested against either member of any pair. Sequence homology to a microbial protein does not establish that the epitope is generated, presented or encountered in vivo, and the microbiota search space is large enough that some 100% matches to short peptides are expected by chance. The paper proposes a mechanism; it does not demonstrate one.

## Provenance

Located in the published literature, dropped into `inbox/` as `2022_Ragone_J_Transl_Med_Molecular_mimicry_between_tumor_associated_ant_PMID35836198.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12967-022-03512-6`; the prose sections were written here from the paper itself.

## Citation

Ragone et al. Journal of Translational Medicine 2022. Molecular mimicry between tumor associated antigens and microbiota-derived epitopes. doi: 10.1186/s12967-022-03512-6

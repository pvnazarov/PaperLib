---
# --- identity ------------------------------------------------
id: 2023-01-01_li-2023-nature-communications-crystal-st
id_basis: filename-year
source: Li(2023) Nature Communications; Crystal structures of MHC class I complexes reveal the elusive intermediate conformations explored during peptide editing.pdf
sha256: dccc33ff1c79c90cd65dba4444b1da3a5caea17fbe3d0be52d76d27ab7fc9579
size_bytes: 3267653
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 88545

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-023-40736-6"
year: 2023
title: "Crystal structures of MHC class I complexes reveal the elusive intermediate conformations explored during peptide editing"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Li_Nat_Commun_Crystal_structures_of_MHC_class_I_complexes_re_PMID37596268.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

X-ray crystal structures of HLA-B8 loaded with 20mer peptides show pronounced distortion at the N-terminus of the binding groove, with long stretches of N-terminal residues missing from electron density, creating an open-ended groove. Molecular dynamics simulations show conformational flexibility consistent with the structures, capturing intermediates of peptide editing that had previously been inferred but not observed.

## Summary

MHC class I molecules are known to fluctuate between conformational states during peptide sampling, but the intermediates themselves had escaped experimental characterisation. Using oversized 20mer peptides forces the groove into non-canonical states that can be crystallised.

The result matters for prediction because essentially every binding predictor treats the groove as a fixed pocket geometry with defined anchor positions. These structures show the groove exploring conformations in which that model does not hold.

## Key points

- First experimental structures of MHC-I intermediate conformations during peptide editing.
- 20mer peptides open the N-terminus of the groove, revealing highly unusual MHC-peptide interactions there.
- Molecular dynamics independently supports the flexibility the structures imply.
- Challenges the fixed-groove, fixed-anchor assumption underlying sequence-based binding predictors.

## Limitations

One allotype (HLA-B8) with atypically long peptides: 20mers are a deliberate experimental device, not a physiological ligand length, so how far these conformations occur during normal editing is inference. Missing electron density is absence of observation and is interpreted here as disorder, which is reasonable but not directly measured. Molecular dynamics is corroborating simulation, not independent experiment.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Li_Nat_Commun_Crystal_structures_of_MHC_class_I_complexes_re_PMID37596268.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-023-40736-6`; the prose sections were written here from the paper itself.

## Citation

Li et al. Nature Communications 2023. Crystal structures of MHC class I complexes reveal the elusive intermediate conformations explored during peptide editing. doi: 10.1038/s41467-023-40736-6

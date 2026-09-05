---
# --- identity ------------------------------------------------
id: 1995-01-01_almagro-1995-protein-science-molecular-m
id_basis: filename-year
source: Almagro(1995) Protein Science; Molecular modeling of a T-cell receptor bound to a major histocompatibility complex molecule Implications for T-cell recognition.pdf
sha256: 68f29b773f2333e3f7e74b5c31033032a504151025263ca410a93149d1b829a7
size_bytes: 5990278
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 66913

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1002/pro.5560040906"
year: 1995
title: "Molecular modeling of a T-cell receptor bound to a major histocompatibility complex molecule: Implications for T-cell recognition"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1995_Almagro_Protein_Sci_Molecular_modeling_of_a_T_cell_receptor_bound_PMID8528069.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Before any TCR:peptide:MHC crystal structure existed, this paper built a computational 3D model of the 5C.C7 TCR bound to moth cytochrome c peptide 93-103 presented by I-Ek. The modelled complex shows high surface complementarity, and the residues it places at the interface agree with the mutational data available at the time.

## Summary

The approach is homology modelling: TCR V-alpha/V-beta domains were treated as structurally close to immunoglobulin Fv fragments, the six hypervariable loops assigned by analogy to Ig CDRs, and the assembled receptor docked onto a known peptide-MHC class II structure.

The model is then used to reason about what each loop contributes to recognition, and cross-checked against an independent sequence variability analysis by the same group.

## Key points

- Produces an explicit interface model at a time when no TCR:pMHC structure had been solved.
- Interface residue assignments agree with the mutational experiments of Jorgensen et al. (1992).
- Frames TCR recognition through the Ig-analogous loop architecture, assigning roles to individual alpha and beta loops.
- Predates and anticipates the docking-geometry constraints later confirmed crystallographically.

## Limitations

Every structural claim is modelled, not observed: there was no experimental TCR:pMHC structure to validate against, and agreement with mutational data is indirect evidence about an interface rather than a measurement of it. It is a class II complex and a single system, so nothing here generalises quantitatively. Its value in this collection is historical - it marks where structure-based TCR recognition started.

## Provenance

Located in the published literature, dropped into `inbox/` as `1995_Almagro_Protein_Sci_Molecular_modeling_of_a_T_cell_receptor_bound_PMID8528069.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1002/pro.5560040906`; the prose sections were written here from the paper itself.

## Citation

Almagro et al. Protein Science 1995. Molecular modeling of a T-cell receptor bound to a major histocompatibility complex molecule: Implications for T-cell recognition. doi: 10.1002/pro.5560040906

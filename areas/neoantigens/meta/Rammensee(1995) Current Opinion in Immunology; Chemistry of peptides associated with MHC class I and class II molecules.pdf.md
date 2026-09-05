---
# --- identity ------------------------------------------------
id: 1995-01-01_rammensee-1995-current-opinion-in-immuno
id_basis: filename-year
source: Rammensee(1995) Current Opinion in Immunology; Chemistry of peptides associated with MHC class I and class II molecules.pdf
sha256: 8fcf7e18293cdcf7505f12ff20da69242a0498c2dad2dc6a3abf1d329dc871bd
size_bytes: 1138664
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 94280

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/0952-7915(95)80033-6"
year: 1995
title: "Chemistry of peptides associated with MHC class I and class II molecules"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-0952791595800336-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review setting out that peptides presented by MHC class I and class II follow stringent, allele-specific rules involving a nine-amino-acid stretch spanning the groove, with anchor side chains held in complementary pockets. The sum of these requirements is described as a motif - the number, spacing and specificity of anchors plus degenerate preferences at non-anchor positions.

## Summary

This is where the motif abstraction that organises the whole field comes from, and it is worth reading for how carefully it is stated. Anchors and non-anchor preferences are distinguished, and the non-anchor positions are explicitly described as degenerate rather than irrelevant.

The class I / class II difference is set out clearly too: for class I the entire ligand participates in allele-specific interaction, while for class II peptides are longer and the nine-residue stretch sits roughly centrally, which is why class II binding-core identification is a separate problem.

## Key points

- Defines the anchor-motif abstraction on which every subsequent binding predictor is built.
- Anchors are complementary side-chain-in-pocket interactions; non-anchor positions have degenerate preferences, not none.
- Class I ligands interact along their whole length; class II peptides extend beyond a roughly central nine-residue core.
- States the motif's purpose as T-cell epitope prediction, thirty years before the models in this collection.

## Limitations

A 1995 review: every quantitative claim belongs to a cited study of that era and must be traced there. The motif abstraction it establishes is now known to be incomplete - the reverse-binding HLA-DP ligands and the conformational effects in this collection are both outside it. Motifs were derived from pool sequencing and a limited set of characterised alleles, far fewer than modern immunopeptidomics covers.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-0952791595800336-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/0952-7915(95)80033-6`; the prose sections were written here from the paper itself.

## Citation

Rammensee et al. Current Opinion in Immunology 1995. Chemistry of peptides associated with MHC class I and class II molecules. doi: 10.1016/0952-7915(95)80033-6

---
# --- identity ------------------------------------------------
id: 2007-01-01_kawashima-2007-nucleic-acids-research-aa
id_basis: filename-year
source: Kawashima(2007) Nucleic Acids Research; AAindex amino acid index database, progress report 2008.pdf
sha256: 6e8353d2c163c753256e29073242d6743f1bffbb7663d9d4acf19c47eab82dba
size_bytes: 303176
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 20174

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gkm998"
year: 2007
title: "AAindex: amino acid index database, progress report 2008"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2008_Kawashima_Nucleic_Acids_Res_AAindex_amino_acid_index_database_progress_rep_PMID17998252.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

AAindex is a database of numerical indices for physicochemical and biochemical properties of amino acids and amino acid pairs, in three sections: AAindex1 (single amino acid indices), AAindex2 (substitution matrices) and AAindex3 (statistical protein contact potentials, added in this release). All values are derived from published literature.

## Summary

A reference resource rather than a method. Its relevance to this collection is that the physicochemical descriptors used by immunogenicity predictors - hydrophobicity scales, bulkiness, polarity - are very often taken from here, so it is the common ancestor of a large family of features.

The authors themselves name immunogenicity of MHC class I binding peptides as one of the applications the database is used for.

## Key points

- Three sections: amino acid indices, substitution matrices, and (new in this release) statistical contact potentials.
- Every index is drawn from published literature rather than recomputed, so each carries its original experimental context.
- Explicitly cited as used for MHC class I peptide immunogenicity prediction.
- The source of the physicochemical feature space that appears in PredIG, ANN-Hydro and similar models in this collection.

## Limitations

It is a compilation, and the indices are heterogeneous in how they were measured, on what scale, and under what conditions; combining them in a feature vector treats incommensurable quantities alike. Many indices are strongly correlated, so a model using dozens of them has fewer independent features than it appears to. This is a 2008 progress report and the database has moved on.

## Provenance

Located in the published literature, dropped into `inbox/` as `2008_Kawashima_Nucleic_Acids_Res_AAindex_amino_acid_index_database_progress_rep_PMID17998252.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gkm998`; the prose sections were written here from the paper itself.

## Citation

Kawashima et al. Nucleic Acids Research 2007. AAindex: amino acid index database, progress report 2008. doi: 10.1093/nar/gkm998

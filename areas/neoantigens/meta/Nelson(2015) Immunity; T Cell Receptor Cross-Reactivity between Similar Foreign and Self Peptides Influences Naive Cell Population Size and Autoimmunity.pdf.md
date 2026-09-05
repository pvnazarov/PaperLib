---
# --- identity ------------------------------------------------
id: 2015-01-01_nelson-2015-immunity-t-cell-receptor-cro
id_basis: filename-year
source: Nelson(2015) Immunity; T Cell Receptor Cross-Reactivity between Similar Foreign and Self Peptides Influences Naive Cell Population Size and Autoimmunity.pdf
sha256: 0a2146d8906ad6effdb359381419ee7c6c92dcb43b97d90e6a830dfbbca1afcf
size_bytes: 3087384
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 125639

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.immuni.2014.12.022"
year: 2015
title: "T Cell Receptor Cross-Reactivity between Similar Foreign and Self Peptides Influences Naive Cell Population Size and Autoimmunity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS1074761314004890.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

MHC class II-bound nonamer peptides need share only five residues to bind the same TCR. A self peptide can therefore delete T cells specific for a similar foreign peptide, making some naive T cell populations small, and a foreign peptide can provoke autoimmunity against a similar self peptide that was previously ignored.

## Summary

This supplies the quantitative basis for the tolerance argument running through this collection: five shared residues out of nine is enough for cross-recognition, which makes the space of self peptides that could have deleted a given specificity far larger than sequence-identity intuitions suggest.

The consequence runs both ways, and the paper demonstrates both directions. Weak responses to some foreign antigens are explained by prior clonal deletion against similar self peptides, and immunisation with a foreign peptide can break ignorance of a self peptide.

## Key points

- Five shared residues in a class II nonamer suffice for the same TCR to bind both peptides.
- Naive precursor population size is set partly by deletion against similar self peptides - so repertoire availability varies by epitope.
- A response can be weak because the foreign peptide resembles a tolerated self peptide, not because the peptide is poorly presented.
- A foreign peptide can induce autoimmunity against a similar self peptide, the mechanism behind the mimicry toxicity papers here.

## Limitations

Mouse, MHC class II, and a defined set of peptide pairs: the five-residue threshold comes from these systems and should not be quoted as a general rule for human class I. Naive precursor frequencies are measured with tetramer-based enrichment, which has its own detection floor. The autoimmunity demonstrated is experimental immunisation, some distance from spontaneous disease.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS1074761314004890.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.immuni.2014.12.022`; the prose sections were written here from the paper itself.

## Citation

Nelson et al. Immunity 2015. T Cell Receptor Cross-Reactivity between Similar Foreign and Self Peptides Influences Naive Cell Population Size and Autoimmunity. doi: 10.1016/j.immuni.2014.12.022

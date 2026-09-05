---
# --- identity ------------------------------------------------
id: 2019-01-01_richman-2019-cell-systems-neoantigen-dis
id_basis: filename-year
source: Richman(2019) Cell Systems; Neoantigen Dissimilarity to the Self-Proteome Predicts Immunogenicity and Response to Immune Checkpoint Blockade.pdf
sha256: d1d201d97798a41b69ff849be7fcfce927814b04e003fc9f2323fc16cd6eb509
size_bytes: 3261787
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 72801

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cels.2019.08.009"
year: 2019
title: "Neoantigen Dissimilarity to the Self-Proteome Predicts Immunogenicity and Response to Immune Checkpoint Blockade"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS2405471219303072.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Dissimilarity of a neoantigen to the non-mutated proteome is identified as a predictor of peptide immunogenicity. Implemented in the antigen.garnish R package, dissimilarity identifies a distinct set of high-quality neoantigens that correlates with survival in clinical checkpoint blockade datasets.

## Summary

The metric is deliberately different from the mutant-versus-wild-type contrast used by differential agretopicity: this compares the neoantigen against the whole self proteome, not just the peptide it came from. A neoepitope can differ sharply from its own wild type and still resemble some other self protein a T cell is tolerant to.

High-dissimilarity neoantigens form a set that other quality metrics do not select, so it adds information rather than re-expressing existing scores.

## Key points

- Dissimilarity is measured against the entire non-mutated proteome, not only the wild-type counterpart.
- High-dissimilarity peptides form a unique set not captured by other quality metrics.
- Associated with immunogenicity and with survival under checkpoint blockade in clinical cohorts.
- Released as antigen.garnish, an open-source R package.

## Limitations

Read against Koncz (2021) elsewhere in this collection, which argues the opposite bound: a peptide too dissimilar from self may have no positively selected T cell to see it, so dissimilarity cannot be monotonically good. The clinical association is retrospective and observational across public datasets. What counts as 'self' is a reference proteome, ignoring individual germline variation, which is precisely what determines an individual's tolerance.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS2405471219303072.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cels.2019.08.009`; the prose sections were written here from the paper itself.

## Citation

Richman et al. Cell Systems 2019. Neoantigen Dissimilarity to the Self-Proteome Predicts Immunogenicity and Response to Immune Checkpoint Blockade. doi: 10.1016/j.cels.2019.08.009

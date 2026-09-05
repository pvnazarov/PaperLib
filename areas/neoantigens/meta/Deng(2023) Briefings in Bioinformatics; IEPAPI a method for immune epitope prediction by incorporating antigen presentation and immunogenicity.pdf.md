---
# --- identity ------------------------------------------------
id: 2023-01-01_deng-2023-briefings-in-bioinformatics-ie
id_basis: filename-year
source: Deng(2023) Briefings in Bioinformatics; IEPAPI a method for immune epitope prediction by incorporating antigen presentation and immunogenicity.pdf
sha256: 0ba48924ffd86badfa6f3824d5cc460e549cc64d9ec78601403c789dc6ce08bd
size_bytes: 1583535
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 61446

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbad171"
year: 2023
title: "IEPAPI: a method for immune epitope prediction by incorporating antigen presentation and immunogenicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as bbad171.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

IEPAPI uses transformer-based feature extraction for peptides and HLA-I proteins, then feeds the antigen presentation prediction into the input of the immunogenicity branch, explicitly modelling the sequence of biological steps in a T-cell response. It also reveals HLA-restricted motifs for presentation and immunogenicity separately.

## Summary

The architectural claim is about wiring rather than capacity: presentation and immunogenicity are chained, not predicted in parallel, so the immunogenicity branch conditions on how likely the peptide is to be presented at all.

The diagnosis motivating it is the standard one - binding and presentation predictors lack precision because they ignore TCR recognition, while direct immunogenicity modelling is weak because the recognition mechanism is still poorly understood.

## Key points

- Presentation prediction is an input to immunogenicity prediction, mirroring the biological ordering.
- Transformer representations for both peptide and HLA protein sequence.
- Recovers HLA-restricted motifs separately for presentation and for immunogenicity, which are not the same motifs.
- Aimed explicitly at neoantigen screening for T-cell vaccine design.

## Limitations

Trained and evaluated on the same public epitope resources whose intra-HLA imbalance Zhang (2026) shows drives shortcut learning across all models of this kind, and no bias control is reported. Chaining the two predictions also chains their errors: a presentation mistake propagates into the immunogenicity call. No prospective experimental validation is presented.

## Provenance

Located in the published literature, dropped into `inbox/` as `bbad171.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbad171`; the prose sections were written here from the paper itself.

## Citation

Deng et al. Briefings in Bioinformatics 2023. IEPAPI: a method for immune epitope prediction by incorporating antigen presentation and immunogenicity. doi: 10.1093/bib/bbad171

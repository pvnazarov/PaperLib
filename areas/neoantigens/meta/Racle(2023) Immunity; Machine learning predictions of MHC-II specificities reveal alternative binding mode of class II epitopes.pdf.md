---
# --- identity ------------------------------------------------
id: 2023-01-01_racle-2023-immunity-machine-learning-pre
id_basis: filename-year
source: Racle(2023) Immunity; Machine learning predictions of MHC-II specificities reveal alternative binding mode of class II epitopes.pdf
sha256: d93c8cae376f46381bb9b727105288695e0a2f420e31aeb6117ac6317dfdf80c
size_bytes: 8459816
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 180561

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.immuni.2023.03.009"
year: 2023
title: "Machine learning predictions of MHC-II specificities reveal alternative binding mode of class II epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS1074761323001292.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Curating over 600,000 MHC-II ligands and deconvolving motifs yields high-resolution binding motifs for 88 MHC-II alleles. Structural analysis reveals a widespread reverse binding mode for HLA-DP ligands, and MixMHC2pred improves CD4+ T cell epitope prediction.

## Summary

The reverse-binding finding is the substantive discovery. Class II prediction assumed a single N-to-C orientation in the groove; a substantial fraction of HLA-DP ligands bind in the opposite direction, which means motifs derived under the single-orientation assumption were partly wrong for that locus.

It is also a good example of scale producing biology rather than only accuracy: the reverse mode became visible because 600,000 ligands across 88 alleles were deconvolved together.

## Key points

- Over 600,000 MHC-II ligands curated; high-resolution motifs for 88 alleles.
- A widespread reverse binding mode for HLA-DP ligands, confirmed structurally - a mechanism, not a fitting artefact.
- Explains part of why HLA-DP prediction lagged behind HLA-DR.
- MixMHC2pred improves CD4+ epitope prediction on the back of the corrected motifs.

## Limitations

The authors state that the reverse binding mode was demonstrated for HLA-DP but not observed for other loci, and that they cannot exclude it occurring elsewhere below their detection limit - so its true prevalence is unknown. Leave-one-species-out cross-validation gave lower though not random accuracy, which they identify as a limitation of all pan-allele MHC-II predictors: they should be used with care in distant species such as fish or birds.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS1074761323001292.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.immuni.2023.03.009`; the prose sections were written here from the paper itself.

## Citation

Racle et al. Immunity 2023. Machine learning predictions of MHC-II specificities reveal alternative binding mode of class II epitopes. doi: 10.1016/j.immuni.2023.03.009

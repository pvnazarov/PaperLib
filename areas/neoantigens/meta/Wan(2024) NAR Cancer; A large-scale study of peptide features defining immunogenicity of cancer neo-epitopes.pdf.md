---
# --- identity ------------------------------------------------
id: 2024-01-01_wan-2024-nar-cancer-a-large-scale-study
id_basis: filename-year
source: Wan(2024) NAR Cancer; A large-scale study of peptide features defining immunogenicity of cancer neo-epitopes.pdf
sha256: 91a17ac1d615dd0ce0d89c868c3dd02c2dc0944981b941a57e67ab48e3ad6efe
size_bytes: 2082960
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 99373

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/narcan/zcae002"
year: 2024
title: "A large-scale study of peptide features defining immunogenicity of cancer neo-epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Wan_NAR_Cancer_A_large_scale_study_of_peptide_features_defini_PMID38288446.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A comprehensive analysis of peptide features for neo-epitope immunogenicity using CEDAR's experimentally validated annotations, yielding ICERFIRE. The model extracts the predicted ICORE - the nested peptide with the highest MHC binding potential together with its presentation %Rank - and adds the BLOSUM mutation score and wild-type antigen expression level, outperforming existing models in cross-validation and on external data.

## Summary

Two of the three key features are relational rather than intrinsic: the BLOSUM score measures how radical the mutation is relative to the wild type, and expression of the wild-type counterpart proxies the neo-epitope's abundance. This is the same mutant-versus-wild-type framing as the differential agretopicity literature, made concrete.

The ICORE step matters because a neo-epitope is a region, not a peptide: which nested peptide and register is actually presented has to be decided before any feature can be computed on it.

## Key points

- Uses CEDAR - cancer-specific, experimentally validated - rather than general pathogen epitope sets.
- ICORE extraction picks the best-binding nested peptide and register before featurisation.
- BLOSUM mutation score and wild-type expression both improve accuracy, relating the neo-epitope to its origin.
- Performance relies on positional weighting that masks out anchor positions, focusing the model on TCR-facing residues.

## Limitations

The authors note that large differences in optimal features and positional weighting between datasets highlight the challenges of generalisation and the limits of dataset-specific models - a caution about their own result as much as others'. Training rests on CEDAR's curated positives with the usual unreliable negatives. Anchor masking is tuned, so some of the reported gain is a fitted preprocessing choice rather than a learnt biological signal.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Wan_NAR_Cancer_A_large_scale_study_of_peptide_features_defini_PMID38288446.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/narcan/zcae002`; the prose sections were written here from the paper itself.

## Citation

RichieWan et al. NAR Cancer 2024. A large-scale study of peptide features defining immunogenicity of cancer neo-epitopes. doi: 10.1093/narcan/zcae002

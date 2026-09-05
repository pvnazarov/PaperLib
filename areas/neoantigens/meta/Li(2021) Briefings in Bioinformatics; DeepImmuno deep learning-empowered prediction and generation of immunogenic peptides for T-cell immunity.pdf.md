---
# --- identity ------------------------------------------------
id: 2021-01-01_li-2021-briefings-in-bioinformatics-deep
id_basis: filename-year
source: Li(2021) Briefings in Bioinformatics; DeepImmuno deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity.pdf
sha256: d8d615289849056f42402a1fcab709bb6dfc118dfa6153fc3a0ca030dd1b3de9
size_bytes: 1228106
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 62430

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbab160"
year: 2021
title: "DeepImmuno: deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2021_Li_Brief_Bioinform_DeepImmuno_deep_learning_empowered_prediction_PMID34009266.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

DeepImmuno derives peptide immunogenic potential from sequence using a beta-binomial model to produce a continuous score, benchmarked across five classical machine learning and three deep learning architectures on dengue, cancer neoantigen and SARS-CoV-2 validation sets. A CNN was selected; a companion GAN generates synthetic immunogenic peptides for given HLA alleles.

## Summary

The methodological argument is against hard binary labels. Immunogenicity is not a property of a peptide-MHC pair alone - it depends on the subject's immune profile and TCR repertoire - so a beta-binomial fit that weights each pair by the strength of the underlying experimental evidence is a better target than a thresholded yes/no.

The generative half is unusual in this field: DeepImmuno-GAN produces synthetic immunogenic peptides, intended both for synthetic biology applications and to augment scarce training data.

## Key points

- Continuous immunogenicity score from a beta-binomial fit, weighting each peptide-MHC pair by evidence strength rather than thresholding.
- Systematic comparison of eight model families across three independent validation collections.
- The CNN recovers which residues matter most for T-cell recognition, agreeing with the TCR-facing-position literature.
- DeepImmuno-GAN generates synthetic HLA-specific immunogenic peptides for data augmentation.

## Limitations

Training and evaluation still rest on curated immunogenicity databases whose negatives are largely assumed. GAN-generated peptides are plausible under the learnt distribution, which is not evidence that they are immunogenic; using them to augment training risks reinforcing whatever the model already believes. The three validation collections are dominated by pathogen epitopes, so cancer-neoantigen performance rests on the smallest of the three.

## Provenance

Located in the published literature, dropped into `inbox/` as `2021_Li_Brief_Bioinform_DeepImmuno_deep_learning_empowered_prediction_PMID34009266.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbab160`; the prose sections were written here from the paper itself.

## Citation

Li et al. Briefings in Bioinformatics 2021. DeepImmuno: deep learning-empowered prediction and generation of immunogenic peptides for T-cell immunity. doi: 10.1093/bib/bbab160

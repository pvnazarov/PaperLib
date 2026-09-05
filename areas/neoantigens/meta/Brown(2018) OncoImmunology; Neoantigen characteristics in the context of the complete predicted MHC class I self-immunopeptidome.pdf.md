---
# --- identity ------------------------------------------------
id: 2018-01-01_brown-2018-oncoimmunology-neoantigen-cha
id_basis: filename-year
source: Brown(2018) OncoImmunology; Neoantigen characteristics in the context of the complete predicted MHC class I self-immunopeptidome.pdf
sha256: f4cd6b42b990ef48f92d1470bb98633238424f7950f515e86b3b813aca5c3882
size_bytes: 1530875
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 86303

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1080/2162402X.2018.1556080"
year: 2018
title: "Neoantigen characteristics in the context of the complete predicted MHC class I self-immunopeptidome"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2019_Brown_Oncoimmunology_Neoantigen_characteristics_in_the_context_of_t_PMID30723589.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The authors computed 134 billion peptide-MHC binding predictions - every unique 8-11mer in the human proteome against every available HLA class I allele - to define each individual's predicted self-immunopeptidome. They find that self-immunopeptidome size varies with HLA genotype, combines with mutational load to predict survival, and shows evidence of immunoediting.

## Summary

The premise is that a person whose HLA variants present fewer self-peptides will also present fewer mutated peptides, so the size of the presentable self repertoire should act as a proxy for how much immune pressure a tumour is under.

The scale is the contribution: rather than sampling, they enumerate the whole predicted space, which lets them describe how presentation capacity is distributed across peptides and alleles rather than inferring it.

## Key points

- Most peptides are presentable by fewer than 250 MHC variants, while some are presentable by more than 1,500.
- Nearly 30% of self-peptides are presentable by at least one MHC, leaving about 70% of the human peptidome unsurveyed by T cells.
- No relationship was found between the number of peptides an allele presents and its population frequency.
- Predicted self-immunopeptidome size combined with mutational load predicts survival pan-cancer, suggesting HLA genotyping as a cheap candidate biomarker.

## Limitations

Every peptide in this study is predicted, never measured: 134 billion binding predictions inherit the error rate of the predictor across all of them, and binding is not presentation. The self-immunopeptidome is defined without reference to the transcriptional profile of any actual cell, so it is an upper bound on what could be presented rather than what is. The survival association is observational.

## Provenance

Located in the published literature, dropped into `inbox/` as `2019_Brown_Oncoimmunology_Neoantigen_characteristics_in_the_context_of_t_PMID30723589.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1080/2162402X.2018.1556080`; the prose sections were written here from the paper itself.

## Citation

Brown et al. OncoImmunology 2018. Neoantigen characteristics in the context of the complete predicted MHC class I self-immunopeptidome. doi: 10.1080/2162402X.2018.1556080

---
# --- identity ------------------------------------------------
id: 2024-01-01_xu-2024-nature-communications-immuneapp
id_basis: filename-year
source: Xu(2024) Nature Communications; ImmuneApp for HLA-I epitope prediction and immunopeptidome analysis.pdf
sha256: 37f50d5be161b2472a72940e7fdbc793f0e7e301c8e364754c4cfae87a21ce87
size_bytes: 7375826
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 238413

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-024-53296-0"
year: 2024
title: "ImmuneApp for HLA-I epitope prediction and immunopeptidome analysis"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Xu_Nat_Commun_ImmuneApp_for_HLA_I_epitope_prediction_and_imm_PMID39414796.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ImmuneApp is an interpretable deep learning framework for HLA-I epitope prediction, neoepitope prioritisation and immunopeptidomics deconvolution. Systematic analysis of 216 multi-allelic immunopeptidomics samples identified 835,551 ligands across more than 100 HLA-I alleles; the composite ImmuneApp-MA integrates mono- and multi-allelic data, and ImmuneApp-Neo is built on it as an immunogenicity predictor.

## Summary

The structure is a pre-trained presentation model reused as the backbone for an immunogenicity model, which is the transfer-learning answer to the fact that presentation data are plentiful and immunogenicity labels are scarce.

The deconvolution contribution matters independently: most immunopeptidomics is multi-allelic, so assigning each observed ligand to its presenting allele is what turns raw MS output into per-allele training data.

## Key points

- 835,551 ligands across >100 HLA-I alleles from 216 multi-allelic samples, via a model-based deconvolution approach.
- ImmuneApp-MA integrates mono- and multi-allelic data; ImmuneApp-Neo reuses it as a pre-trained backbone for immunogenicity.
- Identifies key residues for pHLA binding, giving some interpretability over the learnt embeddings.
- Both unsupervised (GibbsCluster-style) and supervised allele-specific deconvolution approaches are implemented.

## Limitations

The authors list their own: ImmuneApp is HLA-I only, while some competing methods cover class II as well. Sample input requirements were reduced from over 10^9 to 10^7 cells, but they state this still substantially limits clinical applicability - fine-needle biopsies typically yield too little material for pMHC profiling. Their immunogenicity assessment is limited in scope, and mass-spectrometry detection bias propagates from the ligand atlas into both models.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Xu_Nat_Commun_ImmuneApp_for_HLA_I_epitope_prediction_and_imm_PMID39414796.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-024-53296-0`; the prose sections were written here from the paper itself.

## Citation

Xu et al. Nature Communications 2024. ImmuneApp for HLA-I epitope prediction and immunopeptidome analysis. doi: 10.1038/s41467-024-53296-0

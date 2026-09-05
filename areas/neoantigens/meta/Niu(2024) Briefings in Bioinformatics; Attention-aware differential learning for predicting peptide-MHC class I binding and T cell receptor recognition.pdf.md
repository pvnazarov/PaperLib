---
# --- identity ------------------------------------------------
id: 2024-01-01_niu-2024-briefings-in-bioinformatics-att
id_basis: filename-year
source: Niu(2024) Briefings in Bioinformatics; Attention-aware differential learning for predicting peptide-MHC class I binding and T cell receptor recognition.pdf
sha256: b536289a7e80e01c88e8c06105750ae71ddc5ff39c22b39ec649db0bbbd8f0cb
size_bytes: 2339970
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 70307

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbaf038"
year: 2024
title: "Attention-aware differential learning for predicting peptide-MHC class I binding and T cell receptor recognition"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Niu_Brief_Bioinform_Attention_aware_differential_learning_for_pred_PMID39883517.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

An attention-based framework in two parts: TranspMHC for pMHC-I binding prediction and TransTCR for TCR-pMHC-I recognition, the latter using transfer learning and a differential learning strategy. Both are reported to outperform existing methods on independent datasets, and attention weights identify amino acids associated with peptide and TCR binding motifs.

## Summary

The architectural argument is that convolutional and LSTM predictors capture local sequence patterns and miss long-range dependencies within the peptide and receptor sequences, which attention handles natively.

The second problem named is the long-tail distribution of known binding pairs: a few epitopes have thousands of recorded TCRs and most have none. Differential learning and transfer between the binding and recognition tasks are the response to that imbalance.

## Key points

- Splits the problem into presentation (TranspMHC) and recognition (TransTCR), trained together via transfer.
- Attention addresses long-range dependencies that convolutional and LSTM architectures cannot represent.
- Explicitly targets the long-tail distribution of TCR-pMHC pairs in public databases.
- Attention weights recover binding-motif positions, offering some interpretability.

## Limitations

Performance is reported on independent datasets drawn from the same public databases whose long tail is the stated problem, so 'independent' does not mean 'unseen epitope' - the Culka and Jensen papers in this collection show that distinction dominates. Interpretability from attention weights is suggestive, not validated against structures. No prospective experimental validation is reported.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Niu_Brief_Bioinform_Attention_aware_differential_learning_for_pred_PMID39883517.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbaf038`; the prose sections were written here from the paper itself.

## Citation

Niu et al. Briefings in Bioinformatics 2024. Attention-aware differential learning for predicting peptide-MHC class I binding and T cell receptor recognition. doi: 10.1093/bib/bbaf038

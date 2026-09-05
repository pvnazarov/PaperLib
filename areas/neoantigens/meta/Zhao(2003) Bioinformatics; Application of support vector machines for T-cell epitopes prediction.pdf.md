---
# --- identity ------------------------------------------------
id: 2003-01-01_zhao-2003-bioinformatics-application-of
id_basis: filename-year
source: Zhao(2003) Bioinformatics; Application of support vector machines for T-cell epitopes prediction.pdf
sha256: a90597bec33d60df6c76befa214943aec7bc2a95409eaeb0802840d53bed6916
size_bytes: 217554
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 42912

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btg255"
year: 2003
title: "Application of support vector machines for T-cell epitopes prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as bioinformatics_19_15_1978.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The first application of support vector machines to T-cell epitope prediction, trained on an MHC class I restricted T-cell clone. Cross-validation shows SVMs can be trained on relatively small datasets to give predictions more accurate than previously published methods or than MHC binding alone.

## Summary

Two things make this worth keeping. First, it is an origin point - the SVM approach it introduces became standard for a decade and appears in several later tools in this collection.

Second, its framing was ahead of its data. It states that T cell recognition, long considered exquisitely specific, is highly flexible, with one receptor able to recognise thousands of peptides - the cross-reactivity that Nelson (2015) and the mimicry papers here later quantified and that made engineered TCR safety a problem.

## Key points

- First SVM applied to T cell epitope prediction, on a small training set.
- Outperforms both prior methods and MHC binding alone - the presentation-versus-recognition distinction, made in 2003.
- States TCR flexibility explicitly: one receptor may recognise thousands of different peptides.
- Data for 203 synthesised peptides released alongside the paper.

## Limitations

Trained on a single MHC class I restricted T-cell clone, so what is learnt is that clone's specificity rather than a general immunogenicity rule. The dataset is very small even by 2003 standards, and cross-validation on it gives an optimistic estimate. Superseded many times over; its value here is historical and conceptual, not as a usable predictor.

## Provenance

Located in the published literature, dropped into `inbox/` as `bioinformatics_19_15_1978.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btg255`; the prose sections were written here from the paper itself.

## Citation

Zhao et al. Bioinformatics 2003. Application of support vector machines for T-cell epitopes prediction. doi: 10.1093/bioinformatics/btg255

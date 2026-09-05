---
# --- identity ------------------------------------------------
id: 2024-01-01_jensen-2024-elife-enhancing-tcr-specific
id_basis: filename-year
source: Jensen(2024) eLife; Enhancing TCR specificity predictions by combined pan- and peptide-specific training, loss-scaling, and sequence similarity integration.pdf
sha256: 8c86c3b3dc78839ab76501215f14abea7ac6eddf7a15c1cce77a76f486d22fcf
size_bytes: 10592328
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 135975

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.7554/elife.93934"
year: 2024
title: "Enhancing TCR specificity predictions by combined pan- and peptide-specific training, loss-scaling, and sequence similarity integration"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Jensen_Elife_Enhancing_TCR_specificity_predictions_by_combi_PMID38437160.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05; DOI supplied by --doi-override (the PDF prints a different registered identifier)"
---

## Abstract

NetTCR 2.2 explores architectures and training strategies for TCR specificity prediction on a larger paired-chain dataset, addressing the imbalance caused by a handful of well-studied epitopes dominating available data. Combining pan-specific and peptide-specific modelling, loss-scaling, outlier removal and similarity-based predictions yields acceptable accuracy for peptides with as few as 15 positive TCRs, and state-of-the-art performance on the IMMREP 2022 benchmark.

## Summary

The engineering is aimed squarely at data imbalance rather than at a new architecture. Loss-scaling stops abundant epitopes dominating training, and a hybrid of pan-specific and peptide-specific models gets the benefits of both.

The practically useful result is the 15-positive-TCR threshold: it says roughly how much data a new epitope needs before a model can say anything useful about it, which is what determines whether expanding peptide coverage is feasible.

## Key points

- Uses paired-chain data rather than CDR3-beta alone, which most models are restricted to.
- Loss-scaling and outlier detection address the bias towards a few heavily studied epitopes.
- Combining pan-specific and peptide-specific models beats either; similarity-based integration helps most when a low false-positive rate is wanted.
- About 15 positive TCRs suffice for acceptable accuracy on a new peptide - a concrete data requirement.

## Limitations

The authors state that predictions on unseen peptides remain challenging, especially for peptides distant from the training set - the same generalisation wall Culka quantifies. Outlier removal improves reported performance but risks discarding genuine but atypical binders. IMMREP 2022 is a benchmark whose epitopes are largely well-studied ones, so state-of-the-art there does not establish performance on novel cancer neoepitopes.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Jensen_Elife_Enhancing_TCR_specificity_predictions_by_combi_PMID38437160.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.7554/elife.93934`; the prose sections were written here from the paper itself.

## Citation

FynboJensen et al. eLife 2024. Enhancing TCR specificity predictions by combined pan- and peptide-specific training, loss-scaling, and sequence similarity integration. doi: 10.7554/elife.93934

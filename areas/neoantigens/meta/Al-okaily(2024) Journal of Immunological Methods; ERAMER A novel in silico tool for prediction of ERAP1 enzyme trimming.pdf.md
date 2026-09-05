---
# --- identity ------------------------------------------------
id: 2024-01-01_al-okaily-2024-journal-of-immunological
id_basis: filename-year
source: Al-okaily(2024) Journal of Immunological Methods; ERAMER A novel in silico tool for prediction of ERAP1 enzyme trimming.pdf
sha256: 7be0cfde2faecae51cd583c5a86cfce952efbfc7e4dca21544ba8def43674c62
size_bytes: 434144
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 33992

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.jim.2024.113713"
year: 2024
title: "ERAMER: A novel in silico tool for prediction of ERAP1 enzyme trimming"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-S002217592400098X-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ERAMER is a prediction model for the trimming performed by ERAP1, the ER-resident aminopeptidase that shortens precursor peptides from the N-terminus to the 8-10 residues a stable MHC-I complex requires. The authors note that although ERAP1 specificities had been reported, no in silico tool existed for the trimming step.

## Summary

The MHC-I pathway has four steps - proteasomal cleavage, TAP transport, ERAP1 trimming, then surface presentation - and prediction tools have concentrated almost entirely on the last. ERAP1 decides which precursors become the right length to bind at all, so a peptide that would be an excellent binder may never exist in that form.

This fills the trimming step specifically, which makes it one of the few tools addressing what happens upstream of the binding groove.

## Key points

- Models ERAP1 N-terminal trimming, a step with no prior in silico tool despite documented specificity.
- Places the prediction inside the four-step MHC-I pathway rather than treating binding as the whole problem.
- Relevant to why some predicted strong binders are never observed: the precursor is not trimmed to that length.
- Companion in scope to proteasomal cleavage and TAP transport predictors.

## Limitations

ERAP1 is polymorphic and its variants differ in specificity, so a single trained model is an average over a variable enzyme. The output is a trimming prediction, which is one step of four and does not by itself say whether a peptide is presented, let alone immunogenic. Published in a methods journal with limited independent benchmarking, so its accuracy relative to nothing-at-all is easier to establish than its accuracy in absolute terms.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-S002217592400098X-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.jim.2024.113713`; the prose sections were written here from the paper itself.

## Citation

Al-okaily et al. Journal of Immunological Methods 2024. ERAMER: A novel in silico tool for prediction of ERAP1 enzyme trimming. doi: 10.1016/j.jim.2024.113713

---
# --- identity ------------------------------------------------
id: 2023-01-01_zhang-2023-computers-in-biology-and-medi
id_basis: filename-year
source: Zhang(2023) Computers in Biology and Medicine; DeepTAP An RNN-based method of TAP-binding peptide prediction in the selection of tumor neoantigens.pdf
sha256: 70cd87ea2aea7cbb4b6fa74c1aecef02c87a1a32b13982bc78ccecc06887504d
size_bytes: 3362777
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 71077

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.compbiomed.2023.107247"
year: 2023
title: "DeepTAP: An RNN-based method of TAP-binding peptide prediction in the selection of tumor neoantigens"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-S0010482523007126-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

DeepTAP uses a bidirectional gated recurrent unit to predict TAP-binding peptides, alongside an analysis of TAP-binding motifs and N- and C-terminal amino acid preferences. It is reported to achieve a better balance of precision and false positives than TAPPred, TAPREG and KSMM.

## Summary

TAP transport is the step between proteasomal cleavage and MHC loading, and it is selective - Androlewicz (1993) elsewhere in this collection showed 8-10mers compete efficiently while longer peptides and signal-sequence peptides do not. A peptide that is cleaved out but not transported never reaches the groove.

The emphasis on precision over recall is the right operating point for a filter: in a screening pipeline, false positives are what cost validation effort.

## Key points

- Models the transport step, completing cleavage-transport-binding coverage alongside the other tools here.
- BiGRU architecture over peptide sequence, with derived TAP motifs and terminal residue preferences.
- Optimises the precision / false-positive balance rather than raw accuracy.
- Intended as a filter in neoantigen selection rather than a standalone predictor.

## Limitations

The authors state a serious caveat about their own comparison: because of data limitations, some of their test set may be present in the training data of the baseline methods without their knowledge, so the reported margins over TAPPred, TAPREG and KSMM may be understated or overstated in unknown directions. TAP training data are old and limited relative to MHC binding data. Transport is one step, and predicting it well does not establish presentation.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-S0010482523007126-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.compbiomed.2023.107247`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Computers in Biology and Medicine 2023. DeepTAP: An RNN-based method of TAP-binding peptide prediction in the selection of tumor neoantigens. doi: 10.1016/j.compbiomed.2023.107247

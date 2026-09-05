---
# --- identity ------------------------------------------------
id: 2021-01-01_weeder-2021-bioinformatics-pepsickle-rap
id_basis: filename-year
source: Weeder(2021) Bioinformatics; pepsickle rapidly and accurately predicts proteasomal cleavage sites for improved neoantigen identification.pdf
sha256: 924d096f3dd51aeca964b00c05377c1f3116da0d129c02d2d4b9745d42dde8b3
size_bytes: 749206
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 95617

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btab628"
year: 2021
title: "pepsickle rapidly and accurately predicts proteasomal cleavage sites for improved neoantigen identification"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as btab628.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

pepsickle is an open-source proteasomal cleavage predictor with better in vivo AUC and speed than existing models, and the ability to predict from both constitutive and immunoproteasome profiles. Post hoc filtering of predicted patient neoepitopes with it significantly enriches for immune-responsive epitopes.

## Summary

The specific gap it identifies is that NetChop 3.1, the most cited cleavage tool, does not distinguish constitutive from immunoproteasomal cleavage. Those proteasomes cut differently and the immunoproteasome is what operates in interferon-exposed cells - the state relevant to a tumour under immune attack - so a single undifferentiated prediction is systematically wrong for the case that matters.

The demonstrated payoff is downstream: applying cleavage filtering after epitope prediction enriches for epitopes that actually provoked responses.

## Key points

- Predicts separately for constitutive and immunoproteasome profiles, which NetChop 3.1 does not.
- Trained and evaluated on in vivo as well as in vitro data.
- Post hoc filtering of patient neoepitopes significantly enriches for immune-responsive ones - the practical claim, tested.
- Open source, and fast enough to add to an existing pipeline as a filter.

## Limitations

The authors state the central problem plainly: with in vivo data, non-cleavage events must be determined heuristically, so negatives depend on having sampled true cleavage events adequately and are biased by under-reporting for less studied parts of the proteome. They also note that definitions of non-cleavage differ between studies, making cross-tool comparison imperfect. Cleavage remains one step of several, and enriching for immune-responsive epitopes is not the same as identifying them.

## Provenance

Located in the published literature, dropped into `inbox/` as `btab628.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btab628`; the prose sections were written here from the paper itself.

## Citation

Weeder et al. Bioinformatics 2021. pepsickle rapidly and accurately predicts proteasomal cleavage sites for improved neoantigen identification. doi: 10.1093/bioinformatics/btab628

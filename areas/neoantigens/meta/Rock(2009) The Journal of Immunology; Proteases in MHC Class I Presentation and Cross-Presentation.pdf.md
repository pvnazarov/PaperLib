---
# --- identity ------------------------------------------------
id: 2009-01-01_rock-2009-the-journal-of-immunology-prot
id_basis: filename-year
source: Rock(2009) The Journal of Immunology; Proteases in MHC Class I Presentation and Cross-Presentation.pdf
sha256: 4049cf7bddfc3927a1f5bf74c3c2d3c91f7051bc854d7d214102c972fedb04e5
size_bytes: 965135
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 68468

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.4049/jimmunol.0903399"
year: 2009
title: "Proteases in MHC Class I Presentation and Cross-Presentation"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as ji_0903399.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review of the proteases involved in generating MHC class I presented peptides, in both the classical direct pathway and cross-presentation. Cells continuously degrade their proteins into oligopeptide fragments, a fraction of which are transported by TAP into the ER where those of the right length and sequence bind newly synthesised class I molecules.

## Summary

The framing worth keeping is that antigen presentation is a by-product of ordinary protein turnover: cells degrade proteins to regulate levels and remove damaged ones, and the immune system samples that stream. Presentation is therefore biased towards what is abundantly made and rapidly degraded, not towards what is immunologically interesting.

The review covers the proteases beyond the proteasome - cytosolic and ER aminopeptidases, and the distinct machinery of cross-presentation - which together determine which fragments survive to be presented.

## Key points

- Presentation samples the products of normal protein catabolism, so abundance and turnover shape the immunopeptidome.
- Covers proteases beyond the proteasome, including the trimming steps that predictors mostly ignore.
- Treats cross-presentation as a distinct pathway with its own proteolytic requirements.
- The biological account behind the cleavage and trimming predictors in this collection.

## Limitations

A review: quantitative claims belong to the cited studies. It describes which proteases participate without establishing their relative contribution to any given epitope, which is what a predictor would need. Cross-presentation mechanisms were actively disputed at the time and the review reflects a 2009 state of that debate.

## Provenance

Located in the published literature, dropped into `inbox/` as `ji_0903399.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.4049/jimmunol.0903399`; the prose sections were written here from the paper itself.

## Citation

Rock et al. The Journal of Immunology 2009. Proteases in MHC Class I Presentation and Cross-Presentation. doi: 10.4049/jimmunol.0903399

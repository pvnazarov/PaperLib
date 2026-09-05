---
# --- identity ------------------------------------------------
id: 2005-01-01_nielsen-2005-immunogenetics-the-role-of
id_basis: filename-year
source: Nielsen(2005) Immunogenetics; The role of the proteasome in generating cytotoxic T-cell epitopes insights obtained from improved predictions of proteasomal cleavage.pdf
sha256: 59529c6f581b16c6026c3f0e72f44be2316577512e630d3733f88adf34efdd56
size_bytes: 242254
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 63940

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1007/s00251-005-0781-7"
year: 2005
title: "The role of the proteasome in generating cytotoxic T-cell epitopes: insights obtained from improved predictions of proteasomal cleavage"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s00251-005-0781-7.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

An improved NetChop, using novel sequence encoding, predicts about 10% more proteasomal cleavage sites correctly while lowering false positives by close to 15%. The better predictor is then used to study the proteasome's role: estimating the N-terminal extension of epitope precursors, and how often epitopes are destroyed rather than generated.

## Summary

The proteasome generates the exact C-terminus of a CTL epitope but only an N-terminus with a possible extension, which is why the trimming step exists. That asymmetry is the paper's organising fact and it explains why cleavage prediction targets the C-terminal side.

The less obvious point is destructive cleavage: a CTL response can fail because the proteasome cuts through the epitope rather than around it, so cleavage prediction identifies both what is generated and what is destroyed.

## Key points

- About 10% more cleavage sites predicted correctly with roughly 15% fewer false positives than the previous NetChop.
- The proteasome sets the exact C-terminus but leaves a variable N-terminal extension - the reason ERAP1 trimming exists.
- Epitopes can be destroyed by proteasomal cleavage, so the same prediction serves both directions.
- NetChop remains the standard cleavage component in composite presentation pipelines.

## Limitations

The authors note cleavage is stochastic - not all potential sites are used in a given digest - so a network output has to be transformed into a per-digest probability, an extra modelling step with its own assumptions. They also state they did not normalise natural epitope length when estimating N-terminal extension. Training rests on in vitro digestion data from a limited set of substrates, and 2005-era performance has been improved on since.

## Provenance

Located in the published literature, dropped into `inbox/` as `s00251-005-0781-7.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1007/s00251-005-0781-7`; the prose sections were written here from the paper itself.

## Citation

Nielsen et al. Immunogenetics 2005. The role of the proteasome in generating cytotoxic T-cell epitopes: insights obtained from improved predictions of proteasomal cleavage. doi: 10.1007/s00251-005-0781-7

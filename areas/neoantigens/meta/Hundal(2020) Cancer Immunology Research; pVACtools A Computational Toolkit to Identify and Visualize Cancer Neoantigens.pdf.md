---
# --- identity ------------------------------------------------
id: 2020-01-01_hundal-2020-cancer-immunology-research-p
id_basis: filename-year
source: Hundal(2020) Cancer Immunology Research; pVACtools A Computational Toolkit to Identify and Visualize Cancer Neoantigens.pdf
sha256: c095d95d4cd5ff7380636e65910d8e1a6157c7c05d8bc7dc8ed164b0a3bbcdc8
size_bytes: 1215072
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 93156

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2326-6066.CIR-19-0401"
year: 2020
title: "pVACtools: A Computational Toolkit to Identify and Visualize Cancer Neoantigens"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 409.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

pVACtools is an extensible toolkit covering computational identification, selection, prioritisation and visualisation of neoantigens, taking somatic variants in VCF and handling gene fusions and insertion/deletion frameshift variants as well as missense mutations.

## Summary

This is the pipeline the rest of the ecosystem grew around - pVACview, also in this collection, is its visualisation component, and several papers here use it or extend it.

The design point worth noting is coverage of variant classes beyond missense. Frameshifts and fusions generate long stretches of entirely novel sequence rather than a single substituted residue, which makes them attractive targets and means a missense-only pipeline systematically misses the most foreign candidates.

## Key points

- Covers the whole workflow - identification, selection, prioritisation, visualisation - rather than one step.
- Handles gene fusions and frameshift indels, not just missense variants.
- Standard VCF input, so it drops into existing somatic variant pipelines.
- Explicitly designed to let clinicians and non-specialist researchers participate in neoantigen evaluation.

## Limitations

A framework: its accuracy is the accuracy of the binding and immunogenicity predictors plugged into it, and it inherits every bias those carry. Broader variant coverage widens the candidate list without improving the ranking, so more classes of neoantigen also means more false positives to triage. Nothing here evaluates whether pipeline-selected neoantigens are immunogenic.

## Provenance

Located in the published literature, dropped into `inbox/` as `409.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2326-6066.CIR-19-0401`; the prose sections were written here from the paper itself.

## Citation

Hundal et al. Cancer Immunology Research 2020. pVACtools: A Computational Toolkit to Identify and Visualize Cancer Neoantigens. doi: 10.1158/2326-6066.CIR-19-0401

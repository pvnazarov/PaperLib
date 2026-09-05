---
# --- identity ------------------------------------------------
id: 2016-01-01_jardine-2016-science-hiv-1-broadly-neutr
id_basis: filename-year
source: Jardine(2016) Science; HIV-1 broadly neutralizing antibody precursor B cells revealed by germline-targeting immunogen.pdf
sha256: 6c4ed1cc11beef7984d58a1a0b5ba9c997fc9d6613ace5553e944c1519d84fef
size_bytes: 1222964
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 91216

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/science.aad9195"
year: 2016
title: "HIV-1 broadly neutralizing antibody precursor B cells revealed by germline-targeting immunogen"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as science.aaf1490.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A germline-targeting immunogen, eOD-GT8, is used with human B cell probing to detect naive B cell precursors of VRC01-class broadly neutralising antibodies against HIV-1. Correcting for sorting and PCR losses, the precursor frequency is calculated as roughly 1 in 400,000 naive B cells.

## Summary

This is B cell vaccinology rather than T cell neoantigen work, and it sits in this collection as a methodological parallel: an immunogen designed to engage a rare, defined naive precursor repertoire, with the precursor frequency actually measured rather than assumed.

That is the same problem neoantigen vaccines face from the other side - whether a T cell capable of seeing a given neoepitope exists in the patient's repertoire at all, which the thymic selection papers in this collection argue cannot be taken for granted.

## Key points

- Designs an immunogen to engage germline precursors rather than mature antibodies, then verifies the precursors exist in humans.
- Measures precursor frequency directly: about 1 in 400,000 naive B cells.
- Combines protein design with human B cell probing, a template the authors propose for other antibody classes.
- The repertoire-availability question it answers for B cells is the one the thymic selection papers here raise for T cells.

## Limitations

Heavy and light chain sequences were recovered from fewer than half of the sorted B cells because of the inherent limitations of single-cell PCR, so the frequency rests on a correction rather than a direct count. B cells bearing lambda light chains were not analysed at all. Precursors may also exist in the memory B cell population, whose frequency the authors state remains to be measured. It is an HIV antibody paper, so its relevance here is by analogy, not by result.

## Provenance

Located in the published literature, dropped into `inbox/` as `science.aaf1490.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/science.aad9195`; the prose sections were written here from the paper itself.

## Citation

Jardine et al. Science 2016. HIV-1 broadly neutralizing antibody precursor B cells revealed by germline-targeting immunogen. doi: 10.1126/science.aad9195

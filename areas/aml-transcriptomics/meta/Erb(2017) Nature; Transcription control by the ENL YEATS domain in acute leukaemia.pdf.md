---
# --- identity ------------------------------------------------
id: 2017-01-01_erb-2017-nature-transcription-control-by
id_basis: filename-year
source: Erb(2017) Nature; Transcription control by the ENL YEATS domain in acute leukaemia.pdf
sha256: 03930a733498757de22514c7fc0592d7b59560361bb301b60db8c344ea143efe
size_bytes: 5821562
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 145775

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature21688"
year: 2017
title: "Transcription control by the ENL YEATS domain in acute leukaemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Erb(2017) Nature; Transcription control by the ENL YEATS domain in acute leukaemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A genome-scale CRISPR-Cas9 loss-of-function screen in an MLL-AF4-positive leukemia line identifies ENL as specifically required for proliferation in vitro and in vivo. Using a chemical genetic strategy for targeted protein degradation (dTAG), acute loss of ENL is shown to suppress initiation and elongation of RNA polymerase II at active genes genome-wide, with the most pronounced effects at genes carrying a disproportionate ENL load. An intact YEATS chromatin-reader domain is essential for ENL-dependent leukemic growth, while Enl loss minimally affects normal Lin-Sca-1+c-Kit+ mouse hematopoietic progenitors.

## Summary

ENL was known as a fusion partner of MLL; the finding here is that wild-type ENL is itself the dependency, and specifically its YEATS acyl-lysine reader domain. That reframes a structural curiosity into a druggable module, and the rescue experiments with F47A and Y78A mutants - which lose chromatin localisation to graded degrees and fail to rescue accordingly - are what make the domain, not just the protein, the target.

The methodological argument is equally deliberate. Degradation acts in minutes, so the effects on Pol II initiation and elongation are immediate consequences rather than the accumulated secondary changes that knockdown and knockout produce over days. The authors present this as a general platform for studying 'fast biology', and it is now standard practice. The mechanism is explicitly DOT1L-independent, which matters given how much MLL-fusion therapeutics had converged on DOT1L.

## Key points

- Wild-type ENL, not only the MLL-ENL fusion, is a selective dependency in MLL-rearranged leukemia, in vitro and in xenografts.
- The YEATS chromatin-reader domain is required - point mutants that lose chromatin localisation fail to rescue - nominating a druggable module.
- Targeted degradation resolves immediate from secondary effects: ENL loss suppresses Pol II initiation and elongation genome-wide within minutes.
- Effects concentrate at genes with a disproportionate ENL load, including MYC, MYB and HOXA10.
- Supports a DOT1L-independent mechanism of leukemic maintenance, via ENL recruitment of the super elongation complex.

## Limitations

Published in advance of any direct-acting ENL inhibitor, which the authors state - so the therapeutic claim rests on genetic and degron evidence that a YEATS-domain inhibitor should work. The dTAG system requires engineering a degron onto the endogenous protein, so the acute-degradation experiments are in modified cell lines rather than primary cells. Sensitivity varies across lines - HL-60 and JURKAT were insensitive - and what determines that is not resolved. The comparison with normal hematopoiesis is a competitive growth assay in mouse LSK progenitors, a limited test of the therapeutic window. In vivo work is one MV4;11 xenograft model with CRISPR targeting rather than pharmacology.

## Provenance

Located in the published literature, dropped into `inbox/` as `Erb(2017) Nature; Transcription control by the ENL YEATS domain in acute leukaemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature21688`; the prose sections were written here from the paper itself.

## Citation

Erb et al. Nature 2017. Transcription control by the ENL YEATS domain in acute leukaemia. doi: 10.1038/nature21688

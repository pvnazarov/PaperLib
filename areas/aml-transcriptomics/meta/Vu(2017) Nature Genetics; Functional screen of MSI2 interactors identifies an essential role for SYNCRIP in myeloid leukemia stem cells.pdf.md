---
# --- identity ------------------------------------------------
id: 2017-01-01_vu-2017-nature-genetics-functional-scree
id_basis: filename-year
source: Vu(2017) Nature Genetics; Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells.pdf
sha256: 026b092d345097fee931ab74433737f73504f24c97e2b5137cf01140afe70949
size_bytes: 1697117
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 321449

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/ng.3854"
year: 2017
title: "Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Vu(2017) Nat Genet; Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Proteomic analysis of the MSI2-interacting RNA-binding protein network combined with functional shRNA screening identified 24 genes required for in vivo leukemia, with Syncrip the most differentially required between normal and myeloid leukemia cells. SYNCRIP depletion increased apoptosis and differentiation while delaying leukemogenesis, and expression profiling showed loss of the MLL and HOXA9 leukemia stem cell programme. SYNCRIP and MSI2 interact indirectly through shared mRNA targets; SYNCRIP maintains HOXA9 translation, and overexpressing MSI2 or HOXA9 rescues the effects of SYNCRIP depletion.

## Summary

Approaches leukemia stem cell biology through translational rather than transcriptional control, on the reasoning that RNA-binding proteins are the arbiters of which transcripts become protein and that this layer has been comparatively neglected. The screen design - proteomic mapping of an interaction network, then functional testing in vivo - selects for what matters in the animal rather than in culture.

SYNCRIP is the standout hit precisely because it is the most differentially required between normal and leukemic cells, which is the selection criterion that matters for a target. The rescue by HOXA9 overexpression places SYNCRIP upstream of the same HOXA9 programme that the chromatin-directed work in this collection converges on, reached this time by translational control - so HOXA9 abundance is regulated at more than one level.

## Key points

- Combines proteomic mapping of the MSI2 interactome with in vivo functional shRNA screening, selecting for requirement in the animal.
- SYNCRIP is the most differentially required gene between normal and myeloid leukemia cells among 24 hits.
- Depletion increases apoptosis and differentiation, delays leukemogenesis, and abolishes the MLL/HOXA9 stem cell programme.
- SYNCRIP maintains HOXA9 translation; HOXA9 or MSI2 overexpression rescues depletion, placing it upstream of that programme.
- SYNCRIP is elevated in AML lines and patient samples relative to normal cells.

## Limitations

The authors state that the role of SYNCRIP in normal hematopoiesis needs further study - differential requirement in a screen is not the same as demonstrated safety - and that whether SYNCRIP is a useful diagnostic marker remains for future work. No inhibitor exists: the therapeutic proposal rests on small molecules blocking RNA binding or antisense oligonucleotides, neither developed here. SYNCRIP and MSI2 interact only indirectly through shared targets, so the network framing is looser than a complex. Work is in cell lines and mouse models with patient samples contributing expression comparison. HOXA9 rescue shows sufficiency to restore growth, not that HOXA9 is the only relevant target.

## Provenance

Located in the published literature, dropped into `inbox/` as `Vu(2017) Nat Genet; Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/ng.3854`; the prose sections were written here from the paper itself.

## Citation

Vu et al. Nature Genetics 2017. Functional screen of MSI2 interactors identifies an essential role for SYNCRIP in myeloid leukemia stem cells. doi: 10.1038/ng.3854

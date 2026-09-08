---
# --- identity ------------------------------------------------
id: 2017-01-01_kerry-2017-cell-reports-mll-af4-spreadin
id_basis: filename-year
source: Kerry(2017) Cell Reports; MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia.pdf
sha256: ce87e856e1e9d304b5c90f0f0f5dbab81bbf6b4fd701ffc56ef8b160b01886d2
size_bytes: 5024289
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 154671

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2016.12.054"
year: 2017
title: "MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kerry(2017) Cell Rep; MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

MLL-AF4 binding is shown to require an unmethylated CpG island and Menin, and at a subset of targets both MLL-AF4 and Menin spread into the gene body, which is associated with high transcription and an aberrant chromatin signature. These spreading targets are distinct from super-enhancers, and the presence of spreading - rather than simply the presence of MLL-AF4 and H3K79me2/3 - predicts sensitivity to DOT1L inhibitors. Spreading correlates with Menin and ENL binding and occurs over low-density unmethylated CpG landscapes in gene bodies close to the promoter.

## Summary

A predictive rather than merely descriptive chromatin finding: not every MLL-AF4 target responds to DOT1L inhibition, and what distinguishes the responsive ones is whether the fusion spreads into the gene body. That is a usable criterion, and it corrects the earlier assumption that H3K79 methylation status alone would predict dependence.

The proposed mechanism for spreading is elegant. Gene-body unmethylated CpG regions have CG density too low for a strong CXXC-DNA interaction on its own, so spreading depends on Menin and ENL stabilising the complex across a series of weak anchors in close proximity - something wild-type MLL, lacking the fusion partner that permits dimerisation, cannot do. That would make spreading a property specific to the oncoprotein rather than an exaggeration of normal MLL behaviour.

## Key points

- MLL-AF4 binding requires unmethylated CpG islands and Menin, and the two co-stabilise each other on chromatin.
- At a subset of targets, MLL-AF4 and Menin spread into the gene body, producing an aberrant chromatin signature and high transcription.
- Spreading targets are distinct from super-enhancers, which had been the prevailing way to describe broad oncogenic binding domains.
- Spreading, not the mere presence of MLL-AF4 and H3K79me2/3, predicts sensitivity to DOT1L inhibitors.
- Proposed mechanism: Menin/ENL stabilise the fusion across low-density gene-body uCpGs where CXXC binding alone would be too weak.

## Limitations

The authors state the central unresolved question themselves: it is unknown whether the ability to spread drives higher expression and initiates leukemia, or whether spreading is a consequence of those genes already being highly transcribed - so causation between spreading and the phenotype is open. Their reinterpretation of past work is also worth noting as a caution about this kind of evidence - they find no direct connection between MLL-AF4 recruitment and PAFc, and suggest earlier reports of PAFc dependence may have been indirect. Work is in MLL-AF4 cell lines, so generalisation to other MLL fusion partners and to primary patient samples is assumed rather than shown. The DOT1L sensitivity prediction is established in vitro; DOT1L inhibitors subsequently showed only modest clinical activity in adult acute leukemia, which this predictive framework does not by itself rescue.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kerry(2017) Cell Rep; MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2016.12.054`; the prose sections were written here from the paper itself.

## Citation

Kerry et al. Cell Reports 2017. MLL-AF4 Spreading Identifies Binding Sites that Are Distinct from Super-Enhancers and that Govern Sensitivity to DOT1L Inhibition in Leukemia. doi: 10.1016/j.celrep.2016.12.054

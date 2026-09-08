---
# --- identity ------------------------------------------------
id: 2017-01-01_loke-2017-cell-reports-runx1-eto-and-run
id_basis: filename-year
source: Loke(2017) Cell Reports; RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8,21) and t(3,21) AML.pdf
sha256: a30729f38df09ee7d004150b24a05bf55a9f5a4382f5a3651951aaa1e09b67b1
size_bytes: 4110396
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 254927

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2017.05.005"
year: 2017
title: "RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8;21) and t(3;21) AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Loke(2017) Cell Rep; RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8 21) and t(3 21) AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A comparison of the regulatory landscapes of two AML types driven by fusions of the same transcription factor: RUNX1-ETO in t(8;21) and RUNX1-EVI1 in t(3;21). The two fusion proteins show distinct genomic binding patterns and cooperate with different transcription factors, producing unique gene regulatory networks, yet both downregulate the myeloid differentiation regulator C/EBPalpha. Depleting either fusion initiates C/EBPalpha-dependent myeloid differentiation. Survival of t(8;21) AML depends on RUNX1, whereas t(3;21) AML requires GATA2.

## Summary

A controlled comparison that isolates the contribution of the fusion partner. Both leukemias arise from a RUNX1 fusion, so what differs between them is attributable to ETO versus EVI1 - and what differs turns out to be nearly everything about the wiring: binding pattern, cooperating factors, and which factor the leukemia depends on for survival.

The convergence is as informative as the divergence. Two distinct regulatory networks both funnel into downregulation of C/EBPalpha, and depleting either fusion triggers C/EBPalpha-dependent differentiation - so the differentiation block is the shared endpoint reached by different routes. The divergent dependencies, RUNX1 for t(8;21) and GATA2 for t(3;21), are the practical result, since they say the two subtypes need different drugs despite sharing a driver gene.

## Key points

- Two AMLs driven by fusions of the same gene, RUNX1, are compared to isolate the effect of the fusion partner.
- RUNX1-ETO and RUNX1-EVI1 have distinct binding patterns and distinct cooperating transcription factors.
- Both converge on downregulation of C/EBPalpha, and depleting either fusion triggers C/EBPalpha-dependent differentiation.
- Survival dependencies diverge: t(8;21) requires RUNX1, t(3;21) requires GATA2.
- Fusion-junction-specific siRNA depletes RUNX1-EVI1 without affecting wild-type RUNX1, allowing the fusion's contribution to be separated.

## Limitations

t(3;21) is rare, and the work rests substantially on one cell line, SKH-1, with K562 as control - so the t(3;21) side of the comparison is thinly supported relative to the t(8;21) side. Knockdown effects on binding were mixed rather than clean: RUNX1-EVI1 depletion did not change global binding distribution or overall RUNX1 binding levels, with some sites gaining and others losing signal, which complicates the network interpretation. Depletion is transient siRNA over days, and differentiation and apoptosis develop over that window, so early and late effects are hard to separate. Primary patient material is used for footprinting comparisons rather than for the functional work. No in vivo or therapeutic experiment tests the RUNX1 and GATA2 dependencies as targets.

## Provenance

Located in the published literature, dropped into `inbox/` as `Loke(2017) Cell Rep; RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8 21) and t(3 21) AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2017.05.005`; the prose sections were written here from the paper itself.

## Citation

Loke et al. Cell Reports 2017. RUNX1-ETO and RUNX1-EVI1 Differentially Reprogram the Chromatin Landscape in t(8;21) and t(3;21) AML. doi: 10.1016/j.celrep.2017.05.005

---
# --- identity ------------------------------------------------
id: 2025-01-01_ma-2025-oncogene-super-enhancer-associat
id_basis: filename-year
source: Ma(2025) Oncogene; Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF.pdf
sha256: 40eff55a253bdae72cd73592fd060d08deb538fe7f861e3c55b55cf54c60c4ea
size_bytes: 1532137
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 180025

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41388-025-03612-9"
year: 2025
title: "Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ma(2025) Oncogene; Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Profiling APL-specific super-enhancer-associated lncRNAs from H3K27ac ChIP-seq and RNA-seq in TCGA and Beat AML identified 44 candidates, from which the authors characterise RP11-750H9.5 - lnc-SPI1U - transcribed from the super-enhancer upstream of SPI1, which encodes PU.1. lnc-SPI1U suppressed differentiation and apoptosis and blunted ATRA-induced growth inhibition, opposite to SPI1's role, by interacting with HNRNPH1/F to destabilise SPI1 mRNA. Its induction during myeloid differentiation is PU.1-dependent, forming a feedback loop that tunes SPI1 to an optimal level, and in APL the PML/RARalpha fusion blocks PU.1-dependent transactivation of lnc-SPI1U by hijacking the overlapping super-enhancer region.

## Summary

A tidy piece of regulatory logic: a lncRNA transcribed from the super-enhancer of the transcription factor it regulates, induced by that factor, and acting to destabilise its mRNA - a negative feedback loop encoded in the same locus, which keeps PU.1 at the level myeloid differentiation requires rather than simply as high as possible.

The leukemic relevance is that PML/RARalpha breaks the loop by occupying the same super-enhancer, so the fusion protein disrupts not only PU.1 target genes but the machinery that tunes PU.1 itself. The functional experiments are internally consistent - knocking down the lncRNA enhances ATRA-induced differentiation, apoptosis and growth inhibition, which is the direction the model predicts.

## Key points

- 44 APL-specific super-enhancer-associated lncRNAs identified, of which lnc-SPI1U is characterised in detail.
- lnc-SPI1U is transcribed from the super-enhancer upstream of SPI1 and destabilises SPI1 mRNA via HNRNPH1/F.
- Its induction is PU.1-dependent, creating a negative feedback loop that tunes SPI1 to an optimal differentiation-permissive level.
- Knockdown enhances ATRA-induced differentiation, apoptosis and growth inhibition in APL cells.
- PML/RARalpha hijacks the overlapping super-enhancer, blocking PU.1-dependent transactivation of the lncRNA and breaking the loop.

## Limitations

Functional work is essentially confined to NB4, the standard APL cell line, with no primary patient samples in the perturbation experiments and no in vivo model. The protein partners come from RNA pull-down and mass spectrometry, an approach prone to abundant non-specific binders, and the top hits are taken forward without an independent orthogonal interaction assay described in the summary evidence. Three transcript variants exist at the locus and only the most abundant is studied. APL is the one AML subtype that is already largely curable with ATRA and arsenic, so the therapeutic relevance of enhancing ATRA response there is limited; whether the SPI1 feedback loop operates in other AML subtypes is not addressed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ma(2025) Oncogene; Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41388-025-03612-9`; the prose sections were written here from the paper itself.

## Citation

Ma et al. Oncogene 2025. Super-enhancer-associated long noncoding RNA lnc-SPI1U mediates SPI1 feedback regulation by interacting with HNRNPH1 and HNRNPF. doi: 10.1038/s41388-025-03612-9

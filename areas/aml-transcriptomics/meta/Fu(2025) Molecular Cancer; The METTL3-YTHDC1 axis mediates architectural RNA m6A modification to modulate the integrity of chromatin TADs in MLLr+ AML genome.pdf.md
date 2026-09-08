---
# --- identity ------------------------------------------------
id: 2025-01-01_fu-2025-molecular-cancer-the-mettl3-ythd
id_basis: filename-year
source: Fu(2025) Molecular Cancer; The METTL3-YTHDC1 axis mediates architectural RNA m6A modification to modulate the integrity of chromatin TADs in MLLr+ AML genome.pdf
sha256: 0047fbf241a4080574ef63864e7fc2b736f3f1bbe111e5a6707e0cb20f132c46
size_bytes: 9668195
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 175161

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12943-025-02545-x"
year: 2025
title: "The METTL3-YTHDC1 axis mediates architectural RNA m6A modification to modulate the integrity of chromatin TADs in MLLr+ AML genome"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Fu(2025) Mol Cancer; The METTL3-YTHDC1 axis mediates architectural RNA mA modification to modulate the integrity of chromatin TADs in MLLr + AML genome.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A multi-omics study (RNA-seq, IP-MS, DRIP-seq, ChIP-seq for METTL3, CTCF, H3K4me3 and H3K27ac, RIP-seq, m6A-seq and Hi-C) showing that METTL3 is transcriptionally activated by MLL in MLL-rearranged AML and forms a complex with YTHDC1 and CTCF at promoters and enhancers. METTL3 depletion disrupts CTCF binding sites and reduces chromatin accessibility at leukemic genes including MYB and RUNX1, and YTHDC1 loss compromises CTCF-dependent 3D genome organisation. Mechanistically, YTHDC1 recognises m6A-modified architectural RNAs such as MALAT1, enhancing R-loop formation and sustaining CTCF-mediated TAD activity.

## Summary

An attempt to join two literatures that have grown up separately - RNA modification and 3D genome organisation - into one causal chain running from the MLL fusion to chromatin architecture. The proposed sequence is that the fusion drives METTL3 expression, METTL3 methylates architectural lncRNAs, YTHDC1 reads those marks, the resulting stabilised R-loops hold CTCF at its binding sites, and the TAD boundaries around leukemic genes stay intact.

The reason to take the framing seriously is that it gives METTL3 a role beyond translational control - the mechanism reported by Barbieri elsewhere in this collection - and offers a structural explanation for why m6A machinery is an AML dependency at all.

## Key points

- Places METTL3 downstream of the MLL fusion as a transcriptionally activated target in MLL-rearranged AML.
- METTL3 forms a complex with YTHDC1 and CTCF and co-localises at promoters and enhancers.
- m6A-marked architectural RNAs such as MALAT1 are read by YTHDC1 and stabilise R-loops.
- R-loops sustain CTCF binding and CTCF-dependent TAD integrity at leukemic loci including MYB and RUNX1.
- Connects epitranscriptomics to 3D genome biology, proposing the METTL3-YTHDC1-CTCF axis as a therapeutic target.

## Limitations

A long causal chain assembled largely from correlative genomics - co-localisation, co-immunoprecipitation and loss-of-function effects at each step - without an experiment that isolates the proposed mechanism, such as restoring R-loops or CTCF binding in METTL3-depleted cells and rescuing TAD integrity. R-loop measurement by DRIP-seq is antibody-dependent and known to be sensitive to RNase H controls and processing. Depleting METTL3 or YTHDC1 has pervasive effects on the transcriptome, so changes in chromatin accessibility and looping may be downstream of altered gene expression rather than of the architectural mechanism proposed. Hi-C in these experiments has limited resolution for calling boundary changes. Work is in cell lines, with no primary patient or in vivo validation of the architectural claims, and no therapeutic experiment despite the concluding proposal.

## Provenance

Located in the published literature, dropped into `inbox/` as `Fu(2025) Mol Cancer; The METTL3-YTHDC1 axis mediates architectural RNA mA modification to modulate the integrity of chromatin TADs in MLLr + AML genome.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12943-025-02545-x`; the prose sections were written here from the paper itself.

## Citation

Fu et al. Molecular Cancer 2025. The METTL3-YTHDC1 axis mediates architectural RNA m6A modification to modulate the integrity of chromatin TADs in MLLr + AML genome. doi: 10.1186/s12943-025-02545-x

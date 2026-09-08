---
# --- identity ------------------------------------------------
id: 2026-01-01_miller-2026-unknown-long-read-cdna-seque
id_basis: filename-year
source: Miller(2026) unknown; Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS.pdf
sha256: 4177c21de13f5d5efee8aedeba85a2dac255e2cbce02dece393e41f2a06425ef
size_bytes: 1859040
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 88736

# --- classification (LIH WI DC-909) --------------------------
type: preprint
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.64898/2026.05.20.726635"
year: 2026
title: "Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Miller(2026) bioRxiv; Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using the Oxford Nanopore cDNA platform, the authors generated nearly 2 billion long reads (median 25.8 million per sample) from 71 human samples: 48 AML or MDS samples, 25 with SRSF2, U2AF1 or SF3B1 mutations, plus 23 sorted hematopoietic populations from healthy individuals. They identified 174,162 novel isoforms absent from the reference transcriptome alongside 206,601 known Ensembl isoforms, with proteomic validation confirming that many are translated - 307 high-confidence novel peptides. Isoforms enriched in spliceosome-mutant samples were identified, along with proteomic evidence of frequent nonsense-mediated decay regulation of novel transcripts. An interactive portal is provided.

## Summary

A resource whose scale is the point. Short-read sequencing measures exons and junctions but cannot link them into whole transcripts, and previous long-read studies ran at a fraction of this depth; each depth increase has kept revealing new transcripts, which is the paper's argument that current catalogues capture only part of the complexity.

The pairing with proteomics is what makes it more than a catalogue. Detecting 307 novel peptides shows some of these isoforms are real proteins, and the AAMP example is instructive - unchanged mRNA abundance with reduced protein, alongside a shift toward NMD-sensitive isoforms, means NMD regulation is occurring and is completely invisible to gene-level analysis. That is a general warning about how much standard RNA-seq analysis misses. Including flow-sorted subpopulations lets them characterise CD34+ progenitors and lymphocyte compartments that make up a few percent of marrow but carry hundreds to thousands of population-enriched novel transcripts.

## Key points

- Nearly 2 billion long reads across 71 samples - far deeper than previous long-read cancer transcriptome studies.
- 174,162 novel isoforms identified alongside 206,601 known ones, roughly 1.5-fold more novel transcripts than an earlier AML study.
- Proteomic validation confirms translation of some novel isoforms, with 307 high-confidence novel peptides.
- Isoform shifts toward NMD-sensitive transcripts explain protein reduction invisible to gene-level analysis, as for AAMP.
- Flow-sorted subpopulations reveal lineage-specific novel transcripts in rare but disease-relevant compartments; an interactive portal is provided.

## Limitations

A bioRxiv preprint, not certified by peer review. Novel isoform calls from long-read data are sensitive to assembly parameters and to reverse transcription and template-switching artefacts, and 174,162 novel isoforms will include false positives - the 307 validated peptides are a small fraction, so most novel transcripts remain unvalidated at protein level. Deeper sequencing continues to reveal more transcripts, which the authors present as evidence of untapped complexity but which equally reflects the difficulty of distinguishing genuine low-abundance isoforms from noise. Comparison to a previous AML study could not be made directly because that assembly is not public. This is a descriptive resource: no isoform is shown to have a functional role in disease, and the spliceosome-mutant-enriched transcripts are associations rather than mechanisms.

## Provenance

Located in the published literature, dropped into `inbox/` as `Miller(2026) bioRxiv; Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.64898/2026.05.20.726635`; the prose sections were written here from the paper itself.

## Citation

Miller et al. unknown 2026. Long-read cDNA sequencing reveals novel isoforms and spliceosome-mutant-enriched transcripts in AML and MDS. doi: 10.64898/2026.05.20.726635

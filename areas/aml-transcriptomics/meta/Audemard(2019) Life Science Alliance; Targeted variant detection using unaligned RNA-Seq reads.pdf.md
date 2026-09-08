---
# --- identity ------------------------------------------------
id: 2019-01-01_audemard-2019-life-science-alliance-targ
id_basis: filename-year
source: Audemard(2019) Life Science Alliance; Targeted variant detection using unaligned RNA-Seq reads.pdf
sha256: b3cf3b76b99fd4b4afb2dd26793a4a836c3fe1cf787414af4d4410e056c737d2
size_bytes: 1011402
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 64444

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.26508/lsa.201900336"
year: 2019
title: "Targeted variant detection using unaligned RNA-Seq reads"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Audemard(2019) Life Sci Alliance; Targeted variant detection using unaligned RNA-Seq reads.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

km, a method for targeted variant detection that decomposes RNA-seq reads into k-mers and identifies mutations without mapping reads to a reference. Given any sequence as an expected reference, it reports all alternative forms sharing that reference's extremities, and so detects single-base substitutions, insertions, deletions, duplications, inversions and fusions with one mechanism. Evaluated on two independent cohorts, TCGA and Leucegene, across 10,844 samples, detection is shown to be fast, accurate and mainly limited by sequencing depth.

## Summary

A deliberate narrowing of scope that buys both speed and sensitivity. Conventional pipelines map every read and then call variants, which spends most of the compute outside the region anyone cares about and, worse, loses exactly the reads that carry structural variants because those are the reads a mapper cannot place.

FLT3-ITD is the case that makes the argument. Its position and length vary, so it defeats end-to-end alignment, and the existing workarounds depend on soft-clipped reads from one specific aligner. Dropping alignment altogether removes that dependency: the k-mer representation does not care where a read belongs, only whether the sequence between two anchors differs. The cost is that km only ever answers about regions you nominate in advance.

## Key points

- Variant detection without read mapping, using k-mer decomposition anchored on a user-supplied reference sequence.
- One mechanism covers substitutions, indels, duplications, inversions and fusions, rather than a separate tool per variant class.
- Particularly suited to FLT3-ITD, where variable position and length defeat aligners and existing tools require BWA-MEM-specific BAMs.
- Validated across 10,844 RNA-seq samples from TCGA and Leucegene; accuracy is mainly limited by sequencing depth.
- Targeted by design: it returns nothing outside the nominated regions, and analyses are incremental so new regions can be added cheaply.

## Limitations

Targeted by construction, so it is a confirmatory and diagnostic tool rather than a discovery one - it cannot find a variant in a region nobody thought to nominate, which is the opposite tradeoff from the comprehensive pipelines it is faster than. The authors name the k-mer approach's own caveat: read dependency between k-mers is ignored, so evidence from a single read is not distinguished from evidence spread across several, which weakens phasing and low-frequency calls. Sensitivity is bounded by expression level, since an unexpressed or NMD-degraded transcript yields no reads regardless of depth. Accuracy is assessed against existing calls in TCGA and Leucegene, so variants those pipelines also missed do not count against it.

## Provenance

Located in the published literature, dropped into `inbox/` as `Audemard(2019) Life Sci Alliance; Targeted variant detection using unaligned RNA-Seq reads.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.26508/lsa.201900336`; the prose sections were written here from the paper itself.

## Citation

OlivierAudemard et al. Life Science Alliance 2019. Targeted variant detection using unaligned RNA-Seq reads. doi: 10.26508/lsa.201900336

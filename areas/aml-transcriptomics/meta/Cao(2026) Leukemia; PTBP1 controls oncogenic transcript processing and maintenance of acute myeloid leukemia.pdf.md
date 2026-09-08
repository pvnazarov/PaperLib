---
# --- identity ------------------------------------------------
id: 2026-01-01_cao-2026-leukemia-ptbp1-controls-oncogen
id_basis: filename-year
source: Cao(2026) Leukemia; PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia.pdf
sha256: 09e0b0d242d023bf409ce5df90d984e0d260b4f88ba3f25e5effd20e4533cfa5
size_bytes: 4352581
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 108555

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-026-03098-8"
year: 2026
title: "PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Cao(2026) Leukemia; PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A domain-focused CRISPR screen of 3182 sgRNAs targeting 527 RNA-enzymatic and binding domains across 341 RNA-associated proteins identifies several RNA-binding proteins as AML dependencies - including the splicing factor PTBP1 and the m6A reader RBM15 - biased toward KMT2A-rearranged AML. All four RNA-binding domains of PTBP1 are required for KMT2A-r proliferation. PTBP1 is dispensable for myelopoiesis, but its suppression in AML causes cell cycle arrest, apoptosis and myeloid differentiation; transcriptomics shows disruption of the KMT2A-r-essential program and widespread splicing dysregulation, and CLIP-seq shows preferential binding to transcripts critical for KMT2A-r proliferation including IKZF1, MEF2C, EZH2, SIK3 and PBX3.

## Summary

The therapeutic window is the finding. PTBP1 is required for KMT2A-rearranged AML and not for normal myelopoiesis, which is what separates a dependency from an essential gene and is the question most screen hits fail.

Methodologically the domain-focused library is the right instrument: targeting RNA-binding domains rather than whole genes asks whether the binding function is required, and all four PTBP1 domains being necessary is a strong internal control against off-target effects. The mechanism the authors propose is deliberately distributed - PTBP1 tunes splicing and expression of many AML-essential genes at once, each perturbation modest, and the dependency emerges from the sum. That is honest about why no single downstream target reproduces the phenotype, and it is also the claim hardest to falsify.

## Key points

- Domain-focused CRISPR screen across 341 RNA-associated proteins identifies PTBP1 and RBM15 as AML-biased dependencies.
- The dependency is biased to KMT2A-rearranged AML, and all four PTBP1 RNA-binding domains are required.
- PTBP1 is not required for normal myelopoiesis, giving a therapeutic window that most essential-gene hits lack.
- CLIP-seq shows direct binding to IKZF1, MEF2C, EZH2, SIK3 and PBX3 - transcripts important in KMT2A-r but less so in KMT2A-WT cells.
- RNA-binding proteins are becoming druggable: RBM39 degradation by sulfonamides and an allosteric PTBP1-RNA peptide inhibitor are cited as precedents.

## Limitations

The mechanism is diffuse by the authors' own account - no single downstream target reproduces the phenotype, so the causal chain from PTBP1 loss to growth arrest is argued from aggregate effects rather than demonstrated. The claim that mis-splicing generates 'defective protein products detrimental to cell growth' is proposed rather than shown at protein level. Most work is in cell lines; the comparison with myelopoiesis establishes dispensability in normal differentiation but is not a full toxicity assessment. PTBP1 also associates with chromatin, and the authors note they cannot yet say whether that is causal or correlative in AML. No inhibitor with cellular activity exists - the peptide cited 'requires further optimization' - so the target remains hypothetical therapeutically.

## Provenance

Located in the published literature, dropped into `inbox/` as `Cao(2026) Leukemia; PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-026-03098-8`; the prose sections were written here from the paper itself.

## Citation

Cao et al. Leukemia 2026. PTBP1 controls oncogenic transcript processing and maintenance of acute myeloid leukemia. doi: 10.1038/s41375-026-03098-8

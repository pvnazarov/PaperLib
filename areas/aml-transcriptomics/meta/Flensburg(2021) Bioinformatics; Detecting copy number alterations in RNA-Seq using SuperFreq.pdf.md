---
# --- identity ------------------------------------------------
id: 2021-01-01_flensburg-2021-bioinformatics-detecting
id_basis: filename-year
source: Flensburg(2021) Bioinformatics; Detecting copy number alterations in RNA-Seq using SuperFreq.pdf
sha256: 16bad3ddd54304a6925816758a27b5b665b0edcf8834b29ba466f3aac2666bfd
size_bytes: 2001963
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 78731

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btab440"
year: 2021
title: "Detecting copy number alterations in RNA-Seq using SuperFreq"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Flensburg(2021) Bioinformatics; Detecting copy number alterations in RNA-Seq using SuperFreq.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

SuperFreq is adapted to call absolute and allele-sensitive copy number alterations from RNA-seq, using an error-propagation framework to combine read counts and B-allele frequencies. Assessed against TCGA DNA SNP-arrays, it agreed for over 98% of the genome in AML (n = 116) and 87% in colorectal cancer (n = 377) when ploidy estimates were consistent. Sensitivity depended on gene density: 78% of CNA calls covering 100 or more genes were detected at 94% precision, with recall dropping for focal events - all 7 high-level ERBB2 amplifications were found but only 1 of 17 moderate IGF2 amplifications. It offers an integrated platform for CNAs and point mutations, and reproduced the known relationship between mutation load and CNA profile in CRC from RNA-seq alone.

## Summary

A tool paper whose value is as much in its honesty about failure modes as in its performance. Copy number from RNA-seq is hard because coverage varies with expression rather than with DNA content, and the paper reports precisely where that breaks: recall is a function of how many genes a segment spans and how strong the signal is, illustrated with a pair of real examples at opposite extremes rather than a single headline number.

For AML specifically the agreement is high - over 98% of the genome - which matters given the argument elsewhere in this collection that RNA-seq should be the single diagnostic assay. Adding copy number to the fusions, variants and expression that RNA-seq already provides closes one of the remaining gaps. The comparison against CNVkit-RNA is informative in both directions, showing opposite precision-recall trade-offs for gains and losses.

## Key points

- Calls absolute and allele-sensitive copy number from RNA-seq by combining read counts with B-allele frequencies under error propagation.
- Over 98% genome agreement with SNP-arrays in TCGA-AML (n = 116) when ploidy estimates concur; 87% in colorectal cancer.
- 78% recall at 94% precision for events spanning 100+ genes; overall precision 86% across all sizes.
- Recall depends on gene density and signal strength - 7/7 high-level ERBB2 amplifications found, 1/17 moderate IGF2 amplifications.
- Integrates CNA and point mutation calling in one platform, and reproduced the mutation-load/CNA relationship in CRC from RNA-seq alone.

## Limitations

The headline agreement is conditional on ploidy estimates matching the SNP-array, and they often do not - for 134 colorectal samples with discordant ploidy, an independent method sided with the array in 63% of cases and with SuperFreq in 31%, so ploidy misestimation is a real and reasonably common failure. Focal events are largely missed, which excludes many clinically important amplifications and deletions. The comparison is against SNP-array calls treated as truth, so errors shared by both are invisible. Performance is characterised on two TCGA cohorts of bulk tumours; single-cell and low-purity samples are not assessed. Detection is intrinsically limited to expressed regions, so copy number in transcriptionally silent parts of the genome is unreachable in principle.

## Provenance

Located in the published literature, dropped into `inbox/` as `Flensburg(2021) Bioinformatics; Detecting copy number alterations in RNA-Seq using SuperFreq.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btab440`; the prose sections were written here from the paper itself.

## Citation

Flensburg et al. Bioinformatics 2021. Detecting copy number alterations in RNA-Seq using SuperFreq. doi: 10.1093/bioinformatics/btab440

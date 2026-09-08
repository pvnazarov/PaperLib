---
# --- identity ------------------------------------------------
id: 2020-01-01_arindrarto-2020-leukemia-comprehensive-d
id_basis: filename-year
source: Arindrarto(2020) Leukemia; Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing.pdf
sha256: e43aa050c99cb5523800defa596bf8b725c145bed975f476d8c1a73a98c3c115
size_bytes: 2470006
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 158002

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-020-0762-8"
year: 2020
title: "Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Arindrarto(2021) Leukemia; Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

HAMLET (Human AML Expedited Transcriptomics), a bioinformatics pipeline that calls fusion genes, small variants, tandem duplications and gene expression from a single whole-transcriptome RNA-seq run, with results assembled into one annotated output file. Applied to 100 AML cases and validated against reference assays and targeted resequencing, it detected all fusion genes and EVI1 overexpression irrespective of 3q26 aberration, called small variants in 13 recurrently mutated genes at 99.2% sensitivity and 100% specificity, and detected FLT3 and KMT2A tandem duplications at 100% sensitivity and 97.1% specificity using a soft-clipped-read algorithm.

## Summary

The argument for RNA-seq as the single diagnostic platform in AML. Diagnosis currently needs karyotyping, FISH, PCR and a sequencing panel because the aberrations are structurally diverse; this shows one assay can carry all of it, including the two things panels handle worst - fusions and tandem duplications.

The genuinely new engineering is the ReSCU tandem-duplication caller built on soft-clipped reads, since FLT3-ITD and KMT2A-PTD are precisely what short-read pipelines miss and precisely what changes treatment. Detecting EVI1 overexpression without regard to whether a 3q26 rearrangement is visible is the other practical win: expression is the prognostic variable, and the cytogenetic proxy for it is incomplete.

## Key points

- One RNA-seq assay replaces several: fusions, small variants, tandem duplications and prognostic expression from a single run.
- Small variants in 13 AML genes called at 99.2% sensitivity and 100% specificity against reference assays.
- FLT3 and KMT2A tandem duplications detected at 100% sensitivity and 97.1% specificity by a soft-clipped-read algorithm.
- EVI1 overexpression is detected directly, independent of whether a 3q26 aberration is seen cytogenetically.
- Output is a single annotated file intended for a diagnostic laboratory, not a research pipeline requiring interpretation.

## Limitations

Validated on 100 cryopreserved samples from one biobank at a single centre, so performance on fresh diagnostic material, other library preparations and other sequencers is untested, and 100% specificity on a cohort this size has wide confidence intervals. Sensitivity is measured against the reference assays, which means variants those assays also miss cannot be counted as false negatives - the denominator is what current diagnostics already find. Restricted to 13 genes for small variants rather than being genuinely comprehensive. Germline DNA is deliberately not sequenced, so germline and somatic variants are not separated. RNA-seq cannot see aberrations in genes that are not transcribed or transcripts destroyed by nonsense-mediated decay, and the 97.1% tandem-duplication specificity means false positives on a class of call that directs targeted therapy.

## Provenance

Located in the published literature, dropped into `inbox/` as `Arindrarto(2021) Leukemia; Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-020-0762-8`; the prose sections were written here from the paper itself.

## Citation

Arindrarto et al. Leukemia 2020. Comprehensive diagnostics of acute myeloid leukemia by whole transcriptome RNA sequencing. doi: 10.1038/s41375-020-0762-8

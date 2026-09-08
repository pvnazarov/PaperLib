---
# --- identity ------------------------------------------------
id: 2021-01-01_rejeski-2021-oncogene-aml1-eto-and-its-f
id_basis: filename-year
source: Rejeski(2021) Oncogene; AML1 ETO and its function as a regulator of gene transcription via epigenetic mechanisms.pdf
sha256: e7f0d88d8def2dff8607d729946ee750b50f59a8af1bf3ffa38cdba856084a9c
size_bytes: 1449366
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 99616

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41388-021-01952-w"
year: 2021
title: "AML1/ETO and its function as a regulator of gene transcription via epigenetic mechanisms"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Rejeski(2021) Oncogene; AML1 ETO and its function as a regulator of gene transcription via epigenetic mechanisms.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of AML1/ETO in t(8;21) leukemogenesis, focused on aberrant epigenetic regulation of transcription. It covers how genomic breakpoints, splice variants and post-translational modifications shape protein function; how the oncofusion recruits chromatin-modifying enzymes and alters chromatin marks, transcription factor binding and gene expression; the impact of these changes on leukemic growth; the genetic landscape of cooperating mutations in KIT, FLT3, NRAS, ASXL1 and ASXL2; and how the resulting transcriptional alterations create vulnerabilities exploitable by epigenetically active agents.

## Summary

A synthesis of the t(8;21) mechanistic literature that this collection samples heavily in primary form. Its most useful function is as a map of which chromatin marks the fusion moves and where - H3K27me3 and acetylated H4 redistributed at IL-3, chromatin modifications at LAT2, and genome-wide changes in H3, H3K9 and H4 acetylation and in H3K4, H3K9 and H3K27 methylation - with a table of the profiling studies behind each claim.

It also states the clinical framing correctly. t(8;21) is core-binding factor AML with better outcomes than most subtypes and cure rates above 60% in patients under 60, so the unmet need is relapse rather than initial response - which is why the preleukemic and stem-cell-directed work elsewhere in this collection matters more here than in adverse-risk disease. The point that AML1/ETO's chromatin landscape differs from that of RUNX1-EVI1, another RUNX1 fusion, is the Loke result summarised.

## Key points

- Systematic account of how AML1/ETO recruits chromatin-modifying enzymes and alters specific histone marks, locally and genome-wide.
- Structural variation - breakpoints, splice variants, post-translational modification - shapes fusion protein function.
- Cooperating mutations in KIT, FLT3, KRAS/NRAS, ASXL1 and ASXL2 define the genetic landscape of the entity.
- ETS factors ERG and FLI1 guide genome-wide binding of AML1/ETO, and its binding to ERG sites decreases acetylation.
- t(8;21) has cure rates above 60% in younger patients, so the therapeutic problem is relapse rather than primary refractoriness.

## Limitations

A narrative review from 2021 with no systematic search or evidence appraisal, so coverage reflects the authors' selection and predates several primary papers in this collection. It synthesises across cell lines, mouse models and primary blasts without consistently distinguishing the strength of evidence behind each mechanistic claim. The therapeutic section surveys rationales for epigenetically active agents rather than clinical results, and the agents discussed - HDAC and DNMT inhibitors in particular - have a long record of preclinical promise and clinical disappointment in AML. Some of the mark-level findings cited come from single studies in single systems.

## Provenance

Located in the published literature, dropped into `inbox/` as `Rejeski(2021) Oncogene; AML1 ETO and its function as a regulator of gene transcription via epigenetic mechanisms.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41388-021-01952-w`; the prose sections were written here from the paper itself.

## Citation

Rejeski et al. Oncogene 2021. AML1/ETO and its function as a regulator of gene transcription via epigenetic mechanisms. doi: 10.1038/s41388-021-01952-w

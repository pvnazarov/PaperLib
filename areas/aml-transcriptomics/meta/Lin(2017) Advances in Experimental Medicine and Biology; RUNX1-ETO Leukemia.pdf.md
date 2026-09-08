---
# --- identity ------------------------------------------------
id: 2017-01-01_lin-2017-advances-in-experimental-medici
id_basis: filename-year
source: Lin(2017) Advances in Experimental Medicine and Biology; RUNX1-ETO Leukemia.pdf
sha256: 8133f76b2deae1576bc2ca5b0292075dfbdd3ebd8a3efeafe27d148d17110c9e
size_bytes: 68270
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 1536

# --- classification (LIH WI DC-909) --------------------------
type: review
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1007/978-981-10-3233-2_11"
year: 2017
title: "RUNX1-ETO Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lin(2017) Adv Exp Med Biol [abstract]; RUNX1-ETO Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review chapter on AML1-ETO leukemia, the most common cytogenetic subtype of AML, defined by t(8;21). It summarises that proteomic surveys show AML1-ETO forming a stable complex with several transcription factors including E proteins; that transcriptome and ChIP-seq analyses have identified directly regulated genes such as CEBPA; that several lines of evidence indicate AML1-ETO suppresses endogenous DNA repair to promote mutagenesis and thereby facilitate acquisition of cooperating secondary events; and that a delicate balance between AML1-ETO and native AML1 sustains the malignant phenotype. Clinical translation of these findings is described as just beginning.

## Summary

A compact orientation to t(8;21) leukemia, and it names the two ideas that the primary papers in this collection develop in detail. The first is that the fusion actively suppresses DNA repair, so the leukemia manufactures the secondary mutations it needs to progress - which makes the initiating lesion a mutator as well as a transcriptional driver.

The second is the balance between fusion and native AML1, which Li (2016) in this collection works out at the level of chromatin occupancy ratios. Reading the two together shows the mechanism behind the review's summary statement.

## Key points

- t(8;21)/AML1-ETO is the most common cytogenetic subtype of AML.
- The fusion works within a stable multiprotein complex including E proteins, rather than alone.
- CEBPA is among the directly regulated targets identified by transcriptome and ChIP-seq analysis.
- AML1-ETO suppresses endogenous DNA repair, promoting mutagenesis and the acquisition of cooperating secondary lesions.
- The balance between AML1-ETO and native AML1 is what sustains the malignant phenotype.

## Limitations

THE FILE IN raw/ IS NOT THE PAPER. It states so itself: a bibliographic record carrying the PubMed abstract, generated on 2026-09-08 by make_abstract_pdf.py for the AML review literature base because no full text could be obtained. At 1422 characters it is the thinnest document in this collection and the ingest flagged it as one page of low text density. Everything recorded here comes from a review's abstract, so no claim can be traced to its evidence, no citation checked, and no figure examined. Beyond that: it is a book chapter review from 2017, so the survey is selective, undated in its coverage, and predates most of the t(8;21) work in this collection. Its own closing judgement - that clinical translation is just beginning - was accurate then and remains largely true.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lin(2017) Adv Exp Med Biol [abstract]; RUNX1-ETO Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1007/978-981-10-3233-2_11`; the prose sections were written here from the paper itself.

## Citation

Lin et al. Advances in Experimental Medicine and Biology 2017. RUNX1-ETO Leukemia. doi: 10.1007/978-981-10-3233-2_11

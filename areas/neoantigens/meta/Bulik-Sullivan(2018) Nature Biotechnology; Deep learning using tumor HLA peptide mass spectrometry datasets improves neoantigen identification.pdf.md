---
# --- identity ------------------------------------------------
id: 2018-01-01_bulik-sullivan-2018-nature-biotechnology
id_basis: filename-year
source: Bulik-Sullivan(2018) Nature Biotechnology; Deep learning using tumor HLA peptide mass spectrometry datasets improves neoantigen identification.pdf
sha256: df75df0550dae79bf8c579c399482d971d22baf086f81892f43182e519c090ca
size_bytes: 1262556
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 170847

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nbt.4313"
year: 2018
title: "Deep learning using tumor HLA peptide mass spectrometry datasets improves neoantigen identification"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nbt.4313.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

EDGE applies deep learning to a large HLA peptide and transcriptome dataset from 74 patients to predict neoantigen presentation, improving on binding-affinity prediction. The stated aim is to remove the need for invasive specimens, screening of thousands of synthetic peptides or tandem minigenes, and HLA-allele-restricted multimer reagents.

## Summary

The clinical argument is about what a method demands of the patient, not only about accuracy. Existing routes to neoantigen-reactive T cells needed TILs or leukapheresis, impractically large peptide libraries, or MHC multimers available for few alleles; a sufficiently specific prediction from sequencing data alone sidesteps all three.

Training on tumour mass spectrometry rather than binding assays is what buys the specificity, and the paper is one of the earliest at this scale to make that case with patient data.

## Key points

- Trained on tumour HLA peptide MS plus transcriptome from 74 patients, not on synthetic binding assays.
- Motivated by removing three practical barriers: invasive specimens, huge peptide libraries, and allele-limited multimers.
- Peptides scoring high with weak predicted binding were observed - direct evidence that presentation is not reducible to affinity.
- Outperformed binding-affinity prediction on cysteine-containing epitopes (3 of 7 in the top five, versus 0-1) despite MS's known difficulty detecting them.

## Limitations

The cysteine result cuts both ways: mass spectrometry systematically under-detects cysteine-containing peptides, so the training data are biased against exactly the epitopes the model is credited with ranking well. Seventy-four patients is large for immunopeptidomics and small for a deep model. This predicts presentation; immunogenicity remains a further step the paper does not close.

## Provenance

Located in the published literature, dropped into `inbox/` as `nbt.4313.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nbt.4313`; the prose sections were written here from the paper itself.

## Citation

Bulik-Sullivan et al. Nature Biotechnology 2018. Deep learning using tumor HLA peptide mass spectrometry datasets improves neoantigen identification. doi: 10.1038/nbt.4313

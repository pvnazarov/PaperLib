---
# --- identity ------------------------------------------------
id: 2020-01-01_o-donnell-2020-cell-systems-mhcflurry-2
id_basis: filename-year
source: O’Donnell(2020) Cell Systems; MHCflurry 2.0 Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by Incorporating Antigen Processing.pdf
sha256: 4deec32d345088a37420e788fd56f1bd5529478c2ba2edf60086b062db21cada
size_bytes: 3096539
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 91532

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cels.2020.06.010"
year: 2020
title: "MHCflurry 2.0: Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by Incorporating Antigen Processing"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS2405471220302398.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

MHCflurry 2.0 trains separate predictors for MHC class I binding and for antigen processing, the latter on mass-spectrometry-identified MHC ligands, and combines them into a presentation predictor that outperforms existing methods. It is an open-source Python package with command-line and library interfaces.

## Summary

The architectural choice is to keep binding and processing as separate trained models and compose them, rather than learning presentation end to end. That makes each component's contribution inspectable and lets the binding model be used alone where that is what is wanted.

The antigen processing predictor learns signals about how a peptide came to exist - flanking sequence, cleavage context - that binding affinity cannot represent, which is what closes part of the gap between predicted binders and observed ligands.

## Key points

- Separate binding and antigen-processing predictors, composed rather than fused - each remains usable and inspectable alone.
- The processing model is trained on MS-identified ligands with their flanking context.
- Open source with both CLI and library interfaces, widely used as a component in other pipelines.
- Pan-allele, so alleles without their own training data are covered.

## Limitations

The authors state the important caveat directly: MS-detected ligand datasets are used both to train and to benchmark, so assay biases - which they expect the processing predictor to model - may erroneously inflate accuracy scores. They checked the best-known bias, cysteine depletion, and found no dramatic effect, but explicitly cannot rule out other biases. They also note that a detailed deconvolution of what the processing predictor learned remains future work.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS2405471220302398.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cels.2020.06.010`; the prose sections were written here from the paper itself.

## Citation

O’Donnell et al. Cell Systems 2020. MHCflurry 2.0: Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by Incorporating Antigen Processing. doi: 10.1016/j.cels.2020.06.010

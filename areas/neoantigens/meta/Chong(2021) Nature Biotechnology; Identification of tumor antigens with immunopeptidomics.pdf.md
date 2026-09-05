---
# --- identity ------------------------------------------------
id: 2021-01-01_chong-2021-nature-biotechnology-identifi
id_basis: filename-year
source: Chong(2021) Nature Biotechnology; Identification of tumor antigens with immunopeptidomics.pdf
sha256: f911d410ad5fb629607dd4f6ddc76646368415b7f1886d80adb896c259272c2d
size_bytes: 1505530
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 127984

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41587-021-01038-8"
year: 2021
title: "Identification of tumor antigens with immunopeptidomics"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41587-021-01038-8.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review of mass-spectrometry immunopeptidomics for tumour antigen discovery, covering canonical antigens from protein-coding regions and, increasingly, noncanonical antigens arising from outside coding sequence or from noncanonical processing. Combined with transcriptomics and ribosome profiling it can identify thousands of noncanonical peptides, a substantial fraction detectable only in tumours.

## Summary

The review is careful about a specific statistical hazard: searching spectra against an immense noncanonical reference database inflates the false positive rate, because the search space grows far faster than the true signal.

It also names a subtler problem in the personalised case - reference databases used to detect predicted altered peptides are usually not fully personalised, since single-nucleotide polymorphisms are typically not included, so a patient's own germline variation can be mistaken for tumour-specific signal or hide it.

## Key points

- Distinguishes canonical antigens from noncanonical ones arising outside ORFs or from noncanonical processing.
- Noncanonical antigens substantially expand the target space, especially for tumours with few mutations.
- Spectral matching against a large noncanonical reference generates false positives - a scale problem, not a technique problem.
- Reference databases are usually not personalised for SNPs, which confounds tumour-specificity claims.

## Limitations

A review: every quantitative claim belongs to a cited study and must be traced there. It surveys a fast-moving field as of 2021 and the noncanonical discovery methods it describes have since moved on. It sets out challenges without resolving them, and the central one - controlling false positives when the search space is enormous - remains open.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41587-021-01038-8.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41587-021-01038-8`; the prose sections were written here from the paper itself.

## Citation

Chong et al. Nature Biotechnology 2021. Identification of tumor antigens with immunopeptidomics. doi: 10.1038/s41587-021-01038-8

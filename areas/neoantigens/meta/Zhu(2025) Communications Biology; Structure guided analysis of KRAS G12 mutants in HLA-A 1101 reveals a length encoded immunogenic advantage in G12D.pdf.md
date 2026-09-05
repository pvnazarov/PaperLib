---
# --- identity ------------------------------------------------
id: 2025-01-01_zhu-2025-communications-biology-structur
id_basis: filename-year
source: Zhu(2025) Communications Biology; Structure guided analysis of KRAS G12 mutants in HLA-A 1101 reveals a length encoded immunogenic advantage in G12D.pdf
sha256: 75d6475f9c180e06372a68438d848832b66ceab307d57a17510f1b2fe7769cac
size_bytes: 4129236
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 88346

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s42003-025-09285-0"
year: 2025
title: "Structure guided analysis of KRAS G12 mutants in HLA-A*11:01 reveals a length encoded immunogenic advantage in G12D"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s42003-025-09285-0.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Structural, biophysical and functional analysis of KRAS G12 variants presented by HLA-A*11:01 shows that single substitutions at position 12 induce distinct conformational changes in the MHC groove, with G12D uniquely destabilising the complex through a buried aspartate. G12D peptides adopt both 9-mer and 10-mer registers that differ sharply in structure and immunogenicity.

## Summary

KRAS G12 mutations are among the most common oncogenic drivers and are shared across patients, which makes them the most attractive targets in the whole field - so why the variants differ in immunogenicity is a question with direct therapeutic consequences.

The register result is the striking part: the same mutation yields two peptides of different length from the same sequence, and only the 10-mer forms a compact, stable complex with a TCR-accessible surface. Immunogenicity is decided by which register is presented, something no sequence-level feature represents.

## Key points

- Explains differential immunogenicity among KRAS G12 variants, the field's most attractive shared targets.
- G12D uniquely destabilises the pMHC complex through a buried aspartate side chain.
- The same G12D sequence yields 9-mer and 10-mer registers with sharply different structure and immunogenicity.
- Register choice, not sequence, decides the outcome - invisible to sequence-based prediction.

## Limitations

One HLA allele (HLA-A*11:01) and one mutation hotspot: the register effect is demonstrated here and its generality is unknown. Structural and biophysical work on purified complexes does not establish what registers are actually presented on a patient's tumour. It explains a difference in immunogenicity without providing a way to predict register choice for other peptides.

## Provenance

Located in the published literature, dropped into `inbox/` as `s42003-025-09285-0.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s42003-025-09285-0`; the prose sections were written here from the paper itself.

## Citation

Zhu et al. Communications Biology 2025. Structure guided analysis of KRAS G12 mutants in HLA-A*11:01 reveals a length encoded immunogenic advantage in G12D. doi: 10.1038/s42003-025-09285-0

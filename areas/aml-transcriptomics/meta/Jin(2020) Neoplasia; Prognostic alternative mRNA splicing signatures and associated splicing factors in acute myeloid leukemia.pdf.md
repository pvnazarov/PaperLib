---
# --- identity ------------------------------------------------
id: 2020-01-01_jin-2020-neoplasia-prognostic-alternativ
id_basis: filename-year
source: Jin(2020) Neoplasia; Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia.pdf
sha256: 143b4ab02d40e51ec8bf8cd76f49bed9e3e255f0eb6d3b740f5fbe1376a583c0
size_bytes: 1646640
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 229553

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.neo.2020.06.004"
year: 2020
title: "Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Jin(2020) Neoplasia; Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using three AML patient datasets, the authors define the landscape of alternative splicing events and identify 7033 associated with survival, from which they build a 15-event prognostic signature that is independent of cytogenetic risk and age and outperforms known gene expression signatures. The signature markedly improves European LeukemiaNet risk classification. A splicing-regulatory network correlates prognostic splicing events with splicing factors, and CRISPR data support the finding that increased RBM39 expression drives higher SETD5 exon inclusion and confers poor outcome.

## Summary

The argument is that existing expression-based risk models discard a real biological layer, since roughly 95% of multi-exon human genes are alternatively spliced and the isoform, not just the gene level, carries information. Building a prognostic signature from splicing events rather than expression is a direct test of that, and it improves on the ELN classification.

The RBM39-SETD5 link is the part that goes beyond correlation. Rather than leaving 15 events as a statistical signature, the authors connect one to a specific splicing factor and validate the direction with CRISPR knockout data - RBM39 loss lowers SETD5 exon inclusion. RBM39 is also independently interesting because it is degradable by sulfonamides, which makes the association actionable rather than merely descriptive.

## Key points

- 7033 survival-associated alternative splicing events identified across three AML datasets.
- A 15-event signature is independent of cytogenetic risk and age and outperforms known expression signatures.
- The signature improves ELN risk classification, the practical claim of the paper.
- A splicing-regulatory network links prognostic events to their splicing factors.
- RBM39 drives SETD5 exon inclusion, validated with CRISPR data, and associates with poor outcome.

## Limitations

A retrospective computational study on public datasets: the signature is derived and evaluated in the same body of data, with no prospective or independently collected validation cohort, and 15 events selected from 7033 candidates in cohorts of this size is a setting where overfitting is the default expectation rather than a remote risk. Percent-spliced-in estimates from short-read RNA-seq are noisy and sensitive to coverage and to blast content, which is a practical obstacle to using them as a clinical assay. The regulatory network is co-expression-based, so most splicing factor-event links are correlational; only RBM39-SETD5 is supported by perturbation, and that from re-used CRISPR screen data rather than a targeted experiment. No functional consequence of the SETD5 isoform is established, so the mechanism connecting it to outcome is unknown.

## Provenance

Located in the published literature, dropped into `inbox/` as `Jin(2020) Neoplasia; Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.neo.2020.06.004`; the prose sections were written here from the paper itself.

## Citation

Jin et al. Neoplasia 2020. Prognostic alternative mRNA splicing signatures and associated splicing factors in acute myeloid leukemia. doi: 10.1016/j.neo.2020.06.004

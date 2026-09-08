---
# --- identity ------------------------------------------------
id: 2019-01-01_petti-2019-nature-communications-a-gener
id_basis: filename-year
source: Petti(2019) Nature Communications; A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing.pdf
sha256: dc6252d66dffa63b3605a36226b22d7e3b2538c9316fa6ae24844b52b5d3e210
size_bytes: 6002526
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 184935

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-019-11591-1"
year: 2019
title: "A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Petti(2019) Nat Commun; A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An approach integrating enhanced whole genome sequencing with single-cell RNA sequencing to detect expressed mutations in individual cells. Applied to five cryopreserved AML samples, it identified hundreds to thousands of cells carrying tumour-specific mutations in each case, allowing AML cells - including normal-karyotype AML cells - to be distinguished from normal cells, expression signatures to be associated with subclonal mutations, and cell surface markers to be identified for purifying subclones. The cases averaged 26 coding mutations, with subclones inferred by SciClone, and at least one subclone identified in every case.

## Summary

Addresses the central weakness of single-cell transcriptomics in cancer: expression alone cannot tell a malignant cell from a normal one. The authors make the point sharply - AML cells often mimic more differentiated normal cells, and some display lineage infidelity, resembling cell types from other lineages including T cells. Those cells are invisible to classification by expression signature and are recovered only when genotype is read from the same cell.

The practical output is the surface markers. Once subclones are genotypically defined and their expression profiles known, markers can be chosen to sort them for functional study - which is what makes subclonal biology testable rather than only observable. The method is presented as applicable to any tumour without modification.

## Key points

- Combines enhanced whole genome sequencing with single-cell RNA-seq to read mutations and expression from the same cells.
- Expression alone cannot identify malignant cells, because AML cells mimic differentiated normal cells and show lineage infidelity.
- Works for normal-karyotype AML, where no cytogenetic marker distinguishes tumour from normal.
- Associates expression signatures with specific subclonal mutations, and identifies surface markers for purifying subclones.
- Separates the sources of transcriptional heterogeneity - differentiation state, cell cycle, subclonal genotype and stochastic variation.

## Limitations

Five samples, so this is a methods demonstration rather than a study of AML biology. Detection depends entirely on a mutation being expressed and captured, and 5' scRNA-seq covers only a small part of each transcript, so most cells will carry mutations that go undetected - the method assigns genotype to the subset of cells where a mutant read happens to be sampled, which biases toward highly expressed genes and against low-coverage cells. Allelic dropout means absence of a mutant read is not evidence of wild-type status. Subclonal structure is inferred from bulk sequencing by SciClone and then mapped onto cells, so the clonal framework is not itself derived at single-cell resolution. Cryopreserved samples may not represent all cell populations equally. Two authors were employed by 10x Genomics, whose platform the method depends on.

## Provenance

Located in the published literature, dropped into `inbox/` as `Petti(2019) Nat Commun; A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-019-11591-1`; the prose sections were written here from the paper itself.

## Citation

Petti et al. Nature Communications 2019. A general approach for detecting expressed mutations in AML cells using single cell RNA-sequencing. doi: 10.1038/s41467-019-11591-1

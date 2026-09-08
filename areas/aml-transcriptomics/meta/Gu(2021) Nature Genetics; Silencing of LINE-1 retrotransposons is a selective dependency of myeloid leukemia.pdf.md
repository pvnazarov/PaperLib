---
# --- identity ------------------------------------------------
id: 2021-01-01_gu-2021-nature-genetics-silencing-of-lin
id_basis: filename-year
source: Gu(2021) Nature Genetics; Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia.pdf
sha256: 0dc1c3b0c9e70a1621cf052c0e37fbe4fa93c815f277615b6dbcc435cd86f2ef
size_bytes: 9930165
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 826266

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41588-021-00829-8"
year: 2021
title: "Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Gu(2021) Nat Genet; Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An epigenetic regulator-focused CRISPR screen identifies MPHOSPH8/MPP8, a component of the human silencing hub (HUSH) complex, as an AML-selective dependency. MPP8 is dispensable for steady-state hematopoiesis, but its loss inhibits AML development by reactivating LINE-1 retrotransposons, inducing a DNA damage response and cell cycle exit. Activating endogenous or ectopic L1s mimics MPP8 loss, while blocking retrotransposition abrogates the phenotype. AML oncogenic mutations promote L1 suppression, and enhanced L1 silencing is associated with poor prognosis in human AML - so retrotransposons act here as tumour suppressors rather than cancer promoters.

## Summary

An inversion of the usual account. Retrotransposons are generally cast as agents of genome instability that help cancer along; here their activity is what the leukemia cannot tolerate, and the cell must spend effort silencing them. That reframing is supported from both directions - removing the silencer and adding L1 activity produce the same phenotype, and blocking retrotransposition rescues it - which is the control that makes the mechanism rather than merely the correlation.

The therapeutic shape is attractive because the dependency is selective: MPP8 is dispensable for steady-state hematopoiesis. The orthogonal validation is unusually thorough for a claim about L1s, which are notoriously hard to manipulate given 500,000 copies of varying integrity - reporter assays, CRISPRa activation, transgenic L1-EGFP mice and pharmacological inhibition of retrotransposition are all used.

## Key points

- MPP8, a HUSH complex component, is an AML-selective dependency identified by chromatin-focused CRISPR screening.
- MPP8 loss reactivates LINE-1 retrotransposons, triggering DNA damage response and cell cycle exit in AML cells.
- L1 activation mimics MPP8 loss and blocking retrotransposition rescues it, establishing causation in both directions.
- MPP8 is dispensable for steady-state hematopoiesis, giving a therapeutic window.
- AML oncogenic mutations promote L1 suppression, and stronger L1 silencing associates with poor prognosis - a tumour-suppressive role for retrotransposons.

## Limitations

No selective HUSH or MPP8 inhibitor exists; the authors state that more specific agents for HUSH inhibition or L1 modulation are needed before translation, so the therapeutic proposal is genetic. Quantifying L1 activity remains difficult because of copy number and sequence variability, and the assays used measure reporter retrotransposition or aggregate expression rather than genuine endogenous insertion events at scale. Dispensability for steady-state hematopoiesis does not establish safety under stress, when normal HSCs are proliferating. The prognostic association between L1 silencing and outcome is correlative in human cohorts. Whether reactivating L1s might itself be mutagenic in surviving cells - the conventional worry about retrotransposons - is not addressed as a therapeutic risk.

## Provenance

Located in the published literature, dropped into `inbox/` as `Gu(2021) Nat Genet; Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41588-021-00829-8`; the prose sections were written here from the paper itself.

## Citation

Gu et al. Nature Genetics 2021. Silencing of LINE-1 retrotransposons is a selective dependency of myeloid leukemia. doi: 10.1038/s41588-021-00829-8

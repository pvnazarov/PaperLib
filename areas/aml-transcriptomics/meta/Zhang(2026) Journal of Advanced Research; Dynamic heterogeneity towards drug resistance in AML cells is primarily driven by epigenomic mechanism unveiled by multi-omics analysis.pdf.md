---
# --- identity ------------------------------------------------
id: 2026-01-01_zhang-2026-journal-of-advanced-research
id_basis: filename-year
source: Zhang(2026) Journal of Advanced Research; Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis.pdf
sha256: 56e176f8adf91f1d9cec6e4313651b99d3a5cdaed795297e4590f0df2b9ab0de
size_bytes: 3518249
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 114796

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.jare.2025.05.038"
year: 2026
title: "Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zhang(2026) J Adv Res; Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A multi-omics approach integrating single-cell RNA sequencing, chromatin accessibility profiling, DNA methylation analysis and whole-exome sequencing was applied to AML cell lines (KG-1a, Kasumi-1, HL-60) treated with standard chemotherapeutics. Drug exposure induced a transition to stem-like states; cytarabine-resistant KG-1a cells predominantly originated from G2/M phase subpopulations, indicating cell-cycle-specific mechanisms; and rapid acquisition of drug resistance was driven primarily by epigenomic regulation of the transcriptome, with minimal contribution from genetic mutations.

## Summary

Tests the genetic and non-genetic accounts of resistance against each other in the same experiment, which most studies do not, by profiling mutations, methylation, accessibility and expression in parallel. The answer is that resistance acquired rapidly is epigenomic, with negligible mutational contribution - supporting the chemotherapy-induced cellular plasticity model over clonal selection.

The cell cycle observation is the more specific finding: cytarabine-resistant KG-1a cells arise predominantly from G2/M subpopulations, so the resistant population has a defined origin within the cycle rather than being a random survivor. The authors also make the reasonable point that this constrains how much can be learned from genomic data alone when studying resistance dynamics.

## Key points

- Genetic and epigenetic mechanisms are assessed in parallel in the same system, allowing their contributions to be compared.
- Rapidly acquired chemotherapy resistance is driven by epigenomic regulation with minimal mutational contribution.
- Drug exposure induces a transition toward stem-like states, consistent with chemotherapy-induced cellular plasticity.
- Cytarabine-resistant KG-1a cells originate predominantly from G2/M phase subpopulations.
- Argues against relying exclusively on genomic data to understand resistance dynamics.

## Limitations

The authors state their design limits directly: the study evaluated four single-agent therapies plus one cytarabine/daunorubicin combination, whereas contemporary AML treatment increasingly uses multi-drug combinations - so the resistance modelled may not correspond to what develops clinically. All work is in three established cell lines, which cannot reproduce the clonal and microenvironmental context in which resistance actually arises, and 'rapidly acquired' resistance in culture over short exposures is a different phenomenon from relapse over months. The conclusion that mutations contribute minimally may partly reflect the short timescale, since selection of pre-existing clones requires time. The therapeutic suggestion of targeting site-specific methylation and chromatin remodelling is not tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zhang(2026) J Adv Res; Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.jare.2025.05.038`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Journal of Advanced Research 2026. Dynamic heterogeneity towards drug resistance in AML cells is primarily driven by epigenomic mechanism unveiled by multi-omics analysis. doi: 10.1016/j.jare.2025.05.038

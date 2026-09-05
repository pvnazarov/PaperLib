---
# --- identity ------------------------------------------------
id: 2026-01-01_zhang-2026-cell-genomics-cross-task-inte
id_basis: filename-year
source: Zhang(2026) Cell Genomics; Cross-task interpretability through unified modeling reveals a universal shortcut bias in neoantigen prediction.pdf
sha256: 45e98268b0f4039ce5c6ce300dde7bf0a15db0492472d5f2fb661e4267091b82
size_bytes: 2851446
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 127202

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.xgen.2026.101214"
year: 2026
title: "Cross-task interpretability through unified modeling reveals a universal shortcut bias in neoantigen prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2026_Zhang_Cell_Genom_Cross_task_interpretability_through_unified_mo_PMID41985452.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ImmUni is a unified framework modelling neoantigen binding, presentation and immunogenicity together, enabling cross-task attention analysis. That analysis shows deep learning models systematically learn shortcuts in immunogenicity prediction rather than immunogenic features, driven by intra-HLA imbalance in training data; a mutual-information-guided debiasing strategy mitigates it.

## Summary

The finding is that immunogenicity models attend abnormally to the HLA rather than to the peptide - they learn which HLA a peptide is paired with as a proxy for the label, because within each HLA the positives and negatives are unbalanced in ways that make this predictive.

The authors checked the obvious alternative explanation and ruled it out: across all models and both benchmarks they found no significant correlation between an HLA's training sample count and its benchmark AUROC, so inter-HLA sample size differences alone do not explain the behaviour. Intra-HLA imbalance does.

## Key points

- Shortcut learning is model-agnostic - it is a property of the datasets, not of any one architecture.
- Intra-HLA imbalance, not inter-HLA sample size, is the cause; the alternative was tested and rejected.
- Without bias control, existing benchmarks do not support fair evaluation - which puts a question mark over reported performance across this whole subfield.
- A mutual-information-guided debiasing strategy is offered as a mitigation.

## Limitations

Debiasing mitigates rather than removes the problem, and the underlying cause - scarce, unevenly collected experimental data shaped by predefined assumptions and narrow designs - is not fixed by any modelling change. The authors cite that only 6% of predicted epitopes were validated as immunogenic in one study, which bounds how much any of this currently delivers. The analysis rests on attention as an interpretability signal, which is indicative rather than definitive.

## Provenance

Located in the published literature, dropped into `inbox/` as `2026_Zhang_Cell_Genom_Cross_task_interpretability_through_unified_mo_PMID41985452.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.xgen.2026.101214`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Cell Genomics 2026. Cross-task interpretability through unified modeling reveals a universal shortcut bias in neoantigen prediction. doi: 10.1016/j.xgen.2026.101214

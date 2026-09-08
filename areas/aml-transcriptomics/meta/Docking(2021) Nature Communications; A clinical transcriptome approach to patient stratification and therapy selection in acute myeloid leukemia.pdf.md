---
# --- identity ------------------------------------------------
id: 2021-01-01_docking-2021-nature-communications-a-cli
id_basis: filename-year
source: Docking(2021) Nature Communications; A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia.pdf
sha256: 25ff14a37aa8ca36cf33c333c11ef3936d9387f54e33f0aeeb21deefc2c697ee
size_bytes: 4014727
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 157556

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-021-22625-y"
year: 2021
title: "A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Docking(2021) Nat Commun; A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A clinical transcriptome-based assay for AML stratification, developed and validated against whole genome and exome sequencing, which shows that standalone RNA-seq gives the greatest diagnostic return - expressed gene fusions, SNVs and short indels, and whole-transcriptome expression together. Expression data from 154 AML patients yield a prognostic score strongly associated with outcome across 620 patients in three independent cohorts and 42 in a prospective cohort. Combined with molecular risk guidelines it re-stratifies 22.1% to 25.3% of patients into correct risk groups, and within the adverse-risk subgroup identifies patients with dysregulated integrin signalling and RUNX1 or TP53 mutation who may benefit from focal adhesion kinase (PTK2) inhibitors.

## Summary

The argument that a single RNA-seq assay should replace the current patchwork of cytogenetics and targeted panels, made with the validation work that claim requires: replicate material, a prospective local cohort, and reanalysis of TCGA, Beat AML and TARGET. The head-to-head against WGS and WES is the part that makes the case, since the obvious objection is that DNA sequencing is more comprehensive.

Re-stratifying about a quarter of patients is a large and clinically consequential number, because risk group determines whether someone is sent to transplant. The FAK inhibitor observation is a second, weaker layer - a therapy hypothesis for RUNX1- and TP53-mutant adverse-risk AML, groups with essentially nothing available - and the authors note pointedly that integrin activation also occurs without those mutations, which is itself an argument for expression-based rather than mutation-based testing.

## Key points

- Standalone RNA-seq outperforms WGS and WES for diagnostic return in AML: fusions, small variants and expression from one assay.
- A prognostic score built on 154 patients validates across 620 patients in three independent cohorts plus a 42-patient prospective cohort.
- Combined with molecular risk guidelines, it re-stratifies 22.1-25.3% of patients - directly relevant to transplant decisions.
- Identifies an adverse-risk subset with dysregulated integrin signalling and RUNX1 or TP53 mutation as candidates for FAK/PTK2 inhibition.
- Integrin and PTK2 activation also occurs without RUNX1 or TP53 mutation, which is an argument for expression-based over mutation-based testing.

## Limitations

The FAK inhibitor proposal is a hypothesis from expression correlation - no functional or clinical demonstration that these patients respond, and the authors call it proof-of-concept. Prognostic score development and validation both draw on retrospective cohorts treated with heterogeneous regimens across eras, so 'correct risk group' is defined by observed outcomes under varying treatment. The prospective cohort is 42 patients. RNA-seq cannot detect variants in untranscribed regions or transcripts destroyed by nonsense-mediated decay, and expression measurement is sensitive to sample handling, blast content and library preparation in ways that cytogenetics is not - a real obstacle to deploying a quantitative score across laboratories. Clinical utility is inferred from re-stratification rather than shown by any trial in which the assay changed treatment.

## Provenance

Located in the published literature, dropped into `inbox/` as `Docking(2021) Nat Commun; A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-021-22625-y`; the prose sections were written here from the paper itself.

## Citation

RoderickDocking et al. Nature Communications 2021. A clinical transcriptome approach to patient stratification and therapy selection in acute myeloid leukemia. doi: 10.1038/s41467-021-22625-y

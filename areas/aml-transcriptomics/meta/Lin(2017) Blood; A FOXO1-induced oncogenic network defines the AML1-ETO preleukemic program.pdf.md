---
# --- identity ------------------------------------------------
id: 2017-01-01_lin-2017-blood-a-foxo1-induced-oncogenic
id_basis: filename-year
source: Lin(2017) Blood; A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program.pdf
sha256: 1be31b5121eb81f9487ed178a5ec85fe6b1087b98b090f01bbf07115f6160870
size_bytes: 1742804
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 114919

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood-2016-11-750976"
year: 2017
title: "A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lin(2017) Blood; A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

FOXO1, generally regarded as a tumour suppressor, is shown to be consistently upregulated in t(8;21) AML and to drive aberrant self-renewal in preleukemic human CD34+ cells expressing AML1-ETO. Expressing FOXO1 in normal CD34+ cells produces a preleukemic state with enhanced self-renewal and dysregulated differentiation, dependent on its DNA binding domain, and activates a stem cell signature also present in AML1-ETO preleukemia cells and preserved in patient samples. AML1-ETO and FOXO1 share the majority of their binding sites, with FOXO1 required to activate multiple self-renewal genes; genetic and pharmacological ablation of FOXO1 inhibited long-term proliferation and clonogenicity of both preleukemic and t(8;21) leukemia cells.

## Summary

A tumour suppressor recast as an oncogene in a specific context, which the authors handle by laying out how contested FOXO biology in AML already is - FOXO3 has been described both as a suppressor whose restoration impairs growth and as a requirement for AML stem cell maintenance.

The target is the preleukemic stem cell, which matters clinically in t(8;21): AML1-ETO-positive cells are detectable long before diagnosis and after complete remission, and roughly half of these otherwise good-prognosis patients relapse. A therapy that eliminated the preleukemic reservoir rather than the bulk disease would address relapse at its source. The genome-wide overlap between AML1-ETO and FOXO1 binding, with FOXO1 required for activation of self-renewal genes, places FOXO1 as an executor of the fusion's program rather than a parallel pathway.

## Key points

- FOXO1, a canonical tumour suppressor, is consistently upregulated in t(8;21) AML and acts oncogenically there.
- Expressing FOXO1 in normal human CD34+ cells partly recapitulates the AML1-ETO preleukemic phenotype and signature.
- AML1-ETO and FOXO1 share the majority of genomic binding sites; FOXO1 is required to activate self-renewal genes.
- The DNA binding domain of FOXO1 is essential for these functions.
- Targets the preleukemic stem cell reservoir, which persists in remission and underlies the ~50% relapse rate in t(8;21) AML.

## Limitations

Preleukemic modelling by transduction of human CD34+ cells produces enhanced self-renewal, not leukemia, so the 'preleukemic program' is defined by phenotype and signature rather than by progression to disease. FOXO1 expression in normal cells only partially recapitulates the AML1-ETO state, which the authors say. Pharmacological ablation uses tool compounds against a transcription factor with no clinical-grade inhibitor, and FOXO1 has essential functions in normal hematopoietic stem cells and lymphocytes, so the therapeutic window is unaddressed. Effects are measured as proliferation and clonogenicity in vitro rather than in vivo leukemia models. The wider FOXO literature in AML is inconsistent, and this paper adds a context-specific result rather than resolving it.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lin(2017) Blood; A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood-2016-11-750976`; the prose sections were written here from the paper itself.

## Citation

Lin et al. Blood 2017. A FOXO1-induced oncogenic network defines the AML1-ETO preleukemic program. doi: 10.1182/blood-2016-11-750976

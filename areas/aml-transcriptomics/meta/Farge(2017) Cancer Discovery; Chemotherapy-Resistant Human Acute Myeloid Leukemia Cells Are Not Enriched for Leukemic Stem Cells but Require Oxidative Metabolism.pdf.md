---
# --- identity ------------------------------------------------
id: 2017-01-01_farge-2017-cancer-discovery-chemotherapy
id_basis: filename-year
source: Farge(2017) Cancer Discovery; Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism.pdf
sha256: 86bec7089efde157dccf2aabe59eb849f468c796a8be1a7d4681d29ec817a4e4
size_bytes: 40514620
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 218201

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-16-0441"
year: 2017
title: "Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Farge(2017) Cancer Discov; Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using a clinically relevant, well-tolerated cytarabine regimen in patient-derived xenografts, the authors show that residual AML cells after treatment are enriched in neither immature nor quiescent cells nor leukemic stem cells, formally assessed by limiting dilution into secondary recipients. Instead, resistant preexisting and persisting cells show high reactive oxygen species, increased mitochondrial mass and active polarised mitochondria consistent with high oxidative phosphorylation, together with increased fatty-acid oxidation and upregulated CD36, and a high OXPHOS gene signature predictive of treatment response in PDX and patients. High-OXPHOS but not low-OXPHOS cell lines were chemoresistant in vivo, and targeting mitochondrial protein synthesis, electron transfer or fatty-acid oxidation shifted cells to low OXPHOS and enhanced cytarabine's effect.

## Summary

The paper that moved the field's explanation of chemoresistance from cell identity to cell metabolism. The standing hypothesis was that residual disease consists of quiescent immature leukemic stem cells; this tests it properly - with a tolerated dose rather than the high doses earlier studies used, and with secondary transplantation to actually count LSCs rather than inferring them from surface markers - and it does not hold.

What is left is a metabolic state: high ROS, more mitochondria, fatty-acid oxidation through CD36, and an OXPHOS signature that predicts response in both models and patients. The therapeutic corollary is tested directly, by three independent routes into mitochondrial function, each of which resensitises cells to cytarabine. Much of the rest of the mitochondrial work in this collection descends from this result.

## Key points

- Cytarabine-residual AML cells are not enriched for immature, quiescent or leukemic stem cells - shown by limiting dilution secondary transplantation, not surface phenotype.
- Residual cells are defined instead by high OXPHOS: raised ROS, increased mitochondrial mass, polarised mitochondria, and fatty-acid oxidation via CD36.
- A high-OXPHOS gene signature predicts cytarabine response in PDX models and in patients.
- High-OXPHOS but not low-OXPHOS human AML cell lines are chemoresistant in vivo.
- Inhibiting mitochondrial protein synthesis, electron transfer or fatty-acid oxidation shifts cells to low OXPHOS and enhances cytarabine's antileukemic effect.

## Limitations

NSG xenografts lack an immune system and a normal marrow niche, and the paper's own discussion notes that hypoxic marrow and spleen niches behave differently - so the metabolic state of residual cells in a patient may not match. Response is measured over days to weeks as tumour burden rather than as long-term relapse or survival. The OXPHOS signature is derived and evaluated on these cohorts rather than validated prospectively. The mitochondrial inhibitors used are preclinical tool compounds, and OXPHOS is essential in normal tissue, so the therapeutic window is not addressed. Metabolic state is measured in cells that survived treatment, which does not by itself establish that the state caused survival, though the cell-line comparison and the resensitisation experiments do address this. The negative claim about LSCs rests on limiting dilution in mice, itself an imperfect assay of human leukemia-initiating capacity.

## Provenance

Located in the published literature, dropped into `inbox/` as `Farge(2017) Cancer Discov; Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-16-0441`; the prose sections were written here from the paper itself.

## Citation

Farge et al. Cancer Discovery 2017. Chemotherapy-Resistant Human Acute Myeloid Leukemia Cells Are Not Enriched for Leukemic Stem Cells but Require Oxidative Metabolism. doi: 10.1158/2159-8290.CD-16-0441

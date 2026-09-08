---
# --- identity ------------------------------------------------
id: 2020-01-01_aroua-2020-cancer-discovery-extracellula
id_basis: filename-year
source: Aroua(2020) Cancer Discovery; Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia.pdf
sha256: e714054ec92b6e96180a6ad159528cb911318ab28cdabd7b7f5c7181e4a2749d
size_bytes: 7262750
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 224730

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-19-1008"
year: 2020
title: "Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Aroua(2020) Cancer Discov; Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The ectonucleotidase CD39 (ENTPD1) is shown to be upregulated in cytarabine-resistant leukemic cells in AML cell lines and patient samples, both in vitro and in vivo. CD39 surface expression and activity rise in patients after chemotherapy compared with diagnosis, and enrichment for CD39-expressing blasts marks adverse prognosis. High CD39 activity promotes cytarabine resistance by driving mitochondrial activity and biogenesis through a cAMP-mediated adaptive mitochondrial stress response, via a P2RY13-cAMP-PKA and ATF4 axis; genetic and pharmacologic inhibition of CD39 ecto-ATPase activity blocks that reprogramming and markedly increases cytarabine cytotoxicity in vitro and in xenografts.

## Summary

A mechanistic account of why the cells that survive induction chemotherapy are metabolically different rather than simply fewer. Extracellular ATP released under chemotherapy is hydrolysed by CD39, which signals through P2RY13 and cAMP to raise oxidative phosphorylation and antioxidant defence - the residual cell buys its survival with mitochondrial capacity.

The practical claim is dual: CD39 is a residual-disease marker measurable by flow cytometry after treatment, and a target whose inhibition resensitises cells to a drug already in universal use. Both shRNA knockdown and the inhibitor POM1 combined with cytarabine reduce burden in cell-line and patient-derived xenografts, which is the part that turns the mechanism into a proposal.

## Key points

- CD39 is upregulated on chemoresistant AML blasts and rises in patients from diagnosis to post-chemotherapy.
- Enrichment for CD39-expressing blasts is associated with adverse prognosis, making it a candidate residual-disease marker.
- The resistance mechanism is an adaptive mitochondrial stress response through P2RY13-cAMP-PKA and ATF4, raising OxPHOS and antioxidant capacity.
- Both genetic knockdown and pharmacologic inhibition (POM1) of CD39 restore cytarabine sensitivity in vitro and in xenografts.
- Fits the wider argument in this collection that chemoresistant AML cells depend on oxidative metabolism rather than on stem-cell identity.

## Limitations

POM1 is a poorly selective ecto-ATPase inhibitor, so the pharmacological arm does not cleanly isolate CD39; the shRNA experiments carry the specificity, and they are done in one cell line (MOLM14). Xenografts in NSG mice lack the immune compartment, which matters unusually much here because CD39's best-known role is immunosuppression through adenosine - a whole arm of the biology this model cannot report on. The prognostic association is drawn from patient cohorts without multivariable adjustment presented alongside established risk factors, so CD39 is not shown to add information beyond them. Response is measured days after treatment with tumour burden and mitochondrial readouts rather than long-term survival in the PDX arm, and no clinical-grade CD39 inhibitor is tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Aroua(2020) Cancer Discov; Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-19-1008`; the prose sections were written here from the paper itself.

## Citation

Aroua et al. Cancer Discovery 2020. Extracellular ATP and CD39 Activate cAMP-Mediated Mitochondrial Stress Response to Promote Cytarabine Resistance in Acute Myeloid Leukemia. doi: 10.1158/2159-8290.CD-19-1008

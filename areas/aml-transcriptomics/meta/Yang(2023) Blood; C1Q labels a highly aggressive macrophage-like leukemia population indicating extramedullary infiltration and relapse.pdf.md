---
# --- identity ------------------------------------------------
id: 2023-01-01_yang-2023-blood-c1q-labels-a-highly-aggr
id_basis: filename-year
source: Yang(2023) Blood; C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse.pdf
sha256: f3fca41b714581f3cbb672a39a772c9184255253b45d57960fe9954362a80f73
size_bytes: 12082399
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 304354

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2022017046"
year: 2023
title: "C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yang(2023) Blood; C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Single-cell RNA sequencing of bone marrow and extramedullary infiltration samples from an AML patient with pervasive leukemia cutis identified a complement C1Q-positive macrophage-like leukemia subset, enriched in skin and present in marrow before extramedullary manifestations, then verified in multiple patients. C1Q expression, modulated by the transcription factor MAFB, conferred tissue infiltration ability sufficient to establish cutaneous and gastrointestinal nodules in xenograft models, and was independently associated with adverse prognosis. Fibroblasts attracted C1Q+ leukemia cells through C1Q-gC1QR recognition and subsequent TGF-beta1 stimulation, which also supported survival of these cells under chemotherapy stress.

## Summary

Starts from one extreme case and generalises, which the authors defend explicitly: patients with extreme manifestations, though rare and unrepresentative, can reveal biomarkers linked to a phenotype that would be invisible in averaged cohorts. Extramedullary infiltration is poorly understood and has few therapeutic options, so a mechanism is worth having.

The most clinically useful observation is that C1Q+ cells were present in marrow before any extramedullary manifestation appeared, which makes C1Q a candidate predictive marker rather than only a descriptive one. The mechanism is a specific cell-to-cell interaction - fibroblasts attracting leukemia cells through gC1QR recognition of C1Q's globular domain and TGF-beta1 induction - and the differential expression of surface gC1QR explains why fibroblasts but not epithelial cells attract these cells.

## Key points

- A C1Q+ macrophage-like leukemia subset drives extramedullary infiltration, identified by single-cell sequencing of paired marrow and skin.
- C1Q+ cells are present in marrow before extramedullary disease appears, making C1Q a candidate predictive marker.
- MAFB modulates C1Q expression; its depletion reduces C1Q and abolishes nodule formation in xenografts.
- Fibroblasts attract C1Q+ cells via gC1QR recognition of the C1Q globular domain and TGF-beta1 induction.
- The same interaction supports survival of C1Q+ cells under chemotherapy stress, linking infiltration to resistance.

## Limitations

The discovery rests on a single patient with an extreme presentation, with verification in a limited further cohort - the authors defend this design but it constrains generalisation. They state that how leukemia cells home to particular tissues, and the signalling downstream of C1Q-receptor recognition, still require investigation, and that other mechanisms of extramedullary infiltration need exploring, including trafficking of immune effector cells between marrow and skin. Tissue distribution of chemotherapy drugs is raised as an alternative contributor to extramedullary relapse that this mechanism does not address. In vivo work is in xenograft models using MOLM13 and patient-derived cells. No therapeutic intervention against the axis is tested.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yang(2023) Blood; C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2022017046`; the prose sections were written here from the paper itself.

## Citation

Yang et al. Blood 2023. C1Q labels a highly aggressive macrophage-like leukemia population indicating extramedullary infiltration and relapse. doi: 10.1182/blood.2022017046

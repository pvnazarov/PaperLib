---
# --- identity ------------------------------------------------
id: 2021-01-01_bosc-2021-nature-cancer-mitochondrial-in
id_basis: filename-year
source: Bosc(2021) Nature Cancer; Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia.pdf
sha256: 565e044622bf98de22950942fe1eeac327d4d51f5cda0694fcc98a299c8c837c
size_bytes: 23664881
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 334896

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s43018-021-00264-y"
year: 2021
title: "Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Bosc(2021) Nat Cancer; Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The authors define a 'MitoScore' signature identifying high mitochondrial oxidative phosphorylation in vivo and in patients with AML. Primary AML cells resistant to cytarabine with a high MitoScore depend on mitochondrial BCL2 and are highly sensitive to venetoclax plus cytarabine but not venetoclax plus azacitidine. Single-cell transcriptomics of cells surviving venetoclax + cytarabine shows adaptive resistance involving oxidative phosphorylation, electron transport chain complexes and the TP53 pathway; treating those resistant cells with ETC complex inhibitors, pyruvate dehydrogenase inhibitors or mitochondrial ClpP protease agonists substantially delays relapse.

## Summary

Two clinically actionable claims sit on one mechanism. The first is stratification: the two venetoclax doublets are not interchangeable, and a mitochondrial signature says which one a patient should get - high MitoScore predicts response to venetoclax + cytarabine specifically and not to venetoclax + azacitidine, which is a molecular difference between combinations usually treated as alternatives.

The second is what to do when that fails. Single-cell profiling of the surviving cells shows resistance is again mitochondrial adaptation, so the proposal is sequential: alternate the two doublets, or add a mitochondrial inhibitor. The finding that alternating venetoclax + azacitidine with venetoclax + cytarabine beats two cycles of the former is the concrete scheduling recommendation.

## Key points

- A MitoScore signature identifies high-OxPHOS AML in vivo and in patients, and predicts sensitivity to venetoclax + cytarabine.
- The two venetoclax doublets are mechanistically different: high MitoScore predicts response to VEN + AraC but not VEN + azacitidine.
- Cytarabine-resistant cells depend on mitochondrial BCL2, which is why adding venetoclax works in that setting.
- Residual cells after VEN + AraC show adaptive resistance in OxPHOS, electron transport chain and TP53 pathways by single-cell transcriptomics.
- ETC inhibitors, PDH inhibitors or mitochondrial ClpP agonists delay relapse after VEN + AraC; alternating the two doublets outperforms repeating one.

## Limitations

The stratification claim is built and tested largely on ex vivo primary cells and xenografts, not in a prospective trial, and the MitoScore is derived from these datasets rather than validated in an independent clinical cohort with outcomes. Xenograft 'relapse delay' is a survival endpoint in immunodeficient mice, where the immune contribution to relapse is absent. The mitochondrial inhibitors used - including ClpP agonists and PDH inhibitors - are tool compounds of varying clinical maturity and selectivity, so 'target mitochondrial metabolism' is more established as a principle than as a drug. Single-cell transcriptomics of residual populations describes states that survived, which need not be the states that caused survival. The clinical observation the paper reinterprets - that VEN + AraC underperformed VEN + HMA on overall survival - remains a real result, and better stratification is a hypothesis for why.

## Provenance

Located in the published literature, dropped into `inbox/` as `Bosc(2021) Nat Cancer; Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s43018-021-00264-y`; the prose sections were written here from the paper itself.

## Citation

Bosc et al. Nature Cancer 2021. Mitochondrial inhibitors circumvent adaptive resistance to venetoclax and cytarabine combination therapy in acute myeloid leukemia. doi: 10.1038/s43018-021-00264-y

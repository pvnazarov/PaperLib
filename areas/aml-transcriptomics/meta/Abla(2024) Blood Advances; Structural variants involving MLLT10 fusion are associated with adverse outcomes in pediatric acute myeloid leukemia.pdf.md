---
# --- identity ------------------------------------------------
id: 2024-01-01_abla-2024-blood-advances-structural-vari
id_basis: filename-year
source: Abla(2024) Blood Advances; Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia.pdf
sha256: eda03904dfb881be81c90a7bf3f228e3e29a1c18916853827fcc01e26f76822d
size_bytes: 1583042
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 110075

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/bloodadvances.2023010805"
year: 2024
title: "Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Abla(2024) Blood Adv; Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A retrospective study of 2080 children and young adults on the Children's Oncology Group AAML0531 and AAML1031 trials, using transcriptome profiling and karyotyping to identify MLLT10 fusions and relate them to outcome. 127 patients (6.1%) carried an MLLT10 fusion - 104 KMT2A::MLLT10, 13 PICALM::MLLT10, 10 with other partners - and all fared badly: 5-year event-free survival 18.6% versus 49%, overall survival 38.2% versus 65.7%, relapse risk 76% versus 38.6%.

## Summary

The clinical point is that the partner does not rescue the prognosis. MLLT10 was known to be bad in partnership with KMT2A; this asks whether the other partners behave differently and finds they do not, which turns a set of individually unstudiable rare fusions into one actionable high-risk group.

The molecular half is more interesting than the survival half. PICALM::MLLT10 and the rare X::MLLT10 fusions carry a DNA hypermethylation signature resembling NUP98::NSD1, while KMT2A::MLLT10 acts mainly on distal regulatory elements - so two routes to the same dismal outcome, which matters if the intended therapy is epigenetic. Six new partners are named here from single patients each.

## Key points

- MLLT10 fusions occur in 6.1% of pediatric AML and confer very high risk regardless of the fusion partner.
- PICALM::MLLT10 and X::MLLT10 show DNA hypermethylation resembling NUP98::NSD1; KMT2A::MLLT10 instead perturbs distal regulatory elements.
- Six previously unreported MLLT10 partners (DDX3Y, CEP164, SCN2B, TREH, NAP1L1, XPO1) were each seen in one patient.
- The authors argue both karyotyping and RNA sequencing are needed: neither alone caught every structural alteration.
- A case for prioritising these patients for alternative therapy rather than treatment intensification.

## Limitations

Retrospective, on trials that ran 2006-2016, so the outcomes describe a treatment era rather than current practice. The subgroups that carry the novel biology are tiny - 13 PICALM::MLLT10 and 10 X::MLLT10, several partners represented by a single patient - and the comparisons between fusion partners are frankly not significant (EFS P = .628, OS P = .361, PICALM vs other P = .788), so 'the partner does not matter' is a failure to detect a difference in small groups, not a demonstration of equivalence. The methylation signatures are associations in profiled subsets, with no functional test that either mechanism drives the outcome, and no evidence is offered that any targeted therapy would help.

## Provenance

Located in the published literature, dropped into `inbox/` as `Abla(2024) Blood Adv; Structural variants involving MLLT10 fusion are associated with adverse outcomes in pediatric acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/bloodadvances.2023010805`; the prose sections were written here from the paper itself.

## Citation

Abla et al. Blood Advances 2024. Structural variants involving <i>MLLT10</i> fusion are associated with adverse outcomes in pediatric acute myeloid leukemia. doi: 10.1182/bloodadvances.2023010805

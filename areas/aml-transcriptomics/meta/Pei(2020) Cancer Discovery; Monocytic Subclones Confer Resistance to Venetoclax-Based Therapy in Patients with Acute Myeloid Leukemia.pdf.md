---
# --- identity ------------------------------------------------
id: 2020-01-01_pei-2020-cancer-discovery-monocytic-subc
id_basis: filename-year
source: Pei(2020) Cancer Discovery; Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia.pdf
sha256: d17f2d1f5ddcde51078376c1bad3fc6fb32c387ff6e28d19130b64269a7efdcf
size_bytes: 4556206
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 231248

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-19-0710"
year: 2020
title: "Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Pei(2020) Cancer Discov; Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Responses to venetoclax plus azacitidine correlate closely with developmental stage: phenotypically primitive AML is sensitive while monocytic AML is resistant. Resistant monocytic AML has a distinct transcriptomic profile, loses expression of the venetoclax target BCL2, and relies on MCL1 to mediate oxidative phosphorylation and survival. This differential sensitivity drives selection favouring outgrowth of monocytic subpopulations at relapse. The authors conclude that resistance can arise from biological properties intrinsic to monocytic differentiation, and that AML therapies should be designed to target subclones arising at different developmental stages independently.

## Summary

The explanation that made monocytic AML a recognised venetoclax-resistant category. The mechanism is almost tautological once stated: monocytic cells lose BCL2, so a BCL2 inhibitor has nothing to inhibit, and they run oxidative phosphorylation through MCL1 instead - so both the target and the dependency shift with differentiation state.

The clonal analysis is what makes this clinically important rather than merely descriptive. In one patient two genetically independent subclones each carried their own LSC population and the monocytic one was selected under treatment; in another, primitive and monocytic populations shared a genotype in a parent-progeny relationship, therapy eradicated that clone, and rare genetically distinct monocytic subclones were selected instead. So resistance can be developmental, genetic, or both, and the authors' conclusion - that therapy must target subclones at different developmental stages independently - follows from both cases.

## Key points

- Response to venetoclax plus azacitidine tracks developmental stage: primitive AML sensitive, monocytic AML resistant.
- Monocytic AML loses BCL2 expression and depends on MCL1 to sustain oxidative phosphorylation.
- Cells can switch from BCL2 to MCL1 dependence as they acquire a more differentiated state.
- Primitive and monocytic LSC phenotypes coexist within patients and follow different response trajectories.
- Treatment selects for monocytic subpopulations at relapse, whether they are genetically distinct or developmentally derived.

## Limitations

The detailed clonal analysis rests on two patients presented as case studies, and the authors state that the prevalence of dual-LSC pathogenesis remains to be determined and that further resistance mechanisms will emerge as relapse continues to be characterised. In one of those patients the relapse population had itself changed transcriptionally, acquiring a more stem-like profile, so 'selection of a pre-existing monocytic clone' is an incomplete account even there. Developmental stage is defined immunophenotypically and transcriptomically; other groups in this collection report that monocytic markers do not reliably predict venetoclax response in clinical practice, so the correlation may be less clean at the bedside. MCL1 inhibitors, the implied alternative, have had significant cardiac toxicity in trials.

## Provenance

Located in the published literature, dropped into `inbox/` as `Pei(2020) Cancer Discov; Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-19-0710`; the prose sections were written here from the paper itself.

## Citation

Pei et al. Cancer Discovery 2020. Monocytic Subclones Confer Resistance to Venetoclax-Based Therapy in Patients with Acute Myeloid Leukemia. doi: 10.1158/2159-8290.CD-19-0710

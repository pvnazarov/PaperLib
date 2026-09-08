---
# --- identity ------------------------------------------------
id: 2023-01-01_stelmach-2023-haematologica-leukemic-ste
id_basis: filename-year
source: Stelmach(2023) Haematologica; Leukemic stem cells and therapy resistance in acute myeloid leukemia.pdf
sha256: 4625f9636aae3d5ac177eeb23797e429548b37e9623f59aeea7ec48070602a28
size_bytes: 6972865
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 85783

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3324/haematol.2022.280800"
year: 2023
title: "Leukemic stem cells and therapy resistance in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Stelmach(2023) Haematologica; Leukemic stem cells and therapy resistance in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of leukemic stem cell biology and its relationship to therapy resistance in AML. It presents the cancer stem cell concept in which LSCs sit at the top of each genetically defined subclone forming epigenetically controlled downstream hierarchies, and emphasises their phenotypic and epigenetic plasticity under therapy stress. It argues that targeted strategies must be incorporated into first-line regimens to prevent LSC-mediated relapse, discusses venetoclax plus azacitidine as the current promising approach, and surveys LSC vulnerabilities, current clinical trial activity and the contribution of single-cell multi-omics to characterising relapse-initiating populations.

## Summary

The clearest statement in this collection of the conceptual framework that the primary papers around it test or contest. Its central argument is architectural: genetically diverse LSCs are present at diagnosis, each subclone carrying its own hierarchy, which is why therapies aimed at the dominant clone's properties fail - and why different relapse patterns need different treatments.

It is also honest about what is unresolved. Which patients should receive standard chemotherapy versus venetoclax and azacitidine in first line has not been established, and the resistance mechanisms are still being discovered. The observation that stemness drives primary IDH inhibitor resistance, while mechanistically plausible given that those drugs work by inducing differentiation, is noted alongside the admission that the mechanisms driving stemness in IDH-mutant AML remain poorly understood.

## Key points

- LSCs sit atop each genetically defined subclone with its own epigenetically controlled hierarchy - so targeting the dominant clone alone is insufficient.
- LSC resistance rests on phenotypic plasticity, dormancy and senescence rather than on a single mechanism.
- Argues LSC-targeted strategies must enter first-line regimens rather than be reserved for relapse.
- Patient selection between standard chemotherapy and venetoclax plus azacitidine in first line is explicitly unresolved.
- Single-cell multi-omics on longitudinal samples is presented as the route to tracing relapse-initiating populations.

## Limitations

A narrative review without systematic search or evidence grading, and it argues a position - the cancer stem cell model - that some primary work in this collection directly challenges, notably the finding that chemotherapy-resistant AML cells are not enriched for leukemic stem cells but are defined by oxidative metabolism, and the demonstration that a transient senescence-like state confers relapse capacity independent of stem cell status. The review does not engage with those results in the depth their challenge to the framework warrants. Its clinical trial survey dates from early 2023. Much of the forward-looking content describes what single-cell multi-omics may enable rather than what it has established.

## Provenance

Located in the published literature, dropped into `inbox/` as `Stelmach(2023) Haematologica; Leukemic stem cells and therapy resistance in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3324/haematol.2022.280800`; the prose sections were written here from the paper itself.

## Citation

Stelmach et al. Haematologica 2023. Leukemic stem cells and therapy resistance in acute myeloid leukemia. doi: 10.3324/haematol.2022.280800

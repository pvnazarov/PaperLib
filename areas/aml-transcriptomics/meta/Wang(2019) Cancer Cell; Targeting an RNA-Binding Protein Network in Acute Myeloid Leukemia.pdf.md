---
# --- identity ------------------------------------------------
id: 2019-01-01_wang-2019-cancer-cell-targeting-an-rna-b
id_basis: filename-year
source: Wang(2019) Cancer Cell; Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia.pdf
sha256: 74ca25c972de4c7cfec1f13af07c2d110c68ef217236526a71edab765a655270
size_bytes: 5972014
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 114361

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2019.01.010"
year: 2019
title: "Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Wang(2019) Cancer Cell; Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A CRISPR/Cas9 domain-focused screen targeting the RNA-binding domains of 490 classical RNA-binding proteins across human cancers uncovered a network of physically interacting RBPs upregulated in AML relative to normal CD34+ cells and required for RNA splicing and AML survival. Genetic or pharmacologic targeting of one member, RBM39, repressed cassette exon inclusion and promoted intron retention in mRNAs encoding HOXA9 targets and other AML-preferential RBPs. The splicing effects of RBM39 loss produced preferential lethality in spliceosomal-mutant AML, offering a strategy for AML bearing splicing factor mutations.

## Summary

Identifies not a single dependency but a network - physically interacting RNA-binding proteins that are collectively upregulated in AML and collectively maintain splicing - which reframes the target from one protein to a module.

RBM39 is the tractable entry point because it is degradable by aryl sulfonamides through DCAF15 recruitment, an existing pharmacology rather than a hypothetical one. The most useful clinical inference is the preferential lethality in spliceosomal-mutant AML, which fits the principle established elsewhere in this collection that cells already tolerating a partial splicing defect cannot absorb a second one - and the authors nominate spliceosomal mutation and high DCAF15 expression together as response biomarkers.

## Key points

- A domain-focused CRISPR screen across 490 RNA-binding proteins identifies AML-specific rather than generally essential dependencies.
- The hits form a physically interacting network upregulated in AML over normal CD34+ cells and required for splicing and survival.
- RBM39 loss represses cassette exon inclusion and promotes intron retention in HOXA9 target mRNAs and in other network RBPs.
- RBM39 is pharmacologically degradable by aryl sulfonamides via DCAF15, so the target has existing chemistry.
- Spliceosomal-mutant AML is preferentially killed, and spliceosomal mutation plus high DCAF15 are proposed as response biomarkers.

## Limitations

Degradation requires DCAF15, so response depends on its expression - which restricts the addressable population and adds a resistance mechanism through DCAF15 loss. RBM39 is one of a network, and targeting it perturbs the others through mis-splicing, so effects are distributed rather than clean. Preferential lethality in spliceosomal-mutant cells is relative, not absolute, and splicing is essential in normal cells, so the window is a matter of degree. Screening and most validation are in cell lines with primary samples and mouse models supporting. Two authors are Eisai employees and the senior author declares consulting and prior research funding from multiple companies including one developing splicing-directed therapeutics.

## Provenance

Located in the published literature, dropped into `inbox/` as `Wang(2019) Cancer Cell; Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2019.01.010`; the prose sections were written here from the paper itself.

## Citation

Wang et al. Cancer Cell 2019. Targeting an RNA-Binding Protein Network in Acute Myeloid Leukemia. doi: 10.1016/j.ccell.2019.01.010

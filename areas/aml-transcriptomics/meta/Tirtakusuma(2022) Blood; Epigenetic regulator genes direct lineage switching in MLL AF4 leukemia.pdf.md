---
# --- identity ------------------------------------------------
id: 2022-01-01_tirtakusuma-2022-blood-epigenetic-regula
id_basis: filename-year
source: Tirtakusuma(2022) Blood; Epigenetic regulator genes direct lineage switching in MLL AF4 leukemia.pdf
sha256: 54e3f66b6c3c557e6fae39be1e462a14813cb7ae6234a38a35170fde0f4e3d27
size_bytes: 2334721
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 206280

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2021015036"
year: 2022
title: "Epigenetic regulator genes direct lineage switching in MLL/AF4 leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tirtakusuma(2022) Blood; Epigenetic regulator genes direct lineage switching in MLL AF4 leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

MLL/AF4 defines a high-risk pro-B acute lymphoblastic leukemia whose relapse can involve a lineage switch to acute myeloid leukemia, conferring resistance to chemotherapy and immunotherapy. Myeloid relapses share oncogene fusion breakpoints with their matched lymphoid presentations and can originate from varying differentiation stages, from immature progenitors through committed B-cell precursors. Lineage switching involves substantial changes in chromatin accessibility and rewiring of transcriptional programmes including alternative splicing, and is recurrently associated with altered expression, splicing or mutation of chromatin modifiers, notably CHD4, the ATPase/helicase of the NuRD complex. Perturbing CHD4 alone or with other mutated epigenetic modifiers induces myeloid gene expression in MLL/AF4 cell models.

## Summary

Explains a clinically catastrophic event - a B-ALL returning as AML, and therefore escaping every lineage-directed therapy including CD19 immunotherapy - and shows it is epigenetic rather than genetic, since the fusion breakpoints are shared between presentation and relapse.

The cell-of-origin analysis is the more nuanced part. Using BCR rearrangements to trace ancestry, relapse can evolve directly from pro-B blasts or, alternatively, from MLL/AF4-expressing MPP-like cells in the HSPC compartment - so there is no single answer. The mechanistic framing is well argued: lymphoid commitment requires not just activating a B-cell programme but silencing a default myeloid one, and losing that repression is what allows the switch. CHD4 is a satisfying candidate because NuRD is the machinery that would normally enforce it.

## Key points

- Myeloid relapses share fusion breakpoints with the matched lymphoid presentation, so lineage switching is not a second leukemia.
- Relapse can originate from pro-B blasts or from MLL/AF4-expressing MPP-like cells in the HSPC compartment - the origin is heterogeneous.
- Switching involves large changes in chromatin accessibility, transcriptional rewiring and alternative splicing.
- Lymphoid commitment requires silencing a default myeloid programme; losing that repression permits the switch.
- CHD4, the NuRD ATPase, is recurrently altered, and perturbing it induces myeloid gene expression in MLL/AF4 models.

## Limitations

The authors state they cannot exclude additional cells of origin, and the two routes they identify are inferred from BCR rearrangement comparison in a limited cohort of matched cases - lineage-switched relapses being rare. Functional evidence is CHD4 perturbation inducing myeloid gene expression in MLL/AF4 cell models, which is a partial phenotype rather than a demonstrated lineage switch, and CHD4 is one of several altered chromatin modifiers whose relative contribution is not resolved. The disease is predominantly ALL, so its relevance to this AML collection is as a lineage-plasticity mechanism rather than as AML biology. Two authors are Illumina employees. This record's file is the accepted manuscript version rather than the typeset article.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tirtakusuma(2022) Blood; Epigenetic regulator genes direct lineage switching in MLL AF4 leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2021015036`; the prose sections were written here from the paper itself.

## Citation

Tirtakusuma et al. Blood 2022. Epigenetic regulator genes direct lineage switching in 
                    <i>MLL/AF4</i>
                    leukemia. doi: 10.1182/blood.2021015036

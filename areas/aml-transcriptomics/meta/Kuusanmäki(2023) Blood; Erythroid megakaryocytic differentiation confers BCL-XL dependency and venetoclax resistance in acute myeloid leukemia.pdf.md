---
# --- identity ------------------------------------------------
id: 2023-01-01_kuusanm-ki-2023-blood-erythroid-megakary
id_basis: filename-year
source: Kuusanmäki(2023) Blood; Erythroid megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia.pdf
sha256: dd33e433c20a3e5ae0e6d5dcf9d9e80fa189576dd56e9e276ba50f6d3a27a9b7
size_bytes: 6764252
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 214855

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2021011094"
year: 2023
title: "Erythroid/megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kuusanmäki(2023) Blood; Erythroid megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using combined ex vivo drug sensitivity testing, genetic perturbation and transcriptomic profiling, AML with erythroid or megakaryocytic differentiation is shown to depend on BCL-XL rather than BCL-2. High-throughput screening of more than 500 compounds identified the BCL-XL-selective inhibitor A-1331852 and navitoclax as highly effective against erythroid/megakaryoblastic leukemia cell lines, while these subtypes were resistant to venetoclax. Genome-scale CRISPR-Cas9 and RNAi screening data confirmed essentiality of BCL2L1 but not BCL2 or MCL1, and A-1331852 reduced tumour burden in a xenograft model, though cells persisted in some animals and regrew after drug withdrawal.

## Summary

Explains a clinical failure by lineage biology. Venetoclax is standard in AML and does not work in pure erythroid leukemia, MDS with erythroid features or acute megakaryoblastic leukemia - and the reason turns out to be simple and predictable from normal hematopoiesis: erythroblasts characteristically lack BCL-2 and depend on BCL-XL, and their leukemic counterparts inherit that dependency.

The same reasoning immediately identifies the problem with the therapy. BCL-XL is essential for terminal erythropoiesis and for platelet survival, and conditional knockout in mouse progenitors causes severe anemia and thrombocytopenia - so the dependency that makes these leukemias targetable is shared with the normal cells of the same lineage. The authors set this out plainly rather than leaving it implicit, and their xenograft result is correspondingly honest: burden falls, cells persist in some animals, and disease regrows after withdrawal.

## Key points

- AML with erythroid or megakaryocytic differentiation depends on BCL-XL, not BCL-2 or MCL-1, explaining its venetoclax resistance.
- Established by three independent approaches: a >500-compound ex vivo screen, genome-scale CRISPR and RNAi data, and transcriptomic profiling.
- The BCL-XL-selective inhibitor A-1331852 and navitoclax were highly effective in these subtypes.
- The dependency mirrors normal biology - erythroblasts lack BCL-2 and rely on BCL-XL, which is also essential for platelet survival.
- In a xenograft, A-1331852 reduced burden but cells persisted in some animals and regrew after drug withdrawal.

## Limitations

The therapeutic window is the central problem and the paper's own discussion makes it unavoidable: BCL-XL is essential for terminal erythropoiesis and platelet survival, so inhibiting it causes thrombocytopenia - the known dose-limiting toxicity of navitoclax that stopped its development as a single agent. The in vivo test is a single cell-line xenograft (HEL) with incomplete responses and regrowth after two weeks of treatment, which is a modest efficacy result. These are rare subtypes, so primary sample numbers are inevitably small. Ex vivo drug sensitivity correlates imperfectly with clinical response. The lineage-based framing may also be less clean in practice than in cell lines, since patient AML frequently contains mixed differentiation states rather than a uniform erythroid or megakaryocytic phenotype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kuusanmäki(2023) Blood; Erythroid megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2021011094`; the prose sections were written here from the paper itself.

## Citation

Kuusanmäki et al. Blood 2023. Erythroid/megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia. doi: 10.1182/blood.2021011094

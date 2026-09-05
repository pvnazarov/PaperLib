---
# --- identity ------------------------------------------------
id: 2018-01-01_wood-2018-bmc-cancer-population-level-di
id_basis: filename-year
source: Wood(2018) BMC Cancer; Population-level distribution and putative immunogenicity of cancer neoepitopes.pdf
sha256: f5af97952b54a12a31f36d14f97c9dbd5866cfedfa4172509d71b3401397f76c
size_bytes: 2539587
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 105819

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12885-018-4325-6"
year: 2018
title: "Population-level distribution and putative immunogenicity of cancer neoepitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2018_Wood_BMC_Cancer_Population_level_distribution_and_putative_imm_PMID29653567.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Four peptide novelty metrics are proposed to refine neoantigen prediction - tumour versus paired normal binding affinity difference, tumour versus paired normal sequence similarity, tumour versus closest human peptide similarity, and tumour versus closest microbial peptide similarity - and applied across TCGA, a melanoma cohort, and peptides with neoepitope-specific immune response data.

## Summary

The population-level view is what distinguishes this from the single-cohort ranking papers. Neoepitope burden varies across diseases and HLA alleles, and the authors report surprisingly little repetition of neoepitope sequences between patients, which is the quantitative case for personalised rather than shared vaccines.

The headline filtering number is that only 20.3% of predicted neoepitopes across TCGA patients showed a novel binding change by their affinity-difference criterion, so the great majority of predicted candidates present nothing a T cell has not effectively seen.

## Key points

- Four explicit novelty metrics, including similarity to the closest microbial peptide - unusual, and connected to the mimicry papers in this collection.
- Only 20.3% of TCGA-predicted neoepitopes displayed a novel binding change.
- Very low repetition of neoepitope sequences across patients, and little neoepitope preference among HLA allele sets.
- Applied through an extension of pVAC-Seq, so the metrics are usable in an existing pipeline.

## Limitations

The authors state that for simplicity they did not consider expression levels or variant allele frequencies - both well-established and important prioritisation criteria - so these results are about sequence novelty in isolation. The microbial comparison was not restricted a priori to organisms associated with human health, broadening the search space with likely uninformative sequences. Immunogenicity here is 'putative', derived from metrics rather than measured for most of the analysed peptides.

## Provenance

Located in the published literature, dropped into `inbox/` as `2018_Wood_BMC_Cancer_Population_level_distribution_and_putative_imm_PMID29653567.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12885-018-4325-6`; the prose sections were written here from the paper itself.

## Citation

Wood et al. BMC Cancer 2018. Population-level distribution and putative immunogenicity of cancer neoepitopes. doi: 10.1186/s12885-018-4325-6

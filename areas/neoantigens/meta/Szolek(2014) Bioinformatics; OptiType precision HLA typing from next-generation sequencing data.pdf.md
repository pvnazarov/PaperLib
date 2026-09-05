---
# --- identity ------------------------------------------------
id: 2014-01-01_szolek-2014-bioinformatics-optitype-prec
id_basis: filename-year
source: Szolek(2014) Bioinformatics; OptiType precision HLA typing from next-generation sequencing data.pdf
sha256: ba3048a3292b9551c64e9ce9bfe33ce901b08fd7d7b5b1d106adae6cb2014591
size_bytes: 747975
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 56965

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btu548"
year: 2014
title: "OptiType: precision HLA typing from next-generation sequencing data"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2014_Szolek_Bioinformatics_OptiType_precision_HLA_typing_from_next_genera_PMID25143287.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

OptiType genotypes HLA from NGS data using integer linear programming, without requiring HLA-specific enrichment. Benchmarked on a purpose-built dataset spanning RNA, exome and whole-genome sequencing, it reports 97% overall accuracy, significantly better than previous in silico approaches.

## Summary

The practical claim is that HLA typing need not cost an extra assay: exome or genome data collected for mutation calling already contain enough information, which matters because every neoantigen pipeline needs the genotype anyway.

Formulating genotyping as an integer linear program gives a globally optimal solution to the allele-assignment problem under the read evidence, rather than a heuristic search through a highly homologous reference.

## Key points

- No HLA-specific enrichment needed - removes an extra assay, cost and turnaround from the pipeline.
- Integer linear programming gives an optimal assignment rather than a heuristic one.
- Benchmarked across RNA, exome and whole-genome data rather than one data type.
- 97% overall accuracy; a long-standing default first step in neoantigen pipelines.

## Limitations

97% overall accuracy means roughly one in thirty typings is wrong, and a wrong allele invalidates every downstream binding prediction for that patient - the error does not degrade gracefully. Accuracy depends on coverage at the HLA locus, which is incidental rather than designed in non-enriched data. It is class I focused, and the reference databases of 2014 have since expanded considerably.

## Provenance

Located in the published literature, dropped into `inbox/` as `2014_Szolek_Bioinformatics_OptiType_precision_HLA_typing_from_next_genera_PMID25143287.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btu548`; the prose sections were written here from the paper itself.

## Citation

Szolek et al. Bioinformatics 2014. OptiType: precision HLA typing from next-generation sequencing data. doi: 10.1093/bioinformatics/btu548

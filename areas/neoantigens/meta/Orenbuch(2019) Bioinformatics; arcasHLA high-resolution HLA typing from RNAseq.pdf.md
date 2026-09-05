---
# --- identity ------------------------------------------------
id: 2019-01-01_orenbuch-2019-bioinformatics-arcashla-hi
id_basis: filename-year
source: Orenbuch(2019) Bioinformatics; arcasHLA high-resolution HLA typing from RNAseq.pdf
sha256: 9d22fa69fa782dfd1f91fefd1dca68e6720b4e9f1e6c5341dfe02df40eef0cad
size_bytes: 401938
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 60429

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btz474"
year: 2019
title: "arcasHLA: high-resolution HLA typing from RNAseq"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2020_Orenbuch_Bioinformatics_arcasHLA_high_resolution_HLA_typing_from_RNAse_PMID31173059.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

arcasHLA infers HLA genotypes from RNA-sequencing data, reporting 100% accuracy at two-field resolution for class I and over 99.7% for class II on the gold-standard benchmark, faster than established tools. It is further evaluated on 447 single-end total RNA samples from nasopharyngeal swabs to establish applicability to metatranscriptomes.

## Summary

HLA typing is the input every neoantigen pipeline depends on and few papers examine: predict binding to the wrong allele and everything downstream is wrong. Typing from RNA-seq is harder than from DNA because of post-transcriptional modification and amplification bias, on top of the polymorphism and homology that make the locus difficult in the first place.

The practical value is that RNA-seq is already collected for expression filtering in neoantigen pipelines, so genotype comes free from data that is there anyway.

## Key points

- 100% two-field accuracy for class I and >99.7% for class II on the benchmark set, with lower runtime than competitors.
- Works from RNA-seq, which neoantigen pipelines already generate for expression filtering.
- Validated on a second, harder biological dataset: 447 single-end nasopharyngeal swab samples.
- Open source, and a standard upstream component for the pipelines elsewhere in this collection.

## Limitations

The headline accuracy is on a gold-standard benchmark; on the harder swab dataset it falls to 97.7% (class I) and 94.1% (class II), and the authors did not attempt partial typing there because single-end reads cannot resolve single-base ambiguities. Accuracy depends on HLA locus coverage and RNA integrity, so low-input or degraded samples will do worse. Reference-database completeness bounds what can be called at all.

## Provenance

Located in the published literature, dropped into `inbox/` as `2020_Orenbuch_Bioinformatics_arcasHLA_high_resolution_HLA_typing_from_RNAse_PMID31173059.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btz474`; the prose sections were written here from the paper itself.

## Citation

Orenbuch et al. Bioinformatics 2019. arcasHLA: high-resolution HLA typing from RNAseq. doi: 10.1093/bioinformatics/btz474

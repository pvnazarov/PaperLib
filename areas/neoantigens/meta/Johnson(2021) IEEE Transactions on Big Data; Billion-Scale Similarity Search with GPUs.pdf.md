---
# --- identity ------------------------------------------------
id: 2021-01-01_johnson-2021-ieee-transactions-on-big-da
id_basis: filename-year
source: Johnson(2021) IEEE Transactions on Big Data; Billion-Scale Similarity Search with GPUs.pdf
sha256: 89b2371b261846059d416bdf1423b15a6e3cc7d1b2d5dc2729ee5f6c3399049a
size_bytes: 1233821
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 106419

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1109/tbdata.2019.2921572"
year: 2021
title: "Billion-Scale Similarity Search with GPUs"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2021_Johnson_IEEE_Transactions_on_B_Billion_Scale_Similarity_Search_with_GPUs_DOI_10_1109_tbdata_2019_2921572.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The Faiss approach to approximate k-nearest-neighbour search on GPUs, using product-quantization codes so that billion-scale vector collections can be searched without reconstructing the vectors or holding them uncompressed in memory. The flagship application is building k-NN graphs at a scale where exact indexing and existing methods such as NN-Descent do not fit.

## Summary

This is infrastructure, not immunology. It is in this collection because peptide, TCR and embedding-based methods increasingly reduce to nearest-neighbour search over large vector sets, and the similarity-based components of several models here need exactly this.

The core trade is stated directly: accepting a small accuracy loss buys orders of magnitude of compression, which is what makes memory-limited GPU search practical.

## Key points

- Product-quantization codes allow neighbour search without reconstructing the original vectors.
- A small, controlled accuracy loss buys orders-of-magnitude compression - the trade that makes billion-scale GPU search possible.
- k-NN graph construction is the target application; NN-Descent's memory overhead does not scale to this size.
- Underpins the similarity-search components of sequence and embedding based immunology tools.

## Limitations

Nothing in this paper concerns peptides, MHC or immunogenicity; its presence here is as a dependency, and any biological claim built on it needs its own evidence. The results are approximate by construction, and the accuracy/compression trade-off has to be tuned per application. Hardware-specific performance figures from 2021 GPUs should not be quoted as current.

## Provenance

Located in the published literature, dropped into `inbox/` as `2021_Johnson_IEEE_Transactions_on_B_Billion_Scale_Similarity_Search_with_GPUs_DOI_10_1109_tbdata_2019_2921572.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1109/tbdata.2019.2921572`; the prose sections were written here from the paper itself.

## Citation

Johnson et al. IEEE Transactions on Big Data 2021. Billion-Scale Similarity Search with GPUs. doi: 10.1109/tbdata.2019.2921572

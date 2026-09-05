---
# --- identity ------------------------------------------------
id: 2025-01-01_wang-2025-biomarker-research-computation
id_basis: filename-year
source: Wang(2025) Biomarker Research; Computation strategies and clinical applications in neoantigen discovery towards precision cancer immunotherapy.pdf
sha256: 20ba94c58b124d90ef2016fec718c29560452ac6f7f28cb61279486070418a46
size_bytes: 3563313
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 131895

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s40364-025-00808-9"
year: 2025
title: "Computation strategies and clinical applications in neoantigen discovery towards precision cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Wang_Biomark_Res_Computation_strategies_and_clinical_applicatio_PMID40629481.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review of integrated neoantigen prediction algorithms covering task definition, theoretical development, benchmark datasets and applications, with emphasis on HLA-peptide binding and TCR recognition methods, and on the use of neoantigens in personalised vaccines and adoptive cell therapy.

## Summary

The most useful part for orientation is the treatment of neoantigen sources: somatic mutations, but also RNA-derived neoantigens from aberrant transcripts, splicing and isoform dysregulation, which substantially broaden the target space in tumours with few mutations.

The review is careful about the cost of that breadth. RNA-derived epitopes are not encoded in the tumour genome, so their expression can be lost under immune pressure - for instance through altered splicing factor expression - making them less stable targets than DNA-mutation-derived ones.

## Key points

- Surveys the whole pipeline: source characterisation, binding, presentation, TCR recognition, then clinical application.
- Treats RNA-derived neoantigens as a major source, with an explicit account of why they are less stable targets.
- Covers benchmark datasets as a first-class topic, not an afterthought.
- A reasonable entry point to the field and to the rest of this collection.

## Limitations

A review: every quantitative claim belongs to a cited study and must be traced there before it is used. It surveys methods largely on their authors' reported terms and does not benchmark them independently, so the relative rankings implied should not be taken as measured. Fast-moving field, and the coverage is a 2025 snapshot.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Wang_Biomark_Res_Computation_strategies_and_clinical_applicatio_PMID40629481.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s40364-025-00808-9`; the prose sections were written here from the paper itself.

## Citation

Wang et al. Biomarker Research 2025. Computation strategies and clinical applications in neoantigen discovery towards precision cancer immunotherapy. doi: 10.1186/s40364-025-00808-9

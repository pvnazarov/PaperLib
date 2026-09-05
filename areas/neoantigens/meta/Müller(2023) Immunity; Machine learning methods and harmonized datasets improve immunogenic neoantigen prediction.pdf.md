---
# --- identity ------------------------------------------------
id: 2023-01-01_m-ller-2023-immunity-machine-learning-me
id_basis: filename-year
source: Müller(2023) Immunity; Machine learning methods and harmonized datasets improve immunogenic neoantigen prediction.pdf
sha256: f22589badcac44fb8a44673b696f616360fe9094a8b09e1206bcd202315b51b1
size_bytes: 4403924
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 130745

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.immuni.2023.09.002"
year: 2023
title: "Machine learning methods and harmonized datasets improve immunogenic neoantigen prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_M_ller_Immunity_Machine_learning_methods_and_harmonized_datase_PMID37816353.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

WES and RNA-seq from 120 patients across two large external neoantigen immunogenicity screens plus 11 in-house patients were reprocessed uniformly, yielding 46,017 somatic SNVs and 1,781,445 neo-peptides, of which 212 mutations and 178 neo-peptides were immunogenic. Classifiers trained on these harmonised data improved neoantigen ranking by up to 30%, and features beyond the usual ones proved predictive.

## Summary

The harmonisation is the contribution as much as the model. Immunogenicity screens differ in processing, so pooling their published outputs mixes pipeline artefacts with biology; reprocessing everything through one pipeline makes the datasets comparable and reusable as a benchmark.

The class imbalance is the number to keep in view: 178 immunogenic peptides out of 1.78 million. Any reported ranking improvement has to be read against that base rate.

## Key points

- 1,781,445 neo-peptides, 178 immunogenic - a base rate of roughly one in ten thousand.
- Predictive features beyond the standard set: position within HLA presentation hotspots, binding promiscuity, and oncogenicity of the mutated gene.
- Ranking improved by up to 30% and the classifiers transferred across datasets.
- The harmonised datasets are released for benchmarking companion algorithms - arguably the more durable output.

## Limitations

The authors state it plainly: only a subset of neo-peptides was screened, so the datasets contain false negatives, and in vitro T cell exhaustion may cause genuine responses to be missed. A negative label here means 'not detected in this assay', not 'not immunogenic'. With 178 positives, confidence intervals on any performance figure are wide, and a 30% ranking improvement on a one-in-ten-thousand base rate still leaves most top candidates wrong.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_M_ller_Immunity_Machine_learning_methods_and_harmonized_datase_PMID37816353.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.immuni.2023.09.002`; the prose sections were written here from the paper itself.

## Citation

Müller et al. Immunity 2023. Machine learning methods and harmonized datasets improve immunogenic neoantigen prediction. doi: 10.1016/j.immuni.2023.09.002

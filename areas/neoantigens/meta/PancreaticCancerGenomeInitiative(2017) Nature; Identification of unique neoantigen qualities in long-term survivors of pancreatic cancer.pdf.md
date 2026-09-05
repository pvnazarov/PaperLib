---
# --- identity ------------------------------------------------
id: 2017-01-01_pancreaticcancergenomeinitiative-2017-na
id_basis: filename-year
source: PancreaticCancerGenomeInitiative(2017) Nature; Identification of unique neoantigen qualities in long-term survivors of pancreatic cancer.pdf
sha256: 54399e17a67629d5639059690e2cd2603b007d5875cf9f385787e917b3abaa85
size_bytes: 5889243
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 322449

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature24462"
year: 2017
title: "Identification of unique neoantigen qualities in long-term survivors of pancreatic cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nature24462.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Comparing long-term pancreatic cancer survivors (median survival 6 years, n=82) with short-term survivors (median 0.8 years, n=68), the authors find that survival is associated not with neoantigen quantity but with neoantigen quality, and identify MUC16 as a candidate immunogenic hotspot.

## Summary

This is the study that established neoantigen quality as the operative variable and set up the Q = R x D formalism that Luksza (2022) later developed in the same cohort. PDAC has few mutations, so quantity-based measures such as tumour mutation burden have little to work with, which makes it the setting where quality can be seen most clearly.

The functional check matters: peripheral blood from two long-term survivors, both disease-free eight years after surgery, was stimulated with predicted MUC16 neoantigens and responded - so the predicted hotspot was recognised by the patients' own T cells.

## Key points

- Long-term versus short-term survivor design in a low-mutation cancer isolates quality from quantity.
- Neoantigen quality, not number, distinguishes the two groups.
- MUC16 identified as a candidate immunogenic hotspot, with peripheral T cell responses confirmed in two long-term survivors.
- The foundation for the neoantigen fitness and quality models elsewhere in this collection.

## Limitations

The authors state that the number of long-term survivors with MUC16 neoantigens was small and that validation in a larger cohort is warranted. They checked whether the MUC16 signal was simply a gene-size artefact and found no trend towards neoantigen formation by gene size, but MUC16 is very large and the concern is reasonable. Functional confirmation is two patients. Long-term survivors are a selected population, so associations may reflect what allowed survival rather than what caused it.

## Provenance

Located in the published literature, dropped into `inbox/` as `nature24462.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature24462`; the prose sections were written here from the paper itself.

## Citation

PancreaticCancerGenomeInitiative et al. Nature 2017. Identification of unique neoantigen qualities in long-term survivors of pancreatic cancer. doi: 10.1038/nature24462

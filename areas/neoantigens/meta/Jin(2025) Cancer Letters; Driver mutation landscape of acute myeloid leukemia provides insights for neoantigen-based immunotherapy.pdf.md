---
# --- identity ------------------------------------------------
id: 2025-01-01_jin-2025-cancer-letters-driver-mutation
id_basis: filename-year
source: Jin(2025) Cancer Letters; Driver mutation landscape of acute myeloid leukemia provides insights for neoantigen-based immunotherapy.pdf
sha256: 50f231f68f1554492046cc3cbae148be79f0d67ddd5ee2e71b146655490dd060
size_bytes: 16416337
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 85377

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.canlet.2024.217427"
year: 2025
title: "Driver mutation landscape of acute myeloid leukemia provides insights for neoantigen-based immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-S030438352400822X-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Matched DNA and RNA sequencing of 304 AML patients, integrated with about 2,500 further cases, identifies 49 driver genes with a notably high proportion of indels. Indels yielded more and higher-quality neoantigens than SNVs or fusions; two immunogenicity models were built, 30 neoantigens validated by direct MHC binding and 20 confirmed immunogenic by IFN-gamma ELISpot.

## Summary

AML has lagged in immunotherapy because it has few actionable antigens, and this asks whether driver mutations can supply them. The answer turns on mutation class: indels shift the reading frame and produce long novel sequences, so they generate both more neoantigens and better ones than single-substitution SNVs.

The validation is more substantial than most computational neoantigen papers - binding assays for 30 candidates and functional confirmation for 20.

## Key points

- 49 driver genes across a large integrated AML cohort, with an unusually high indel proportion.
- Indels outperform SNVs and fusions on both neoantigen quantity and quality - a mutation-class effect, not a gene-specific one.
- 30 neoantigens validated by direct peptide-MHC binding; 20 confirmed immunogenic by IFN-gamma ELISpot.
- Links the neoantigen landscape to patient outcome and to the immunosuppressive AML microenvironment.

## Limitations

The authors note that the large public cohorts they integrate consist mainly of white and black populations from Western countries, and added their own institutional cohort to broaden representation - HLA-dependent findings are sensitive to exactly this. Validation is in vitro binding and ELISpot, not patient response. Neoantigen 'quality' is computed with models built in the same study, so quality and immunogenicity are not independently established.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-S030438352400822X-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.canlet.2024.217427`; the prose sections were written here from the paper itself.

## Citation

Jin et al. Cancer Letters 2025. Driver mutation landscape of acute myeloid leukemia provides insights for neoantigen-based immunotherapy. doi: 10.1016/j.canlet.2024.217427

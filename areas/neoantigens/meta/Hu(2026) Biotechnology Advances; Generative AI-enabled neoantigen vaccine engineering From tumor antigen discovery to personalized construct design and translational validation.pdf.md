---
# --- identity ------------------------------------------------
id: 2026-01-01_hu-2026-biotechnology-advances-generativ
id_basis: filename-year
source: Hu(2026) Biotechnology Advances; Generative AI-enabled neoantigen vaccine engineering From tumor antigen discovery to personalized construct design and translational validation.pdf
sha256: 4b5a809a3404187318db78e7f0d362f8852582dda8aa5ab4006bc054f3a4b088
size_bytes: 8327025
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 183854

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.biotechadv.2026.109028"
year: 2026
title: "Generative AI-enabled neoantigen vaccine engineering: From tumor antigen discovery to personalized construct design and translational validation"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 1-s2.0-S073497502600234X-main.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review arguing that current neoantigen pipelines are dominated by discriminative models that rank pre-existing mutant peptides on binding and presentation features, and that generative AI offers a complementary design-oriented framework: exploring and iteratively optimising sequence space under explicit constraints rather than scoring predefined candidates.

## Summary

The distinction it draws is genuinely useful. Everything else in this collection ranks candidates the tumour happened to produce; a generative framework designs constructs against multiple objectives at once - presentation, recognition potential, and translational feasibility such as manufacturability.

It also insists on the boundary: generative models are components of an AI-assisted workflow, not substitutes for tumour-derived evidence. Given that the same review states peptide-MHC binding is necessary but not sufficient, and that a neoepitope also depends on expression, processing, transport, loading, stability, clonality, foreignness and productive TCR recognition, that caution is earned.

## Key points

- Frames the field's methods as discriminative ranking and proposes generative design as the complement, not the replacement.
- Extends optimisation to multi-epitope and mRNA construct engineering, not just peptide choice.
- Incorporates tumour-specific constraints - antigen-presentation defects, clonal architecture, microenvironment state - into the design objective.
- Explicitly positions generative models as components subordinate to tumour-derived evidence.

## Limitations

A review of a direction rather than a report of results: it argues what generative AI may enable, and the clinical evidence for any of it is not yet in. Designed sequences are hypotheses, and this collection's own record shows that predicted binders convert to immunogenic epitopes at a low rate. Every quantitative claim belongs to a cited study.

## Provenance

Located in the published literature, dropped into `inbox/` as `1-s2.0-S073497502600234X-main.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.biotechadv.2026.109028`; the prose sections were written here from the paper itself.

## Citation

Hu et al. Biotechnology Advances 2026. Generative AI-enabled neoantigen vaccine engineering: From tumor antigen discovery to personalized construct design and translational validation. doi: 10.1016/j.biotechadv.2026.109028

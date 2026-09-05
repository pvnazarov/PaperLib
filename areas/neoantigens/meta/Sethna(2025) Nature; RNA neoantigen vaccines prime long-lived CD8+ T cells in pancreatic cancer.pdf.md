---
# --- identity ------------------------------------------------
id: 2025-01-01_sethna-2025-nature-rna-neoantigen-vaccin
id_basis: filename-year
source: Sethna(2025) Nature; RNA neoantigen vaccines prime long-lived CD8+ T cells in pancreatic cancer.pdf
sha256: 11aac3f106055b2d67231e90fc122d65d54acac30a4ea4253e978a6f856368be
size_bytes: 22026962
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 324946

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-024-08508-4"
year: 2025
title: "RNA neoantigen vaccines prime long-lived CD8+ T cells in pancreatic cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Sethna_Nature_RNA_neoantigen_vaccines_prime_long_lived_CD8_T_PMID39972124.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Extended follow-up of the autogene cevumeran PDAC trial shows mRNA-lipoplex neoantigen vaccines induce CD8+ T cell clones that persist as long-lived memory. Clonal histories of more than 9,000 single cells across six patients show most vaccine-induced clones transition into a stable effector memory phase, and the association between vaccine response and recurrence-free survival holds at 3.2 years.

## Summary

The open question left by the original trial was durability: raising T cells is not the same as keeping them. Single-cell clonal tracking answers it directly by following individual vaccine-induced clones over years rather than measuring bulk response.

The negative finding is equally worth having: the authors looked for epitope spread - acquired immunity against tumour neoantigens not included in the vaccine - and did not detect clear evidence of it in any responder.

## Key points

- Vaccine-induced CD8+ clones persist as long-lived memory; tracked through complete clonal histories of >9,000 single cells in 6 patients.
- The vaccine-response/recurrence-free-survival association holds at 3.2 years with effect size similar to 1.5 years.
- No clear evidence of neoepitope spread to non-vaccine neoantigens in any responder.
- Demonstrated in PDAC, a lethal cancer with few mutations - the unfavourable case.

## Limitations

The authors state that unknown factors may confound the correlation between vaccine response and recurrence-free survival, having ruled out only the confounders they could measure. Six patients for the clonal analysis is a very small base for claims about memory formation generally. The absence of detected epitope spread is a negative result in a small cohort and should not be read as establishing that it does not occur.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Sethna_Nature_RNA_neoantigen_vaccines_prime_long_lived_CD8_T_PMID39972124.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-024-08508-4`; the prose sections were written here from the paper itself.

## Citation

Sethna et al. Nature 2025. RNA neoantigen vaccines prime long-lived CD8+ T cells in pancreatic cancer. doi: 10.1038/s41586-024-08508-4

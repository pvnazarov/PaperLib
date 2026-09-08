---
# --- identity ------------------------------------------------
id: 2019-01-01_yoshimi-2019-nature-coordinated-alterati
id_basis: filename-year
source: Yoshimi(2019) Nature; Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis.pdf
sha256: c85e4a6a6028d7c585810755acd00eddd78630b1c9a3409f94b40f4b3044f86f
size_bytes: 27038621
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 212282

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-019-1618-0"
year: 2019
title: "Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yoshimi(2019) Nature; Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Analysis of transcriptomes from 982 AML patients identified frequent overlap of IDH2 and SRSF2 mutations - 47% of SRSF2-mutant patients also had IDH2 mutation and 56% of IDH2-mutant patients had SRSF2 mutation - with high, correlated variant allele frequencies indicating early events. Although each mutation alone imparts distinct splicing changes, co-expressing mutant IDH2 alters the splicing effects of mutant SRSF2 and produces more profound changes than either alone. Co-expression caused lethal myelodysplasia with proliferative features in vivo and enhanced self-renewal not seen with either mutation alone. Double-mutant cells showed aberrant splicing and reduced INTS3, a member of the integrator complex, with increased RNA polymerase II stalling.

## Summary

Provides the first functional evidence that splicing factor mutations can initiate leukemia, and does it by showing that they need a partner. Neither mutation alone produces disease in these models; together they cause lethal myelodysplasia with proliferative features and enhanced self-renewal, so the cooperation is not additive but qualitative - mutant IDH2 changes what mutant SRSF2 does to splicing.

The clinical grounding is strong: the co-occurrence is highly significant across TCGA, Beat AML and Leucegene, present in 5-6% of over 1600 consecutive unselected patients, and double-mutant cases have the shortest overall survival of the four genotypes with prognosis resembling adverse cytogenetic risk despite mostly intermediate cytogenetics. The mechanism converges on INTS3 and increased polymerase stalling, linking a splicing defect to a transcriptional one.

## Key points

- IDH2 and SRSF2 mutations co-occur far more than chance across three large cohorts, with high correlated variant allele frequencies indicating early events.
- First functional evidence that splicing factor mutations initiate leukemia - but only in combination.
- Mutant IDH2 alters the splicing consequences of mutant SRSF2, producing changes greater than either alone.
- Co-expression causes lethal myelodysplasia with proliferative features and enhanced self-renewal in vivo.
- The mechanism runs through aberrant INTS3 splicing and increased RNA polymerase II stalling, and depends on mutant SRSF2 binding.

## Limitations

The survival disadvantage of double-mutant cases was not statistically significant despite being the shortest of the four genotypes, so the prognostic claim rests on a trend. Double-mutant patients were also significantly older than IDH2-only patients, confounding the outcome comparison. The functional model uses conditional knock-in mice and overexpression, producing myelodysplasia with proliferative features rather than frank AML, so 'initiate leukaemia' describes a preleukemic state. INTS3 is one of many mis-spliced targets and its contribution is shown to be partial. The co-occurrence is specific to IDH2 and SRSF2, so the finding does not generalise to other splicing factor mutations without testing.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yoshimi(2019) Nature; Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-019-1618-0`; the prose sections were written here from the paper itself.

## Citation

Yoshimi et al. Nature 2019. Coordinated alterations in RNA splicing and epigenetic regulation drive leukaemogenesis. doi: 10.1038/s41586-019-1618-0

---
# --- identity ------------------------------------------------
id: 2025-01-01_hosseini-2025-nature-perturbing-lsd1-and
id_basis: filename-year
source: Hosseini(2025) Nature; Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation.pdf
sha256: 310ea8970c195417665f08e81cadbb332777d6e446fe941bcdb725a47d9ce6dc
size_bytes: 60967307
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 359463

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-025-08915-1"
year: 2025
title: "Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Hosseini(2025) Nature; Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Simultaneous inhibition of the histone demethylase LSD1 and of GSK3, the WNT pathway antagonist kinase, robustly promotes differentiation of AML cell lines and primary human AML cells, reduces tumour burden and significantly extends survival in a patient-derived xenograft model. The mechanism is activation of type I interferon pathway genes: LSD1 inhibition induces transcription factors such as IRF7, GSK3 inhibition induces the co-activator beta-catenin, and the two selectively co-occupy targets including STAT1, which is required for the combination-induced differentiation. The combination also suppresses canonical pro-oncogenic WNT signalling and cell cycle genes, and the induced signature correlates with better prognosis in patient datasets.

## Summary

An attempt to generalise differentiation therapy beyond acute promyelocytic leukemia, where ATRA and arsenic are curative and where nothing comparable has transferred to other AML. LSD1 inhibitors do induce differentiation but have underperformed clinically with dose-limiting toxicity, so the strategy is to make them work at tolerable exposure by adding a second, mechanistically orthogonal perturbation.

The pharmacological paradox is handled explicitly and is the most interesting feature. GSK3 inhibition stabilises beta-catenin, and WNT/beta-catenin signalling sustains leukemia stem cells and drug resistance - so the combination should make things worse. It does not, because in this context beta-catenin is redirected to act as a co-activator on interferon targets alongside LSD1-induced IRF7, while canonical WNT output is suppressed. Whether that redirection is robust is the question the paper's own discussion circles.

## Key points

- Combined LSD1 and GSK3 inhibition drives differentiation in AML cell lines, primary human AML, and a patient-derived xenograft with survival benefit.
- The mechanism is type I interferon pathway activation, via LSD1i-induced IRF7 and GSK3i-induced beta-catenin co-occupying targets such as STAT1.
- STAT1 is required for the combination-induced differentiation.
- Canonical pro-oncogenic WNT signalling and cell cycle genes are suppressed despite beta-catenin stabilisation.
- Aimed at the clinical failure of single-agent LSD1 inhibitors, which differentiate AML cells but carry dose-limiting toxicity.

## Limitations

GSK3 inhibition is the weak point and the authors say so: it has shown insufficient efficacy clinically, it stabilises beta-catenin, and WNT/beta-catenin maintains the leukemia stem cell population and drug resistance - so the combination depends on a context-specific redirection of beta-catenin that may not hold across subtypes, since the role of beta-catenin in primary AML is reported to vary. GSK3 loss in hematopoietic progenitors has been linked to aggressive myelodysplasia and AML, a concern the authors address by questioning the underlying mouse experiments rather than by testing it. GSK3 is a pleiotropic kinase with many substrates, so selectivity in patients is uncertain. Efficacy evidence is one PDX model; the prognostic correlation of the induced signature is retrospective and does not show that inducing it helps.

## Provenance

Located in the published literature, dropped into `inbox/` as `Hosseini(2025) Nature; Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-025-08915-1`; the prose sections were written here from the paper itself.

## Citation

Hosseini et al. Nature 2025. Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. doi: 10.1038/s41586-025-08915-1

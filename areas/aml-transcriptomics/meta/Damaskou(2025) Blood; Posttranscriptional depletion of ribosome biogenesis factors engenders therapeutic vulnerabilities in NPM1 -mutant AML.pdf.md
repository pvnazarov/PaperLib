---
# --- identity ------------------------------------------------
id: 2025-01-01_damaskou-2025-blood-posttranscriptional
id_basis: filename-year
source: Damaskou(2025) Blood; Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1 -mutant AML.pdf
sha256: 5bf372bfe8a31f1c3d39ae7eb644490d265033be537a8030a1d2a81898f4e457
size_bytes: 3321026
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 186040

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2024026113"
year: 2025
title: "Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1 -mutant AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Damaskou(2025) Blood; Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1-mutant AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using conditional knockin Npm1cA/+ mice to isolate the effect of the NPM1c mutation on the proteome of preleukemic HSPCs, the authors find many ribosome biogenesis proteins significantly depleted - without corresponding mRNA changes, indicating posttranscriptional regulation - and confirm the depletion in human NPM1-mutant AML. Preleukemic Npm1cA/+ HSPCs are more sensitive to RNA polymerase I inhibitors including actinomycin D; ActD combined with venetoclax inhibits growth and colony formation of preleukemic and leukemic NPM1c+ cells, and low-dose ActD resensitises resistant NPM1c+ cells to venetoclax. From CRISPR dropout screens they identify TSR3, a 40S ribosomal maturation factor whose knockout preferentially inhibits NPM1c+ AML by activating a p53-dependent apoptotic response and partially restores venetoclax sensitivity.

## Summary

The design is the strength. A conditional knockin isolates NPM1c from the comutations and cell-line adaptations that confound almost all NPM1 work, so the proteomic changes can be attributed to the mutation itself. What emerges is that NPM1-mutant cells are already running a partly broken ribosome biogenesis machine, at the protein level only - mRNAs are unchanged.

That sets up a clean synthetic-lethal logic: push an already-impaired process further and p53 activation follows. Both routes tested - RNA pol I inhibition and TSR3 knockout - resensitise venetoclax-resistant cells, which is the clinically pointed result, since venetoclax resistance in NPM1-mutant AML is a live problem. Actinomycin D is an old, available drug, which makes the low-dose combination unusually translatable.

## Key points

- A conditional knockin mouse isolates NPM1c effects from comutations, showing posttranscriptional depletion of ribosome biogenesis proteins with unchanged mRNA.
- The same depletion is confirmed in human NPM1-mutant AML.
- NPM1c+ cells are preferentially sensitive to RNA polymerase I inhibition; low-dose actinomycin D resensitises venetoclax-resistant cells.
- TSR3, a 40S maturation factor, is a preferential dependency of NPM1c+ AML acting through p53-dependent apoptosis.
- Proposes targeted disruption of ribosome biogenesis as a strategy in the 30% of AML driven by NPM1 mutation.

## Limitations

The mechanism connecting NPM1c to ribosome factor depletion is not resolved - the authors offer two scenarios (loss of stabilising interaction with wild-type NPM1, or haploinsufficiency) and say the mechanisms require further investigation. Why NPM1c+ cells depend on TSR3 specifically is also 'poorly understood', including whether its enzymatic activity matters. The strategy depends on p53, so it should fail in TP53-mutant disease, which is not tested and matters because TP53 mutations emerge under venetoclax pressure. Actinomycin D is a potent, non-selective cytotoxic with a narrow therapeutic index, and 'low-dose' tolerability in combination with venetoclax is not established clinically. Resensitisation is partial. One author is employed by AstraZeneca.

## Provenance

Located in the published literature, dropped into `inbox/` as `Damaskou(2025) Blood; Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in NPM1-mutant AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2024026113`; the prose sections were written here from the paper itself.

## Citation

Damaskou et al. Blood 2025. Posttranscriptional depletion of ribosome biogenesis factors engenders therapeutic vulnerabilities in
                    <i>NPM1</i>
                    -mutant AML. doi: 10.1182/blood.2024026113

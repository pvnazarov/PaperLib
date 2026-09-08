---
# --- identity ------------------------------------------------
id: 2022-01-01_li-2022-blood-hmga1-chromatin-regulators
id_basis: filename-year
source: Li(2022) Blood; HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression.pdf
sha256: 81ac736f2f51acc9d70643c525f0f5995721a7a1b6ff3dcc05cb320141a9d49f
size_bytes: 5220951
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 243724

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2021013925"
year: 2022
title: "HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Li(2022) Blood; HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

HMGA1 is identified as a driver of myeloproliferative neoplasm progression to myelofibrosis and AML, upregulated in MPN with highest levels after transformation. Depleting HMGA1 in JAK2V617F AML cell lines disrupts proliferation, clonogenicity and leukemic engraftment, and loss of a single Hmga1 allele prevents progression to myelofibrosis in JAK2V617F mice. RNA-seq and ChIP-seq show HMGA1 networks and chromatin occupancy at proliferation genes and at the GATA2 master regulator, which HMGA1 transactivates through sequences near the +9.5 developmental enhancer; silencing GATA2 recapitulates most HMGA1-depletion phenotypes and its re-expression partially rescues leukemogenesis. HMGA1 depletion also enhances responses to ruxolitinib.

## Summary

A haploinsufficiency result is the striking one: losing a single Hmga1 allele prevents progression to myelofibrosis in JAK2V617F mice, which implies the pathway is dose-sensitive and that partial pharmacological inhibition might suffice - an unusually favourable property for a chromatin target.

The epistasis is handled with appropriate care. GATA2 silencing reproduces most of the HMGA1-depletion phenotype and GATA2 re-expression only partially rescues, from which the authors correctly conclude that GATA2 is one effector among several rather than the whole mechanism. They also distinguish HMGA1 from its better-studied paralog HMGA2 with direct evidence - barely detectable HMGA2 transcripts, and no effect of Hmga2 deficiency on progression in the same model - which is the kind of negative control that usually goes unreported.

## Key points

- HMGA1 is upregulated across MPN progression, highest after transformation to myelofibrosis or AML.
- Loss of one Hmga1 allele prevents progression to myelofibrosis in JAK2V617F mice - a dose-sensitive, therapeutically encouraging result.
- HMGA1 transactivates GATA2 via sequences near the +9.5 enhancer, increasing accessibility and recruiting active histone marks.
- GATA2 is one effector, not the whole mechanism: silencing it recapitulates most phenotypes but restoring it only partially rescues.
- HMGA1 depletion enhances ruxolitinib response, prevents myelofibrosis and prolongs survival in murine JAK2V617F models.

## Limitations

No HMGA1 inhibitor exists - HMGA1 is a non-enzymatic architectural chromatin protein and therefore a difficult pharmacological target, so every result here is genetic. The authors did not test Gata2 loss in the JAK2V617F mice because Gata2 deficiency disrupts normal hematopoiesis, which is itself a warning about targeting that axis. HMGA1 is required for normal stem cell function under homeostatic conditions by their own account, so the therapeutic window for reducing it is uncertain. Human evidence is expression association across MPN stages plus cell line work; the co-occurrence with mutant EZH2 and ASXL1 in the highest-HMGA1 blasts is noted as a hypothesis needing further study. One author is employed by Incyte, which markets ruxolitinib.

## Provenance

Located in the published literature, dropped into `inbox/` as `Li(2022) Blood; HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2021013925`; the prose sections were written here from the paper itself.

## Citation

Li et al. Blood 2022. HMGA1 chromatin regulators induce transcriptional networks involved in GATA2 and proliferation during MPN progression. doi: 10.1182/blood.2021013925

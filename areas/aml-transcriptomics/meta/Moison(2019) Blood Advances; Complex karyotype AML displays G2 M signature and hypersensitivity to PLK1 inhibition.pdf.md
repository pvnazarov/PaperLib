---
# --- identity ------------------------------------------------
id: 2019-01-01_moison-2019-blood-advances-complex-karyo
id_basis: filename-year
source: Moison(2019) Blood Advances; Complex karyotype AML displays G2 M signature and hypersensitivity to PLK1 inhibition.pdf
sha256: a62cdeb79149c414074b1f59d75654ce5eca54a79e08897eaa8fa1e141bcd53d
size_bytes: 2175195
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 128950

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/bloodadvances.2018028480"
year: 2019
title: "Complex karyotype AML displays G2/M signature and hypersensitivity to PLK1 inhibition"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Moison(2019) Blood Adv; Complex karyotype AML displays G2 M signature and hypersensitivity to PLK1 inhibition.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

RNA sequencing of the 68 complex-karyotype AML samples in the Leucegene 415-patient cohort confirms frequent TP53 alteration and characterises its allele expression and transcript changes, and documents frequent RAS pathway alteration (N/KRAS, NF1, PTPN11, BRAF) as the second most affected pathway. Chemical interrogation of genetically characterised primary samples identifies PLK1 inhibitors as the most selective agents for this subgroup, with sensitivity independent of TP53 status. CK AML specimens show a G2/M transcriptomic signature including higher PLK1 expression that correlates with inhibitor sensitivity, and volasertib shows strong anti-AML activity in xenotransplantation models.

## Summary

A vulnerability found by screening rather than reasoning, in the AML subgroup with the worst outcomes - long-term survival under 20%, falling below 5% at three years when TP53 is altered. The correlation between the G2/M signature, PLK1 expression and inhibitor sensitivity gives the finding a coherent basis, and PLK1 inhibitors were already in clinical trials, so the rationale is immediately testable.

The most useful result is a negative one that the authors handle honestly. Because PLK1 and p53 interact in cell cycle and DNA damage control, prior work suggested TP53-altered cells should be more sensitive; in these screens TP53-altered and wild-type primary AML were equally sensitive. That is not the hoped-for synthetic lethality, but it is arguably better news clinically - it means the drug works across the subgroup rather than only in part of it.

## Key points

- PLK1 inhibitors emerged as the most selective agents for complex-karyotype AML in chemical screening of genetically characterised primary samples.
- Sensitivity is independent of TP53 status, contrary to the predicted synthetic lethality - so the drug covers the whole subgroup.
- CK AML shows a G2/M transcriptomic signature with elevated PLK1 expression that correlates with sensitivity.
- The RAS pathway (N/KRAS, NF1, PTPN11, BRAF) is the second most frequently altered pathway after TP53 in this subgroup.
- Volasertib shows strong activity in xenotransplantation models of adverse human AML.

## Limitations

PLK1 inhibitors have a poor clinical record in AML - volasertib failed its phase III trial in combination with low-dose cytarabine after this work's rationale was established, largely on toxicity and lack of survival benefit, which this preclinical evidence did not predict. PLK1 is required in all dividing cells, so selectivity is relative rather than absolute and myelosuppression is the expected toxicity. The authors note that PLK1 inhibitors also act on bromodomain proteins and that the contribution of this to antileukemic activity warrants further investigation, so target attribution is not complete despite the concordance between two structurally different compounds. Sixty-eight CK AML samples from one cohort, with ex vivo sensitivity as the primary readout and xenograft activity as the in vivo test.

## Provenance

Located in the published literature, dropped into `inbox/` as `Moison(2019) Blood Adv; Complex karyotype AML displays G2 M signature and hypersensitivity to PLK1 inhibition.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/bloodadvances.2018028480`; the prose sections were written here from the paper itself.

## Citation

Moison et al. Blood Advances 2019. Complex karyotype AML displays G2/M signature and hypersensitivity to PLK1 inhibition. doi: 10.1182/bloodadvances.2018028480

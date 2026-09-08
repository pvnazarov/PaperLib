---
# --- identity ------------------------------------------------
id: 2023-01-01_waclawiczek-2023-cancer-discovery-combin
id_basis: filename-year
source: Waclawiczek(2023) Cancer Discovery; Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine Venetoclax.pdf
sha256: 8ab6dbd8d188274b585f396f093c232d22d92b63f017910acc93038c8e01cef3
size_bytes: 54570393
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 208868

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-22-0939"
year: 2023
title: "Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine/Venetoclax"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Waclawiczek(2023) Cancer Discov; Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine Venetoclax.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Integrating transcriptomic, proteomic, functional and clinical data to find predictors of azacitidine/venetoclax response, the authors found that although cultured monocytic AML cells showed upfront resistance, monocytic differentiation was not clinically predictive in their patient cohort. Leukemic stem cells were the primary targets whose elimination determined outcome, and LSCs of refractory patients showed perturbed apoptotic dependencies. A flow cytometry-based Mediators of Apoptosis Combinatorial score (MAC-Score), combining BCL2, BCL-xL and MCL1 protein expression in LSCs, predicted initial response with positive predictive value above 97% and was associated with increased event-free survival, validated across four patient cohorts including salvage therapy.

## Summary

Directly contradicts a widely accepted biomarker and replaces it with a better one. Monocytic differentiation is the standard explanation for venetoclax resistance, supported by strong mechanistic work elsewhere in this collection - and here cultured monocytic cells did show upfront resistance, yet monocytic differentiation failed to predict clinical response in patients. The resolution is that what matters is not the bulk phenotype but the apoptotic dependency of the leukemic stem cells.

The MAC-Score is designed for use rather than for publication: a flow cytometry ratio of three proteins in LSC-like cells, with a defined threshold of 0.4, validated across separate cohorts including relapsed/refractory salvage patients, and independent of genetics in multivariable analysis. A positive predictive value above 97% is unusual for any AML biomarker.

## Key points

- Monocytic differentiation predicted resistance in culture but not in patients - contradicting the accepted biomarker.
- Leukemic stem cells are the population whose elimination determines outcome; refractory patients' LSCs show perturbed apoptotic dependencies.
- The MAC-Score combines BCL2, BCL-xL and MCL1 protein levels in LSC-like cells by flow cytometry, with a threshold of 0.4.
- Positive predictive value above 97% for initial response, associated with event-free survival, and independent of genetics on multivariable analysis.
- Validated across four cohorts including relapsed/refractory patients receiving salvage therapy.

## Limitations

Cohorts are modest - 59 patients in the multivariable analysis and 23 in the salvage cohort - and the 0.4 threshold is defined on the same data, so performance in a truly independent prospective setting is untested. Genotype subgroup analyses (RUNX1-mutant, complex karyotype) rest on 2 to 8 patients per arm. The score requires flow cytometric intracellular staining of three proteins within a defined LSC-like gate, which demands standardisation across laboratories that the paper does not establish. It predicts initial response; whether acting on it improves outcomes has not been tested. The discrepancy with the monocytic-differentiation literature is reported but not mechanistically reconciled.

## Provenance

Located in the published literature, dropped into `inbox/` as `Waclawiczek(2023) Cancer Discov; Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine Venetoclax.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-22-0939`; the prose sections were written here from the paper itself.

## Citation

Waclawiczek et al. Cancer Discovery 2023. Combinatorial BCL2 Family Expression in Acute Myeloid Leukemia Stem Cells Predicts Clinical Response to Azacitidine/Venetoclax. doi: 10.1158/2159-8290.CD-22-0939

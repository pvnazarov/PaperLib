---
# --- identity ------------------------------------------------
id: 2025-01-01_m-tois-2025-biomarker-research-il1rap-is
id_basis: filename-year
source: Métois(2025) Biomarker Research; IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia.pdf
sha256: 8f69f35186b6a26b54f65cd0a8c7e98a66e75c7c4ce638917b46cfe675a33653
size_bytes: 3768653
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 84709

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s40364-025-00769-z"
year: 2025
title: "IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Métois(2025) Biomark Res; IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Seeking surface antigens for immunotherapy in normal-karyotype triple-mutated AML (NPM1c with FLT3-ITD and DNMT3A), the authors performed surface proteome enrichment on 100 primary AML samples including 12 NKt-AML, transcriptome analysis on 691 samples, and single-cell RNA sequencing on 23. IL1RAP is identified as expressed on primitive AML cells resembling leukemic stem cells in NKt-AML while relatively low on normal bone marrow HSCs. Elevated IL1RAP associates with poor overall and relapse-free survival and predicts non-response to hematopoietic stem cell transplantation, and IL1RAP protein internalises after antibody exposure, supporting antibody-drug conjugate development.

## Summary

Targets the specific genotype that spoils an otherwise favourable prognosis. NPM1-mutant normal-karyotype AML does well unless FLT3-ITD is present, and the triple-mutant combination with DNMT3A is particularly hard to eradicate - so a subgroup-directed antigen is worth more than a general one.

The evidence is assembled in the right order for an immunotherapy target: expressed on the primitive cells that cause relapse, relatively spared on normal HSCs, prognostically meaningful, and - the step most antigen papers omit - internalised on antibody binding, which is the property an antibody-drug conjugate actually requires. That IL1RAP-directed agents already exist in early clinical development for other indications makes the patient-selection contribution the useful part.

## Key points

- IL1RAP is expressed on primitive, LSC-like cells in NK triple-mutated AML but relatively low on normal bone marrow HSCs.
- High IL1RAP associates with poor overall and relapse-free survival and predicts non-response to transplant.
- The protein internalises after antibody binding, the specific property an antibody-drug conjugate needs.
- Multi-omic approach: surface proteomics on 100 samples, transcriptome on 691, single-cell RNA-seq on 23.
- t(6;9) and t(8;21) AML also express significant IL1RAP, suggesting broader application.

## Limitations

The authors list their own limitations clearly. Surface proteomics covered 100 samples of which only 12 were NKt-AML, too few to characterise antigen heterogeneity within the subgroup or to give good statistical power. Flow cytometry validation was robust for NKt-AML but did not cover the other subgroups - t(8;21) and t(6;9) - that showed high IL1RAP in the omics data, so the broader application is unvalidated. Most importantly, no in vivo antibody-drug conjugate experiment in patient-derived xenografts was performed, which the authors say would be needed to assess efficacy and off-target effects before clinical translation. 'Relatively low' expression on normal HSCs is not absence, and the therapeutic window for an ADC against a marrow antigen depends on exactly that margin.

## Provenance

Located in the published literature, dropped into `inbox/` as `Métois(2025) Biomark Res; IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s40364-025-00769-z`; the prose sections were written here from the paper itself.

## Citation

Métois et al. Biomarker Research 2025. IL1RAP is an immunotherapeutic target for normal karyotype triple-mutated acute myeloid leukemia. doi: 10.1186/s40364-025-00769-z

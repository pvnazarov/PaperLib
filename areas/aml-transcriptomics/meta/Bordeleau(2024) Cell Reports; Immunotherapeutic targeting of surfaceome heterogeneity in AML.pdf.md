---
# --- identity ------------------------------------------------
id: 2024-01-01_bordeleau-2024-cell-reports-immunotherap
id_basis: filename-year
source: Bordeleau(2024) Cell Reports; Immunotherapeutic targeting of surfaceome heterogeneity in AML.pdf
sha256: df1dbb765064f99c5301d75db112d294f1cc230f92c85176d6d19497e55054d5
size_bytes: 6928788
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 350480

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2024.114260"
year: 2024
title: "Immunotherapeutic targeting of surfaceome heterogeneity in AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Bordeleau(2024) Cell Rep; Immunotherapeutic targeting of surfaceome heterogeneity in AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A surface proteome analysis of 100 genetically diverse primary human AML specimens, combined with single-cell transcriptomics on a subset to assess antigen expression at sub-population level. The effort identifies numerous antigens and markers preferentially expressed by primitive AML cells, many of them already targeted by therapeutic antibodies in clinical evaluation for other cancers, and characterises AML heterogeneity at the surfaceome level by identifying antigens and candidate primitive-cell markers specific to genetic subgroups including KMT2A-r, NPM1-mut, NK triple-mut, inv(16), complex karyotype and RUNX1-mut. The dataset is released publicly through LASA.

## Summary

A resource built around a specific gap: AML has exactly one approved therapeutic antibody, gemtuzumab ozogamicin, and it helps favourable-risk patients while failing adverse-risk ones. This asks the surfaceome directly what else could be targeted, and answers per genetic subgroup rather than for AML as a whole.

The design choice that matters is pairing proteomics with single-cell RNA-seq. A surface protein averaged over a bulk sample says nothing about whether the primitive cells that cause relapse carry it, and the sub-population analysis is what turns a list of antigens into candidate LSC targets. ENG for complex-karyotype and MECOM-rearranged AML is their worked example for a poor-prognosis subgroup, and the antigen-pair analysis for combination targeting is a sensible extension of the same logic.

## Key points

- Largest surface proteome dataset of primary human AML reported at the time - 100 genetically diverse specimens - released publicly as LASA.
- Antigens are reported per genetic subgroup, not for AML in aggregate, which is the level at which immunotherapy has been failing.
- Single-cell transcriptomics assesses whether an antigen is on primitive cells, distinguishing candidate LSC targets from bulk blast markers.
- 19 identified antigens are already targeted by therapeutic antibodies in clinical development, most with phase I safety established.
- ENG is proposed for complex-karyotype and MECOM-rearranged AML; antigen pairs are shown to cover more cells than either alone.

## Limitations

A discovery resource, and the authors present it as one: no antigen here is functionally validated as a therapeutic target, and no killing, CAR-T or antibody experiment is reported. Surface proteomics on primary specimens is sensitive to sample handling and to the capture chemistry, and detection depends on abundance, so absence from the list is not evidence of absence on the cell. The critical missing comparison is normal hematopoietic tissue - an antigen 'preferentially expressed by primitive AML cells' relative to other AML cells may still be shared with normal HSCs, which is what determines whether targeting it is tolerable, and CD33 is the cautionary precedent. Single-cell transcriptome is used as a proxy for protein at the sub-population level, and the two correlate imperfectly for surface proteins. Subgroup sizes within 100 specimens are small.

## Provenance

Located in the published literature, dropped into `inbox/` as `Bordeleau(2024) Cell Rep; Immunotherapeutic targeting of surfaceome heterogeneity in AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2024.114260`; the prose sections were written here from the paper itself.

## Citation

Bordeleau et al. Cell Reports 2024. Immunotherapeutic targeting of surfaceome heterogeneity in AML. doi: 10.1016/j.celrep.2024.114260

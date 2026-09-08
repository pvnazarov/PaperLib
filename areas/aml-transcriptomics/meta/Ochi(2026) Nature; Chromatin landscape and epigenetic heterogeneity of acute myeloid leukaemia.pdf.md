---
# --- identity ------------------------------------------------
id: 2026-01-01_ochi-2026-nature-chromatin-landscape-and
id_basis: filename-year
source: Ochi(2026) Nature; Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia.pdf
sha256: 02775576d76a032f832ad63502d380ddbb86465881925d0134885b93bf20f0ee
size_bytes: 58837121
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 287877

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-026-10703-4"
year: 2026
title: "Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ochi(2026) Nature; Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

ATAC-seq in 1563 individuals with newly diagnosed AML (the eCHROMA cohort) classifies the disease into 16 subgroups by chromatin accessibility. Multiomics analysis of mutations, transcriptome, DNA methylation and histone marks shows these subgroups have distinct driver mutations, differentiation states, expression, methylation and super-enhancer profiles, and are associated with clinical outcomes, validated in independent cohorts. Single-cell ATAC shows all leukemic cells within a subgroup share a common accessibility profile. The subgroups have distinct gene-regulatory networks driven by hematopoietic transcription factors with subgroup-specific super-enhancers, have independent prognostic effect beyond genomic classification, and are associated with particular drug sensitivities.

## Summary

The largest epigenomic dataset assembled for any single cancer, and the finding that justifies the scale is that most of the 16 chromatin subgroups are not defined by known genomic alterations or combinations of them, and do not correspond to WHO, ICC or ELN categories. They are genuinely new AML subtypes, visible only epigenetically.

Two results make this more than a taxonomy. The subgroups carry independent prognostic information beyond genomic classification, which is the test any new classification must pass; and single-cell ATAC shows that all leukemic cells within a subgroup share the accessibility profile, so these are coherent epigenomic fingerprints rather than averages over mixed populations - the objection that would otherwise apply to bulk chromatin profiling of a heterogeneous disease.

## Key points

- ATAC-seq across 1563 newly diagnosed AML patients - the most comprehensive epigenomic dataset for a single cancer type.
- Sixteen chromatin accessibility subgroups, most of which do not correspond to any conventional genetic classification.
- Subgroups have independent prognostic effect beyond genomic classification and distinct drug sensitivities.
- Single-cell ATAC confirms all leukemic cells in a subgroup share the accessibility profile, so subgroups are not artefacts of cellular mixing.
- Subgroup-specific super-enhancers and hematopoietic transcription factor networks provide the mechanistic basis.

## Limitations

Sixteen subgroups derived by clustering a large dataset is a choice about granularity, and the paper does not establish that 16 is the right number rather than a defensible one; clinical utility depends on subgroups being reproducible in new samples, which the independent-cohort validation addresses but does not settle for every subgroup. Prognostic and drug sensitivity associations are retrospective, with treatment heterogeneous across contributing cohorts. ATAC-seq is technically demanding and sensitive to sample handling, cell viability and blast content - substantial obstacles to deploying it as a clinical assay. Drug sensitivities come from ex vivo screening. No functional experiment tests whether the subgroup-defining super-enhancers or transcription factor networks are required for the phenotype; the resource is descriptive by design.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ochi(2026) Nature; Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-026-10703-4`; the prose sections were written here from the paper itself.

## Citation

Ochi et al. Nature 2026. Chromatin landscape and epigenetic heterogeneity of acute myeloid leukaemia. doi: 10.1038/s41586-026-10703-4

---
# --- identity ------------------------------------------------
id: 2025-01-01_voss-2025-leukemia-clinical-experience-o
id_basis: filename-year
source: Voss(2025) Leukemia; Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagnosis and risk assessment.pdf
sha256: 31084e97a777c59c063657f1670cff286a994f42cca61f16c313dcf214983d7c
size_bytes: 1983189
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 101373

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-025-02774-5"
year: 2025
title: "Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagnosis and risk assessment"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Voss(2025) Leukemia; Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagn.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A systematic review of real-time clinical experience with integrated whole genome and whole transcriptome sequencing (iWGS-WTS) for pediatric AML diagnostic workup at a single institution, comparing results against whole genome sequencing, whole exome sequencing, whole transcriptome sequencing, cytogenetics and targeted panel NGS. The integrated approach improved identification of clinically relevant alterations, enhancing disease classification and risk assessment; 18 AML-driver gene fusions found by iWGS-WTS were missed by karyotyping owing to their cryptic or complex nature, and combining copy number analysis with soft-clipped reads identified 12 small CNVs under 10 kb that SNP arrays would miss. It also streamlines sample acquisition and reduces testing redundancy.

## Summary

A practical implementation study rather than a discovery paper, and valuable because it reports what happened when a comprehensive genomics workflow was actually run clinically since 2016. The concrete number carries the argument: 18 driver fusions missed by karyotyping in real diagnostic cases.

It is also careful about where the new approach is worse. Conventional cytogenetics gives single-cell resolution while WGS gives a population-level view, so WGS may miss subclonal numerical abnormalities present in under 30-40% of cells - though the authors note none of the undetected subclonal events in their series were of established clinical significance. The comparison with optical genome mapping is similarly even-handed, noting its limitations in ploidy detection and inability to call small variants.

## Key points

- Real-world clinical implementation, comparing iWGS-WTS against cytogenetics, panels, WGS, WES and WTS in the same workflow.
- 18 AML-driver fusions identified by iWGS-WTS were missed by karyotyping because they were cryptic or complex.
- Combining CNV analysis with soft-clipped reads found 12 small CNVs under 10 kb that SNP arrays would miss.
- WGS gives a population-level view and may miss subclonal numerical abnormalities below 30-40% of cells, where cytogenetics has single-cell resolution.
- Consolidating tests reduces redundancy and sample requirements, which matters in pediatric practice.

## Limitations

A single-institution retrospective review of a specialist paediatric centre's practice, so the workflow, expertise and case mix are not representative of general diagnostic laboratories; cost and infrastructure requirements are not addressed. The comparison is not blinded or prospective, and improved classification is measured against the institution's own interpretation rather than against outcome. Turnaround time is raised as critical for AML decisions but is discussed rather than quantified in the summary evidence. No demonstration that the additional findings changed treatment or improved survival - the benefit is in detection, with clinical utility assumed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Voss(2025) Leukemia; Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagn.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-025-02774-5`; the prose sections were written here from the paper itself.

## Citation

Voss et al. Leukemia 2025. Clinical experience of using integrated whole genome and transcriptome sequencing as a framework for pediatric and adolescent acute myeloid leukemia diagnosis and risk assessment. doi: 10.1038/s41375-025-02774-5

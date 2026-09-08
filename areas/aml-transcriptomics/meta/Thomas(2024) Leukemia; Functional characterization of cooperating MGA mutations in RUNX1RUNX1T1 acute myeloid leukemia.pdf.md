---
# --- identity ------------------------------------------------
id: 2024-01-01_thomas-2024-leukemia-functional-characte
id_basis: filename-year
source: Thomas(2024) Leukemia; Functional characterization of cooperating MGA mutations in RUNX1RUNX1T1 acute myeloid leukemia.pdf
sha256: 4ea71b257d01d15642d8adbe7be3ff10bc52ded6127b334bf127831d66df4231
size_bytes: 3275230
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 133340

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-024-02193-y"
year: 2024
title: "Functional characterization of cooperating MGA mutations in RUNX1::RUNX1T1 acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Thomas(2024) Leukemia; Functional characterization of cooperating MGA mutations in RUNX1 RUNX1T1 acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

MGA, a dual-specificity transcription factor that negatively regulates MYC-target genes and is part of the non-canonical polycomb repressive complex PRC1.6, carries recurrent loss-of-function mutations in AML with RUNX1::RUNX1T1. Representative patient mutations abolish protein-protein interactions and transcriptional activity. Using human and mouse systems including a new conditional knockout strain, MGA loss upregulates MYC and E2F targets, cell cycle genes, mTOR signalling and oxidative phosphorylation in normal hematopoietic cells, opening chromatin at cell cycle and proliferation gene promoters and enhancing proliferation. RUNX1::RUNX1T1 expression in Mga-deficient cells produces more aggressive AML with significantly shortened latency - median survival 177 days for controls, 146 for heterozygous and 132 for null.

## Summary

Tests a cooperating mutation properly rather than inferring cooperation from co-occurrence. The gene-dose effect on latency across wild-type, heterozygous and null animals is the clearest evidence, and it matters that heterozygous loss - the state actually seen in patients, since MGA alterations are heterozygous - already shortens survival.

The conditional knockout was necessary because constitutive MGA deficiency is embryonically lethal, which is why the gene had gone unstudied in hematopoiesis despite recurring across several hematological malignancies. The chromatin result is reported honestly against expectation: H2AK119Ub1 did not change on MGA depletion, which the authors find surprising and interpret as functional redundancy with other PRC1 complexes, while decreased H3K27me3 and increased H3K27ac indicate derepression by another route.

## Key points

- Patient-derived MGA mutations abolish protein-protein interactions and transcriptional activity, confirming loss of function.
- A conditional knockout circumvents the embryonic lethality that had prevented study of MGA in hematopoiesis.
- MGA loss upregulates MYC and E2F targets, cell cycle genes, mTOR signalling and oxidative phosphorylation, and opens chromatin at proliferation promoters.
- Cooperation with RUNX1::RUNX1T1 shows a gene-dose effect on leukemia latency: 177, 146 and 132 days for wild-type, heterozygous and null.
- H2AK119Ub1 was unchanged despite MGA loss, implying redundancy with other PRC1 complexes; H3K27me3 fell and H3K27ac rose.

## Limitations

Mouse genetics with human cell line work; RUNX1::RUNX1T1 is expressed as the 9a truncated isoform by transduction rather than arising from a translocation, and requires cooperating events in any case. Latency differences, while dose-dependent, are modest - 30 to 45 days - so the cooperation is real but not dramatic. The mechanism by which derepression occurs is incompletely resolved given the unchanged H2AK119Ub1, and the authors' redundancy explanation is inferred rather than tested. No therapeutic implication is developed: MGA is a lost tumour suppressor, so the finding identifies a biology rather than a target, and the upregulated pathways it implicates - MYC, E2F, mTOR, oxidative phosphorylation - are not selective to this genotype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Thomas(2024) Leukemia; Functional characterization of cooperating MGA mutations in RUNX1 RUNX1T1 acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-024-02193-y`; the prose sections were written here from the paper itself.

## Citation

Thomas et al. Leukemia 2024. Functional characterization of cooperating MGA mutations in RUNX1::RUNX1T1 acute myeloid leukemia. doi: 10.1038/s41375-024-02193-y

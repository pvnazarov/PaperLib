---
# --- identity ------------------------------------------------
id: 2022-01-01_yan-2022-cancer-discovery-kat6a-and-enl
id_basis: filename-year
source: Yan(2022) Cancer Discovery; KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs.pdf
sha256: 037a278379e8af552c801ef6d722ff672493f588afececa4e27ec697a938b3dc
size_bytes: 2816718
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 153993

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-20-1459"
year: 2022
title: "KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yan(2022) Cancer Discov; KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A differentiation-focused CRISPR screen in AML cells identified the histone acetyltransferase KAT6A as a regulator of myeloid differentiation driving leukemogenic gene expression programs. KAT6A initiates a transcriptional control module in which KAT6A-catalysed promoter H3K9ac is bound by the acetyllysine reader ENL, which in turn cooperates with chromatin factors to induce transcriptional elongation. KAT6A inhibition has strong anti-AML effects in vitro and in vivo, supporting small-molecule KAT6A inhibitors for mono or combinatorial differentiation-based treatment.

## Summary

Supplies the missing half of an established mechanism. ENL was shown to read H3K9ac at AML oncogene promoters and recruit the super elongation complex, but the writer producing that mark was unknown - and identifying KAT6A completes a writer-reader module operating at promoters, where most AML chromatin work has concentrated on enhancers.

The target has an attractive property the authors state explicitly: wild-type proteins co-opted to support aberrant transcription are generally better therapeutic targets than the transcription factors they serve. KAT6A was known only as the fusion partner in the rare MOZ-TIF2 translocation, and its wild-type role in leukemia differentiation had not been described. The paper also places it among several MYST-family acetyltransferases with distinct roles - HBO1/KAT7 acetylating H3K14 to sustain leukemia stem cells, MOF/KAT8 acetylating H4K16 for DNA repair genes - so multiple HATs are needed but not interchangeably.

## Key points

- A differentiation-focused rather than viability-focused CRISPR screen identifies regulators of AML cell fate.
- KAT6A is the H3K9 acetyltransferase whose mark ENL reads at AML oncogene promoters - completing a writer-reader module.
- The module drives transcriptional elongation at MYC, MYB and other regulators of AML cell fate.
- Addresses promoter regulation, where AML chromatin research has concentrated on enhancers.
- Wild-type KAT6A, not only the rare MOZ-TIF2 fusion, is a dependency - and co-opted wild-type proteins make better targets than transcription factors.

## Limitations

KAT6A small-molecule inhibitors are proposed as being of high therapeutic interest, but the anti-AML data here rest on genetic inhibition and available tool compounds rather than a clinical candidate. Differentiation therapy has succeeded only in APL and shows promise in IDH-mutant AML; extending it further is the aim rather than the demonstrated result. The writer-reader model is supported by the co-occurrence of KAT6A activity, H3K9ac and ENL binding rather than by an experiment separating KAT6A's contribution to ENL recruitment from its other effects. KAT6A is required in normal hematopoiesis and development, so the therapeutic window is not established. Work is largely in AML cell lines with in vivo models.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yan(2022) Cancer Discov; KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-20-1459`; the prose sections were written here from the paper itself.

## Citation

Yan et al. Cancer Discovery 2022. KAT6A and ENL Form an Epigenetic Transcriptional Control Module to Drive Critical Leukemogenic Gene-Expression Programs. doi: 10.1158/2159-8290.CD-20-1459

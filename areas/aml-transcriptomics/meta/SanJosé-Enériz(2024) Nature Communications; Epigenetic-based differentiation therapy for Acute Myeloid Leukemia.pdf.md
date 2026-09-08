---
# --- identity ------------------------------------------------
id: 2024-01-01_sanjos-en-riz-2024-nature-communications
id_basis: filename-year
source: SanJosé-Enériz(2024) Nature Communications; Epigenetic-based differentiation therapy for Acute Myeloid Leukemia.pdf
sha256: 19f6a45d3ca25a6503912670330f85c58cad4bd51490e2b3c0de7badcf9601f5
size_bytes: 5844260
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 167058

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-024-49784-y"
year: 2024
title: "Epigenetic-based differentiation therapy for Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as SanJosé-Enériz(2024) Nat Commun; Epigenetic-based differentiation therapy for Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Two lysine deacetylase inhibitors, CM-444 and CM-1758, are identified and characterised as promoting myeloid differentiation across all AML subtypes at low non-cytotoxic doses, unlike other commercial HDAC inhibitors. Acetylome analysis after treatment reveals modulation of non-histone proteins in the enhancer-promoter chromatin regulatory complex, including bromodomain proteins, and this acetylation is essential for enhancing expression of the transcription factors that drive the differentiation response. The compounds are proposed as differentiation-based therapeutic agents applicable across AML subtypes.

## Summary

Attempts to generalise the acute promyelocytic leukemia success - where ATRA cures a subtype representing about 10% of AML - to the other 90%, and does so by combining epigenetic and differentiation therapy rather than treating them as separate strategies. Working at low non-cytotoxic doses is the key design choice: the aim is maturation, not killing.

The mechanistic finding is that what matters is not histone acetylation. Comparing the acetylome against panobinostat and vorinostat, the authors find large differences between the four inhibitors' acetylation signatures and close similarity between their own two, and conclude that acetylation of non-histone proteins in the enhancer-promoter complex - bromodomain proteins in particular - is more important than classical histone acetylation for inducing the differentiation transcription factors. That reframes what a deacetylase inhibitor is doing.

## Key points

- CM-444 and CM-1758 induce myeloid differentiation across all AML subtypes at low, non-cytotoxic doses.
- Other commercial HDAC inhibitors do not achieve this, and their acetylome signatures differ substantially.
- The mechanism runs through acetylation of non-histone proteins in the enhancer-promoter complex, including bromodomain proteins - not classical histone acetylation.
- This acetylation is required to raise expression of the transcription factors that drive differentiation.
- Aimed at extending differentiation therapy from APL, about 10% of AML, to the remaining subtypes.

## Limitations

Entirely preclinical, with two experimental compounds and no clinical data. The authors themselves note that approved HDAC inhibitors have had modest success in AML and carry serious toxicity - severe cardiac effects, myelosuppression, gastrointestinal and hepatic effects - and their claim that these next-generation compounds overcome those limitations rests on the low doses required for differentiation rather than on any toxicity study presented. 'All AML subtypes' is established across cell lines representing subtypes, not across patient samples spanning them. Differentiation is measured by marker and morphology readouts rather than by functional maturation or in vivo disease control in the summary evidence. The mechanistic claim that non-histone acetylation matters more than histone acetylation is inferred from acetylome comparison rather than from separating the two experimentally.

## Provenance

Located in the published literature, dropped into `inbox/` as `SanJosé-Enériz(2024) Nat Commun; Epigenetic-based differentiation therapy for Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-024-49784-y`; the prose sections were written here from the paper itself.

## Citation

SanJosé-Enériz et al. Nature Communications 2024. Epigenetic-based differentiation therapy for Acute Myeloid Leukemia. doi: 10.1038/s41467-024-49784-y

---
# --- identity ------------------------------------------------
id: 2025-01-01_zehtabcheh-2025-biomarker-research-insig
id_basis: filename-year
source: Zehtabcheh(2025) Biomarker Research; Insights into KMT2A rearrangements in acute myeloid leukemia from molecular characteristics to targeted therapies.pdf
sha256: 2f198b94119ae2e28fcbb149e0c75dbc4bd36c964a5145b14c2fd71bffadb348
size_bytes: 1504203
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 96798

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s40364-025-00786-y"
year: 2025
title: "Insights into KMT2A rearrangements in acute myeloid leukemia: from molecular characteristics to targeted therapies"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zehtabcheh(2025) Biomark Res; Insights into KMT2A rearrangements in acute myeloid leukemia from molecular characteristics to targeted therapies.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of KMT2A-rearranged AML, found in 3-10% of adult cases and associated with resistance to standard treatment and high relapse. It covers how the chimeric proteins disrupt epigenetic regulation and activate HOXA and MEIS1 by recruiting menin and DOT1L; diagnostic approaches from FISH and RT-PCR to next-generation sequencing and machine learning models that predict KMT2A rearrangement from transcriptomic data and identify biomarkers such as LAMP5 and SKIDA1; and the therapeutic shift to menin inhibitors (revumenib, ziftomenib), DOT1L inhibitors (pinometostat), WDR5 inhibitors and PROTAC-mediated degradation. Remaining challenges include optimising measurable residual disease monitoring, overcoming resistance and validating biomarkers.

## Summary

A current survey of the subtype that this collection covers most heavily in primary form, written after the first FDA approval of a menin inhibitor - so it is useful mainly as an orientation to where the field stands and what is being tried next.

The forward-looking content is the more informative part: WDR5 inhibitors and PROTAC-mediated degradation as alternatives to occupancy-based menin inhibition, machine-learning prediction of KMT2A rearrangement from expression with LAMP5 and SKIDA1 as markers, and CD123-directed CAR T-cell approaches proposed for combination with menin inhibitors. The authors are appropriately direct that patient selection criteria and predictive biomarkers are still evolving, and that the influence of genetic and clinical factors beyond KMT2A rearrangement and NPM1 mutation on treatment response is not understood.

## Key points

- Orientation to KMT2A-rearranged AML after the first FDA approval of a menin inhibitor.
- Machine learning on transcriptomic data can predict KMT2A rearrangement and identifies LAMP5 and SKIDA1 as biomarkers.
- Surveys the therapeutic shift from chemotherapy through menin and DOT1L inhibitors to WDR5 inhibitors and PROTAC degradation.
- CD123-directed CAR T-cell therapies are proposed for combination with menin inhibitors.
- Patient selection criteria and predictive biomarkers remain unresolved, as do clonal heterogeneity and resistance mechanisms.

## Limitations

A narrative review by a student research group, without systematic search or evidence appraisal, and its tone is notably promotional - phrases such as 'renewed hope', 'transformative era' and 'poised to redefine prognostic paradigms' overstate a field where menin inhibitor responses are incomplete, resistance is rapid, and DOT1L inhibitors have already underperformed clinically. Reported KMT2A-r frequency is inconsistent within the paper, given as 3-10% in the abstract and 3-6% in the introduction. Machine-learning biomarkers and immunotherapy approaches are described from single studies without appraisal. The review adds synthesis rather than new evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zehtabcheh(2025) Biomark Res; Insights into KMT2A rearrangements in acute myeloid leukemia from molecular characteristics to targeted therapies.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s40364-025-00786-y`; the prose sections were written here from the paper itself.

## Citation

Zehtabcheh et al. Biomarker Research 2025. Insights into KMT2A rearrangements in acute myeloid leukemia: from molecular characteristics to targeted therapies. doi: 10.1186/s40364-025-00786-y

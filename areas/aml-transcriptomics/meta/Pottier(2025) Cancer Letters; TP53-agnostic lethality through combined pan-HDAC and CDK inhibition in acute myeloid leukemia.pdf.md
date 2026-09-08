---
# --- identity ------------------------------------------------
id: 2025-01-01_pottier-2025-cancer-letters-tp53-agnosti
id_basis: filename-year
source: Pottier(2025) Cancer Letters; TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia.pdf
sha256: 04078f5e207525d07bbe724e494cb905ce7a05f2546e6f52a32b31228fb6f887
size_bytes: 14981299
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 100934

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.canlet.2025.218011"
year: 2025
title: "TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Pottier(2025) Cancer Lett; TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Simultaneous inhibition of cyclin-dependent kinases and histone deacetylases with dinaciclib and CAY10603 is reported to eliminate the therapeutic response gap between TP53-mutant and TP53 wild-type AML. Biochemical profiling showed CAY10603 has pan-HDAC activity similar to SAHA rather than being HDAC6-selective as assumed. Across parental wild-type lines and isogenic TP53 mutants the combination suppressed clonogenic growth, induced caspase-dependent apoptosis, downregulated CDK2, CDK4/6 and their cyclins along with MYC and E2F1, and restored CDKN1A/p21. In an orthotopic NSG model it reduced leukemia burden and extended survival without adverse toxicity.

## Summary

Aims at the group that every other strategy in this collection excludes. TP53-mutant AML resists chemotherapy and venetoclax-azacitidine, and the paper's introduction is a useful catalogue of what has failed there - magrolimab stopped for futility, eprenetapopt reaching 17% complete remission and failing phase III, flotetuzumab giving transient responses with about 4 months survival. A TP53-agnostic mechanism is worth pursuing precisely because p53-restoring approaches have not worked.

The logic is to bypass p53 rather than restore it: HDAC inhibition restores p21 independently of p53 and suppresses MYC, CDK inhibition removes the cell cycle drivers TP53-mutant cells rely on, and together they normalise mutant cells to behave like wild-type. A useful incidental finding is that CAY10603, widely used as an HDAC6-selective probe, is actually a pan-HDAC inhibitor - which matters for interpreting other work that used it as a selective tool.

## Key points

- Combined dinaciclib and CAY10603 closes the response gap between TP53-mutant and wild-type AML - a TP53-agnostic mechanism.
- CAY10603, generally treated as HDAC6-selective, is shown to have pan-HDAC activity comparable to SAHA.
- The combination restores p21 independently of p53 and downregulates CDK2, CDK4/6, cyclins, MYC and E2F1.
- Tested across parental and isogenic TP53-mutant pairs, which isolates the effect of TP53 status.
- Reduced burden and extended survival in an orthotopic NSG model without reported adverse toxicity.

## Limitations

Both agents have difficult clinical histories: dinaciclib has repeatedly failed to establish itself in hematologic malignancy on toxicity and efficacy grounds, and pan-HDAC inhibitors are broadly toxic, with myelosuppression the dose-limiting problem when treating a marrow disease - so 'without adverse toxicity' in short mouse experiments is weak reassurance for this pairing. CAY10603 is a chemical probe, not a clinical candidate. The isogenic TP53-mutant lines are engineered rather than patient-derived, and the in vivo work uses cell-line xenografts. Neither agent is selective, so 'dual targeting of transcriptional and cell cycle pathways' describes a broadly cytotoxic combination whose therapeutic index is the unanswered question. No primary TP53-mutant patient sample or patient-derived xenograft experiment is reported in the summary evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Pottier(2025) Cancer Lett; TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.canlet.2025.218011`; the prose sections were written here from the paper itself.

## Citation

Pottier et al. Cancer Letters 2025. TP53-agnostic lethality through combined pan-HDAC and CDK inhibition in acute myeloid leukemia. doi: 10.1016/j.canlet.2025.218011

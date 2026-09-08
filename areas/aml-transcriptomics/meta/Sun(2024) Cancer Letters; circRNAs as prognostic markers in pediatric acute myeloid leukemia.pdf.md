---
# --- identity ------------------------------------------------
id: 2024-01-01_sun-2024-cancer-letters-circrnas-as-prog
id_basis: filename-year
source: Sun(2024) Cancer Letters; circRNAs as prognostic markers in pediatric acute myeloid leukemia.pdf
sha256: f1c980767f507947aaa0efd57b2f67a053ae14c985d405babc4ffc3368a2ac2f
size_bytes: 10181462
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 73026

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.canlet.2024.216880"
year: 2024
title: "circRNAs as prognostic markers in pediatric acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Sun(2024) Cancer Lett; circRNAs as prognostic markers in pediatric acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A genome-wide analysis of circular RNAs from RNA-seq data in pediatric AML identified a group associated with inferior outcomes and acting on cancer-related pathways, several transcribed from genes with established AML functions including circRUNX1, circWHSC1 and circFLT3. An increased number of circRNAs and of linear RNA splicing events correlated significantly with worse clinical outcome, implicating splicing dysregulation. Upregulated RNA binding proteins were identified in AMLs with high circRNA numbers, with TROVE2 prominent; TROVE2 binds flanking intron Alu sequences and participates in circRNA processing, and linear TROVE2 expression associated with prognosis, validated in the pediatric TARGET and adult BeatAML2 cohorts.

## Summary

The prognostic signal turns out to be quantitative rather than specific: it is the overall number of circRNAs, alongside increased linear splicing, that tracks with poor outcome - which points at global splicing dysregulation as the underlying phenomenon rather than at any individual circRNA.

Following that to an RNA binding protein is the useful step. TROVE2 tops the list of upregulated RBPs in dysregulated cases, and the eCLIP analysis showing it binds flanking intron Alu sequences supplies a plausible mechanism, since Alu pairing is the canonical driver of back-splicing. That linear TROVE2 expression is prognostic in two independent cohorts, pediatric and adult, makes it a more tractable biomarker than a circRNA panel would be.

## Key points

- Circular RNAs associated with inferior outcome in pediatric AML include circRUNX1, circWHSC1 and circFLT3.
- The prognostic signal is quantitative - the number of circRNAs and of linear splicing events - implicating global splicing dysregulation.
- TROVE2 is the most upregulated RNA binding protein in AMLs with high circRNA numbers.
- eCLIP shows TROVE2 binds flanking intron Alu sequences, the canonical driver of back-splicing.
- Linear TROVE2 expression is prognostic and validates in independent pediatric TARGET and adult BeatAML2 cohorts.

## Limitations

The authors state that the detailed function of TROVE2 requires further investigation - its role in circRNA processing is inferred from binding position in K562 cells plus correlation, with no perturbation experiment. No circRNA is functionally tested, so the association between circRNA burden and outcome is not shown to be causal and may simply mark a more dysregulated transcriptome. circRNA quantification from total RNA-seq is sensitive to library preparation and to the detection algorithm, and circRNA counts scale with sequencing depth and RNA quality, which is a concern when the prognostic variable is a count. The 25 nominated drugs come from integrating public drug sensitivity data with expression, without testing. Retrospective throughout.

## Provenance

Located in the published literature, dropped into `inbox/` as `Sun(2024) Cancer Lett; circRNAs as prognostic markers in pediatric acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.canlet.2024.216880`; the prose sections were written here from the paper itself.

## Citation

Sun et al. Cancer Letters 2024. circRNAs as prognostic markers in pediatric acute myeloid leukemia. doi: 10.1016/j.canlet.2024.216880

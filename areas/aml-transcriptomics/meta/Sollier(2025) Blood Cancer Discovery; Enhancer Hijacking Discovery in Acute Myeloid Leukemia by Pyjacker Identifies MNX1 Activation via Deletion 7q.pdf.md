---
# --- identity ------------------------------------------------
id: 2025-01-01_sollier-2025-blood-cancer-discovery-enha
id_basis: filename-year
source: Sollier(2025) Blood Cancer Discovery; Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q.pdf
sha256: 3e8245148aa51aa65b6cd171faad62d91c6ddd3ace6053919acfec2c417e3922
size_bytes: 9275177
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 179195

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2643-3230.BCD-24-0278"
year: 2025
title: "Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Sollier(2025) Blood Cancer Discov; Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Pyjacker, a computational tool for systematic detection of enhancer hijacking from whole genome sequencing, RNA-seq and enhancer information, was applied to 39 complex-karyotype AML samples and detected 19 genes putatively activated by structural variants at FDR below 20%. Among them, aberrant MNX1 expression can result from del(7)(q22q36) via hijacking of a CDK6 enhancer; MNX1 activation occurred in 1.4% of AML patients, co-occurred significantly with BCOR mutations, and was required for leukemia cell fitness in a xenograft model. GSX2 and EPO were also identified as putatively activated.

## Summary

Overturns a standing assumption about a common lesion. Deletion of 7q in AML has been read as haploinsufficiency - losing tumour suppressors - and this shows the same deletion can activate an oncogene, by removing the DNA between MNX1 and a CDK6 enhancer. A deletion that turns a gene on is a genuinely different pathomechanism.

The tool's design choice is also well argued. Pyjacker looks for strong gene overexpression alongside structural variants rather than relying on Hi-C contact data, on the reasoning that Hi-C yields many contacts where expression barely changes, and that RNA-seq is far more widely available - which makes the method applicable to existing cohorts. The MNX1-activated adult cases resemble t(7;12) pediatric AML transcriptionally, suggesting the two could be targeted together.

## Key points

- Pyjacker detects enhancer hijacking from WGS, RNA-seq and enhancer annotation, without requiring Hi-C or germline data.
- Nineteen genes were found putatively activated by structural variants across 39 complex-karyotype AML samples.
- del(7)(q22q36) can activate MNX1 by hijacking a CDK6 enhancer - a deletion causing oncogene activation, not only haploinsufficiency.
- MNX1 activation occurs in 1.4% of AML, co-occurs with BCOR mutations, and is required for leukemia cell fitness in xenografts.
- Adult MNX1-activated cases resemble pediatric t(7;12) AML transcriptionally, suggesting shared therapeutic strategies.

## Limitations

Thirty-nine samples and an FDR threshold of 20% - permissive by any standard - so a substantial share of the 19 candidate genes may be false positives; only MNX1 is functionally validated. MNX1 activation occurs in 1.4% of patients, so the finding is mechanistically important but affects few. The proposed transcriptional repressor activity of MNX1, inferred from suppression of HLX, TFEC, GFI1, EVI2B, TLE4 and MYD88, is an interpretation of expression correlations rather than a demonstrated function. EPO and GSX2 activation each rest on single samples. The choice to prioritise expression over Hi-C trades one error mode for another: genes whose hijacking produces modest expression change will be missed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Sollier(2025) Blood Cancer Discov; Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2643-3230.BCD-24-0278`; the prose sections were written here from the paper itself.

## Citation

Sollier et al. Blood Cancer Discovery 2025. Enhancer Hijacking Discovery in Acute Myeloid Leukemia by Pyjacker Identifies MNX1 Activation via Deletion 7q. doi: 10.1158/2643-3230.BCD-24-0278

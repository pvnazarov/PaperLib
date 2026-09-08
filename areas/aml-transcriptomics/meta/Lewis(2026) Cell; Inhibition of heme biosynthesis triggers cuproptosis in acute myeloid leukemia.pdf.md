---
# --- identity ------------------------------------------------
id: 2026-01-01_lewis-2026-cell-inhibition-of-heme-biosy
id_basis: filename-year
source: Lewis(2026) Cell; Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia.pdf
sha256: 1f093dc8cd489f47084d2f05b26939f668956e5e377cc086e6cd3cf39bd5610d
size_bytes: 15849037
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 674534

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2025.10.028"
year: 2026
title: "Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lewis(2026) Cell; Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Integrating mouse models, human cell lines and primary patient samples, de novo heme biosynthesis is identified as a selective dependency in AML. The dependency arises because AML cells, and especially leukemic stem cells, downregulate heme biosynthesis enzymes, which promotes self-renewal. Inhibiting these enzymes collapses mitochondrial Complex IV and dysregulates the copper-chaperone system, inducing cuproptosis - programmed cell death caused by copper-driven oligomerisation of lipoylated proteins. Pathways synthetic lethal with heme biosynthesis, including glycolysis, are identified for combination strategies.

## Summary

The dependency arises from an unusual logic worth following. AML cells, and leukemic stem cells most of all, actively downregulate heme biosynthesis enzymes because low heme promotes self-renewal - so the cells choose to run the pathway at low output, which leaves them with no reserve when it is inhibited. The vulnerability is created by the cancer's own adaptation.

The cell death mechanism is the more novel part. Heme starvation raises intracellular copper and collapses Complex IV, which needs both heme and copper, triggering cuproptosis. Because cancers routinely inactivate apoptosis, necroptosis and ferroptosis, a molecularly independent death pathway is valuable precisely for the resistant cases, and this connects two metabolic systems - heme and copper - that are not usually considered together.

## Key points

- De novo heme biosynthesis is a selective dependency in AML, most pronounced in leukemic stem cells.
- AML cells downregulate heme biosynthesis enzymes because low heme promotes self-renewal - the adaptation creates the vulnerability.
- Inhibition collapses mitochondrial Complex IV, which requires both heme and copper, and dysregulates copper chaperones.
- The resulting death is cuproptosis, a pathway molecularly independent of apoptosis, necroptosis and ferroptosis.
- Glycolysis is synthetic lethal with heme biosynthesis, giving a rational combination.

## Limitations

The authors are explicit that they cannot exclude serious hematological toxicity such as hemolysis or thrombotic microangiopathy, or non-hematological toxicity, from heme biosynthesis enzyme inhibitors. Their argument for tolerability is indirect: normal HSCs were more resilient than AML cells in vitro, and inherited porphyrias with severely compromised enzyme activity show incomplete penetrance - but erythroid progenitors account for roughly 85% of heme synthesis, so the tissue most exposed to this intervention is the one that makes red cells. No selective clinical-grade inhibitor exists. The synthetic lethal interactions are identified computationally and in vitro rather than tested therapeutically. Cuproptosis is itself a recently proposed pathway whose criteria are still being established, which the authors acknowledge by framing their result as strengthening the case that it is bona fide.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lewis(2026) Cell; Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2025.10.028`; the prose sections were written here from the paper itself.

## Citation

Lewis et al. Cell 2026. Inhibition of heme biosynthesis triggers cuproptosis in acute myeloid leukemia. doi: 10.1016/j.cell.2025.10.028

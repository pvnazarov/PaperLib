---
# --- identity ------------------------------------------------
id: 2024-01-01_bauer-2024-american-journal-of-hematolog
id_basis: filename-year
source: Bauer(2024) American Journal of Hematology; BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL.pdf
sha256: c0a624f260b32cece79cd4c5a58e5710a67141f862746ab04b6f3cf194a4c5b0
size_bytes: 2908812
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 62785

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1002/ajh.27385"
year: 2024
title: "BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Bauer(2024) Am J Hematol; BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A comparison of the BET inhibitor JQ1 with the BRD4 degraders dBET1 and dBET6 in AML and ALL cell lines and primary patient cells, including CD34+/CD38- and CD34+/CD38+ leukemic stem and progenitor cells. All three suppressed growth and viability regardless of leukemia variant or molecular driver; dBET6 additionally overcame osteoblast-induced drug resistance, combined synergistically with gilteritinib in FLT3-ITD AML and with ponatinib in BCR::ABL1+ ALL, and all three suppressed interferon-gamma- and TNF-alpha-induced PD-L1 expression. dBET6 was the superior agent in every assay.

## Summary

The practical claim is that degrading BRD4 beats occupying it. JQ1 blocks the bromodomain and BRD4 remains present; dBET6 removes the protein, and across viability, stem-cell compartments, stromal resistance and checkpoint expression the degrader wins each comparison.

Three resistance mechanisms are addressed in one paper, which is the reason to keep it: intrinsic LSC resistance in the CD34+/CD38- compartment, microenvironment-induced resistance modelled with osteoblasts, and immune escape through inducible PD-L1. The authors also do the experiment that usually goes missing - normal bone marrow cells - and report that these drugs inhibit those too, with a smaller effect, so a therapeutic window is claimed but not a clean one.

## Key points

- BRD4 degradation (dBET1, dBET6) is more effective than BET bromodomain inhibition (JQ1) across every assay tested.
- Activity extends to CD34+/CD38- leukemic stem cells and is independent of leukemia variant or driver mutation.
- dBET6 overcomes osteoblast-induced drug resistance, addressing a microenvironment mechanism rather than only a cell-intrinsic one.
- Synergy with gilteritinib in FLT3-ITD AML and with ponatinib in BCR::ABL1+ ALL.
- All BRD4-targeting drugs suppress cytokine-induced PD-L1 on leukemic cells including LSC, linking the target to immune escape.

## Limitations

Entirely preclinical and largely in vitro; the osteoblast co-culture is a simplified stand-in for the marrow niche and no in vivo model is presented. dBET1 and dBET6 are chemical-probe degraders, not clinical candidates, so the comparison with JQ1 - also a probe - does not speak to any drug a patient could receive. Growth inhibition of normal bone marrow cells is confirmed, and the authors concede the therapeutic window's sufficiency 'remains to be determined in clinical trials'; prolonged cytopenia is the anticipated toxicity of exactly this mechanism. Synergy is asserted from combination assays in cell lines. The hedged title - 'may effectively counteract' - matches the strength of the evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Bauer(2024) Am J Hematol; BRD4 degraders may effectively counteract therapeutic resistance of leukemic stem cells in AML and ALL.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1002/ajh.27385`; the prose sections were written here from the paper itself.

## Citation

Bauer et al. American Journal of Hematology 2024. <scp>BRD4</scp> degraders may effectively counteract therapeutic resistance of leukemic stem cells in <scp>AML</scp> and <scp>ALL</scp>. doi: 10.1002/ajh.27385

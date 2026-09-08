---
# --- identity ------------------------------------------------
id: 2021-01-01_qing-2021-molecular-cell-r-2-hydroxyglut
id_basis: filename-year
source: Qing(2021) Molecular Cell; R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO m6A PFKP LDHB axis.pdf
sha256: 735de5265ebb85021d9414c7a9d150f9dae4632e8abda22d580719808df0a860
size_bytes: 8864120
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 136978

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.molcel.2020.12.026"
year: 2021
title: "R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO/m6A/PFKP/LDHB axis"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Qing(2021) Mol Cell; R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO mA PFKP LDHB axis.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

R-2-hydroxyglutarate, the metabolite produced by mutant IDH enzymes, is shown to attenuate aerobic glycolysis in sensitive leukemia cells. Mechanistically it abrogates FTO/m6A/YTHDF2-mediated post-transcriptional upregulation of the glycolytic genes PFKP and LDHB. Knocking down FTO, PFKP or LDHB reproduces the glycolytic inhibition in sensitive leukemia cells but not in normal CD34+ hematopoietic stem/progenitor cells, and inhibits leukemogenesis in vivo; overexpression reverses the effect. R-2HG also suppresses glycolysis and downregulates FTO, PFKP and LDHB in human primary IDH-wild-type AML cells.

## Summary

An inversion of the standard reading of an oncometabolite. R-2HG is normally the villain of IDH-mutant leukemia; here it has anti-tumour activity in sensitive cells, and the mechanism runs through the same FTO/m6A axis that Li (2017) established as oncogenic in this collection - R-2HG inhibits FTO, and FTO was maintaining glycolytic gene expression.

The therapeutic reading is about FTO rather than R-2HG. Because FTO loss downregulates both PFKP and LDHB while knocking down either alone gives a weaker effect, an FTO inhibitor should outperform a single glycolytic enzyme inhibitor - and the effect is absent in normal CD34+ cells, which is the selectivity the strategy needs. The authors also note the clinical implication that IDH-mutant patients treated with mutant-IDH inhibitors lose their own endogenous R-2HG, which cuts against the assumption that removing it is straightforwardly good.

## Key points

- R-2HG, usually cast as an oncometabolite, suppresses aerobic glycolysis and has anti-tumour activity in sensitive leukemia cells.
- The mechanism is inhibition of FTO, which otherwise upregulates PFKP and LDHB post-transcriptionally via m6A and YTHDF2.
- The effect is absent in normal CD34+ HSPCs, giving selectivity.
- FTO knockdown outperforms knockdown of either PFKP or LDHB alone, arguing that FTO inhibitors would be the better agents.
- R-2HG also suppresses this axis in primary IDH-wild-type AML cells, extending relevance beyond IDH-mutant disease.

## Limitations

Sensitivity to R-2HG varies between leukemia cell lines and the determinants are not established here, so 'R-2HG-sensitive' is defined empirically rather than predicted. The authors state that existing FTO inhibitors are unlikely to be clinically applicable because of low selectivity or efficacy, and their own newer compounds are only mentioned - so the therapeutic proposal rests on agents not tested in this work. LDHB's role in cancer is genuinely contested, silenced in some tumours and amplified in others, and this study resolves it only for leukemia. The paradox that R-2HG is both leukemogenic and anti-leukemic is noted rather than reconciled, and it complicates the clinical interpretation for IDH-mutant patients receiving mutant-IDH inhibitors. In vivo work is knockdown-based rather than pharmacological.

## Provenance

Located in the published literature, dropped into `inbox/` as `Qing(2021) Mol Cell; R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO mA PFKP LDHB axis.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.molcel.2020.12.026`; the prose sections were written here from the paper itself.

## Citation

Qing et al. Molecular Cell 2021. R-2-hydroxyglutarate attenuates aerobic glycolysis in leukemia by targeting the FTO/m6A/PFKP/LDHB axis. doi: 10.1016/j.molcel.2020.12.026

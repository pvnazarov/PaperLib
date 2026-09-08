---
# --- identity ------------------------------------------------
id: 2022-01-01_szewczyk-2022-redox-biology-prmt5-regula
id_basis: filename-year
source: Szewczyk(2022) Redox Biology; PRMT5 regulates ATF4 transcript splicing and oxidative stress response.pdf
sha256: 56118c249e5543874993ebd85332bc7f78efa8311deb9d8a0409d52a141428b2
size_bytes: 9406370
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 107284

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.redox.2022.102282"
year: 2022
title: "PRMT5 regulates ATF4 transcript splicing and oxidative stress response"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Szewczyk(2022) Redox Biol; PRMT5 regulates ATF4 transcript splicing and oxidative stress response.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Transcriptomic analysis identified PRMT5 regulation of the ATF4 pathway in AML. PRMT5 inhibition produces an unstable, intron-retaining ATF4 mRNA detained in the nucleus; the accompanying loss of the spliced cytoplasmic transcript lowers ATF4 protein and downregulates its target genes. Cells with low ATF4 after PRMT5 loss show increased oxidative stress, growth arrest and senescence. Leukemia cells overexpressing the EVI1 oncogene depend on PRMT5 function: EVI1-high AML has reduced ATF4, elevated baseline reactive oxygen species and increased sensitivity to PRMT5 inhibition, with EVI1 and ATF4 gene signatures inversely correlated.

## Summary

Supplies a biomarker for a drug class in clinical trials, and does so through a mechanism rather than a correlation. PRMT5 dependency has been hard to predict beyond MTAP co-deletion; here the determinant is oxidative stress load, and EVI1 overexpression provides it.

The logic is a squeeze. EVI1 suppresses ATF4, raising baseline reactive oxygen species; PRMT5 inhibition suppresses ATF4 further by switching its transcript to an intron-retaining nuclear form; and a cell already running high ROS with a compromised stress response cannot absorb the second hit. That makes EVI1-high AML - an adverse-risk group with few options - the predicted responder, and the inverse correlation between EVI1 and ATF4 signatures is the readout.

## Key points

- PRMT5 inhibition switches ATF4 to an unstable intron-retaining transcript detained in the nucleus, lowering ATF4 protein and target gene expression.
- Loss of ATF4 raises oxidative stress and drives growth arrest and senescence.
- EVI1 independently suppresses ATF4, so EVI1-high AML runs elevated baseline ROS with a compromised stress response.
- EVI1-high cells are consequently more sensitive to PRMT5 inhibition - a mechanistically grounded biomarker for a drug class in trials.
- EVI1 and ATF4 gene signatures are inversely correlated in AML.

## Limitations

Work is in AML cell lines with patient samples contributing expression correlation; no in vivo model or patient-derived xenograft experiment is described in the summary evidence. EVI1 dependence is demonstrated partly by lentiviral EVI1 overexpression, which is not equivalent to the enhancer-driven overexpression in inv(3)/t(3;3) patients. PRMT5 has many substrates and affects splicing broadly, so ATF4 is one consequence among many and is not shown to account for the full dependency. The biomarker is proposed from these experiments rather than validated against clinical response to a PRMT5 inhibitor. Senescence and growth arrest are the endpoints, not leukemia control.

## Provenance

Located in the published literature, dropped into `inbox/` as `Szewczyk(2022) Redox Biol; PRMT5 regulates ATF4 transcript splicing and oxidative stress response.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.redox.2022.102282`; the prose sections were written here from the paper itself.

## Citation

Szewczyk et al. Redox Biology 2022. PRMT5 regulates ATF4 transcript splicing and oxidative stress response. doi: 10.1016/j.redox.2022.102282

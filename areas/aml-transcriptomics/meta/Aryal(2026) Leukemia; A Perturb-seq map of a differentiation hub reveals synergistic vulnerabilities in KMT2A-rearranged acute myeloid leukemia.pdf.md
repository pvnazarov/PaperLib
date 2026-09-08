---
# --- identity ------------------------------------------------
id: 2026-01-01_aryal-2026-leukemia-a-perturb-seq-map-of
id_basis: filename-year
source: Aryal(2026) Leukemia; A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia.pdf
sha256: 12986a50608e6ccc2096b6c071861b10fb0ba8e465c93c2c24e8ad91dff59aec
size_bytes: 3659156
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 144000

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-026-02917-2"
year: 2026
title: "A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Aryal(2026) Leukemia; A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Perturb-seq screening is used to map the functional architecture of the epigenetic network in KMT2A-rearranged AML. The authors identify a compensatory circuit in which KAT6A, Menin and DOT1L converge to silence a core differentiation module they call the Myeloid Program, whose activity correlates with favourable survival in large patient cohorts. Single perturbations only partially derepress the program, whereas simultaneous pharmacological inhibition collapses the circuit's buffering capacity and produces synergistic anti-leukemic activity; loss of the PRC1.1 component PCGF1 confers resistance to DOT1L inhibition, and high baseline Myeloid Program activity marks a state selectively targetable by MEK, AKT and mTOR inhibitors.

## Summary

An explanation for a clinical disappointment. Menin and DOT1L inhibitors work on paper and underperform in patients, and the usual explanations are incomplete target engagement or off-target effects; this argues instead that the network buffers, and that single-node inhibition is defeated by redundancy rather than by pharmacology.

The framing is the useful part - a differentiation program held down by several chromatin complexes at once, so that the therapeutic unit is the circuit, not the enzyme. The PCGF1 result is the same logic inverted: removing an antagonist of the Myeloid Program confers resistance, which is counterintuitive until the program rather than the drug target is taken as the thing that matters.

## Key points

- KAT6A, Menin and DOT1L form a synergistic hub co-repressing a shared myeloid differentiation program (CD14, CD33, ITGAM, MPO, LYZ, CEBPA, SPI1).
- Single-node perturbation only partially derepresses the program; combined pharmacological inhibition collapses the buffering and is synergistic.
- Myeloid Program activity correlates with favourable survival in large patient cohorts, so the module is not merely a cell-line artefact.
- PCGF1 loss confers resistance to DOT1L inhibition, extending to DOT1L a principle previously reported for Menin inhibitors.
- High baseline Myeloid Program activity defines a state selectively vulnerable to MEK, AKT and mTOR inhibitors, proposed as a predictive biomarker.

## Limitations

Perturb-seq is a cell-line screen, and the paper does not demonstrate the circuit in primary patient blasts or in vivo; the synergy is measured pharmacologically in culture, where combination indices are sensitive to dose and schedule. The Myeloid Program is defined by co-regulation within this dataset, so its correlation with survival in external cohorts is a signature-score association and does not establish that reactivating it causes benefit. The biomarker claim - high baseline activity predicting MEK/AKT/mTOR sensitivity - is derived and tested in the same system rather than in a held-out clinical cohort. Several of the interactions are described as validated by agreement with prior published results, which is corroboration rather than independent experiment.

## Provenance

Located in the published literature, dropped into `inbox/` as `Aryal(2026) Leukemia; A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-026-02917-2`; the prose sections were written here from the paper itself.

## Citation

Aryal et al. Leukemia 2026. A Perturb-seq map of a differentiation hub reveals synergistic vulnerabilities in KMT2A-rearranged acute myeloid leukemia. doi: 10.1038/s41375-026-02917-2

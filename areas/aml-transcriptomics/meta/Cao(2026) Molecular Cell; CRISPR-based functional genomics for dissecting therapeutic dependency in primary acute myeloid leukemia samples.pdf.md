---
# --- identity ------------------------------------------------
id: 2026-01-01_cao-2026-molecular-cell-crispr-based-fun
id_basis: filename-year
source: Cao(2026) Molecular Cell; CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples.pdf
sha256: 84c9bff5fc326554d6ad292166becbcccacc67efd462cfcd299c4849ec3cd03e
size_bytes: 3923219
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 179349

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.molcel.2026.02.003"
year: 2026
title: "CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Cao(2026) Mol Cell; CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An optimized CRISPR platform for functional genomics directly in patient-derived xenograft and primary AML samples carrying diverse pathogenic mutations. Integrated in vitro and in vivo CRISPR-Cas9 knockout and CRISPR interference dropout screens validated known AML-biased targets and identified cis-regulatory elements essential for leukemic growth, while coupling pooled perturbations with single-cell RNA sequencing (Perturb-seq) resolved perturbation-induced changes in regulatory networks, cell cycle states and cellular hierarchies. The system achieved successful editing in about 88% (22 of 25) of samples tested, across 3 PDX and 22 primary patient samples.

## Summary

A methods paper aimed squarely at the reason cancer functional genomics has been confined to cell lines: primary AML cells are hard to transduce, die readily, and do not expand. The three optimisations are unglamorous and decisive - better Cas9 and sgRNA vectors, ultra-concentrated virus, and RetroNectin to bridge virus to integrins on hematopoietic cells - and lentivirus rather than electroporation is chosen because it keeps cells alive and permits sequencing-based readout.

The most useful empirical result for anyone planning such work is the concordance between matched in vitro and in vivo screens. In vivo takes two to five months with variable engraftment; in vitro takes two to three weeks. If the two agree for cell-autonomous dependencies, most screening can move in vitro, and the authors are explicit that non-cell-autonomous microenvironment effects are what in vivo is still needed for.

## Key points

- CRISPR knockout, CRISPRi and Perturb-seq performed directly in primary AML samples rather than cell lines or mouse models.
- Editing succeeded in 22 of 25 samples, including poor-prognosis genotypes with no representative cell line.
- Three concrete optimisations: improved Cas9/sgRNA vectors, ultra-concentrated virus, and RetroNectin-mediated delivery via VLA-4/VLA-5.
- Matched in vitro and in vivo dropout screens agree strongly for cell-autonomous dependencies, making the 2-3 week in vitro route viable.
- Screens identified cis-regulatory elements, not only genes, as essential for leukemic growth.

## Limitations

A platform paper: the biology it reports is proof-of-concept, and the dependencies found are largely validation of already-known AML-biased targets rather than new discoveries. Primary AML cells survive briefly in culture, which bounds screen duration and biases hits toward strong, fast phenotypes - slow dependencies are systematically invisible in a two-to-three-week dropout. Library size is correspondingly limited by available cell numbers, so these are focused rather than genome-wide screens. Three samples failed to edit, and no account is given of what distinguishes them, which matters for knowing when the platform will not work. The in vitro/in vivo concordance is established on a small number of screens and, by construction, says nothing about the microenvironment-dependent dependencies that make AML relapse.

## Provenance

Located in the published literature, dropped into `inbox/` as `Cao(2026) Mol Cell; CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.molcel.2026.02.003`; the prose sections were written here from the paper itself.

## Citation

Cao et al. Molecular Cell 2026. CRISPR-based functional genomics for dissecting therapeutic dependency in primary acute myeloid leukemia samples. doi: 10.1016/j.molcel.2026.02.003

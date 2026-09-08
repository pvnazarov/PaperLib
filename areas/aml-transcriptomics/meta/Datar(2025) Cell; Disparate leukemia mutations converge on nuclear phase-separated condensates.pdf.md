---
# --- identity ------------------------------------------------
id: 2025-01-01_datar-2025-cell-disparate-leukemia-mutat
id_basis: filename-year
source: Datar(2025) Cell; Disparate leukemia mutations converge on nuclear phase-separated condensates.pdf
sha256: 0064d6344d8890a0ce77b12277a6b4e9a48321fbeff0e062e29acc40ba50e893
size_bytes: 5279410
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 199247

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2025.10.010"
year: 2025
title: "Disparate leukemia mutations converge on nuclear phase-separated condensates"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Datar(2025) Cell; Disparate leukemia mutations converge on nuclear phase-separated condensates.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Mutant NPM1 (NPM1c) is shown to form nuclear phase-separated condensates - termed coordinating bodies, or C-bodies - in human cell lines, mouse models and primary patient samples. NPM1c phase separation is necessary and sufficient to recruit NUP98 and KMT2A into these condensates. Through extensive mutagenesis and pharmacological destabilisation of phase separation, C-bodies are shown to be necessary for regulating gene expression, promoting leukemic expansion in vivo and maintaining the undifferentiated state. Nucleoporin and KMT2A fusion proteins form condensates biophysically indistinguishable from NPM1c C-bodies, establishing them as a shared feature and therapeutic vulnerability.

## Summary

This resolves a long-standing paradox and unifies three genetic groups at once. NPM1c is defined by cytoplasmic mislocalisation, yet its effects are transcriptional - the question of how a cytoplasmic protein drives nuclear gene expression has been open for two decades. The answer offered is that the functionally decisive pool is neither cytoplasmic nor nucleolar but a distinct nuclear condensate, and the mutagenesis is designed to make that a causal rather than correlative claim: localisation to cytoplasm, nucleoplasm or nucleolus is not sufficient for the leukemic phenotype, only C-body formation is.

The convergence claim is the wider contribution. NUP98 fusions, KMT2A rearrangements and NPM1 mutations all produce HOXA-driven leukemia by routes that looked mechanistically unrelated; if their condensates are biophysically indistinguishable, one therapeutic approach might address all three.

## Key points

- NPM1c forms nuclear phase-separated condensates (C-bodies) across cell lines, mouse models and primary patient samples.
- Phase separation is necessary and sufficient to recruit NUP98 and KMT2A; XPO1 and MENIN also localise there.
- Mutagenesis shows cytoplasmic, nucleoplasmic or nucleolar localisation is not sufficient - C-body formation is what drives the leukemic phenotype.
- C-bodies are required for leukemic gene expression, blocked differentiation and in vivo expansion, and enrich at active loci such as HOXA9.
- Nucleoporin and KMT2A fusion condensates are biophysically indistinguishable from C-bodies, consolidating disparate lesions into one mechanism.

## Limitations

Demonstrating phase separation in cells rather than in vitro is contested methodologically: puncta by microscopy, and recovery in photobleaching experiments, are consistent with condensates but also with other forms of clustering, and the field's criteria are still moving. 'Biophysically indistinguishable' is a claim about the measurements made, not about identity of composition or function. Pharmacological destabilisation of phase separation uses agents such as aliphatic alcohols that are notoriously non-specific and disrupt many cellular processes, so those experiments carry less weight than the mutagenesis. How C-bodies act is explicitly speculative - the authors say they 'speculate' that condensates selectively regulate a small set of leukemia-driving genes. As a therapeutic vulnerability, no selective way to target a condensate exists.

## Provenance

Located in the published literature, dropped into `inbox/` as `Datar(2025) Cell; Disparate leukemia mutations converge on nuclear phase-separated condensates.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2025.10.010`; the prose sections were written here from the paper itself.

## Citation

Datar et al. Cell 2025. Disparate leukemia mutations converge on nuclear phase-separated condensates. doi: 10.1016/j.cell.2025.10.010

---
# --- identity ------------------------------------------------
id: 2022-01-01_ellegast-2022-cancer-discovery-unleashin
id_basis: filename-year
source: Ellegast(2022) Cancer Discovery; Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts.pdf
sha256: f6bc3ba50d47603a87852570d03d5b44ad3591bc4c01cf1bd30c5a9c2a8ba89e
size_bytes: 2831304
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 177053

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-21-0956"
year: 2022
title: "Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ellegast(2022) Cancer Discov; Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genome-wide screens for genetic vulnerabilities in inflammatory pathways identify the immune modulator IRF2BP2 as a selective AML dependency, validated genetically and by targeted protein degradation in vitro and genetically in vivo. Chromatin and expression studies show that IRF2BP2 represses IL-1beta/TNFalpha signalling via NF-kB, binding enhancers and promoters, with gain of H3K27ac at upregulated targets after its degradation. Perturbing IRF2BP2 produces an acute inflammatory state that kills AML cells, establishing IRF2BP2-mediated transcriptional repression as a mechanism of blast survival.

## Summary

The organising idea is that leukemic blasts are immune cells that failed to mature, and that they must actively suppress the inflammatory program their lineage is built to run. Rather than recruiting the immune system against AML - which has largely not worked - this turns the cell's own inflammatory machinery back on and lets it kill itself, a cell-intrinsic self-directed immunotherapy.

Two things give it weight. IRF2BP2 acts as a repressor, unusual in a field where dependencies are typically activators like BRD4, MYB or MYC, and the H3K27ac gain at derepressed targets supports that directly. And the dependency is strongest in monocytic AML, the subtype that resists venetoclax, where IRF2BP2 was the top AML-selective dependency. Intersecting three screens across RNAi and CRISPR, with MYB and CBFB recovered as internal positive controls, is careful screen practice.

## Key points

- IRF2BP2 is a selective AML dependency - AML cell lines depend on it more than any other cancer type.
- It acts as a transcriptional repressor, restraining IL-1beta/TNFalpha signalling through NF-kB; degradation causes H3K27ac gain at derepressed targets.
- Derepression produces an acute inflammatory state that kills the blast: inflammation as a cell-intrinsic, self-directed immunotherapy.
- The dependency is strongest in monocytic AML, the subtype most resistant to venetoclax.
- Three intersecting screens across RNAi and CRISPR, recovering MYB and CBFB as controls, reduce the chance of off-target artefact.

## Limitations

No inhibitor exists: validation uses genetic knockout and the dTAG degradation system, which is a chemical-biology tool requiring the target to be engineered with a degron tag, not a drug. In vivo validation is genetic only. AML cells require 'a precise set point of NF-kB signalling', and normal myeloid cells plausibly need one too, so the therapeutic window for forcing inflammation is not established - normal hematopoiesis is not assessed in comparable depth. The mechanism is largely worked out in cell lines. Several authors declare substantial commercial interests, including inventorship on dTAG patents and multiple company affiliations and funding sources, which is disclosed at length.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ellegast(2022) Cancer Discov; Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-21-0956`; the prose sections were written here from the paper itself.

## Citation

Ellegast et al. Cancer Discovery 2022. Unleashing Cell-Intrinsic Inflammation as a Strategy to Kill AML Blasts. doi: 10.1158/2159-8290.CD-21-0956

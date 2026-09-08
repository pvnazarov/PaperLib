---
# --- identity ------------------------------------------------
id: 2025-01-01_derevyanko-2025-blood-fusion-gene-deplet
id_basis: filename-year
source: Derevyanko(2025) Blood; Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia.pdf
sha256: 1816da1e26049f49e43b6aea4dec2218618e8de3e5b0e99882d0cba5069aee27
size_bytes: 9791258
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 210354

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025028988"
year: 2025
title: "Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Derevyanko(2025) Blood; Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Primary t(8;21) AML cells are shown to depend critically on RUNX1::RUNX1T1 to suppress differentiation and maintain stemness. Silencing the fusion with fusion-site-specific siRNA delivered in lipid nanoparticles produces substantial changes in chromatin accessibility, redirecting the leukemia-associated transcriptional network toward myeloid differentiation. Single-cell analyses show depletion of immature stem and progenitor-like populations alongside expansion of granulocytic and eosinophilic/mast cell-like populations with impaired self-renewal.

## Summary

Two contributions, one technical and one biological. The technical one is delivery: fusion transcripts are ideal targets because they are entirely cancer-specific, but the proteins are transcription factors and thus hard to drug, and siRNA has always foundered on getting into primary blasts. Lipid nanoparticles carrying a siRNA that spans the fusion junction do both jobs at once.

The biology is that differentiation is bidirectional and partly unexpected. Losing the fusion pushes cells down granulocytic and eosinophilic/mast routes, and the eosinophilic arm proceeds without added IL-5 - the authors detect no IL5 transcript - implying the LSCs were already chromatin-poised for that fate. The paper is careful to connect this to a real clinical observation: RUNX1::RUNX1T1-positive mast cells are a documented source of persisting measurable residual disease, so the cells produced by differentiation are not obviously harmless.

## Key points

- Primary t(8;21) AML, not just cell lines, requires continuous RUNX1::RUNX1T1 expression for self-renewal.
- Lipid nanoparticles deliver fusion-junction-specific siRNA into primary AML cells - a route to targeting 'undruggable' fusion transcription factors.
- Silencing remodels chromatin accessibility and redirects the network toward myeloid differentiation.
- Differentiation is bidirectional - granulocytic and eosinophilic/mast - at the expense of LSC-enriched immature populations.
- Eosinophilic differentiation occurs without exogenous IL-5 and with no detectable IL5 transcript, implying LSCs are already poised for it.

## Limitations

An ex vivo culture system with siRNA knockdown, not an in vivo therapeutic demonstration - no animal treatment or survival data, and lipid nanoparticle delivery to leukemic cells in marrow is a very different problem from delivery in culture. Knockdown is transient and partial, whereas the therapeutic premise requires sustained suppression. The authors raise, and do not resolve, whether silencing eliminates leukemia-restoring capacity at all: mature AML populations can regain an LSC-like phenotype, and RUNX1::RUNX1T1-positive mast cells are a known reservoir of measurable residual disease, so producing differentiated fusion-positive cells may relocate the problem rather than remove it. Confined to one fusion in one AML subtype. The differentiated populations are characterised by transcriptome and marker expression rather than by functional proof that they cannot re-initiate disease.

## Provenance

Located in the published literature, dropped into `inbox/` as `Derevyanko(2025) Blood; Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025028988`; the prose sections were written here from the paper itself.

## Citation

Derevyanko et al. Blood 2025. Fusion gene depletion eliminates stemness and induces bidirectional differentiation of acute myeloid leukemia. doi: 10.1182/blood.2025028988

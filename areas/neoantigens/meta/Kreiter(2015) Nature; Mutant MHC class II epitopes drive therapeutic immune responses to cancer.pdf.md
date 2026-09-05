---
# --- identity ------------------------------------------------
id: 2015-01-01_kreiter-2015-nature-mutant-mhc-class-ii
id_basis: filename-year
source: Kreiter(2015) Nature; Mutant MHC class II epitopes drive therapeutic immune responses to cancer.pdf
sha256: 1e4e37613ac492d58813d177fcf896991bd89c92e99d56f27f452b918317e805
size_bytes: 5632472
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 214396

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature14426"
year: 2015
title: "Mutant MHC class II epitopes drive therapeutic immune responses to cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nature14426-1.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Across three mouse tumour models with different MHC backgrounds, a considerable fraction of non-synonymous cancer mutations is immunogenic, and the immunogenic mutanome is predominantly recognised by CD4+ T cells. RNA vaccination with a single class II epitope, B16-M30, profoundly retarded B16F10 tumour growth, with efficacy depending on CD4+ and not CD8+ T cells.

## Summary

The finding was unexpected and it reframed vaccine design: neoantigen work had concentrated on MHC class I and CD8 killing, and this showed that in these models most of the immunogenic mutanome is class II restricted and CD4-dependent.

The depletion experiment is what makes the claim causal rather than correlative - removing CD4 cells abolished the therapeutic effect, removing CD8 cells did not.

## Key points

- The immunogenic mutanome is predominantly CD4-recognised across three MHC backgrounds - not a single-model artefact.
- A single class II neoepitope delivered as optimised RNA retarded tumour growth; about two thirds of treated mice were alive at day 100 versus none of the controls by day 65.
- CD4 depletion abolished efficacy, CD8 depletion did not - the mechanism is established, not inferred.
- The mutated residue was essential: the wild-type peptide was not recognised.

## Limitations

Mouse models with transplantable tumours and defined MHC backgrounds; the balance between class I and class II immunogenicity in human tumours is not established by this and may differ. B16F10 is a well-studied model whose mutanome has been characterised repeatedly, which risks the epitopes being unusually well-chosen. The dose-dependence Sultan (2024) later found for class II neoantigens - helpful at low dose, suppressive at high - is not addressed here.

## Provenance

Located in the published literature, dropped into `inbox/` as `nature14426-1.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature14426`; the prose sections were written here from the paper itself.

## Citation

Kreiter et al. Nature 2015. Mutant MHC class II epitopes drive therapeutic immune responses to cancer. doi: 10.1038/nature14426

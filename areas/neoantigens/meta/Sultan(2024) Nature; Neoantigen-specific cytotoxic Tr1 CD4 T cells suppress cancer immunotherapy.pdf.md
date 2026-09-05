---
# --- identity ------------------------------------------------
id: 2024-01-01_sultan-2024-nature-neoantigen-specific-c
id_basis: filename-year
source: Sultan(2024) Nature; Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy.pdf
sha256: db233cd444758297a2b5d14d9e5968a6cabae629acf5c5e800fb38f21c419c03
size_bytes: 32499421
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 320879

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-024-07752-y"
year: 2024
title: "Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Sultan_Nature_Neoantigen_specific_cytotoxic_Tr1_CD4_T_cells_PMID39048822.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Using vaccines combining MHC-I neoantigens with varying doses of tumour-derived MHC-II neoantigens, the authors find that low doses of class II peptides promote tumour rejection while high doses of the same peptides inhibit it. The inhibitory cells induced at high dose are type 1 regulatory (Tr1) CD4 T cells, which are cytotoxic and neoantigen-specific.

## Summary

The finding is a dose inversion, not a difference of antigen: the same MHC-II neoantigen helps at low dose and harms at high dose. That makes it a design constraint for vaccines rather than an argument about which peptides to include.

It also complicates the general push to include class II neoantigens in vaccine design, which most of the computational work in this collection treats as unambiguously desirable.

## Key points

- The same MHC-II neoantigen promotes rejection at low dose (LDVax) and inhibits it at high dose (HDVax).
- High-dose inhibition is mediated by neoantigen-specific cytotoxic Tr1 CD4 T cells, not conventional regulatory T cells.
- Establishes that CD4 neoantigen content is a dose-sensitive design parameter, not a quantity to maximise.
- Directly relevant to the MHC-II-aware ranking frameworks elsewhere in this collection, which have no notion of dose.

## Limitations

A mouse model with defined transplantable tumours and vaccine doses that can be controlled precisely; human vaccine dosing and antigen exposure are neither so clean nor so measurable. The dose threshold separating helpful from harmful is specific to this system and gives no number that transfers. Whether Tr1 induction explains any human vaccine non-response is untested here.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Sultan_Nature_Neoantigen_specific_cytotoxic_Tr1_CD4_T_cells_PMID39048822.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-024-07752-y`; the prose sections were written here from the paper itself.

## Citation

Sultan et al. Nature 2024. Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. doi: 10.1038/s41586-024-07752-y

---
# --- identity ------------------------------------------------
id: 2023-01-01_schmidt-2023-nature-communications-neoan
id_basis: filename-year
source: Schmidt(2023) Nature Communications; Neoantigen-specific CD8 T cells with high structural avidity preferentially reside in and eliminate tumors.pdf
sha256: 40ba78f7491ae8ac577f7c88d6b590f8d5588a943baded84278435e15a398729
size_bytes: 3409958
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 153533

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-023-38946-z"
year: 2023
title: "Neoantigen-specific CD8 T cells with high structural avidity preferentially reside in and eliminate tumors"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Schmidt_Nat_Commun_Neoantigen_specific_CD8_T_cells_with_high_stru_PMID37280206.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Functional (antigen sensitivity) and structural (monomeric pMHC-TCR off-rate) avidities were measured for 371 CD8 T cell clones specific for neoantigens, tumour-associated antigens or viral antigens, from tumours and blood of patients and healthy donors. T cells from tumours show stronger avidity on both measures than their blood counterparts, and high structural avidity tracks with tumour residence and killing.

## Summary

This is a measurement paper rather than a prediction paper, and its most useful contribution to the collection is a direct test of whether prediction tools track a physical quantity that matters.

The answer is largely no. Measured structural avidity and antigen sensitivity correlated poorly with in silico predictors of pMHC affinity, stability or processing - all of which are presentation proxies. The exception is PRIME, an immunogenicity rather than presentation predictor, which did correlate.

## Key points

- 371 T cell clones with both functional and structural avidity measured, spanning neoantigen, TAA and viral specificities.
- Tumour-resident T cells have higher avidity than blood-derived ones, so the compartment sampled changes the answer.
- Poor correlation between measured avidity and in silico affinity, stability and processing predictors - a direct rebuke to presentation-as-proxy.
- PRIME's immunogenicity score did correlate with structural avidity, separating immunogenicity models from presentation models empirically.

## Limitations

The clones are those that could be isolated and expanded, which selects for T cells that grow in culture and may bias towards higher avidity. Structural avidity is measured as a monomeric off-rate, one physical correlate of recognition among several. The correlation with PRIME is encouraging but is a correlation across a set of clones, not a demonstration that PRIME ranks candidates well prospectively.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Schmidt_Nat_Commun_Neoantigen_specific_CD8_T_cells_with_high_stru_PMID37280206.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-023-38946-z`; the prose sections were written here from the paper itself.

## Citation

Schmidt et al. Nature Communications 2023. Neoantigen-specific CD8 T cells with high structural avidity preferentially reside in and eliminate tumors. doi: 10.1038/s41467-023-38946-z

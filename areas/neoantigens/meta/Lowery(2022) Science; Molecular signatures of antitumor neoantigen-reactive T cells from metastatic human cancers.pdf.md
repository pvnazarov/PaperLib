---
# --- identity ------------------------------------------------
id: 2022-01-01_lowery-2022-science-molecular-signatures
id_basis: filename-year
source: Lowery(2022) Science; Molecular signatures of antitumor neoantigen-reactive T cells from metastatic human cancers.pdf
sha256: 2999aaea2d01f309502572181a1481d249ff21a3008ad38532b25cb304038430
size_bytes: 3509279
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 103553

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/science.abl5447"
year: 2022
title: "Molecular signatures of antitumor neoantigen-reactive T cells from metastatic human cancers"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as science.abl5447.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Mapping 55 neoantigen-specific TCR clonotypes from 10 metastatic human tumours to their single-cell transcriptomes yields NeoTCR signatures for CD8+ and CD4+ neoantigen-reactive TILs. Prospective testing of 73 signature-derived clonotypes showed half recognised tumour antigens or autologous tumours.

## Summary

The important part is that the prediction was made prospectively and then tested: TCRs were selected purely from transcriptomic state, synthesised, and screened. A 50% hit rate from transcriptome alone, with no antigen knowledge, is a usable engineering yield.

Neoantigen-specific TILs show tumour-specific expansion with dysfunctional phenotypes, distinct from blood-emigrant bystanders and from regulatory TILs - so exhaustion, usually treated as failure, is here a positive marker of the cells worth recovering.

## Key points

- 55 neoantigen-specific TCR clonotypes from 10 metastatic tumours, mapped to single-cell transcriptomes.
- Prospective test: 73 signature-derived clonotypes synthesised and screened, about half reactive.
- The signature also captures TCRs against driver neoantigens, non-mutated TAAs and viral antigens - a common metastatic TIL exhaustion program rather than a neoantigen-specific one.
- Enables TCR selection from transcriptomic state alone, bypassing antigen prediction entirely.

## Limitations

The authors report a notable negative: they found no significant gene expression differences between TIL TCRs that were reactive and those that were not in their screens, so the signature marks a cluster rather than cleanly separating reactive from non-reactive cells within it. Their 0.1-9.1% estimate of neoantigen-reactive TILs is stated as a likely underestimate, since not every clonotype in the clusters was tested. Cross-presentation as a route to the observed reactivity was not evaluated.

## Provenance

Located in the published literature, dropped into `inbox/` as `science.abl5447.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/science.abl5447`; the prose sections were written here from the paper itself.

## Citation

Lowery et al. Science 2022. Molecular signatures of antitumor neoantigen-reactive T cells from metastatic human cancers. doi: 10.1126/science.abl5447

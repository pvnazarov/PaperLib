---
# --- identity ------------------------------------------------
id: 2022-01-01_taylor-2022-frontiers-in-immunology-mech
id_basis: filename-year
source: Taylor(2022) Frontiers in Immunology; Mechanisms of MHC-I Downregulation and Role in Immunotherapy Response.pdf
sha256: 26b095cddc72a03e8dad165b9715abb8782956fda949359aac5ed4eca243fea8
size_bytes: 807127
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 80186

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3389/fimmu.2022.844866"
year: 2022
title: "Mechanisms of MHC-I Downregulation and Role in Immunotherapy Response"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2022_Taylor_Front_Immunol_Mechanisms_of_MHC_I_Downregulation_and_Role_in_PMID35296095.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A mini-review of the mechanisms by which tumours downregulate MHC class I - transcriptional, post-transcriptional, genetic loss and pathway disruption - and how this contributes to intrinsic and acquired resistance to immune checkpoint inhibition. Therapeutic strategies for restoring surface MHC-I, including interferon-mediated upregulation, are surveyed.

## Summary

Every neoantigen prediction in this collection assumes the peptide will be presented. This review is the systematic account of when that assumption fails for reasons the tumour controls, which is the complement to McGranahan's HLA loss of heterozygosity.

The therapeutic direction it surveys - restoring tumour-specific MHC-I to make cold tumours visible - is the reason the mechanisms matter practically rather than only diagnostically.

## Key points

- MHC-I downregulation spans transcriptional silencing, antigen-processing machinery defects and genetic loss - different mechanisms with different reversibility.
- Both intrinsic and acquired checkpoint-inhibitor resistance are linked to reduced surface MHC-I.
- Interferons upregulate MHC-I but carry potentially life-threatening toxicity; antibody-directed, site-specific cytokine release is proposed as a way round this, untested in large trials.
- Frames why a correct neoantigen prediction can still fail clinically.

## Limitations

A mini-review: every quantitative claim belongs to a cited study and must be traced there. The authors note checkpoint inhibition benefits remain low in common tumour types such as breast and prostate, that intertumoral heterogeneity in response is substantial, and that the proposed targeted-cytokine workaround has not been tested in large clinical trials. It surveys mechanisms rather than establishing their relative frequency.

## Provenance

Located in the published literature, dropped into `inbox/` as `2022_Taylor_Front_Immunol_Mechanisms_of_MHC_I_Downregulation_and_Role_in_PMID35296095.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3389/fimmu.2022.844866`; the prose sections were written here from the paper itself.

## Citation

Taylor et al. Frontiers in Immunology 2022. Mechanisms of MHC-I Downregulation and Role in Immunotherapy Response. doi: 10.3389/fimmu.2022.844866

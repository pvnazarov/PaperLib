---
# --- identity ------------------------------------------------
id: 2013-01-01_calis-2013-plos-computational-biology-pr
id_basis: filename-year
source: Calis(2013) PLoS Computational Biology; Properties of MHC Class I Presented Peptides That Enhance Immunogenicity.pdf
sha256: eb86ddb55dc1ae31a50d0ded53b69c1c3b5105de0676a4e8f037211e1b33cceb
size_bytes: 700103
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 100291

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1371/journal.pcbi.1003266"
year: 2013
title: "Properties of MHC Class I Presented Peptides That Enhance Immunogenicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2013_Calis_PLoS_Comput_Biol_Properties_of_MHC_class_I_presented_peptides_t_PMID24204222.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

By assembling a large dataset of immunogenicity measurements for peptides presented on various MHC-I molecules, the authors identify two determinants: positions P4-P6 of the presented peptide matter most, and large aromatic side chains are associated with immunogenicity. These are combined into a simple, published model validated on two independent epitope discovery studies.

## Summary

This is the paper that separates presentation from immunogenicity as prediction targets. Binding predictors answer whether a peptide reaches the surface; this asks which of the presented peptides a T cell will actually respond to, and shows the answer is partly predictable from amino-acid composition and position.

The central positions P4-P6 are the ones pointing towards the TCR rather than into the MHC groove, so the finding has a structural reading and is not purely statistical.

## Key points

- Positions P4-P6 - the TCR-facing centre of the peptide - carry most of the immunogenicity signal.
- Amino acids with large aromatic side chains are enriched in immunogenic peptides.
- The model is deliberately simple and was released through the IEDB tools site, which is why it became a standard baseline.
- Validated on two independent epitope discovery studies rather than by cross-validation alone.

## Limitations

The model is simple by design and captures a modest part of the variance; it should be read as establishing that immunogenicity is partly predictable, not as a solution. It is trained on curated positive epitopes against assumed negatives, so the negative class is unreliable in a way that inflates apparent performance. Later benchmarks in this collection show such composition-based scores generalise poorly to naturally processed neoepitopes.

## Provenance

Located in the published literature, dropped into `inbox/` as `2013_Calis_PLoS_Comput_Biol_Properties_of_MHC_class_I_presented_peptides_t_PMID24204222.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1371/journal.pcbi.1003266`; the prose sections were written here from the paper itself.

## Citation

Calis et al. PLoS Computational Biology 2013. Properties of MHC Class I Presented Peptides That Enhance Immunogenicity. doi: 10.1371/journal.pcbi.1003266

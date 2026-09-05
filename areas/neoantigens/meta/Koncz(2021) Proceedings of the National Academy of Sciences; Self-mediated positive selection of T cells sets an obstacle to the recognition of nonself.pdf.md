---
# --- identity ------------------------------------------------
id: 2021-01-01_koncz-2021-proceedings-of-the-national-a
id_basis: filename-year
source: Koncz(2021) Proceedings of the National Academy of Sciences; Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself.pdf
sha256: fbbdfbe1654b8f4c32d1e25ace28e9cbf67156c95de897f02005b18106e3c0fc
size_bytes: 1866865
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 120914

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1073/pnas.2100542118"
year: 2021
title: "Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2021_Koncz_Proc_Natl_Acad_Sci_U_S_Self_mediated_positive_selection_of_T_cells_se_PMID34507984.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Positive selection in the thymus keeps only T cells that recognise human peptides on cortical thymic epithelial cells (cTECs). The authors argue this leaves the repertoire systematically blind: TCR-contact motifs rare or absent in the human proteome, or absent from cTEC expression, are unlikely to be recognised at all.

## Summary

The claim inverts the usual foreignness logic. Neoantigen ranking generally assumes that the more unlike self a peptide is, the better - but a peptide whose TCR-facing motif never occurs in the human proteome may have no T cell selected to see it, because positive selection is itself mediated by self peptides.

The authors predict and find a bimodal relationship with cTEC gene expression: motifs from genes too lowly expressed to mediate positive selection are poorly recognised, and so are motifs from abundantly expressed housekeeping genes, where tolerance suppresses the response.

## Key points

- Recognition is analysed at the level of TCR-exposed motifs (TCEMs) rather than whole peptides.
- Motifs absent from the human proteome, or from cTEC expression, are unlikely to be recognised - too foreign can be as bad as too similar.
- The predicted bimodal relationship between cTEC expression and immunogenicity is borne out.
- Sets a principled ceiling on 'maximise dissimilarity-to-self' as a neoantigen ranking strategy.

## Limitations

The authors state the open questions themselves: whether mutated cancer peptides actually reach the level of dissimilarity at which this obstacle bites is left to future work, and the hypothesis is untested for HLA-II and CD4+ T cells. cTEC expression is taken from one published dataset and used as a proxy for what mediated selection in any given individual. The analysis is statistical over motifs, not experimental over T cells.

## Provenance

Located in the published literature, dropped into `inbox/` as `2021_Koncz_Proc_Natl_Acad_Sci_U_S_Self_mediated_positive_selection_of_T_cells_se_PMID34507984.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1073/pnas.2100542118`; the prose sections were written here from the paper itself.

## Citation

Koncz et al. Proceedings of the National Academy of Sciences 2021. Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. doi: 10.1073/pnas.2100542118

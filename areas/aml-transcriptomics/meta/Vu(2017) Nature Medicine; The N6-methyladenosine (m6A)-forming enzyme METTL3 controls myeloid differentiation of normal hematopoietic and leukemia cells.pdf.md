---
# --- identity ------------------------------------------------
id: 2017-01-01_vu-2017-nature-medicine-the-n6-methylade
id_basis: filename-year
source: Vu(2017) Nature Medicine; The N6-methyladenosine (m6A)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells.pdf
sha256: 1f779629a69de7aadf2f37498823a5f0b482eba9582e8708d0816836a879d226
size_bytes: 3754894
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 272400

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nm.4416"
year: 2017
title: "The N6-methyladenosine (m6A)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Vu(2017) Nat Med; The N-methyladenosine (mA)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

shRNA depletion of METTL3 in human hematopoietic stem/progenitor cells promotes differentiation with reduced proliferation, while overexpressing wild-type but not catalytically inactive METTL3 inhibits differentiation and increases growth. METTL3 is more abundant in AML cells than in healthy HSPCs or other tumour types; its depletion in myeloid leukemia lines induces differentiation and apoptosis and delays leukemia progression in mice. Single-nucleotide-resolution m6A mapping with ribosome profiling shows m6A promotes translation of c-MYC, BCL2 and PTEN mRNAs, and loss of METTL3 raises phosphorylated AKT, contributing to the differentiation effect.

## Summary

Establishes m6A as a controller of myeloid differentiation state, with the catalytically inactive overexpression control doing the essential work of showing the effect requires methyltransferase activity rather than protein presence.

The PTEN result is the mechanistically satisfying detail. Reduced PTEN translation raises phospho-AKT, and PTEN carries six mapped m6A sites - so a single enzyme's loss produces an apparently contradictory outcome (an oncogene pathway activated by removing an oncogenic enzyme) that turns out to be part of the differentiation programme. The authors also note the context-dependence honestly: in glioblastoma m6A depletion promotes tumorigenesis, the opposite direction, so m6A biology does not generalise across tissues.

## Key points

- METTL3 depletion drives differentiation and reduces proliferation in normal HSPCs; overexpression does the reverse, requiring catalytic activity.
- METTL3 is more abundant in AML than in normal HSPCs or other tumour types.
- Depletion induces differentiation and apoptosis in leukemia lines and delays progression in mice.
- m6A promotes translation of c-MYC, BCL2 and PTEN; reduced PTEN translation raises phospho-AKT, contributing to differentiation.
- The direction is tissue-specific - m6A depletion promotes tumorigenesis in glioblastoma, the opposite of the leukemic effect.

## Limitations

The authors state that whether elevated METTL3 is sufficient to initiate leukemia remains for future study, so METTL3 is established as required for maintenance rather than as a driver. Depletion is by shRNA and CRISPR in cell lines, with in vivo evidence limited to delayed progression in recipient mice. m6A mapping of this era, even at single-nucleotide resolution, is antibody-dependent, and only three transcripts are followed through to protein. The selectivity claim - apoptosis in leukemia but not normal hematopoietic cells - is the basis of the therapeutic proposal but is demonstrated in culture rather than in a tolerability study. No METTL3 inhibitor is tested here.

## Provenance

Located in the published literature, dropped into `inbox/` as `Vu(2017) Nat Med; The N-methyladenosine (mA)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nm.4416`; the prose sections were written here from the paper itself.

## Citation

Vu et al. Nature Medicine 2017. The N6-methyladenosine (m6A)-forming enzyme METTL3 controls myeloid differentiation of normal hematopoietic and leukemia cells. doi: 10.1038/nm.4416

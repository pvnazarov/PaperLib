---
# --- identity ------------------------------------------------
id: 2022-01-01_xu-2022-nature-subtype-specific-3d-genom
id_basis: filename-year
source: Xu(2022) Nature; Subtype-specific 3D genome alteration in acute myeloid leukaemia.pdf
sha256: 7bda0e549015a1b57b16d6ed4a7ac0229f36306170ea90a69f81178613a645b8
size_bytes: 19502553
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 343558

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-022-05365-x"
year: 2022
title: "Subtype-specific 3D genome alteration in acute myeloid leukaemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Xu(2022) Nature; Subtype-specific 3D genome alteration in acute myeloid leukaemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Hi-C and whole-genome sequencing of 25 AML patient samples and 7 healthy donors identified recurrent and subtype-specific alterations in A/B compartments, topologically associating domains and chromatin loops. RNA-seq, ATAC-seq and CUT&Tag for CTCF, H3K27ac and H3K27me3 in the same samples revealed extensive recurrent AML-specific promoter-enhancer and promoter-silencer loops, with the role of repressive loops validated by CRISPR deletion and interference. Structural-variation-induced enhancer-hijacking and silencer-hijacking events were identified; hijacked enhancers contribute to cell growth by CRISPR screening while hijacked silencers downregulate targets. Whole-genome bisulfite sequencing of 20 samples related DNA methylation, CTCF binding and 3D structure, and hypomethylating treatment with triple DNMT knockdown reverted 3D organisation and gene expression.

## Summary

The most complete 3D genome study of AML in this collection, and its distinctive contribution is the repressive side. Promoter-silencer loops are shown to be widespread and, through CRISPR deletion and interference, to actively suppress their targets - which the authors advance as a new mechanism of tumour suppression. Silencer hijacking, where a structural variant delivers a silencer to a gene, is the mirror of the enhancer hijacking that the field has concentrated on.

The methylation experiments close the loop causally rather than descriptively: DNA methylation controls CTCF binding, CTCF binding shapes architecture, and manipulating methylation - pharmacologically and by triple DNMT knockdown - reverts both the 3D organisation and the expression. That matters clinically because hypomethylating agents are standard AML therapy, so a mechanism by which they act on genome architecture is directly relevant.

## Key points

- Hi-C plus WGS, RNA-seq, ATAC-seq and CUT&Tag on the same 25 AML samples gives an integrated structural and regulatory map.
- Promoter-silencer loops are widespread and validated by CRISPR deletion and interference as a tumour suppression mechanism.
- Structural variants produce both enhancer-hijacking and silencer-hijacking neo-loops, with opposite consequences.
- Hijacked enhancers support cell growth, shown by CRISPR screening; hijacked silencers repress, shown by CRISPRi de-repression.
- Manipulating DNA methylation - with a hypomethylating agent and triple DNMT knockdown - reverts 3D organisation and expression.

## Limitations

The authors identify the experiment they could not do: dissolving chromatin interactions without altering the local chromatin state at the cis-regulatory elements, which is what would separate the loop's contribution from the element's. They also note that phenotypic effects need study in greater depth and that animal models would be needed for biological and translational support - the functional work is CRISPR perturbation in cell lines. Twenty-five patient samples across multiple subtypes leaves few per subtype for the subtype-specific claims. Hi-C on primary AML is technically demanding and resolution is limited, particularly for loop calling in samples with the large structural variations that AML frequently carries.

## Provenance

Located in the published literature, dropped into `inbox/` as `Xu(2022) Nature; Subtype-specific 3D genome alteration in acute myeloid leukaemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-022-05365-x`; the prose sections were written here from the paper itself.

## Citation

Xu et al. Nature 2022. Subtype-specific 3D genome alteration in acute myeloid leukaemia. doi: 10.1038/s41586-022-05365-x

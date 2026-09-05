---
# --- identity ------------------------------------------------
id: 2023-01-01_qu-2023-bioinformatics-deepmhci-an-ancho
id_basis: filename-year
source: Qu(2023) Bioinformatics; DeepMHCI an anchor position-aware deep interaction model for accurate MHC-I peptide binding affinity prediction.pdf
sha256: c3613c07d13ae8dff6642c941b811532119da3e995da58294592ce4f401d878a
size_bytes: 3098516
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 64959

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btad551"
year: 2023
title: "DeepMHCI: an anchor position-aware deep interaction model for accurate MHC-I peptide binding affinity prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Qu_Bioinformatics_DeepMHCI_an_anchor_position_aware_deep_interac_PMID37669154.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

DeepMHCI adds a position-wise gated layer and a residual binding-interaction convolution layer so the model is aware of MHC anchor positions and models peptide-MHC interaction directly rather than by concatenating the two sequences. It is validated by five-fold cross-validation, an independent test set, external HPV vaccine identification and external CD8+ epitope identification, with the largest gains on non-9-mer peptides.

## Summary

The defect it targets is specific and mechanical: earlier deep models concatenate the peptide and the MHC pseudo-sequence into a fixed-size input, which cannot represent where the anchor positions fall when peptide length varies. Nine-mers are handled well and everything else suffers.

Gating the peptide positions lets the network locate anchors under variable length, and multiple convolutional kernel sizes let it match the range of real binding peptides.

## Key points

- Diagnoses non-9-mer weakness as a consequence of fixed-size concatenated input, then fixes the representation rather than adding capacity.
- Mixed convolutional kernel sizes (9, 11, 13) outperform any single size; larger kernels were not used because binding peptides are rarely longer than 13.
- Validated externally on HPV vaccine and CD8+ epitope identification, not only on held-out binding data.
- Learned amino acid embeddings outperformed fixed encodings.

## Limitations

This predicts binding affinity, which is the most selective step in presentation but not the same as presentation and much further from immunogenicity - other papers in this collection show the gap. Evaluation is largely against binding-affinity benchmarks that share ancestry and known circularity in how their peptides were selected. Gains on non-9-mers are relative to methods that handle them badly.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Qu_Bioinformatics_DeepMHCI_an_anchor_position_aware_deep_interac_PMID37669154.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btad551`; the prose sections were written here from the paper itself.

## Citation

Qu et al. Bioinformatics 2023. DeepMHCI: an anchor position-aware deep interaction model for accurate MHC-I peptide binding affinity prediction. doi: 10.1093/bioinformatics/btad551

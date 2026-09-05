---
# --- identity ------------------------------------------------
id: 2022-01-01_you-2022-bioinformatics-deepmhcii-a-nove
id_basis: filename-year
source: You(2022) Bioinformatics; DeepMHCII a novel binding core-aware deep interaction model for accurate MHC-II peptide binding affinity prediction.pdf
sha256: 5c25169224361921a1e9674c773b53742d46f705707cabe6f3e745640186ce58
size_bytes: 1077562
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 68886

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btac225"
year: 2022
title: "DeepMHCII: a novel binding core-aware deep interaction model for accurate MHC-II peptide binding affinity prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2022_You_Bioinformatics_DeepMHCII_a_novel_binding_core_aware_deep_inte_PMID35758790.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

DeepMHCII adds a binding-interaction convolution layer that integrates all potential binding cores in a peptide with the MHC class II pseudo-sequence through multiple convolutional kernels, rather than concatenating an estimated core with the MHC sequence. It outperforms four state-of-the-art methods across four large datasets under cross-validation, leave-one-molecule-out, independent test sets and binding-core prediction.

## Summary

Class II is harder than class I because the groove is open at both ends: peptides extend beyond it and which nine-residue core sits in the groove is not determined by length. Committing to a single estimated core early throws away that uncertainty.

DeepMHCII instead evaluates all candidate cores jointly against the MHC pseudo-sequence, so core identification and affinity prediction are solved together. The leave-one-molecule-out setting is the important evaluation, since it tests generalisation to an unseen allele.

## Key points

- Considers all potential binding cores jointly instead of committing to one estimate upfront.
- Evaluated under leave-one-molecule-out, which tests transfer to unseen MHC-II molecules rather than unseen peptides.
- Binding cores are predicted as an output and visualised, not just used internally.
- The class II counterpart of DeepMHCI, also in this collection, with the same architectural argument.

## Limitations

The authors report they could not include BERTMHC in the comparison because a data question to its authors went unanswered, and excluded NetMHCIIpan-3.2 for lack of source code - so the comparison set is shaped by availability as much as by relevance. They document substantial redundancy between the BD2016 and BD2020 datasets, which inflates apparent performance for any method evaluated across both. This predicts binding affinity, two steps removed from immunogenicity.

## Provenance

Located in the published literature, dropped into `inbox/` as `2022_You_Bioinformatics_DeepMHCII_a_novel_binding_core_aware_deep_inte_PMID35758790.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btac225`; the prose sections were written here from the paper itself.

## Citation

You et al. Bioinformatics 2022. DeepMHCII: a novel binding core-aware deep interaction model for accurate MHC-II peptide binding affinity prediction. doi: 10.1093/bioinformatics/btac225

---
# --- identity ------------------------------------------------
id: 2024-01-01_o-brien-2024-plos-computational-biology
id_basis: filename-year
source: O’Brien(2024) PLOS Computational Biology; A modular protein language modelling approach to immunogenicity prediction.pdf
sha256: dbdc97f11b78c95c3f059518105001ce1518c07c2bff035769e4b921ab2e75a6
size_bytes: 4425977
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 112580

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1371/journal.pcbi.1012511"
year: 2024
title: "A modular protein language modelling approach to immunogenicity prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_O_Brien_PLoS_Comput_Biol_A_modular_protein_language_modelling_approach_PMID39527593.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ImmugenX is a modular protein language modelling approach to CD8+ neoantigen immunogenicity prediction, built for a setting where reactivity rates among called neoantigens are low and training data correspondingly limited. Data are drawn from public sources including VDJdb, CEDAR and McPas-TCR.

## Summary

The modularity is the design response to data scarcity: rather than training one end-to-end model on the few thousand labelled examples available, components pre-trained on large unlabelled protein corpora supply representations, and only a small task-specific head is fitted.

This places it with Culka in the group of papers arguing that general protein knowledge, not more task-specific data, is the way past the immunogenicity data bottleneck.

## Key points

- Protein language model representations substitute for training data the field does not have.
- Modular design lets components be swapped or retrained independently rather than as one monolith.
- Trained and evaluated on public resources (VDJdb, CEDAR, McPas-TCR), so the inputs are reproducible.
- Targets CD8+ reactivity specifically, rather than a generic immunogenicity label.

## Limitations

The authors frame the task as one with low reactivity rates and limited training data, and no modelling choice removes that; performance figures rest on small positive sets. Public TCR and epitope databases are biased towards well-studied epitopes, so held-out performance is unlikely to reflect novel neoantigens. Protein language models bring their own biases from the sequence corpora they were pre-trained on, which are not immunological.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_O_Brien_PLoS_Comput_Biol_A_modular_protein_language_modelling_approach_PMID39527593.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1371/journal.pcbi.1012511`; the prose sections were written here from the paper itself.

## Citation

O’Brien et al. PLOS Computational Biology 2024. A modular protein language modelling approach to immunogenicity prediction. doi: 10.1371/journal.pcbi.1012511

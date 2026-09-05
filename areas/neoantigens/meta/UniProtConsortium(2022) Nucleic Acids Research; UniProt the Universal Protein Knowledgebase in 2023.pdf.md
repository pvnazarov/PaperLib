---
# --- identity ------------------------------------------------
id: 2022-01-01_uniprotconsortium-2022-nucleic-acids-res
id_basis: filename-year
source: UniProtConsortium(2022) Nucleic Acids Research; UniProt the Universal Protein Knowledgebase in 2023.pdf
sha256: de11669c8fea1d5fcb414b9acdfaa8e3c03a7d89d73b4688ccf0b70d7495f21a
size_bytes: 1538778
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 54640

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gkac1052"
year: 2022
title: "UniProt: the Universal Protein Knowledgebase in 2023"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_UniProt_Nucleic_Acids_Res_UniProt_the_Universal_Protein_Knowledgebase_in_PMID36408920.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The 2023 update to the UniProt Knowledgebase, now over 227 million sequences, describing improvements to the data-processing pipeline, expanded reference proteomes, machine-learning-derived annotation for unreviewed entries, and a new website including AlphaFold structures for more than 85% of entries.

## Summary

A reference resource, present in this collection because it is the substrate rather than the subject. The human proteome from UniProt is what 'self' means operationally in every dissimilarity-to-self and foreignness metric here, and the wild-type counterpart of a neoepitope is looked up in it.

That makes its completeness and its annotation quality an unexamined dependency of a large fraction of the neoantigen literature.

## Key points

- Over 227 million sequences, with reference proteomes sought for each taxonomic group.
- Reviewed entries are literature-curated; unreviewed entries are annotated by automated machine-learning systems - a quality distinction that matters when the database is used as ground truth.
- AlphaFold structures linked for more than 85% of entries.
- Defines the 'self' proteome against which neoepitope novelty is computed throughout this collection.

## Limitations

The great majority of entries are unreviewed and machine-annotated, so treating UniProt uniformly as curated truth overstates its reliability. Using a reference proteome as 'self' ignores individual germline variation, which is exactly the variation that determines what a given patient is tolerant to. Linked AlphaFold structures are predictions, not experimental structures, despite appearing alongside curated data.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_UniProt_Nucleic_Acids_Res_UniProt_the_Universal_Protein_Knowledgebase_in_PMID36408920.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gkac1052`; the prose sections were written here from the paper itself.

## Citation

UniProtConsortium et al. Nucleic Acids Research 2022. UniProt: the Universal Protein Knowledgebase in 2023. doi: 10.1093/nar/gkac1052

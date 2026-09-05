---
# --- identity ------------------------------------------------
id: 2024-01-01_finnigan-2024-nature-communications-stru
id_basis: filename-year
source: Finnigan(2024) Nature Communications; Structural basis for self-discrimination by neoantigen-specific TCRs.pdf
sha256: b714b661a1404137f5e9cb7bacaaacb3aec471d849ac467b08cff89e7cd54980
size_bytes: 3697312
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 130099

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-024-46367-9"
year: 2024
title: "Structural basis for self-discrimination by neoantigen-specific TCRs"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Finnigan_Nat_Commun_Structural_basis_for_self_discrimination_by_ne_PMID38459027.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A multi-level cellular, molecular and structural analysis of one model neoantigen from B16F10 murine melanoma - H2-Db/Hsf2 p.K72N 68-76 - and its cognate TCR 47BE7. The p.K72N mutation improves H2-Db binding and thereby surface presentation, stabilising the epitope, and the TCR shows high functional avidity with a broad, stringent binding footprint that explains its selectivity for mutant over wild-type.

## Summary

Most neoantigen work asks which mutations produce epitopes. This asks the complementary and less-studied question: given a neoantigen-specific TCR, what structural features let it distinguish the mutant from the near-identical self peptide it derives from.

The answer here is that discrimination is not localised to a single contact but distributed across a broad, stringent interface, which has direct implications for how much off-target self-reactivity to expect from therapeutically engineered TCRs.

## Key points

- The mutation acts on presentation as well as recognition: p.K72N enhances H2-Db binding and stabilises the epitope at the surface.
- Self-discrimination arises from a broad, stringent binding footprint rather than a single discriminating contact.
- Combines cellular, molecular and crystallographic evidence for the same system rather than inferring structure from sequence.
- Provides a structural counterpart to the sequence-level 'foreignness' and differential-agretopicity heuristics used elsewhere in this collection.

## Limitations

One neoantigen and one TCR in a mouse melanoma model: the mechanism is demonstrated, not shown to be typical. H2-Db is not a human HLA and the quantitative binding conclusions do not transfer directly. Because the mutation happens to improve MHC binding, this system cannot speak to neoantigens whose mutations leave presentation unchanged, which are the harder and probably more common case.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Finnigan_Nat_Commun_Structural_basis_for_self_discrimination_by_ne_PMID38459027.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-024-46367-9`; the prose sections were written here from the paper itself.

## Citation

Finnigan et al. Nature Communications 2024. Structural basis for self-discrimination by neoantigen-specific TCRs. doi: 10.1038/s41467-024-46367-9

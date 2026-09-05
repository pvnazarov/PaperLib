---
# --- identity ------------------------------------------------
id: 2022-01-01_uksza-2022-nature-neoantigen-quality-pre
id_basis: filename-year
source: Łuksza(2022) Nature; Neoantigen quality predicts immunoediting in survivors of pancreatic cancer.pdf
sha256: 4426ad97b204c28b956b2bf886b705feb9af0474555eadf3cdc1a7043d6d827f
size_bytes: 9477766
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 199384

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-022-04735-9"
year: 2022
title: "Neoantigen quality predicts immunoediting in survivors of pancreatic cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2022_uksza_Nature_Neoantigen_quality_predicts_immunoediting_in_s_PMID35589842.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Neoantigen quality is defined as Q = R x D, combining the probability that a neoantigen is recognised as non-self with the probability it is discriminated from its wild-type counterpart. Cross-reactivity of three TCRs across every single-amino-acid substitution of a model HLA-A*02:01 epitope is used to parameterise discrimination, and the resulting quality measure predicts immunoediting in long-term pancreatic cancer survivors.

## Summary

The model separates two things usually conflated: whether a T cell exists that can see the peptide at all, and whether that T cell can tell the mutant from the self peptide it derives from. Both are needed, and a neoantigen scoring high on one and low on the other is not useful.

The discrimination term is measured rather than assumed - every substitution at every position of a model epitope was tested against three specific TCRs across a 10,000-fold concentration range, and cross-reactivity fell into high, moderate and poor classes depending on position and residue.

## Key points

- Q = R x D decomposes quality into recognition-as-non-self and discrimination-from-self.
- The discrimination term is grounded in measured TCR cross-reactivity across a full substitution scan, not inferred from sequence similarity.
- Tumours evolving under stronger immune pressure lose more immunogenic neoantigens - direct evidence of immunoediting.
- Demonstrated in PDAC, a low-mutation cancer considered resistant to endogenous immunity, which strengthens the generality claim.

## Limitations

The authors state they did not assess changes in non-mutated antigens, nor how cellular composition and tissue environment modulate editing. The discrimination term is calibrated on one HLA-A*02:01 model epitope with three TCRs, then applied broadly - a substantial extrapolation. Long-term PDAC survivors are a selected and small population, and immunoediting is inferred from the mutational landscape rather than observed as it happens.

## Provenance

Located in the published literature, dropped into `inbox/` as `2022_uksza_Nature_Neoantigen_quality_predicts_immunoediting_in_s_PMID35589842.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-022-04735-9`; the prose sections were written here from the paper itself.

## Citation

Łuksza et al. Nature 2022. Neoantigen quality predicts immunoediting in survivors of pancreatic cancer. doi: 10.1038/s41586-022-04735-9

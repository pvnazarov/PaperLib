---
# --- identity ------------------------------------------------
id: 2020-01-01_devlin-2020-nature-chemical-biology-stru
id_basis: filename-year
source: Devlin(2020) Nature Chemical Biology; Structural dissimilarity from self drives neoepitope escape from immune tolerance.pdf
sha256: eeb82ad6d7ac4810078d92a6aa5ac129843b94ebe9df95b8b337556f3aaad773
size_bytes: 5462419
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 108657

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41589-020-0610-1"
year: 2020
title: "Structural dissimilarity from self drives neoepitope escape from immune tolerance"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41589-020-0610-1.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A point mutation at a non-MHC-anchor position in an immunologically active ovarian cancer neoepitope induces structural and dynamic changes that pre-organise the peptide into the conformation optimal for its cognate TCR, allowing high-affinity binding and potent signalling. Immunogenicity here comes from structural and physical dissimilarity to self, not from changed MHC binding.

## Summary

This is the structural mechanism behind the neoantigen quality idea. The mutation does not improve presentation - it is not at an anchor - so nothing about MHC binding distinguishes the neoepitope from its wild-type counterpart. What changes is the peptide's conformational ensemble.

Pre-organisation is the specific claim: the mutant peptide spends more time in the shape the TCR wants, so the entropic cost of binding falls. That is invisible to every sequence-based and affinity-based predictor in this collection.

## Key points

- The immunogenic mutation is at a non-anchor position, so MHC binding is essentially unchanged - affinity-difference metrics would score it as uninteresting.
- Immunogenicity arises from conformational pre-organisation, measured by SPR and thermal stability rather than inferred.
- Gives a concrete physical meaning to 'dissimilarity from self' beyond sequence distance.
- Explains directly why identifying immunogenic neoepitopes from sequence has proven so difficult.

## Limitations

One neoepitope, one TCR, one HLA - a mechanism demonstrated, not a frequency established, and nothing here says what fraction of immunogenic neoepitopes work this way. Several SPR titrations lacked duplicate injections because of sample limitations, which the authors state. Because the effect is conformational, it currently offers no route to prediction: it explains a failure mode without removing it.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41589-020-0610-1.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41589-020-0610-1`; the prose sections were written here from the paper itself.

## Citation

Devlin et al. Nature Chemical Biology 2020. Structural dissimilarity from self drives neoepitope escape from immune tolerance. doi: 10.1038/s41589-020-0610-1

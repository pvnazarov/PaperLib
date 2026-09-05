---
# --- identity ------------------------------------------------
id: 2017-01-01_ott-2017-nature-an-immunogenic-personal
id_basis: filename-year
source: Ott(2017) Nature; An immunogenic personal neoantigen vaccine for patients with melanoma.pdf
sha256: 18f5c6b6fb1a8e32a447041bf3d86eac1cb18f1811171b3361210e64ffe8db85
size_bytes: 6624920
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 135327

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature22991"
year: 2017
title: "An immunogenic personal neoantigen vaccine for patients with melanoma"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nature22991.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

One of the first-in-human personal neoantigen vaccine trials, immunising melanoma patients against up to 20 predicted personal neoantigens. Neoantigens are argued to be highly immunogenic because they are absent from normal tissue and so bypass central thymic tolerance, and the trial demonstrates that a personalised vaccine can induce neoantigen-specific T cell responses.

## Summary

This is the study that moved personal neoantigen vaccination from proposal to demonstrated immunogenicity in patients, and much of the clinical work in this collection descends from it.

The premise it states - that neoantigens bypass central tolerance because they are not present in normal tissue - is worth reading against the later papers here. Koncz, Nelson and Devlin all complicate it: bypassing tolerance is not automatic, and a peptide can be too dissimilar to self to have a T cell available, or similar enough that the responding clones were deleted.

## Key points

- First demonstration that a personal, prediction-driven neoantigen vaccine induces neoantigen-specific T cells in patients.
- Long peptide vaccine with poly-ICLC adjuvant, targeting up to 20 personal neoantigens per patient.
- Establishes the manufacturing and selection workflow that the mRNA trials in this collection later industrialised.
- Frames neoantigens as tolerance-bypassing, the premise later papers here qualify.

## Limitations

A small, single-arm phase I study establishing immunogenicity, not efficacy; no control arm means clinical observations cannot be attributed to the vaccine. Patients were vaccinated after resection with no evidence of disease, so tumour response was not directly measurable. Neoantigen selection depended on the prediction tools of 2017, which later benchmarks in this collection show ranked poorly.

## Provenance

Located in the published literature, dropped into `inbox/` as `nature22991.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature22991`; the prose sections were written here from the paper itself.

## Citation

Ott et al. Nature 2017. An immunogenic personal neoantigen vaccine for patients with melanoma. doi: 10.1038/nature22991

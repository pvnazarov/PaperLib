---
# --- identity ------------------------------------------------
id: 2017-01-01_uksza-2017-nature-a-neoantigen-fitness-m
id_basis: filename-year
source: Łuksza(2017) Nature; A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy.pdf
sha256: dc4a46a8cc631307414b11a67a799dc0076b2fd086219c4e9af8a373bb32625a
size_bytes: 4114463
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 129413

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature24473"
year: 2017
title: "A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nature24473.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A fitness model for tumours based on immune interactions of neoantigens, predicting response to checkpoint blockade. Neoantigen fitness has two components: likelihood of MHC presentation, estimated from binding affinity relative to the wild-type peptide, and T cell recognition, estimated from a nonlinear dependence on sequence similarity to known antigens.

## Summary

This is the model that made neoantigen quality quantitative, and the direct ancestor of the Q = R x D formulation Luksza (2022) later developed. Treating the tumour as a population under immune selection - where neoantigens impose a fitness cost - lets response be predicted from the neoantigen landscape rather than from a mutation count.

Using similarity to known antigens as the recognition proxy is the pragmatic step: rather than model TCRs, it asks whether a peptide resembles something a T cell is already known to see.

## Key points

- Two components - presentation likelihood and recognition probability - combined into a per-neoantigen fitness.
- Presentation uses mutant-versus-wild-type binding, the differential agretopicity idea in a principled form.
- Recognition is estimated from nonlinear sequence similarity to known antigens, avoiding the need to model TCRs.
- Predicts checkpoint blockade response where neoantigen load alone does not.

## Limitations

The authors report their own null results carefully: neoantigen load was not significant at lower fractional partitions including the median in one cohort, showed no significant separation at any threshold in another, and separated patients only in the 32-50% partition range in a third - and for that cohort they used previously unpublished overall survival data differing from the originally published progression-free survival. Cohorts are small and retrospective. Similarity to known antigens depends on curated epitope databases and their biases.

## Provenance

Located in the published literature, dropped into `inbox/` as `nature24473.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature24473`; the prose sections were written here from the paper itself.

## Citation

Łuksza et al. Nature 2017. A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy. doi: 10.1038/nature24473

---
# --- identity ------------------------------------------------
id: 2020-01-01_wells-2020-cell-key-parameters-of-tumor
id_basis: filename-year
source: Wells(2020) Cell; Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction.pdf
sha256: 5ccbc29eb141d7c98cf8068cf0d6c923c90cfb5d548aff0ef1585b0b8d6e1371
size_bytes: 5992035
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 187488

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2020.09.015"
year: 2020
title: "Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS0092867420311569.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A global consortium ran diverse neoantigen prediction pipelines on shared genomic data with matched experimental immunogenicity measurements. Of 608 tested peptide-MHCs, 37 were bound by patient-matched T cells; presentation and recognition characteristics predicted immunogenicity, and model-based interventions improved prediction.

## Summary

The consortium design is what makes this different from a single-group benchmark: many teams' pipelines run on identical genomic data, with the immunogenicity answer measured afterwards rather than assembled from literature. That removes the pipeline-difference confound and the publication bias in curated positives at the same time.

The base rate deserves to be quoted directly - 37 of 608 tested peptide-MHCs were T cell bound. Any claimed improvement in neoantigen ranking has to be read against roughly six percent.

## Key points

- Shared genomic data, many independent pipelines, and immunogenicity measured prospectively rather than curated.
- 37 of 608 tested peptide-MHCs bound by patient-matched T cells - a measured base rate, not an estimate.
- Both presentation and recognition characteristics contribute, and the paper separates them.
- Released as a community resource, and the origin of the Wells feature set used by later tools in this collection.

## Limitations

608 tested peptide-MHCs yielding 37 positives is a small positive set for fitting and validating models, and confidence intervals on any derived parameter are correspondingly wide. Candidates tested were those the participating pipelines proposed, so immunogenic epitopes that every pipeline missed cannot appear - the evaluation cannot measure that blind spot. Patient-matched T cell binding is one assay definition of immunogenicity among several.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS0092867420311569.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2020.09.015`; the prose sections were written here from the paper itself.

## Citation

Wells et al. Cell 2020. Key Parameters of Tumor Epitope Immunogenicity Revealed Through a Consortium Approach Improve Neoantigen Prediction. doi: 10.1016/j.cell.2020.09.015

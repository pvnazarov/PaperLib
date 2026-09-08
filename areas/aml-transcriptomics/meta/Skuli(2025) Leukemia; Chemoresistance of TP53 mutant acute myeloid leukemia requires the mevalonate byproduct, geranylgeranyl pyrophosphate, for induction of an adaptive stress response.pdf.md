---
# --- identity ------------------------------------------------
id: 2025-01-01_skuli-2025-leukemia-chemoresistance-of-t
id_basis: filename-year
source: Skuli(2025) Leukemia; Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stress response.pdf
sha256: f26517a3bc238f33d065cf4275e97efd737564821bcd396ec82473ff8ffb4ae2
size_bytes: 2182070
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 74972

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-025-02668-6"
year: 2025
title: "Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stress response"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Skuli(2025) Leukemia; Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stres.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

RNA sequencing of purified AML patient samples showed higher mevalonate pathway gene expression in TP53-mutant disease. Using isogenic TP53-mutant cell lines and primary samples, resistance to cytarabine correlated with increased mevalonate pathway activity, lower induction of reactive oxygen species, and a mitochondrial response with increased mass and oxidative phosphorylation; statin pretreatment reversed these and chemosensitised the cells. The geranylgeranyl pyrophosphate branch was required, with a newly identified role in regulating glutathione for managing cytarabine-induced ROS. However, statins alone were inadequate to fully reverse chemoresistance in vivo and in a retrospective study of 364 TP53-mutant AML patients who received chemotherapy with a concurrent statin.

## Summary

Notable for reporting its own negative clinical result rather than stopping at the encouraging preclinical one. The mechanism is worked out carefully - mevalonate pathway activity supports the mitochondrial and antioxidant response that lets TP53-mutant cells survive cytarabine, and the specific byproduct required is geranylgeranyl pyrophosphate, with a role in maintaining glutathione previously described only in adipose tissue.

Then they test it where it counts. Statins did not fully reverse chemoresistance in vivo, and a retrospective analysis of 364 patients who happened to receive a statin alongside chemotherapy showed the same. Rather than abandoning the target, they conclude that statins are the wrong tool - they inhibit the pathway upstream of several branches - and point to specific geranylgeranyl transferase inhibitors such as GGTI2418, already promising in refractory peripheral T-cell lymphoma.

## Key points

- TP53-mutant AML shows elevated mevalonate pathway expression, which supports the mitochondrial and antioxidant response to cytarabine.
- Geranylgeranyl pyrophosphate specifically is required, acting both in mitochondrial biogenesis and in regulating glutathione.
- Statins reverse the phenotype in vitro and chemosensitise TP53-mutant cells.
- Statins were inadequate in vivo and in a retrospective analysis of 364 TP53-mutant patients on concurrent statins - a negative clinical result the authors report themselves.
- The proposed route forward is direct geranylgeranyl transferase inhibition rather than upstream statin blockade.

## Limitations

The clinical test failed, which the authors state, and the retrospective statin analysis carries its own confounding - patients on statins differ systematically, and doses used for cardiovascular indications may not achieve the exposure the mechanism needs. The authors also say the specific function of GGPP remains elusive and that future studies must define how it regulates mitochondrial biogenesis and glutathione synthesis, so the mechanism is localised to a byproduct rather than to a molecular action. The GGTI proposal is extrapolation from a different disease. Isogenic TP53-mutant lines are engineered, and primary sample work supplements rather than replaces them. Direct GGPP targeting is untested here.

## Provenance

Located in the published literature, dropped into `inbox/` as `Skuli(2025) Leukemia; Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stres.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-025-02668-6`; the prose sections were written here from the paper itself.

## Citation

Skuli et al. Leukemia 2025. Chemoresistance of TP53 mutant acute myeloid leukemia requires the mevalonate byproduct, geranylgeranyl pyrophosphate, for induction of an adaptive stress response. doi: 10.1038/s41375-025-02668-6

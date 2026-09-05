---
# --- identity ------------------------------------------------
id: 2024-01-01_jiang-2024-bioinformatics-neoapred-a-dee
id_basis: filename-year
source: Jiang(2024) Bioinformatics; NeoaPred a deep-learning framework for predicting immunogenic neoantigen based on surface and structural features of peptide–human leukocyte antigen complexes.pdf
sha256: 0a4ae06d676731286a0b6daaf2294a8d421d52efdbbe184325afa646c6c8451d
size_bytes: 8391785
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 62717

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioinformatics/btae547"
year: 2024
title: "NeoaPred: a deep-learning framework for predicting immunogenic neoantigen based on surface and structural features of peptide–human leukocyte antigen complexes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Jiang_Bioinformatics_NeoaPred_a_deep_learning_framework_for_predict_PMID39276157.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoaPred builds pHLA-I complex structures (82.37% within 1 Å RMSD) and derives a foreignness score from differences in surface, structural and atom-group features between the mutant peptide and its wild-type counterpart. It reports AUROC 0.81 and AUPRC 0.54 on the test set, above the methods compared.

## Summary

This is the structural version of the differential-agretopicity idea: instead of contrasting two predicted binding affinities, it contrasts two predicted complex surfaces, which captures shape and chemistry the affinity number collapses.

The reported AUPRC of 0.54 is the more informative figure, since immunogenic neoantigens are rare and precision-recall reflects that imbalance where AUROC does not.

## Key points

- Predicts pHLA-I structures itself rather than requiring solved ones, with 82.37% under 1 Å RMSD.
- The foreignness score is a mutant-versus-wild-type surface contrast, not an absolute property of the neopeptide.
- AUROC 0.81 with AUPRC 0.54 - reported together, which is the honest pairing for an imbalanced task.
- Open source under Apache v2.0.

## Limitations

The authors list their own constraints: HLA class II conformations remain unsolved and are not covered despite class II neoantigens mattering for some responses; HLA-C data are sparse and predictions for HLA-C 'warrant particular caution'; and foreignness is explicitly not the only determinant, with antigen processing and presentation still required. Test-set AUPRC of 0.54 means roughly half of top-ranked candidates are expected to be wrong.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Jiang_Bioinformatics_NeoaPred_a_deep_learning_framework_for_predict_PMID39276157.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioinformatics/btae547`; the prose sections were written here from the paper itself.

## Citation

Jiang et al. Bioinformatics 2024. NeoaPred: a deep-learning framework for predicting immunogenic neoantigen based on surface and structural features of peptide–human leukocyte antigen complexes. doi: 10.1093/bioinformatics/btae547

---
# --- identity ------------------------------------------------
id: 2018-01-01_ghorani-2018-annals-of-oncology-differen
id_basis: filename-year
source: Ghorani(2018) Annals of Oncology; Differential binding affinity of mutated peptides for MHC class I is a predictor of survival in advanced lung cancer and melanoma.pdf
sha256: 11e79e4f1f6597cd81bc455d7439bddfcc935e609a12ce89ad1eb8cbc60f43bf
size_bytes: 682532
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 69717

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/annonc/mdx687"
year: 2018
title: "Differential binding affinity of mutated peptides for MHC class I is a predictor of survival in advanced lung cancer and melanoma"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2018_Ghorani_Ann_Oncol_Differential_binding_affinity_of_mutated_pepti_PMID29361136.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The differential agretopicity index (DAI) - the difference in predicted MHC-I binding affinity between a mutant peptide and its wild-type counterpart - is tested against immune infiltration and outcome in advanced NSCLC (n=66) and melanoma (n=72) from TCGA, plus three immunotherapy-treated cohorts (melanoma n=131, NSCLC n=31). DAI is associated with survival.

## Summary

The idea is that what makes a neopeptide visible is not its absolute binding but how much better it binds than the self peptide it came from: a mutation that barely changes affinity presents T cells with something they were tolerised to.

Neopeptides and their clonal status were called from genomic data, so the analysis distinguishes clonal from subclonal neoantigens - which matters because only clonal ones are present in every tumour cell.

## Key points

- DAI reframes immunogenicity as a mutant-versus-wild-type contrast rather than an absolute binding threshold.
- Tested in both untreated TCGA cohorts and immunotherapy-treated cohorts, in two tumour types.
- Clonal status is incorporated, separating neoantigens present in all tumour cells from subclonal ones.
- One of the origins of the 'differential agretopicity' family of features now standard in neoantigen ranking.

## Limitations

Cohorts are small - 66 and 72 in the discovery arms, 31 in one treated arm - and the analysis is retrospective and observational, so survival associations are not causal. DAI is a difference between two predicted affinities, and prediction error enters twice. The paper reports an association with outcome, not a validated ranking improvement, and the later Wan and Muller benchmarks in this collection should be read alongside it.

## Provenance

Located in the published literature, dropped into `inbox/` as `2018_Ghorani_Ann_Oncol_Differential_binding_affinity_of_mutated_pepti_PMID29361136.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/annonc/mdx687`; the prose sections were written here from the paper itself.

## Citation

Ghorani et al. Annals of Oncology 2018. Differential binding affinity of mutated peptides for MHC class I is a predictor of survival in advanced lung cancer and melanoma. doi: 10.1093/annonc/mdx687

---
# --- identity ------------------------------------------------
id: 2018-01-01_zhao-2018-plos-computational-biology-sys
id_basis: filename-year
source: Zhao(2018) PLOS Computational Biology; Systematically benchmarking peptide-MHC binding predictors From synthetic to naturally processed epitopes.pdf
sha256: cd8f5ffd4170a65ced2b91790a5376172771323eda0e341ca37b41c6d2d56143
size_bytes: 4476861
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 140868

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1371/journal.pcbi.1006457"
year: 2018
title: "Systematically benchmarking peptide-MHC binding predictors: From synthetic to naturally processed epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2018_Zhao_PLoS_Comput_Biol_Systematically_benchmarking_peptide_MHC_bindin_PMID30408041.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A blind benchmark of 18 MHC binding predictors across 32 HLA class I and 24 class II alleles, using previously untested data covering both synthetic binding measurements and naturally processed, MHC-eluted epitopes. Neural network approaches outperformed regression and structural modelling, with mhcflurry and nn_align best for class I 9-mers and class II 15-mers respectively (AUC 0.911).

## Summary

The design choice that gives this paper its value is testing on naturally processed ligands as well as synthetic binding data. Predictors trained and tested on binding assays can look excellent while failing at the thing that matters, which is identifying peptides the cell actually presents.

The most consequential negative result is that although the top methods classify binders and non-binders well, they deliver low correlation on absolute affinity - so ranking candidates by predicted affinity value, which is what neoantigen pipelines do, is not well supported by the evidence.

## Key points

- Blind test across 32 class I and 24 class II alleles, on data unseen by any of the 18 predictors.
- Classification is good (AUC 0.911) but absolute affinity correlation is low - prioritising by predicted affinity may not be appropriate.
- The authors recommend using predicted relative rank rather than predicted absolute affinity, which is now standard practice.
- Incorporating mass-spectrometry naturally-presented peptides into training measurably improved accuracy.

## Limitations

The authors flag that experimental binding assays have limited resolution in the high-affinity zone, so the training targets themselves are inaccurate where it matters most - an error floor no model can pass. This benchmarks binding, not immunogenicity. It is a 2018 snapshot and several benchmarked tools have since been superseded, so the rankings are dated even though the methodological conclusions are not.

## Provenance

Located in the published literature, dropped into `inbox/` as `2018_Zhao_PLoS_Comput_Biol_Systematically_benchmarking_peptide_MHC_bindin_PMID30408041.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1371/journal.pcbi.1006457`; the prose sections were written here from the paper itself.

## Citation

Zhao et al. PLOS Computational Biology 2018. Systematically benchmarking peptide-MHC binding predictors: From synthetic to naturally processed epitopes. doi: 10.1371/journal.pcbi.1006457

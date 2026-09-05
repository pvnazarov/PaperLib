---
# --- identity ------------------------------------------------
id: 2020-01-01_reynisson-2020-nucleic-acids-research-ne
id_basis: filename-year
source: Reynisson(2020) Nucleic Acids Research; NetMHCpan-4.1 and NetMHCIIpan-4.0 improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data.pdf
sha256: ac5722a2e7452f3dac4b09c921a1b9c3988b9d8c6f3170522dd2b417466dfca0
size_bytes: 1983921
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 36362

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/nar/gkaa379"
year: 2020
title: "NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2020_Reynisson_Nucleic_Acids_Res_NetMHCpan_4_1_and_NetMHCIIpan_4_0_improved_pre_PMID32406916.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NetMHCpan-4.1 and NetMHCIIpan-4.0 integrate binding-affinity data with mass-spectrometry eluted-ligand data in a single training framework, using NNAlign_MA to assign multi-allelic eluted ligands to individual MHC restrictions during training. This both discovers novel motifs and substantially expands the usable training set.

## Summary

The paper classifies predictors into three generations: trained on binding affinity alone; trained on single-allele eluted ligands; and trained on multi-allele eluted ligands with concurrent motif deconvolution. The third is what this work implements.

The deconvolution matters because most immunopeptidomics comes from poly-allelic samples where the presenting allele is unknown. Pseudolabelling those sequences into single-allele specificities during training turns otherwise unusable data into the largest available source of presentation evidence.

## Key points

- Binding affinity data models only one event in the presentation pathway; eluted ligands capture the pathway's actual output.
- NNAlign_MA clusters ambiguous multi-allele ligands into single-MHC specificities during training, enabling novel motif discovery.
- Covers both MHC-I and MHC-II in one framework.
- The de facto standard baseline that nearly every other predictor in this collection is compared against.

## Limitations

Eluted-ligand data carry mass-spectrometry detection bias towards abundant, well-ionising peptides, and that bias is now baked into the field's most-used predictor. Predicting presentation is not predicting immunogenicity, a gap this paper does not claim to close. Alleles with little immunopeptidomics data still rely on pan-specific extrapolation, so per-allele performance is uneven in ways an aggregate figure hides.

## Provenance

Located in the published literature, dropped into `inbox/` as `2020_Reynisson_Nucleic_Acids_Res_NetMHCpan_4_1_and_NetMHCIIpan_4_0_improved_pre_PMID32406916.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/nar/gkaa379`; the prose sections were written here from the paper itself.

## Citation

Reynisson et al. Nucleic Acids Research 2020. NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data. doi: 10.1093/nar/gkaa379

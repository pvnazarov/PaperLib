---
# --- identity ------------------------------------------------
id: 2025-01-01_tadros-2025-genome-medicine-predicting-m
id_basis: filename-year
source: Tadros(2025) Genome Medicine; Predicting MHC-I ligands across alleles and species how far can we go.pdf
sha256: 819a3f6a746c450183c6547e5bfd143ba8d0ce8b2bc1d71933060b8e896b27ee
size_bytes: 3198404
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 74813

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13073-025-01450-8"
year: 2025
title: "Predicting MHC-I ligands across alleles and species: how far can we go?"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2025_Tadros_Genome_Med_Predicting_MHC_I_ligands_across_alleles_and_sp_PMID40114147.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Using an expanded MixMHCpred3.0 architecture, the authors systematically assess how far MHC-I ligand prediction extends to alleles with no known ligand data. Accuracy is high for most human and laboratory-mouse alleles but significantly lower in other species, and the molecular determinants of that drop are characterised.

## Summary

This asks the question every pan-specific predictor implicitly claims to have answered: for which alleles is the extrapolation actually valid? The answer is quantified through binding-site distance from alleles with known ligands.

The encouraging result is that 127 human HLA-I alleles with available ligands cover the human specificity space well, including most HLA-A, -B and -C. The limiting result is that only 48% of mouse alleles meet the same threshold, and other species fare worse.

## Key points

- Turns 'does pan-specific prediction generalise' into a measurable binding-site distance rather than an assumption.
- 127 human alleles with ligands give very good coverage of human MHC-I specificity space; HLA-F is the exception, lacking reliable ligands.
- Only 48% of mouse MHC-I alleles meet the accuracy threshold - all of them from laboratory strains.
- Two failure modes identified: binding-site positions with amino acids never seen among trained alleles, and larger overall binding-site divergence.

## Limitations

Binding-site distance is a proxy for predictability and is validated against the same predictor family it is used to assess. Coverage claims for human alleles rest on the alleles that have ligands, which follow research and population attention rather than global HLA diversity. Non-human accuracy is characterised but not fixed, so comparative and veterinary applications remain poorly served.

## Provenance

Located in the published literature, dropped into `inbox/` as `2025_Tadros_Genome_Med_Predicting_MHC_I_ligands_across_alleles_and_sp_PMID40114147.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13073-025-01450-8`; the prose sections were written here from the paper itself.

## Citation

Tadros et al. Genome Medicine 2025. Predicting MHC-I ligands across alleles and species: how far can we go?. doi: 10.1186/s13073-025-01450-8

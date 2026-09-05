---
# --- identity ------------------------------------------------
id: 2023-01-01_albert-2023-nature-machine-intelligence
id_basis: filename-year
source: Albert(2023) Nature Machine Intelligence; Deep neural networks predict class I major histocompatibility complex epitope presentation and transfer learn neoepitope immunogenicity.pdf
sha256: b21413320714dc78e36250db4e0e634b329deea723afa85ac18def942421b998
size_bytes: 8198502
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 207630

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s42256-023-00694-6"
year: 2023
title: "Deep neural networks predict class I major histocompatibility complex epitope presentation and transfer learn neoepitope immunogenicity"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s42256-023-00694-6.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

BigMHC is an ensemble of seven pan-allelic deep neural networks trained on peptide-MHC eluted ligand mass spectrometry data, then transfer-learned on antigen-specific immune response assays to predict neoepitope immunogenicity. It significantly improves epitope presentation prediction over four state-of-the-art classifiers.

## Summary

The framing is the needle-in-a-haystack problem: experimental validation of candidate neoepitopes is extremely resource intensive and the vast majority of candidates are non-immunogenic, so precision at the top of the ranking is the only metric that matters operationally.

The two-stage design - learn presentation from plentiful eluted-ligand data, then transfer to scarce immunogenicity labels - is the same strategy ImmuneApp uses, and is currently the field's main answer to the shortage of immunogenicity data.

## Key points

- Seven-model pan-allelic ensemble, so no per-allele training is needed for alleles with little data.
- Transfer learning from presentation to immunogenicity: 5,279 of 6,873 validated examples are neoepitopes, so the transfer target is cancer-specific rather than pathogen-dominated.
- Optimises precision rather than overall discrimination, matching how the predictions are actually used.
- Benchmarked against four current classifiers on a held-out presentation test set.

## Limitations

The authors are unusually candid: presentation is evaluated against mass-spectrometry eluted ligands with RANDOM negatives, so positives are bounded by MS detection efficiency and negatives are not guaranteed negative. BigMHC is MHC-I only. Three strong competitors - MHCflurry-2.0, MixMHCpred-2.2 and HLAthena - could not be included in the presentation comparison because their training data already contained most or all of the test epitopes, which is a clean statement of how circular this subfield's benchmarks have become.

## Provenance

Located in the published literature, dropped into `inbox/` as `s42256-023-00694-6.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s42256-023-00694-6`; the prose sections were written here from the paper itself.

## Citation

AlexanderAlbert et al. Nature Machine Intelligence 2023. Deep neural networks predict class I major histocompatibility complex epitope presentation and transfer learn neoepitope immunogenicity. doi: 10.1038/s42256-023-00694-6

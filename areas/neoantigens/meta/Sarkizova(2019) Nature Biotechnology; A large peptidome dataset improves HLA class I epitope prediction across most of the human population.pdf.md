---
# --- identity ------------------------------------------------
id: 2019-01-01_sarkizova-2019-nature-biotechnology-a-la
id_basis: filename-year
source: Sarkizova(2019) Nature Biotechnology; A large peptidome dataset improves HLA class I epitope prediction across most of the human population.pdf
sha256: 50c254fddf5034fc358ee4ba46093a6f230e3692d8cba87131d2be0dd99c56a5
size_bytes: 5771764
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 221441

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41587-019-0322-9"
year: 2019
title: "A large peptidome dataset improves HLA class I epitope prediction across most of the human population"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41587-019-0322-9.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Mass spectrometry profiling of more than 185,000 peptides eluted from 95 HLA-A, -B, -C and -G mono-allelic cell lines produces training data covering a large fraction of the human population. Predictors trained on it achieve 1.5-2.7x improvements in positive predictive value at the top 0.1% of the dataset, corresponding to 3-12x gains at 40% recall.

## Summary

Mono-allelic cell lines are the point. Ordinary immunopeptidomics comes from cells expressing six class I alleles at once, so every observed peptide has an ambiguous restriction; engineering lines that express a single allele removes the deconvolution problem entirely and yields clean per-allele motifs.

The reported gain is stated as positive predictive value at the extreme top of the ranking, which is the operationally honest metric for a screening task, rather than an AUC.

## Key points

- >185,000 peptides from 95 mono-allelic lines - unambiguous allele assignment by construction.
- Covers HLA-C and -G, chronically under-served by earlier datasets.
- 1.5-2.7x PPV improvement at the top 0.1%, or 3-12x at 40% recall - the metric that matters for screening.
- Peptides proposed to arise from proteasomal splicing scored poorly for predicted binding, bearing on the disputed prevalence of spliced epitopes.

## Limitations

The authors attribute residual error largely to motif complexity and abundance - some alleles are simply harder to learn, so aggregate figures hide uneven per-allele performance. They estimate about 1% of apparent errors may be false-positive MS identifications at 1% FDR. In one external comparison the competing predictor did better on non-9-mers, with the caveat that the evaluation dataset was in its training data - the circularity that recurs throughout this subfield. Mono-allelic cell lines are also not tissues, and lack the processing context of a real cell type.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41587-019-0322-9.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41587-019-0322-9`; the prose sections were written here from the paper itself.

## Citation

Sarkizova et al. Nature Biotechnology 2019. A large peptidome dataset improves HLA class I epitope prediction across most of the human population. doi: 10.1038/s41587-019-0322-9

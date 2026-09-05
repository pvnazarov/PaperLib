---
# --- identity ------------------------------------------------
id: 2024-01-01_li-2024-science-translational-medicine-s
id_basis: filename-year
source: Li(2024) Science Translational Medicine; Splicing neoantigen discovery with SNAF reveals shared targets for cancer immunotherapy.pdf
sha256: f6bd307fe67ec60a2edf8a1ccbf67ed13e818d1d70aa6114aa4fb097f2136117
size_bytes: 2818082
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 168102

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/scitranslmed.ade2886"
year: 2024
title: "Splicing neoantigen discovery with SNAF reveals shared targets for cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nihms-2026803.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

SNAF (Splicing Neo Antigen Finder) defines tumour-specific and likely immunogenic neoantigens from patient RNA-seq, targeting post-transcriptional regulation as a source of neoantigens. Because splicing alterations recur across patients, it identifies shared rather than purely private targets, supported by long-read sequencing and spike-in mass spectrometry.

## Summary

The strategic claim is about shared targets. Mutation-derived neoantigens are almost entirely private, which forces fully individualised manufacturing; splicing-derived neoantigens recur across patients, which would permit off-the-shelf therapies.

It also addresses the group immunotherapy currently excludes - patients with low mutational burden, for whom mutation-based pipelines find too few candidates to work with.

## Key points

- Targets post-transcriptional regulation rather than somatic mutations, a largely untapped source.
- Splicing neoantigens recur across patients, making shared off-the-shelf targets possible.
- Aimed at low-mutation-burden tumours normally excluded from immunotherapy.
- Supported by long-read sequencing, spike-in mass spectrometry and peptide-MHC stability assays rather than prediction alone.

## Limitations

The authors state their open questions: whether tumours suppress presentation of splicing neoantigens the way they balance oncogene mutations against MHC presentation is unknown, and the work focuses on HLA-I and CD8 while HLA-II and CD4 responses to splicing neoantigens are unaddressed. They also note the analysis would ideally need single-cell resolution across hundreds of cell types, which it does not have. Detecting a splice junction and demonstrating an immunogenic epitope remain separate steps.

## Provenance

Located in the published literature, dropped into `inbox/` as `nihms-2026803.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/scitranslmed.ade2886`; the prose sections were written here from the paper itself.

## Citation

Li et al. Science Translational Medicine 2024. Splicing neoantigen discovery with SNAF reveals shared targets for cancer immunotherapy. doi: 10.1126/scitranslmed.ade2886

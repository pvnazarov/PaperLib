---
# --- identity ------------------------------------------------
id: 2024-01-01_lang-2024-bioinformatics-advances-predic
id_basis: filename-year
source: Lang(2024) Bioinformatics Advances; Prediction of tumor-specific splicing from somatic mutations as a source of neoantigen candidates.pdf
sha256: 5e4baa7d732ddc9efd5325a0211cca39b8b12e6b0792dc0760752f963eb89255
size_bytes: 2337345
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 82243

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bioadv/vbae080"
year: 2024
title: "Prediction of tumor-specific splicing from somatic mutations as a source of neoantigen candidates"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as vbae080.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

splice2neo integrates predicted splice effects of somatic mutations with splice junctions detected in tumour RNA-seq and annotates the resulting transcripts and peptides; EasyQuant provides targeted read mapping to candidate junctions. Under a stringent rule, 1.7 splice junctions per patient were predicted as targets at under 5% FDR in a melanoma cohort, with tumour-specificity confirmed against independent healthy tissue.

## Summary

Alternative splicing is an attractive neoantigen source and a treacherous one, because many non-canonical junctions found in tumours also occur in healthy tissue. The design decision here is to restrict attention to splicing caused by a somatic mutation, which supplies a tumour-specific cause rather than relying on absence from a normal reference.

The yield is deliberately small - 1.7 junctions per patient - and that is the point: a stringent rule with a measured false discovery rate, rather than a long list requiring manual triage.

## Key points

- Requires a somatic mutation as the cause of the splice event, giving tumour-specificity by construction.
- 1.7 target junctions per patient at FDR below 5% - a stated error rate, which is rare in this literature.
- Tumour-specificity confirmed against independent healthy tissue, and individual exon-skipping events confirmed experimentally from tumour RNA.
- Most target junctions encoded neoepitope candidates with predicted MHC-I or MHC-II binding.

## Limitations

The pipeline chains two splice-effect predictors (MMSplice, SpliceAI) with junction detection and then MHC binding prediction, so four error rates compound and only the junction-level FDR is quantified. Filtering against normal junctions from 1,740 samples is only as good as that panel's coverage of healthy splicing diversity. Experimental confirmation covers exon skipping events, not the full range of predicted effects, and no epitope is shown to be immunogenic.

## Provenance

Located in the published literature, dropped into `inbox/` as `vbae080.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bioadv/vbae080`; the prose sections were written here from the paper itself.

## Citation

Lang et al. Bioinformatics Advances 2024. Prediction of tumor-specific splicing from somatic mutations as a source of neoantigen candidates. doi: 10.1093/bioadv/vbae080

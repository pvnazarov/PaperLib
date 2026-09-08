---
# --- identity ------------------------------------------------
id: 2024-01-01_zhang-2024-genome-biology-rna-binding-pr
id_basis: filename-year
source: Zhang(2024) Genome Biology; RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9.pdf
sha256: f9065908d508841e96e0de959c80746b2eca3229130c1d78704ae8a614ea6650
size_bytes: 10128828
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 118206

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13059-023-03149-8"
year: 2024
title: "RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Zhang(2024) Genome Biol; RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genome-wide CRISPR/Cas9 screening in HOXA9-driven reporter acute leukemia cells identified the poorly characterised RNA-binding protein RBM5 as the top candidate required for leukemia cell fitness. RBM5 is highly overexpressed in AML patients relative to healthy individuals, and its loss by knockout or knockdown impairs leukemia maintenance in vitro and in vivo. Domain CRISPR screening showed RBM5 acts through a non-canonical transcriptional regulation circuitry rather than RNA splicing, dependent on its DNA-binding domains. HOXA9 is the downstream target: ectopic HOXA9 rescues the proliferation defect, and acute RBM5 degradation via an auxin-inducible degron immediately reduces HOXA9 transcription.

## Summary

A screen designed around the right readout - a HOXA9-driven reporter rather than viability - so the top hit is a regulator of the programme rather than a general fitness gene.

The mechanistic surprise is that an RNA-binding protein works through DNA. Domain-level CRISPR shows the requirement maps to RBM5's DNA-binding domains, not to splicing function, which is what RBM5 is known for. The degron experiment is the decisive control: acute degradation immediately reduces HOXA9 transcription, which distinguishes a direct transcriptional effect from the slow indirect consequences that knockdown over days would produce.

## Key points

- A HOXA9-reporter CRISPR screen identifies regulators of the oncogenic programme rather than general fitness genes.
- RBM5 is the top hit, overexpressed in AML patients, and required for leukemia maintenance in vitro and in vivo.
- Domain CRISPR shows the requirement maps to DNA-binding domains, not splicing - a non-canonical function for an RNA-binding protein.
- HOXA9 is the downstream target: ectopic HOXA9 rescues the proliferation defect of RBM5 loss.
- Acute degron-mediated degradation immediately reduces HOXA9 transcription, establishing a direct rather than indirect effect.

## Limitations

No RBM5 inhibitor exists, so the therapeutic claim rests on genetic perturbation. The degron system requires engineering the endogenous protein, confining those experiments to modified cell lines. HOXA9 rescue shows sufficiency to restore proliferation but not that HOXA9 is the only relevant target of RBM5. RBM5 is described as a tumour suppressor in several solid tumours, so its oncogenic role here is context-specific in a way the paper does not reconcile. Whether normal hematopoietic cells tolerate RBM5 loss - the question that determines any therapeutic window - is not addressed in the summary evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Zhang(2024) Genome Biol; RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13059-023-03149-8`; the prose sections were written here from the paper itself.

## Citation

Zhang et al. Genome Biology 2024. RNA-binding protein RBM5 plays an essential role in acute myeloid leukemia by activating the oncogenic protein HOXA9. doi: 10.1186/s13059-023-03149-8

---
# --- identity ------------------------------------------------
id: 2025-01-01_graber-2025-nature-machine-intelligence
id_basis: filename-year
source: Graber(2025) Nature Machine Intelligence; Resolving data bias improves generalization in binding affinity prediction.pdf
sha256: 735ae566a6a9f8d01f279ae33ed053f979889a12e3451c60074e0b1f8766465e
size_bytes: 7709934
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 127408

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s42256-025-01124-5"
year: 2025
title: "Resolving data bias improves generalization in binding affinity prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s42256-025-01124-5.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Train-test leakage between PDBbind and the CASF benchmarks has severely inflated reported performance of deep-learning protein-ligand binding affinity models. The authors build PDBbind CleanSplit, a structure-based filtered training set removing leakage and internal redundancy; retraining top models on it causes their benchmark scores to drop substantially.

## Summary

Not an immunology paper. It is here because it is the cleanest available demonstration of the failure mode that Zhang (2026) and Zhao (2018) find inside this field: benchmark performance driven by overlap between training and test data rather than by generalisation.

The evidence is unusually direct - the same published models, retrained on a leakage-free split, get substantially worse. That isolates leakage as the cause rather than inferring it.

## Key points

- Structure-based filtering removes both train-test leakage and within-training redundancy.
- Retraining existing top models on the clean split drops their benchmark performance substantially - leakage was doing the work.
- Demonstrates the general principle behind the immunogenicity-benchmark problems documented elsewhere in this collection.
- The authors' own graph neural network is evaluated under the same clean conditions.

## Limitations

The domain is protein-ligand drug design, not peptide-MHC, so the specific numbers transfer to this collection only as an analogy. Structure-based similarity filtering requires choosing a threshold, and where that threshold sits determines how much performance drops. A cleaner split lowers scores; it does not by itself show the retrained models are useful.

## Provenance

Located in the published literature, dropped into `inbox/` as `s42256-025-01124-5.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s42256-025-01124-5`; the prose sections were written here from the paper itself.

## Citation

Graber et al. Nature Machine Intelligence 2025. Resolving data bias improves generalization in binding affinity prediction. doi: 10.1038/s42256-025-01124-5

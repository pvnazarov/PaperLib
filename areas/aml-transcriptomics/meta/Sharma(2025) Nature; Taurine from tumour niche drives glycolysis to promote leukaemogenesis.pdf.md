---
# --- identity ------------------------------------------------
id: 2025-01-01_sharma-2025-nature-taurine-from-tumour-n
id_basis: filename-year
source: Sharma(2025) Nature; Taurine from tumour niche drives glycolysis to promote leukaemogenesis.pdf
sha256: e6eca18ea9f95f7d7cd082929ffd76b577c4f981ea470fddd11f75bea7037c42
size_bytes: 19508082
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 436608

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-025-09018-7"
year: 2025
title: "Taurine from tumour niche drives glycolysis to promote leukaemogenesis"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Sharma(2025) Nature; Taurine from tumour niche drives glycolysis to promote leukaemogenesis.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Temporal single-cell RNA sequencing identifies molecular cues from the bone marrow stromal niche that engage leukemia stem-enriched cells during oncogenic progression; integrating these with human LSC RNA-seq and an in vivo CRISPR screen of LSC dependencies identifies the taurine-taurine transporter (TAUT) axis as a critical dependency of aggressive myeloid leukemias. CDO1-driven taurine biosynthesis is restricted to osteolineage cells and increases with disease progression; blocking CDO1 in those cells impairs LSC growth and improves survival. TAUT loss-of-function models and patient-derived AML cells show that TAUT inhibition impairs leukemia progression in vivo, synergises with venetoclax, and acts by blocking RAG-GTP-dependent mTOR activation and downstream glycolysis.

## Summary

A systematic way of finding microenvironmental dependencies rather than a lucky one. The design intersects three datasets - what the niche secretes over time, which receptors are enriched on human leukemia stem cells, and which of those are required in vivo - so the surviving candidate is a ligand-receptor pair that is present, engaged and necessary.

What emerges is a metabolite the leukemia does not make. Taurine is synthesised by osteolineage cells through CDO1, and the leukemic cells import it; blocking production in the niche or uptake in the tumour both work, which is unusual - it means the dependency can be attacked from either side. TAUT is elevated in venetoclax-resistant AML and inhibition synergises with venetoclax in primary human cells, giving it immediate clinical relevance.

## Key points

- Intersects temporal niche scRNA-seq, human LSC expression and an in vivo CRISPR screen to find microenvironmental dependencies systematically.
- Taurine is produced by osteolineage cells via CDO1 and imported by leukemia cells through TAUT - a dependency attackable from either side.
- CDO1-driven taurine biosynthesis increases during myeloid disease progression, and blocking it in the niche impairs LSC growth and improves survival.
- TAUT inhibition impairs leukemia progression in vivo in genetic models and patient-derived AML.
- TAUT is elevated in venetoclax-resistant AML, and inhibition synergises with venetoclax; the mechanism is loss of RAG-GTP-dependent mTOR activation and glycolysis.

## Limitations

The authors state that stable and effective in vivo taurine inhibitors need to be developed - the current evidence is genetic, and the available pharmacological tools for taurine transport are old and poorly characterised. Taurine is an abundant dietary and endogenous metabolite with roles in bile acid conjugation, osmoregulation and cardiac and retinal function, so systemic inhibition of its transport raises broad toxicity concerns not addressed here. The niche work is in mouse models; human evidence is expression data plus patient-derived AML responses. Whether dietary taurine, widely consumed in supplements and energy drinks, contributes to the leukemic pool is a question the study raises implicitly but does not address. The venetoclax synergy is in vitro in primary cells.

## Provenance

Located in the published literature, dropped into `inbox/` as `Sharma(2025) Nature; Taurine from tumour niche drives glycolysis to promote leukaemogenesis.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-025-09018-7`; the prose sections were written here from the paper itself.

## Citation

Sharma et al. Nature 2025. Taurine from tumour niche drives glycolysis to promote leukaemogenesis. doi: 10.1038/s41586-025-09018-7

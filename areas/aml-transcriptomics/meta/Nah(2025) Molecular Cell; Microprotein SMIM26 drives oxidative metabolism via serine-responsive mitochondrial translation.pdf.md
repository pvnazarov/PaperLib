---
# --- identity ------------------------------------------------
id: 2025-01-01_nah-2025-molecular-cell-microprotein-smi
id_basis: filename-year
source: Nah(2025) Molecular Cell; Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation.pdf
sha256: 0a2b4a39d8836acbd43586494ed552fdddd4fb86d757505c76c753dd7196de29
size_bytes: 36094231
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 155958

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.molcel.2025.05.033"
year: 2025
title: "Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Nah(2025) Mol Cell; Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A genome-wide CRISPR screen targeting small ORF-encoded microproteins found that deleting the LINC00493-encoded microprotein SMIM26 sensitises cells to one-carbon restriction. SMIM26 interacts with the mitochondrial serine transporters SFXN1/2 and the mitoribosome, forming a triad that facilitates translation of the complex I subunit mt-ND5. Its loss impairs serine import, reduces folate intermediates and disrupts mitochondrial tRNA modifications, causing ND5 translation failure and complex I deficiency. SMIM26 deletion is embryonic lethal in mice and impedes tumour growth in a xenograft model of folate-dependent AML.

## Summary

A mechanism for matching respiratory chain capacity to nutrient supply, built on a class of proteins that until recently were not thought to exist - nearly 30% of the 120 proteins needed to build the electron transport chain are under 100 amino acids and therefore microproteins by definition.

The architecture proposed is spatial rather than merely regulatory: SMIM26 physically links a serine transporter to the mitoribosome, so the ribosome translating ND5 sits where serine enters. Serine feeds the mitochondrial folate cycle, folate intermediates are needed for specific tRNA modifications, and those modifications are preferentially required for ND5 - and ND5 is the last module incorporated into complex I, making it a natural control point. The AML relevance is that folate-dependent AML depends on this axis, and the xenograft result follows.

## Key points

- SMIM26, a microprotein from a lncRNA, couples mitochondrial serine import to complex I biogenesis.
- It forms an SFXN1/2-SMIM26-mitoribosome triad, positioning ND5-translating ribosomes at the serine entry point.
- One-carbon-derived metabolites are needed for tRNA modifications preferentially required to translate ND5.
- ND5 is the last module added to complex I, making it a natural node for rapid control of complex I levels.
- SMIM26 deletion is embryonic lethal in mice and impedes growth of a folate-dependent AML xenograft.

## Limitations

Embryonic lethality in mice is the plainest statement of the problem with SMIM26 as a therapeutic target - it is essential in normal development, and no therapeutic window is proposed. The AML application is a single xenograft in a folate-dependent model, so leukemia is one application of a study whose main contribution is general cell biology. The authors state that how SMIM26 potentiates SFXN1 activity remains unclear and offer two alternatives - conformational change or ribosome positioning - without distinguishing them. They also report a discrepancy with prior work: another study attributed reduced glutathione in SMIM26-deficient cells to impaired mitochondrial GSH import via SLC25A11, whereas they attribute it to impaired transsulfuration, so the microprotein's functions across studies are not yet reconciled.

## Provenance

Located in the published literature, dropped into `inbox/` as `Nah(2025) Mol Cell; Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.molcel.2025.05.033`; the prose sections were written here from the paper itself.

## Citation

Nah et al. Molecular Cell 2025. Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation. doi: 10.1016/j.molcel.2025.05.033

---
# --- identity ------------------------------------------------
id: 2023-01-01_spinella-2023-leukemia-dele1-haploinsuff
id_basis: filename-year
source: Spinella(2023) Leukemia; DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5 del(5q) AML.pdf
sha256: 3e5bf50497e19a0711eeaea279d3ddb1b9bc9c71d3861b1d126b35ed42c09ced
size_bytes: 1630900
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 54463

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-023-02107-4"
year: 2023
title: "DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5/del(5q) AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Spinella(2024) Leukemia; DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5 del(5q) AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using the Leucegene dataset of 48 -5/del(5q) AML specimens against 367 controls, DELE1 - located in the common deleted region - was identified as the most consistently downregulated gene. DELE1 encodes the mitochondrial protein that relays mitochondrial stress to the cytosol through the OMA1-DELE1-HRI pathway, activating ATF4 and the integrated stress response. The partial loss of DELE1 expression seen in patients was sufficient to significantly reduce sensitivity to mitochondrial stress in AML cells, suggesting DELE1 haploinsufficiency as a new driver mechanism.

## Summary

A candidate driver for a deletion that has resisted explanation. Several haploinsufficient genes in the 5q region have been proposed - EGR1, APC, CTNNA1, CDC25C, CSNK1A1 - without settling the matter, and DELE1 arrives with a specific mechanism: losing one copy blunts the relay from damaged mitochondria to the apoptotic response, so the cell tolerates mitochondrial stress it should not survive.

The experimental design is the right one for a haploinsufficiency claim. Rather than knocking the gene out, the authors reduce expression to the partial level actually seen in patients and show that is sufficient - which is what distinguishes a dosage effect from a loss-of-function one. They also report two negative results plainly: despite the strong enrichment of TP53 loss in these cases, they found no cooperative interaction between DELE1 haploinsufficiency and TP53 alteration, and no effect on venetoclax response in either Leucegene or Beat AML data.

## Key points

- DELE1, in the 5q common deleted region, is the most consistently downregulated gene in -5/del(5q) AML across 48 cases versus 367 controls.
- DELE1 relays mitochondrial stress to ATF4 via the OMA1-DELE1-HRI pathway and the integrated stress response.
- Partial loss matching the level seen in patients is sufficient to reduce sensitivity to mitochondrial stress-induced apoptosis.
- No cooperative effect was found between DELE1 haploinsufficiency and TP53 alteration, despite their strong co-occurrence.
- No effect on venetoclax response was detected in Leucegene or Beat AML data, despite a plausible ATF4-NOXA-MCL1 rationale.

## Limitations

The common deleted region contains many open reading frames and the authors acknowledge that a phenotype depending on several contributing genes cannot be ruled out - so DELE1 is a candidate among several rather than the established driver. The functional work is knockdown in AML cell lines with a stress-response readout, not an in vivo leukemogenesis model, so 'driver' is inferred from a resistance phenotype rather than demonstrated by transformation. The two negative results limit the translational reach: without a TP53 interaction or a venetoclax link, the finding does not yet connect to a treatment decision. Human evidence is expression association across a single cohort.

## Provenance

Located in the published literature, dropped into `inbox/` as `Spinella(2024) Leukemia; DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5 del(5q) AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-023-02107-4`; the prose sections were written here from the paper itself.

## Citation

Spinella et al. Leukemia 2023. DELE1 haploinsufficiency causes resistance to mitochondrial stress-induced apoptosis in monosomy 5/del(5q) AML. doi: 10.1038/s41375-023-02107-4

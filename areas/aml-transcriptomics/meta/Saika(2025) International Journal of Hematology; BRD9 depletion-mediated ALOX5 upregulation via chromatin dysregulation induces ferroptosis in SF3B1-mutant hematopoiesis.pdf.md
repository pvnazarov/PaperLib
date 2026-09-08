---
# --- identity ------------------------------------------------
id: 2025-01-01_saika-2025-international-journal-of-hema
id_basis: filename-year
source: Saika(2025) International Journal of Hematology; BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis.pdf
sha256: be04e3a5992e9d61c8abb8daecfb43f59db6c06744d10f66d665bc3f3b659def
size_bytes: 6798537
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 62379

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1007/s12185-025-04105-x"
year: 2025
title: "BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Saika(2026) Int J Hematol; BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Building on the finding that SF3B1 mutations cause nonsense-mediated decay of BRD9, a core non-canonical BAF component, the authors show that BRD9 depletion markedly upregulates ALOX5, which oxidises polyunsaturated fatty acids. BRD9 and ALOX5 expression are negatively correlated and SF3B1 mutation associates with ALOX5 upregulation in AML datasets, preferentially in mature myeloid lineages rather than stem/progenitor fractions. Integrated RNA-seq, ChIP-seq and Hi-C show BRD9 loss enhances CTCF occupancy at the ALOX5 locus boundary, enabling aberrant chromatin loop formation that activates transcription, increasing lipid peroxidation and ferroptosis susceptibility as shown by BODIPY-C11 oxidation and erastin sensitivity.

## Summary

A complete causal chain across three levels - spliceosome to chromatin to metabolism - which is unusual to assemble in one study. SF3B1 mutation mis-splices BRD9 into nonsense-mediated decay; losing BRD9 lets CTCF occupy the ALOX5 boundary more heavily; the resulting loop drives ALOX5; ALOX5 peroxidises polyunsaturated lipids; the cells become ferroptosis-prone.

The clinical reasoning that follows is the interesting part. Ineffective hematopoiesis in MDS has always been attributed to apoptosis, yet classical apoptotic features are frequently absent - and this offers ferroptosis as the missing explanation for progenitor loss. It also assembles an account of ring sideroblast-positive MDS specifically: mitochondrial iron accumulation supplies redox-active Fe2+, the SF3B1-BRD9 axis supplies ALOX5, and the two together supply lipid peroxide. The preferential ALOX5 upregulation in mature myeloid cells is offered as a possible explanation for the systemic inflammation and atherosclerotic complications seen in these patients.

## Key points

- A continuous pathway from RNA splicing through chromatin architecture to metabolism and a non-apoptotic cell death.
- SF3B1 mutation degrades BRD9 by nonsense-mediated decay; BRD9 loss increases CTCF occupancy at the ALOX5 boundary and drives its transcription.
- ALOX5 upregulation raises lipid peroxidation and ferroptosis susceptibility, shown by BODIPY-C11 oxidation and erastin sensitivity.
- Offers ferroptosis as an explanation for ineffective hematopoiesis in MDS, where classical apoptotic features are often absent.
- Proposes a coherent account of ring sideroblast MDS combining mitochondrial iron with ALOX5-driven lipid peroxide.

## Limitations

Built on murine BRD9-depleted models plus association analysis in human AML datasets, so the chain is demonstrated in mouse and inferred in patients; primary SF3B1-mutant MDS material contributes expression data rather than functional evidence. BRD9 missplicing is one of several nonsense-mediated-decay-causing defects SF3B1 mutations produce, which the authors acknowledge, so ALOX5 upregulation may not be the dominant consequence. The link to ineffective hematopoiesis, to systemic inflammation and to ring sideroblast biology is interpretive rather than tested. Erastin sensitivity and BODIPY-C11 oxidation are standard but indirect ferroptosis readouts. Whether the ferroptosis susceptibility could be exploited therapeutically, or is instead part of the disease's pathology, is left open.

## Provenance

Located in the published literature, dropped into `inbox/` as `Saika(2026) Int J Hematol; BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1007/s12185-025-04105-x`; the prose sections were written here from the paper itself.

## Citation

Saika et al. International Journal of Hematology 2025. BRD9 depletion-mediated ALOX5 upregulation via chromatin dysregulation induces ferroptosis in SF3B1-mutant hematopoiesis. doi: 10.1007/s12185-025-04105-x

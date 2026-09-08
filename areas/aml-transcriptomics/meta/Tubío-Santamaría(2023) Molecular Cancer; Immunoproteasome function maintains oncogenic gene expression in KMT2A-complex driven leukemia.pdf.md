---
# --- identity ------------------------------------------------
id: 2023-01-01_tub-o-santamar-a-2023-molecular-cancer-i
id_basis: filename-year
source: Tubío-Santamaría(2023) Molecular Cancer; Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia.pdf
sha256: e29757b335b43344d4bac7549f618643bf9b46fbd8bd774e1980c02bf1df2a48
size_bytes: 8876839
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 116034

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s12943-023-01907-7"
year: 2023
title: "Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tubío-Santamaría(2023) Mol Cancer; Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A proteomic approach identified the catalytic immunoproteasome subunit PSMB8 as a specific vulnerability in KMT2A-rearranged AML. Genetic and pharmacologic inactivation impairs proliferation of murine and human leukemic cells while normal hematopoietic cells are unaffected. Disrupting immunoproteasome function increases the transcription factor BASP1, which represses KMT2A-fusion target genes. Pharmacologic PSMB8 targeting improves menin inhibitor efficacy, synergistically reduces leukemia in human xenografts, and retains activity against menin inhibitor resistance mutations. The dependency extends across KMT2A-complex-dependent leukemias including NPM1c.

## Summary

An indirect route to transcriptional control: disrupting proteostasis raises the abundance of a single transcription factor, BASP1, which then represses the fusion protein's target genes. That a selective change in protein degradation produces a specific transcriptional outcome, rather than general proteotoxic stress, is the paper's conceptual claim.

The clinically important result is retained activity against MEN1 resistance mutations - the M327I and T349M variants that emerge under menin inhibitor treatment. Since resistance to menin inhibitors is the central problem in that drug class, a partner that works regardless of the resistance mutation is more valuable than one that merely adds efficacy. Sparing normal hematopoietic cells is plausible here because the immunoproteasome, unlike the constitutive proteasome, is not universally required.

## Key points

- PSMB8, the catalytic immunoproteasome subunit, is a selective vulnerability across KMT2A-complex-dependent leukemias including NPM1c.
- Normal hematopoietic cells are unaffected, since the immunoproteasome is not universally required as the constitutive proteasome is.
- The mechanism is indirect: disrupting immunoproteasome function raises BASP1, which represses KMT2A-fusion target genes.
- Combining PSMB8 and menin inhibition synergistically reduces leukemia in human xenografts.
- Activity is preserved against MEN1 resistance mutations M327I and T349M, addressing the main failure mode of menin inhibitors.

## Limitations

PR-957, the PSMB8 inhibitor used, is a preclinical tool compound; immunoproteasome inhibitors have been developed clinically for autoimmune disease rather than cancer, and their behaviour in combination with a menin inhibitor in patients is untested. The immunoproteasome has an established role in antigen presentation, so inhibiting it in a disease where graft-versus-leukemia and immune surveillance matter carries an immunological cost the paper does not weigh. The BASP1 mechanism is a single transcription factor proposed to carry the effect of a broad change in protein turnover, which is a strong claim from correlated changes plus overexpression experiments. Xenografts in immunodeficient mice cannot detect the immune consequences. Selectivity for leukemic over normal cells is shown in culture and in models rather than in a tolerability study.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tubío-Santamaría(2023) Mol Cancer; Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s12943-023-01907-7`; the prose sections were written here from the paper itself.

## Citation

Tubío-Santamaría et al. Molecular Cancer 2023. Immunoproteasome function maintains oncogenic gene expression in KMT2A-complex driven leukemia. doi: 10.1186/s12943-023-01907-7

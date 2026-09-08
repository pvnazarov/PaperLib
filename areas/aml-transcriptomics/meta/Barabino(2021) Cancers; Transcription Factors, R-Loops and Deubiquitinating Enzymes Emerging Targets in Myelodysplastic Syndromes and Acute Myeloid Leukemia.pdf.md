---
# --- identity ------------------------------------------------
id: 2021-01-01_barabino-2021-cancers-transcription-fact
id_basis: filename-year
source: Barabino(2021) Cancers; Transcription Factors, R-Loops and Deubiquitinating Enzymes Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia.pdf
sha256: 864033961b6bf68028602cf8b2b429df624f60db3903d5e0022b53e554542a1b
size_bytes: 3769376
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 253221

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3390/cancers13153753"
year: 2021
title: "Transcription Factors, R-Loops and Deubiquitinating Enzymes: Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Barabino(2021) Cancers (Basel); Transcription Factors, R-Loops and Deubiquitinating Enzymes Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of three classes of emerging therapeutic target in myelodysplastic syndromes and AML: transcription factors governing myeloid differentiation, RNA splicing factors whose mutations increase R-loop formation, and deubiquitinating enzymes contributing to genome stability in hematopoietic stem cells. It frames myeloid neoplasms as a failure of the equilibrium between HSC self-renewal and differentiated output, traces driver mutations back to HSC/progenitor cells, and describes the clonal mosaic that results as subclones accumulate further mutations.

## Summary

Useful mainly as a map of three target classes that are usually reviewed separately, and for taking the druggability question seriously rather than assuming it. Its most substantive thread is the argument that transcription factors are no longer categorically undruggable: small molecules that inhibit or activate them, masking of DNA-binding consensus sequences, disruption of protein-protein interactions, and targeted degradation are each surveyed with their specificity problems named.

The R-loop section carries the sharpest mechanistic idea in the review. Splicing-factor mutations raise R-loop formation, and elevated R-loops sensitise cells to ATR inhibition - a synthetic-lethal route that does not require inhibiting the spliceosome core, which the authors flag as a toxicity concern precisely because those drugs hit an essential apparatus.

## Key points

- Three target classes reviewed together: myeloid transcription factors, splicing factors and R-loops, and deubiquitinating enzymes.
- The 'undruggable transcription factor' position is treated as outdated, with degradation and interaction-blocking as the newer routes.
- Splicing-factor mutations increase R-loops, which sensitises cells to ATR inhibition - a synthetic-lethal strategy avoiding core spliceosome inhibition.
- Spliceosome inhibitors target essential machinery, so toxicity is presented as the open question rather than efficacy.
- DUB inhibitor development is constrained by conserved catalytic pockets; USP7 inhibitors are given as the counterexample.

## Limitations

A narrative review, not a systematic one: no stated search strategy, inclusion criteria or assessment of the quality of the evidence cited, so the coverage reflects the authors' selection. It surveys preclinical and early-stage work, and the therapeutic claims are largely rationales rather than results - most of the agents discussed had no clinical efficacy data in MDS or AML at the time. Published 2021, so it predates several developments this collection covers, including the clinical menin-inhibitor data. The three target classes are grouped by the authors' interest rather than by a shared mechanism, so the review is three reviews adjacent to each other more than one argument.

## Provenance

Located in the published literature, dropped into `inbox/` as `Barabino(2021) Cancers (Basel); Transcription Factors, R-Loops and Deubiquitinating Enzymes Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3390/cancers13153753`; the prose sections were written here from the paper itself.

## Citation

Barabino et al. Cancers 2021. Transcription Factors, R-Loops and Deubiquitinating Enzymes: Emerging Targets in Myelodysplastic Syndromes and Acute Myeloid Leukemia. doi: 10.3390/cancers13153753

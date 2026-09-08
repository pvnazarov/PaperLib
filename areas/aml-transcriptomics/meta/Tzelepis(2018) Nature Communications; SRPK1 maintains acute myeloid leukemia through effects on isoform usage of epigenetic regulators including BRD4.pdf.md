---
# --- identity ------------------------------------------------
id: 2018-01-01_tzelepis-2018-nature-communications-srpk
id_basis: filename-year
source: Tzelepis(2018) Nature Communications; SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4.pdf
sha256: 6aaeed39827d9846692b3f5ae1913abe60415748243a135e12df839c037c8771
size_bytes: 2113422
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 245296

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-018-07620-0"
year: 2018
title: "SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tzelepis(2018) Nat Commun; SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Following identification of the splicing kinase SRPK1 as a genetic vulnerability of AML, genetic or pharmacological inhibition is shown to cause cell cycle arrest, differentiation and prolonged survival of mice transplanted with MLL-rearranged AML. RNA-seq shows altered isoform levels of many genes with roles in leukemogenesis including MYB, BRD4 and MED24. SRPK1 inhibition produces a switch from the short to the long BRD4 isoform at mRNA and protein level, associated with BRD4 eviction from loci including BCL2 and MYC, and this switch mediates at least part of the anti-leukemic effect. The inhibitor SPHINX31 was synergistic with the BET inhibitor i-BET-151 without noticeable toxicity in mice.

## Summary

Reaches a well-established target, BRD4, by an unusual route - not inhibiting it but changing which isoform is made. The two main BRD4 isoforms have distinct molecular properties, and shifting from short to long evicts BRD4 from BCL2 and MYC.

The authors offer an interesting explanation for specificity: because SRPK1 inhibition switches isoforms rather than removing BRD4 entirely, it may be selective for MLL-rearranged AML in a way that direct BRD4 inhibitors, with their broader activity, are not. That is a plausible general principle - modulating a protein's form may be more selective than eliminating it - though they say the mechanism behind the specificity needs establishing. The rescue by ectopic BRD4-short expression is the control that makes the isoform switch causal rather than incidental.

## Key points

- SRPK1 inhibition works by changing BRD4 isoform usage rather than by inhibiting BRD4 directly.
- The short-to-long BRD4 switch evicts BRD4 from leukemogenic loci including BCL2 and MYC.
- Ectopic BRD4-short expression blocks the anti-leukemic effect, establishing the switch as causal.
- Isoform modulation may be more selective than direct inhibition - SPHINX31 is far more potent in MLL-mutant than other AML lines.
- Extends splicing-directed therapy to AMLs that lack spliceosomal mutations, and synergises with BET inhibition in mice.

## Limitations

The authors state that the mechanism behind the selectivity for MLL-rearranged AML needs to be fully established. SPHINX31 is a tool compound, and although whole-kinome profiling supported its selectivity, SRPK1 acts with CLK1 on shared SR protein substrates, so the pathway is not cleanly isolated. Many isoforms change beyond BRD4 - MYB and MED24 among them - and the BRD4 switch mediates 'at least part' of the effect, so the contribution of the rest is unquantified. In vivo evidence is prolonged survival in transplanted mice rather than cure, and the combination toxicity assessment is short-term. Effects are largely in MLL-rearranged models.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tzelepis(2018) Nat Commun; SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-018-07620-0`; the prose sections were written here from the paper itself.

## Citation

Tzelepis et al. Nature Communications 2018. SRPK1 maintains acute myeloid leukemia through effects on isoform usage of epigenetic regulators including BRD4. doi: 10.1038/s41467-018-07620-0

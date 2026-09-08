---
# --- identity ------------------------------------------------
id: 2026-01-01_guo-2026-nature-cancer-papola-mediated-h
id_basis: filename-year
source: Guo(2026) Nature Cancer; PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming.pdf
sha256: 5f59f9aaf60e842cb4e37d06f09cab290186297ececd0c009688c174024d2253
size_bytes: 11828892
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 699133

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s43018-026-01190-7"
year: 2026
title: "PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Guo(2026) Nat Cancer; PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Widespread poly(A) tail elongation and upregulation of poly(A) polymerase alpha (PAPOLA) are identified in AML, with high PAPOLA expression associated with poor outcomes; PAPOLA upregulation is most pronounced in AML among tumour types while its expression in normal blood cells is the lowest among normal controls. Using primary AML samples, cell lines and multiple mouse models, PAPOLA-driven hyperactive polyadenylation is shown to promote leukemogenesis and sustain leukemia stem cell maintenance, acting through upregulation of glutathione S-transferase mu 2 (GSTM2), which activates a 4-hydroxynonenal (HNE)-dihydrolipoamide dehydrogenase (DLD) axis. Pharmacological inhibition of PAPOLA with cordycepin suppresses metabolic reprogramming and impairs leukemogenesis.

## Summary

Poly(A) tail length is a layer of post-transcriptional control that has been mostly invisible in cancer biology because it is hard to measure at scale; the finding is that it is globally elongated in AML through one enzyme, and that this matters functionally rather than being a by-product.

The expression asymmetry is the most therapeutically encouraging observation - PAPOLA is highest in AML among tumour types and lowest in normal blood among normal tissues - which is about as favourable a starting point for a therapeutic window as an essential RNA-processing enzyme can offer. The mechanism connects RNA processing to metabolism through a specific chain, PAPOLA-GSTM2-HNE-DLD, rather than stopping at a global claim about translation.

## Key points

- Poly(A) tail length is globally elongated in AML through upregulation of the polymerase PAPOLA, whose expression predicts poor outcome.
- PAPOLA is most upregulated in AML among tumour types and least expressed in normal blood among normal tissues.
- It sustains leukemia stem cell maintenance and promotes leukemogenesis across primary samples, cell lines and multiple mouse models.
- Mechanism runs through GSTM2 upregulation and an HNE-DLD axis, linking RNA processing to metabolic reprogramming.
- Cordycepin inhibits PAPOLA, suppresses the metabolic reprogramming and impairs leukemogenesis.

## Limitations

Cordycepin is an old, broadly acting adenosine analogue that inhibits polyadenylation among many other effects and is rapidly deaminated in vivo; attributing its antileukemic activity specifically to PAPOLA is not straightforward, and 'limited side effects' in mouse experiments is a weak basis for the selectivity claim. Poly(A) tail length measurement is technically demanding and method-dependent, and 'widespread elongation' rests on those measurements. The GSTM2-HNE-DLD chain is a specific mechanism proposed downstream of a global change in mRNA processing, which raises the question of why this one axis dominates among all the transcripts whose tails lengthen - a question the summary evidence does not settle. Polyadenylation is essential in all cells, so the therapeutic window depends entirely on the expression differential holding at the level of dependency, not just abundance.

## Provenance

Located in the published literature, dropped into `inbox/` as `Guo(2026) Nat Cancer; PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s43018-026-01190-7`; the prose sections were written here from the paper itself.

## Citation

Guo et al. Nature Cancer 2026. PAPOLA-mediated hyperactive polyadenylation promotes leukemogenesis and leukemia stem cell self-renewal through metabolic reprogramming. doi: 10.1038/s43018-026-01190-7

---
# --- identity ------------------------------------------------
id: 2022-01-01_weng-2022-cancer-cell-the-m6a-reader-igf
id_basis: filename-year
source: Weng(2022) Cancer Cell; The m6A reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia.pdf
sha256: bfe8eb732bff87af2251c76728f0f5e9675ddff6169edd0bdb1d037ac941a99a
size_bytes: 7696047
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 146627

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2022.10.004"
year: 2022
title: "The m6A reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Weng(2022) Cancer Cell; The mA reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

IGF2BP2, an m6A binding protein that enhances mRNA stability and translation, is shown to be highly expressed in AML and associated with unfavourable prognosis. It promotes AML development and self-renewal of leukemia stem and initiating cells by regulating MYC, GPT2 and SLC1A5 in the glutamine metabolism pathway in an m6A-dependent manner, fuelling the TCA cycle and maintaining mitochondrial activity. A small-molecule compound, CWI1-2, that directly binds IGF2BP2 and suppresses its m6A reader activity showed anti-leukemia effects in vitro and in vivo with minimal side effects.

## Summary

Completes the m6A machinery in AML - writers, erasers and now readers - and connects it to metabolism, extending beyond the glycolysis link the same group had previously established. The chain is coherent: IGF2BP2 stabilises transcripts encoding a glutamine transporter and transaminase along with MYC, so glutamine feeds the TCA cycle and sustains the oxidative metabolism that leukemia stem cells depend on.

The distinguishing feature relative to most m6A papers here is the compound. CWI1-2 binds IGF2BP2 directly and inhibits its reader function, which makes this a target with chemistry rather than only genetics, and the comparison against normal CD34+ cord blood cells is the selectivity evidence the therapeutic claim requires.

## Key points

- IGF2BP2, an m6A reader, is highly expressed in AML and associated with unfavourable prognosis.
- It sustains leukemia stem and initiating cell self-renewal by stabilising MYC, GPT2 and SLC1A5 in an m6A-dependent way.
- The mechanism links RNA modification to glutamine metabolism, fuelling the TCA cycle and mitochondrial activity.
- CWI1-2 binds IGF2BP2 directly and suppresses reader activity, with anti-leukemia efficacy in vitro and in vivo.
- Effects spare normal CD34+ cord blood cells, indicating a therapeutic window.

## Limitations

CWI1-2 is a lead compound and the authors state that optimisation and combination testing are warranted - it is not a clinical candidate, and 'minimal side effects' rests on short mouse experiments. IGF2BP2 has functions beyond m6A reading and is expressed in normal tissues, so selectivity depends on the expression differential holding at the level of dependency. Three targets are followed through, but IGF2BP2 binds many transcripts, so their sufficiency to explain the phenotype is not established. Prognostic association comes from public cohorts with a cutoff optimised for survival prediction, which inflates apparent significance. Most functional work is in cell lines and xenografts.

## Provenance

Located in the published literature, dropped into `inbox/` as `Weng(2022) Cancer Cell; The mA reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2022.10.004`; the prose sections were written here from the paper itself.

## Citation

Weng et al. Cancer Cell 2022. The m6A reader IGF2BP2 regulates glutamine metabolism and represents a therapeutic target in acute myeloid leukemia. doi: 10.1016/j.ccell.2022.10.004

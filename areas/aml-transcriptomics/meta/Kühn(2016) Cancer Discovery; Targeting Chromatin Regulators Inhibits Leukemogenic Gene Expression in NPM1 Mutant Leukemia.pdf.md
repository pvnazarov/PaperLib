---
# --- identity ------------------------------------------------
id: 2016-01-01_k-hn-2016-cancer-discovery-targeting-chr
id_basis: filename-year
source: Kühn(2016) Cancer Discovery; Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia.pdf
sha256: 5d74ac06c24dc0fd98d4c7bc85c6f073c00a859f8a1960124b5af7cd3d5c9d24
size_bytes: 33186067
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 182934

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-16-0237"
year: 2016
title: "Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kühn(2016) Cancer Discov; Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The histone modifiers MLL1 and DOT1L are shown to control HOX and FLT3 expression and differentiation in NPM1-mutant AML. A CRISPR/Cas9 genome editing domain screen shows NPM1-mutant AML to be exceptionally dependent on the menin binding site in MLL1, and pharmacologic inhibition of the menin-MLL1 interaction had profound antileukemic activity in human and murine models. Combined inhibition of menin-MLL1 and DOT1L dramatically suppressed HOX and FLT3 expression, induced differentiation, and was superior to either alone.

## Summary

The paper that extended menin inhibition from KMT2A-rearranged leukemia - where the rationale is obvious, since the fusion protein binds menin - to NPM1-mutant AML, which has no MLL rearrangement at all. That extension roughly triples the addressable population, since NPM1 mutation accounts for about 30% of adult AML, and it is the basis for the clinical trials reported elsewhere in this collection.

The domain-level CRISPR screen is the right instrument for the claim: rather than showing MLL1 is required, it localises the requirement to the menin binding site specifically, which is the site a small molecule can occupy. The rescue experiment - exogenous HOX overexpression restoring proliferation under both inhibitors - is the control that makes HOX suppression the mechanism rather than a correlate.

## Key points

- Extends menin-MLL1 inhibition to NPM1-mutant AML, about 30% of adult cases, which carries no MLL rearrangement.
- A CRISPR domain screen localises the dependency specifically to the menin binding site in MLL1 - the druggable interface.
- MLL1 and DOT1L jointly control HOX, MEIS1 and FLT3 expression and the differentiation block.
- Exogenous HOX overexpression rescues the antiproliferative effect of both inhibitors, establishing HOX suppression as the mechanism.
- Combined menin-MLL1 and DOT1L inhibition is synergistic, with deeper HOX/MEIS1 suppression and stronger differentiation.

## Limitations

Preclinical, with much of the mechanistic work in OCI-AML3, the standard NPM1-mutant line, plus murine models. The authors note that future studies must determine how the activity is best combined with current chemotherapy regimens and whether context-specific escape mechanisms - frequent in AML - will undermine it; the proposed combination partners are supported only by a proof-of-principle cell-line study and, for dactinomycin, an anecdotal single-patient report. Drug synergy is assessed by Chou-Talalay in viability assays, a method sensitive to assumptions about dose-response. Published 2016, before clinical menin inhibitor data, and the later finding that HOXA9 and HOXB downregulation is modest in NPM1-mutant PDX models complicates the mechanistic picture presented here.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kühn(2016) Cancer Discov; Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in NPM1 Mutant Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-16-0237`; the prose sections were written here from the paper itself.

## Citation

WMKühn et al. Cancer Discovery 2016. Targeting Chromatin Regulators Inhibits Leukemogenic Gene Expression in
                    <i>NPM1</i>
                    Mutant Leukemia. doi: 10.1158/2159-8290.CD-16-0237

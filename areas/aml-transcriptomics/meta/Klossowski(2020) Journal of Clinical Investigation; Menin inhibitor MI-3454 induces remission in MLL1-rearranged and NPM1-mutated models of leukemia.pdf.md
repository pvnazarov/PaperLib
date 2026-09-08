---
# --- identity ------------------------------------------------
id: 2020-01-01_klossowski-2020-journal-of-clinical-inve
id_basis: filename-year
source: Klossowski(2020) Journal of Clinical Investigation; Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia.pdf
sha256: cece842a49ee3b0b1291a24704aa27b40f2bd1072b2947415ff158ce02b6a00b
size_bytes: 12845172
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 97115

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1172/JCI129126"
year: 2020
title: "Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Klossowski(2020) J Clin Invest; Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

MI-3454, a subnanomolar, orally bioavailable second-generation inhibitor of the menin-MLL1 interaction, is reported to profoundly inhibit proliferation and induce differentiation in acute leukemia cells and primary patient samples with MLL1 translocations or NPM1 mutations. As a single agent it induced complete remission or regression in mouse models including patient-derived xenografts, through downregulation of key leukemogenesis genes. MEIS1 is identified as a candidate pharmacodynamic biomarker of response, and the compound was well tolerated without impairing normal hematopoiesis in mice.

## Summary

The preclinical package that carried menin inhibition toward the clinic, and the first demonstration of single-agent activity in patient-derived xenograft models rather than only in cell lines. Complete remission from a single agent in PDX models of a disease with roughly 35% five-year survival is a strong preclinical result, and the tolerability data - no impairment of normal hematopoiesis - address the obvious concern for a drug targeting a chromatin interaction.

The most informative detail is a discrepancy the authors report rather than smooth over. Earlier in vitro work with first-generation inhibitors showed HOXA9 and HOXB downregulation, but MI-3454 in NPM1-mutant PDX models downregulated those genes only modestly while strongly reducing MEIS1 and FLT3. Their conclusion is that HOXA9 and HOXB regulation in this subtype must involve pathways beyond menin-MLL1 - which complicates the field's standard mechanistic account and bears on the later use of HOX expression as a response biomarker.

## Key points

- MI-3454 is a subnanomolar, orally bioavailable second-generation menin-MLL1 inhibitor.
- Single-agent complete remission or regression in mouse models including patient-derived xenografts of MLL1-rearranged and NPM1-mutant leukemia.
- MEIS1 is proposed as a pharmacodynamic biomarker of response, with FLT3 also strongly downregulated.
- HOXA9 and HOXB genes were only modestly downregulated in NPM1-mutant PDX models, implying menin-independent regulation of those loci.
- Well tolerated in mice with no impairment of normal hematopoiesis.

## Limitations

Preclinical, and the compound advanced under different names commercially rather than as MI-3454 itself. Tolerability in mice over the duration of these experiments is a limited guide to human safety, particularly for differentiation syndrome, which emerged as a real toxicity of this drug class in patients. The mechanistic account is internally unsettled: the authors' own finding that HOXA9 and HOXB are largely unaffected in NPM1-mutant models undercuts the standard explanation of how these drugs work in that subtype, and they can only speculate about the alternative. MEIS1 as a pharmacodynamic biomarker is proposed on the basis of these models, not validated clinically. Multiple authors are employees of Wellspring Biosciences and Kura Oncology, and two senior authors declare research support related to menin inhibitors - the paper is a company-linked development package.

## Provenance

Located in the published literature, dropped into `inbox/` as `Klossowski(2020) J Clin Invest; Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1172/JCI129126`; the prose sections were written here from the paper itself.

## Citation

Klossowski et al. Journal of Clinical Investigation 2020. Menin inhibitor MI-3454 induces remission in MLL1-rearranged and NPM1-mutated models of leukemia. doi: 10.1172/JCI129126

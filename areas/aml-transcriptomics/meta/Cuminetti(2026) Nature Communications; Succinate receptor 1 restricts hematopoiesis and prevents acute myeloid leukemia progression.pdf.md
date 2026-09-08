---
# --- identity ------------------------------------------------
id: 2026-01-01_cuminetti-2026-nature-communications-suc
id_basis: filename-year
source: Cuminetti(2026) Nature Communications; Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression.pdf
sha256: 0eb133e487b0112a819c602c6f5d53cc7ad176b2b1de22cef71f8a73939e7939
size_bytes: 3144672
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 273917

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-026-68906-2"
year: 2026
title: "Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Cuminetti(2026) Nat Commun; Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Low SUCNR1 expression is shown to mark reduced overall and progression-free survival in AML. Succinic acid, acting through both Sucnr1-dependent and independent routes, promotes disease in mouse models of pre-leukemic myelopoiesis, AML and AML xenografts expressing low SUCNR1. Global or hematopoietic deletion of Sucnr1 expands hematopoietic stem and progenitor cells, while Sucnr1-tomato+ HSPCs show restricted engraftment. Mechanistically Sucnr1 activation counterbalances intracellular succinate in HSPCs and preserves their transcriptional programs by controlling S100a8/S100a9; blocking S100a9 with tasquinimod rescues Sucnr1 knockout defects, and combined with a Sucnr1 agonist shows therapeutic value in AML mice.

## Summary

Succinate is usually discussed in AML as an intracellular metabolite feeding the TCA cycle and stabilising HIF-1alpha. This adds an opposing, receptor-mediated arm: the same molecule signalling from outside the cell through SUCNR1 restrains hematopoiesis, so the net effect depends on which route dominates - and in AML with low SUCNR1 the intracellular, disease-promoting arm wins.

That framing makes the therapeutic proposal coherent rather than paradoxical. A Sucnr1 agonist restores the missing brake, and combining it with tasquinimod against S100a9 addresses the downstream effector. The single-cell reanalysis connecting low-SUCNR1, high-S100A8/A9 clusters to the post-cytarabine residual disease signature ties this to the chemoresistance literature elsewhere in this collection.

## Key points

- Low SUCNR1 marks worse overall and progression-free survival in AML patients.
- Succinate has opposing effects: intracellular succinate promotes disease, receptor signalling through Sucnr1 restrains hematopoiesis.
- Sucnr1 deletion expands HSPCs; the mechanism runs through control of S100a8/S100a9.
- Tasquinimod (anti-S100a9) rescues Sucnr1-knockout defects and, with a Sucnr1 agonist, has therapeutic effect in AML mice.
- Single-cell reanalysis links low-SUCNR1, high-S100A8/A9 clusters to the post-cytarabine residual disease signature.

## Limitations

Mechanism is established in mouse genetics; the human evidence is expression-survival association plus reanalysis of published single-cell data, which is hypothesis-generating rather than confirmatory. The authors state directly that succinate has Sucnr1-independent effects and that they do not know whether different succinate analogues act through the same mechanisms - so the pharmacology is not cleanly attributable to the receptor. S100A8 and S100A9 are reported in the literature to have opposing effects on AML (S100a8 sustaining the immature phenotype, S100a9 inducing differentiation), which complicates the interpretation of blocking S100a9. Tasquinimod is not S100a9-selective in the strict sense. The regulation of S100a8/S100a9 across HSPC subsets and its contribution to NRAS-G12D-driven disease are explicitly left to future work.

## Provenance

Located in the published literature, dropped into `inbox/` as `Cuminetti(2026) Nat Commun; Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-026-68906-2`; the prose sections were written here from the paper itself.

## Citation

Cuminetti et al. Nature Communications 2026. Succinate receptor 1 restricts hematopoiesis and prevents acute myeloid leukemia progression. doi: 10.1038/s41467-026-68906-2

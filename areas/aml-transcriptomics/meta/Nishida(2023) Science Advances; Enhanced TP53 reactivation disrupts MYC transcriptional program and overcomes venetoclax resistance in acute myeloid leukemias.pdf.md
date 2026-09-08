---
# --- identity ------------------------------------------------
id: 2023-01-01_nishida-2023-science-advances-enhanced-t
id_basis: filename-year
source: Nishida(2023) Science Advances; Enhanced TP53 reactivation disrupts MYC transcriptional program and overcomes venetoclax resistance in acute myeloid leukemias.pdf
sha256: 226d6b28f77bece63968fd7f52e669842c1d312d74c1f24d773d773fc3e3e5b3
size_bytes: 3213674
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 120869

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/sciadv.adh1436"
year: 2023
title: "Enhanced TP53 reactivation disrupts MYC transcriptional program and overcomes venetoclax resistance in acute myeloid leukemias"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Nishida(2023) Sci Adv; Enhancedreactivation disruptstranscriptional program and overcomes venetoclax resistance in acute myeloid leukemias.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Cotargeting MDM2 and the nuclear exporter XPO1 accumulates nuclear p53 and elicits a 25- to 60-fold increase in its transcriptional targets, disrupting the c-MYC-regulated transcriptome and synergistically inducing apoptosis in AML. Venetoclax-resistant AML expresses high c-MYC and is vulnerable to MDM2/XPO1 inhibition in vivo. Cells persisting after that treatment show a quiescence and stress-response phenotype - high p21, low Ki-67, raised ATF4 and LC3B - which venetoclax overcomes, as shown by single-cell mass cytometry. Triple inhibition of MDM2, XPO1 and BCL2 was highly effective against venetoclax-resistant AML in vivo.

## Summary

Attacks the hardest clinical situation in AML - failure after venetoclax plus hypomethylating agent, where median survival is 2.4 months - and does so through a non-genetic mechanism, since TP53 mutations are relatively infrequent in that setting and p53 is instead inactivated by its negative regulators.

The reasoning behind the triplet is sequential rather than additive, which is what makes it interesting. MDM2/XPO1 inhibition drives p53 activity hard enough to collapse the MYC program that venetoclax-resistant cells depend on; the cells that survive do so by entering a p21-high, Ki-67-low quiescent stress state; and venetoclax kills that state. Each agent addresses the escape route opened by the previous one, and the single-cell mass cytometry is what identifies the residual population well enough to target it.

## Key points

- Combined MDM2 and XPO1 inhibition raises nuclear p53 and increases its transcriptional targets 25- to 60-fold, without requiring TP53 mutation.
- p53 activation collapses the c-MYC transcriptional program, on which venetoclax-resistant AML depends.
- Cells surviving MDM2/XPO1 inhibition enter a quiescent stress-response state - high p21, low Ki-67, raised ATF4 and LC3B.
- Venetoclax eliminates that residual quiescent population, so the triplet works sequentially rather than merely additively.
- Triple MDM2/XPO1/BCL2 inhibition was highly effective against venetoclax-resistant AML in vivo.

## Limitations

The entire strategy requires wild-type TP53 - the authors' own prior work showed that TP53 knockdown or mutation completely abrogates apoptosis under XPO1 inhibition - so it excludes the TP53-mutant patients with the worst outcomes, and MDM2 inhibition is itself known to select for TP53-mutant clones. Combining three agents, each with substantial single-agent toxicity (MDM2 inhibitors cause myelosuppression and gastrointestinal effects, selinexor is poorly tolerated, venetoclax causes cytopenias), raises a tolerability question that mouse experiments cannot answer. Preclinical throughout; the idasanutlin-venetoclax doublet that this extends showed promising early results but has not established itself clinically. Resistance is modelled in venetoclax-resistant lines and xenografts rather than in samples from patients who failed venetoclax-azacitidine.

## Provenance

Located in the published literature, dropped into `inbox/` as `Nishida(2023) Sci Adv; Enhancedreactivation disruptstranscriptional program and overcomes venetoclax resistance in acute myeloid leukemias.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/sciadv.adh1436`; the prose sections were written here from the paper itself.

## Citation

Nishida et al. Science Advances 2023. Enhanced
                    <i>TP53</i>
                    reactivation disrupts
                    <i>MYC</i>
                    transcriptional program and overcomes venetoclax resistance in acute myeloid leukemias. doi: 10.1126/sciadv.adh1436

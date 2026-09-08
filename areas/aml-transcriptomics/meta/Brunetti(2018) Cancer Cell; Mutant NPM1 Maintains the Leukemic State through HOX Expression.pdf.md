---
# --- identity ------------------------------------------------
id: 2018-01-01_brunetti-2018-cancer-cell-mutant-npm1-ma
id_basis: filename-year
source: Brunetti(2018) Cancer Cell; Mutant NPM1 Maintains the Leukemic State through HOX Expression.pdf
sha256: 4baef0b4873ac5f514bf82553319767614cc5c87eccee95cc55f0edea335eedd
size_bytes: 4931093
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 151670

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2018.08.005"
year: 2018
title: "Mutant NPM1 Maintains the Leukemic State through HOX Expression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Brunetti(2018) Cancer Cell; Mutant NPM1 Maintains the Leukemic State through HOX Expression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

NPM1 mutations relocalise the protein to the cytoplasm (NPM1c), but whether that is required to maintain leukemia was unknown. Using allele-specific CRISPR editing of the mutant allele and targeted degradation, the authors show that removing NPM1c from the cytoplasm - by nuclear relocalisation or by degradation - causes immediate downregulation of HOX genes followed by differentiation. XPO1 inhibition relocalises NPM1c to the nucleus, drives differentiation of AML cells and prolongs survival of Npm1-mutated leukemic mice, establishing a dependency of NPM1-mutant AML on NPM1c and a rationale for nuclear export inhibitors.

## Summary

This settles a debate about direction of causation. NPM1-mutant AML has high HOXA/HOXB expression, and it was arguable that HOX levels merely reflected an immature differentiation state rather than being driven by the mutant protein. Allele-specific editing answers it: remove NPM1c and HOX collapses first, differentiation follows.

The therapeutic corollary is the reason this paper matters clinically - XPO1 inhibition works not by killing but by putting the mutant protein back in the nucleus, so the drug's mechanism is relocalisation. The authors are notably careful about the clinical evidence: selinexor showed no higher response rate in NPM1-mutant patients in a phase I trial, and rather than ignore that they argue the dosing schedule cannot sustain relocalisation. The paper's own speculation - that the act of nuclear transport rather than cytoplasmic residence is the pathologic event - is offered as a suggestion.

## Key points

- Allele-specific CRISPR targeting of the 4-bp NPM1 mutant insertion allows the mutant to be removed while leaving the wild-type allele.
- Loss of cytoplasmic NPM1c causes immediate HOX downregulation, then differentiation - establishing HOX as dependent on NPM1c, not merely correlated.
- XPO1 inhibition relocalises NPM1c to the nucleus, differentiates AML cells and prolongs survival in Npm1-mutant mice.
- Provides the mechanistic rationale for nuclear export inhibitors in the largest genetic subgroup of cytogenetically normal AML.
- The authors suggest it is nuclear transport itself, rather than cytoplasmic localisation per se, that is pathologic.

## Limitations

XPO1 inhibition is highly pleiotropic - it raises nuclear levels of many tumour suppressors - so the in vivo benefit cannot be attributed to NPM1c relocalisation, and the authors say as much. The clinical evidence points the other way: single-agent selinexor produced no higher response rate in NPM1-mutant patients, explained here by patient numbers and dosing schedule, which is a plausible but untested reconciliation. Selinexor's toxicity requires intermittent dosing, which the authors concede is probably incompatible with the sustained relocalisation their mechanism needs. The cell work leans on OCI-AML3, the standard NPM1-mutant line, and the mouse model is Npm1-mutant rather than a human xenograft. The molecular link between NPM1c and HOX expression is left unresolved.

## Provenance

Located in the published literature, dropped into `inbox/` as `Brunetti(2018) Cancer Cell; Mutant NPM1 Maintains the Leukemic State through HOX Expression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2018.08.005`; the prose sections were written here from the paper itself.

## Citation

Brunetti et al. Cancer Cell 2018. Mutant NPM1 Maintains the Leukemic State through HOX Expression. doi: 10.1016/j.ccell.2018.08.005

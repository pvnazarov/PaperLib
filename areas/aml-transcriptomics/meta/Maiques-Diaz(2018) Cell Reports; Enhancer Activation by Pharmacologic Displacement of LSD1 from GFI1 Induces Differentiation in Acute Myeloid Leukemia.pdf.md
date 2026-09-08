---
# --- identity ------------------------------------------------
id: 2018-01-01_maiques-diaz-2018-cell-reports-enhancer
id_basis: filename-year
source: Maiques-Diaz(2018) Cell Reports; Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia.pdf
sha256: de7af54394ab6d41de65eecb95922782df25f5ff47a657f0e4541adb1d1f65dc
size_bytes: 3915682
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 195101

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2018.03.012"
year: 2018
title: "Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Maiques-Diaz(2018) Cell Rep; Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

LSD1 inhibitors induce differentiation in MLL-translocated AML, and the assumption had been that this works by blocking LSD1's histone demethylase activity. The authors observe rapid, extensive drug-induced transcriptional changes without genome-wide accumulation of the targeted histone modifications. Instead, inhibitors disrupt the GFI1/CoREST complex and release it from enhancers, and this disruption is required for differentiation; loss of enhancer-bound GFI1/LSD1 activates nearby myeloid transcription factor genes. Fusion constructs mimicking constitutively active GFI1 prevent drug-induced differentiation, and mutation of the K661 residue is identified as a resistance mechanism to tranylcypromine-derivative inhibitors.

## Summary

Corrects the mechanism of a drug class already in trials. LSD1 inhibitors were assumed to work as enzyme inhibitors; here the enzymatic block is largely beside the point, and what matters is that the drug displaces LSD1 from SNAG-domain transcription factors, releasing the GFI1/CoREST repressor complex from enhancers and letting the myeloid differentiation genes beneath them switch on. Scaffolding, not catalysis.

The engineered rescue experiments are what make this more than a correlation - GFI1 zinc-finger fusions to LSD1, RCOR1 or HDAC1 reconstitute repression and block drug-induced differentiation, and a catalytically dead K661A mutant still rescues knockdown. That last point doubles as a predicted resistance mechanism: K661 mutation kills catalysis without disturbing the protein's structure, so LSD1 keeps binding SNAG-domain factors and the drug loses its handle. The authors also note the mechanism is not universal - LSD1 is not displaced from chromatin in small-cell lung cancer - implying cell-type-specific action.

## Key points

- LSD1 inhibitors act mainly by disrupting scaffolding, not enzymatic activity: transcription changes without genome-wide histone mark accumulation.
- The drug displaces the GFI1/CoREST complex from enhancers, activating nearby myeloid differentiation genes.
- Engineered GFI1 zinc-finger fusions to LSD1, RCOR1 or HDAC1 restore repression and block drug-induced differentiation.
- A catalytically dead K661A mutant still rescues LSD1 knockdown - and predicts a resistance mechanism to tranylcypromine derivatives.
- The displacement mechanism is cell-type-specific: LSD1 is not displaced from chromatin in small-cell lung cancer cells.

## Limitations

The authors state that whether a similar mechanism underlies LSD1 inhibitor effects in all malignant cells remains unclear, and cite a direct contradiction in small-cell lung cancer where displacement does not occur - so the mechanism established here may not generalise. Their explanation for why some GFI1 fusions mimic constitutive activity better than others is offered as speculation about complex stoichiometry and orientation. Work is in AML cell lines, principally with tool inhibitors from the authors' own drug discovery unit, and the K661 resistance mechanism is predicted from engineered mutants rather than observed in treated patients. Clinical LSD1 inhibitors have since underperformed with dose-limiting toxicity, which a better mechanistic account does not by itself remedy.

## Provenance

Located in the published literature, dropped into `inbox/` as `Maiques-Diaz(2018) Cell Rep; Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2018.03.012`; the prose sections were written here from the paper itself.

## Citation

Maiques-Diaz et al. Cell Reports 2018. Enhancer Activation by Pharmacologic Displacement of LSD1 from GFI1 Induces Differentiation in Acute Myeloid Leukemia. doi: 10.1016/j.celrep.2018.03.012

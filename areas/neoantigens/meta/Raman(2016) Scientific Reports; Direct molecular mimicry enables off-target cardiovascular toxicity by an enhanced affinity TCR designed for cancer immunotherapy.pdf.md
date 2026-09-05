---
# --- identity ------------------------------------------------
id: 2016-01-01_raman-2016-scientific-reports-direct-mol
id_basis: filename-year
source: Raman(2016) Scientific Reports; Direct molecular mimicry enables off-target cardiovascular toxicity by an enhanced affinity TCR designed for cancer immunotherapy.pdf
sha256: e005fa6899dc915ebbd03cecdc01b77daa7a2f5ab4d071e45188f14881d534cb
size_bytes: 2297722
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 65442

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/srep18851"
year: 2016
title: "Direct molecular mimicry enables off-target cardiovascular toxicity by an enhanced affinity TCR designed for cancer immunotherapy"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2016_Raman_Sci_Rep_Direct_molecular_mimicry_enables_off_target_ca_PMID26758806.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Structural investigation of why a MAGE-A3-specific affinity-enhanced TCR cross-recognised an unrelated Titin epitope presented on cardiac tissue, causing fatal cardiac toxicity in a clinical trial. The authors resolve the mechanism as direct molecular mimicry and use it to design mutants with improved antigen discrimination.

## Summary

This is the cautionary case underlying much of the self-discrimination work in this collection. Natural TCRs are weak, so affinity enhancement is used to make them therapeutically potent - but modifying specificity outside the constraints of thymic selection removes the process that would have deleted a cross-reactive receptor.

Having explained the cross-reactivity structurally, the authors rationally redesign the CDR loops to restore discrimination, offering a route to check and repair engineered TCRs before they reach patients.

## Key points

- The first structural account of direct molecular mimicry causing clinically fatal toxicity from an engineered TCR.
- Affinity enhancement outside thymic selection is identified as the specific source of risk.
- Rational mutant design restored discrimination, demonstrating the mechanism is actionable rather than only explanatory.
- Sets the safety requirement that neoantigen and TCR pipelines must screen against the whole self proteome, not just the intended target.

## Limitations

One TCR and one cross-reactive pair, analysed after the fact: it explains a known failure rather than providing a method to predict unknown ones. The redesigned mutants are shown to improve discrimination in vitro, with no clinical evidence that the redesign is safe. Being a retrospective single case, it gives no estimate of how often affinity-enhanced TCRs carry comparable liabilities.

## Provenance

Located in the published literature, dropped into `inbox/` as `2016_Raman_Sci_Rep_Direct_molecular_mimicry_enables_off_target_ca_PMID26758806.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/srep18851`; the prose sections were written here from the paper itself.

## Citation

Raman et al. Scientific Reports 2016. Direct molecular mimicry enables off-target cardiovascular toxicity by an enhanced affinity TCR designed for cancer immunotherapy. doi: 10.1038/srep18851

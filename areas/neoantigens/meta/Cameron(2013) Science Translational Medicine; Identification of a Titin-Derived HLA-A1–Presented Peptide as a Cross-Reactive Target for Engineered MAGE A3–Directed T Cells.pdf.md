---
# --- identity ------------------------------------------------
id: 2013-01-01_cameron-2013-science-translational-medic
id_basis: filename-year
source: Cameron(2013) Science Translational Medicine; Identification of a Titin-Derived HLA-A1–Presented Peptide as a Cross-Reactive Target for Engineered MAGE A3–Directed T Cells.pdf
sha256: 38f1bd9465169c60c00008b91bd22f1a2c7303a9cd943586a288746ab8a1d242
size_bytes: 784812
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 102089

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/scitranslmed.3006034"
year: 2013
title: "Identification of a Titin-Derived HLA-A1–Presented Peptide as a Cross-Reactive Target for Engineered MAGE A3–Directed T Cells"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nihms958713.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

An affinity-enhanced TCR against the HLA-A*01-restricted MAGE-A3 peptide EVDPIGHLY passed extensive preclinical off-target testing, then caused a serious adverse event and fatal cardiac toxicity in patients. The cross-reactive target is identified here as a Titin-derived peptide presented on cardiac tissue.

## Summary

This is the clinical event itself, and the companion to Raman (2016), which later resolved its structural mechanism. The load-bearing sentence is that extensive preclinical investigation revealed no off-target concerns - the safety process was followed and did not catch it.

The authors' own analysis of why is the most useful part: a single TCR may recognise more than a million HLA-presented peptides, so TCR plasticity, which is what makes an effective repertoire possible, is also what makes engineered specificity dangerous.

## Key points

- Fatal cardiac toxicity from an affinity-enhanced MAGE-A3 TCR cross-reacting with a Titin peptide on cardiac tissue.
- Extensive preclinical off-target investigation found nothing - the failure was of the screening strategy, not of its execution.
- Alanine scanning identified the residues critical for TCR engagement, turning an unknown cross-reactivity into a searchable motif.
- Estimates that one TCR can recognise more than 10^6 HLA-presented peptides, bounding how far homology screening alone can go.

## Limitations

The authors state the core difficulty they could not solve: a homology search needs a stringency threshold, and there is no principled way to set it - too high and cross-reactive peptides are missed, too low and the candidate list becomes untestable. The motif-based search is retrospective, built knowing the answer. One TCR and one cross-reaction gives no estimate of how often affinity-enhanced TCRs carry comparable liabilities.

## Provenance

Located in the published literature, dropped into `inbox/` as `nihms958713.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/scitranslmed.3006034`; the prose sections were written here from the paper itself.

## Citation

Cameron et al. Science Translational Medicine 2013. Identification of a Titin-Derived HLA-A1–Presented Peptide as a Cross-Reactive Target for Engineered MAGE A3–Directed T Cells. doi: 10.1126/scitranslmed.3006034

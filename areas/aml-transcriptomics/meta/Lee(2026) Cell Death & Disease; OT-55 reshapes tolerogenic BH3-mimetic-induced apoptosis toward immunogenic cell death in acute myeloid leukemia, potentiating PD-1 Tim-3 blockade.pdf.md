---
# --- identity ------------------------------------------------
id: 2026-01-01_lee-2026-cell-death-disease-ot-55-reshap
id_basis: filename-year
source: Lee(2026) Cell Death & Disease; OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1 Tim-3 blockade.pdf
sha256: 1a9bbb7f6e20c71be34c0d5ebf23e18c773133f4991d2dbfbce8ddd944e5b9b4
size_bytes: 2691130
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 135004

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41419-026-09000-9"
year: 2026
title: "OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1/Tim-3 blockade"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lee(2026) Cell Death Dis; OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1 Tim-3 blockade.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

BH3 mimetics are apoptogenic but rarely cause immunogenic cell death. The hydroxycoumarin OT-55 was combined with the BCL-xL inhibitor A-1331852 in BCL-xL-dependent murine prophylactic and bilateral AML vaccination models. A nine-gene AML immunogenic-cell-death score (ATG5, CALR, CD8A, CD8B, IFNGR1, IL1B, PDIA3, PIK3CA, TLR4) was derived from three patient cohorts; high scores associated with an immune-activated state, more CD8+ T cells, activated dendritic cells and higher Tim-3 expression. OT-55 reduced C1498 viability, induced calreticulin exposure and ATP release, and conferred calreticulin/ATP-dependent but HMGB1-independent vaccine protection; combined with A-1331852 it enhanced DAMP release and CD8+ effector function, and with PD-1/Tim-3 blockade achieved local and distant tumour control.

## Summary

Addresses a specific limitation of BH3 mimetics: they kill efficiently but tolerogenically, so the death produces no immune memory. Adding an immunogenic adjuvant converts the same apoptosis into immune priming, which is a mechanistically coherent way to combine a targeted agent with checkpoint blockade.

The most interesting reasoning is the resolution of an apparent contradiction in their own data. Myelomonocytic AML marrow has markedly fewer T cells than healthy marrow, which would normally predict checkpoint blockade failure. The authors argue that the T cells present sit in a TCF7+ progenitor-to-intermediate exhausted state that retains self-renewal and cytotoxic potential without terminal commitment - precisely the subset that expands under PD-1 blockade - and that M4/M5 blasts, being monocytic, constitutively express MHC class I and II. So the substrate is a small pool of responsive T cells facing antigen-competent targets, which they argue is more favourable than abundant terminally exhausted infiltrate.

## Key points

- OT-55 converts tolerogenic BH3-mimetic apoptosis into immunogenic cell death, supplying the DAMP context that BCL-xL inhibition alone lacks.
- Vaccine protection was calreticulin- and ATP-dependent but HMGB1-independent, tested by CRT neutralisation and apyrase.
- A nine-gene AML immunogenic-cell-death score, derived across three cohorts, associates with immune activation and favourable prognosis.
- Argues that responsiveness depends on T cell functional state, not abundance: TCF7+ progenitor-exhausted cells facing MHC-competent monocytic blasts.
- Combined with PD-1/Tim-3 blockade, the pair achieved local and distant tumour control in a bilateral model with low toxicity.

## Limitations

This record's PDF is an uncorrected 'article in press' proof, with watermarking that disrupts the text. The in vivo work is entirely in the murine C1498 line in syngeneic mice - a single, immunologically atypical model - with no primary human AML or patient-derived system, and prophylactic vaccination models test prevention rather than treatment of established disease. OT-55 is an early-stage hydroxycoumarin with no clinical data and unestablished selectivity. The nine-gene score is derived retrospectively from public cohorts and is prognostic, not predictive of response to this or any therapy; it is not validated in an independent set. BCL-xL inhibition carries the thrombocytopenia problem noted elsewhere in this collection, and 'low toxicity' rests on short-term hematologic and serum parameters in mice.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lee(2026) Cell Death Dis; OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1 Tim-3 blockade.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41419-026-09000-9`; the prose sections were written here from the paper itself.

## Citation

Lee et al. Cell Death &amp; Disease 2026. OT-55 reshapes tolerogenic BH3-mimetic-induced apoptosis toward immunogenic cell death in acute myeloid leukemia, potentiating PD-1/Tim-3 blockade. doi: 10.1038/s41419-026-09000-9

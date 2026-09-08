---
# --- identity ------------------------------------------------
id: 2020-01-01_stoner-2020-blood-cancer-journal-the-run
id_basis: filename-year
source: Stoner(2020) Blood Cancer Journal; The RUNX1-ETO target gene RASSF2 suppresses t(8,21) AML development and regulates Rac GTPase signaling.pdf
sha256: dd2838a2fcef359c915b17b03805221cc29f5497db2bafa0c720a2c3a93395bd
size_bytes: 2390685
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 89733

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41408-020-0282-9"
year: 2020
title: "The RUNX1-ETO target gene RASSF2 suppresses t(8;21) AML development and regulates Rac GTPase signaling"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Stoner(2020) Blood Cancer J; The RUNX1-ETO target gene RASSF2 suppresses t(8 21) AML development and regulates Rac GTPase signaling.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Characterising transcriptional regulation by RUNX1-ETO identified RASSF2 as aberrantly repressed in t(8;21) AML. Re-expressing RASSF2 specifically inhibits t(8;21) AML development across multiple models. Its function depends on interaction with the Hippo kinases MST1 and MST2 but is independent of canonical Hippo signalling. Proximity-based biotin labelling defined the RASSF2-proximal proteome and revealed association with Rac GTPase-related proteins including the exchange factor DOCK2; RASSF2 knockdown impairs Rac GTPase activation, and RASSF2 expression correlates broadly with Rac-mediated signalling in AML patients.

## Summary

Approaches the fusion oncoprotein from the repression side rather than the activation side - asking what RUNX1-ETO switches off that the leukemia needs kept off, which is the less-studied half of its function. Re-expressing the repressed gene inhibits leukemia specifically in t(8;21), so RASSF2 silencing is load-bearing rather than incidental.

The mechanism is unexpected twice over. RASSF2 acts through the Hippo kinases MST1 and MST2 but not through canonical Hippo signalling, and its proximal proteome points to Rac GTPase regulation via DOCK2. The context-dependence is the interesting part: Rac GTPases are required for growth in MLL-rearranged leukemia, yet appear tumour-suppressive here, and the authors offer a plausible reconciliation - RUNX1-ETO independently induces reactive oxygen species and senescence-like arrest, so additional ROS from Rac/NADPH oxidase activity may be intolerable specifically in this subtype.

## Key points

- RASSF2 is transcriptionally repressed by RUNX1-ETO, and re-expressing it specifically inhibits t(8;21) AML across models.
- RASSF2 function requires the Hippo kinases MST1 and MST2 but is independent of canonical Hippo signalling.
- Proximity labelling links RASSF2 to Rac GTPase regulation via DOCK2, and its knockdown impairs Rac activation.
- Rac activity appears tumour-suppressive in t(8;21) while being required for growth in MLL-rearranged leukemia - a context-specific reversal.
- The proposed reconciliation is that RUNX1-ETO already induces ROS and senescence-like arrest, so further Rac-driven ROS is detrimental.

## Limitations

The mechanism stops short of the effector: the authors state that future studies should delineate which pathways downstream of Rac activation are critical for suppressing t(8;21) growth, so how RASSF2 suppresses leukemia remains unresolved. Re-expression of a repressed gene is not a therapeutic strategy - there is no way to restore RASSF2 pharmacologically, and the paper proposes exploring synthetic lethal interactions in Rac-deficient cells instead. Work is in cell line and mouse models with patient data contributing expression correlation only. The context-dependence of Rac function is inferred from comparing across studies rather than tested directly. Proximity labelling identifies neighbourhood, not interaction, so the DOCK2 association needs orthogonal confirmation.

## Provenance

Located in the published literature, dropped into `inbox/` as `Stoner(2020) Blood Cancer J; The RUNX1-ETO target gene RASSF2 suppresses t(8 21) AML development and regulates Rac GTPase signaling.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41408-020-0282-9`; the prose sections were written here from the paper itself.

## Citation

Stoner et al. Blood Cancer Journal 2020. The RUNX1-ETO target gene RASSF2 suppresses t(8;21) AML development and regulates Rac GTPase signaling. doi: 10.1038/s41408-020-0282-9

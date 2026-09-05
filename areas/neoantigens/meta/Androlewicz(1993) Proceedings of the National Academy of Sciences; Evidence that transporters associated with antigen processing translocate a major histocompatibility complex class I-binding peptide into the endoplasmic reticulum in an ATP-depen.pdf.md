---
# --- identity ------------------------------------------------
id: 1993-01-01_androlewicz-1993-proceedings-of-the-nati
id_basis: filename-year
source: Androlewicz(1993) Proceedings of the National Academy of Sciences; Evidence that transporters associated with antigen processing translocate a major histocompatibility complex class I-binding peptide into the endoplasmic reticulum in an ATP-depen.pdf
sha256: c699932a4ff6b28e7e1d039d351e4047c3aee39163b6766f29ec2652fe504081
size_bytes: 1328365
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 81434

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1073/pnas.90.19.9130"
year: 1993
title: "Evidence that transporters associated with antigen processing translocate a major histocompatibility complex class I-binding peptide into the endoplasmic reticulum in an ATP-dependent manner."

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as androlewicz-et-al-1993-evidence-that-transporters-associated-with-antigen-processing-translocate-a-major.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Using streptolysin-O-permeabilised cells, the authors show that peptide binding to MHC class I is both TAP-dependent and ATP-dependent, and that short 8-10mer peptides known to bind class I compete efficiently for TAP-dependent translocation while longer peptides and an ER signal-sequence peptide do not.

## Summary

This is the experiment establishing that TAP actively pumps antigenic peptides into the ER, and that its substrate preference is already tuned to the length class I will present.

The control that carries the argument is the mutant cell line lacking a functional transporter: uptake still occurs there, but only through a less efficient, ATP-independent route, which separates the TAP pathway from background permeability rather than assuming it.

## Key points

- Peptide loading of MHC-I in permeabilised cells is both transporter-dependent and ATP-dependent.
- TAP's optimal substrates are 8-10mers - the same length window class I presents, so selection begins before the groove.
- Antigen-processing mutant cells show a residual less-efficient, ATP-independent pathway, distinguishing TAP transport from leakage.
- Foundational evidence for the transport step that ERAP1 and cleavage predictors sit either side of.

## Limitations

A permeabilised-cell system is not an intact cell, and streptolysin-O permeabilisation may itself alter membrane behaviour and cytosolic composition. Translocation is inferred from radiolabelled peptide bound to endogenous class I, so transport and binding are measured together rather than separately. Competition experiments show relative preference among a small set of tested peptides, not a general substrate rule; the quantitative specificity of human TAP was worked out later.

## Provenance

Located in the published literature, dropped into `inbox/` as `androlewicz-et-al-1993-evidence-that-transporters-associated-with-antigen-processing-translocate-a-major.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1073/pnas.90.19.9130`; the prose sections were written here from the paper itself.

## Citation

Androlewicz et al. Proceedings of the National Academy of Sciences 1993. Evidence that transporters associated with antigen processing translocate a major histocompatibility complex class I-binding peptide into the endoplasmic reticulum in an ATP-dependent manner.. doi: 10.1073/pnas.90.19.9130

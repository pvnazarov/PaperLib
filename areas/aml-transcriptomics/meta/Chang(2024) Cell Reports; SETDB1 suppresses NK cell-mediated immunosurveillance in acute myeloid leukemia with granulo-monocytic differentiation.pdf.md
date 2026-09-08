---
# --- identity ------------------------------------------------
id: 2024-01-01_chang-2024-cell-reports-setdb1-suppresse
id_basis: filename-year
source: Chang(2024) Cell Reports; SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation.pdf
sha256: 4552face796e06212e83d2641de762b55c88e817ece8c38f0ac52501e528b7bc
size_bytes: 5918806
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 139952

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2024.114536"
year: 2024
title: "SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Chang(2024) Cell Rep; SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

In vivo and in vitro CRISPR-Cas9 library screens in a mouse monocytic AML model identify SETDB1 and its partners ATF7IP and TRIM33 as tumour promoters in vivo. The growth inhibition from Setdb1 depletion depends mainly on NK cell-mediated cytotoxicity: SETDB1 loss demethylates H3K9 at enhancers, upregulating interferon-stimulated genes and NKG2D ligands, raising immunogenicity to NK cells and intrinsic apoptosis. The effects are absent in non-monocytic leukemia cells, and MNDA (murine Ifi203) expression predicts which AML is sensitive to SETDB1 depletion.

## Summary

The methodological point is the finding. An in vitro screen would have missed SETDB1 entirely, because its role is to suppress immune recognition and there is no immune system in a dish; running the same screen in immunocompetent mice is what surfaced it. That is a general warning about the target lists the field has built from cell-line screens.

Biologically it addresses monocytic AML, the subtype that resists venetoclax, and proposes NK cells rather than T cells as the effector arm - defensible in a tumour with low mutational burden that is poorly visible to T cells. The mechanism is coherent: SETDB1 keeps H3K9me3 over endogenous retroviral enhancers, and removing it lets STAT1 and IRF1 drive interferon-stimulated genes and NKG2D ligands. MNDA as a companion biomarker makes the finding usable rather than merely true.

## Key points

- An in vivo CRISPR screen in immunocompetent mice found a target that in vitro screening structurally cannot see.
- SETDB1, with ATF7IP and TRIM33, suppresses NK-mediated immunosurveillance in monocytic AML.
- Mechanism is loss of H3K9 methylation at enhancers, upregulating interferon-stimulated genes and NKG2D ligands.
- The effect is specific to granulo-monocytic differentiation and absent in non-monocytic leukemia cells.
- MNDA (Ifi203 in mouse) is proposed as a biomarker predicting sensitivity to SETDB1 depletion.

## Limitations

The primary model is a mouse monocytic AML line in syngeneic hosts; human evidence is limited to MNDA expression in cell lines and TCGA subtype comparison, with no demonstration that SETDB1 depletion enhances NK killing of primary human AML in vivo. Genetic depletion is not pharmacological inhibition, and no selective SETDB1 inhibitor is tested, so druggability is unaddressed. SETDB1 loss also downregulates MHC class I, which the authors present as helping NK activity - but in a patient that same change would impair T cell recognition, a trade-off not explored. The transcriptional networks downstream of SETDB1 in monocytic AML are stated to 'remain to be elucidated'. Several authors are employees of Janssen Research and Development, which supported the study.

## Provenance

Located in the published literature, dropped into `inbox/` as `Chang(2024) Cell Rep; SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2024.114536`; the prose sections were written here from the paper itself.

## Citation

Chang et al. Cell Reports 2024. SETDB1 suppresses NK cell-mediated immunosurveillance in acute myeloid leukemia with granulo-monocytic differentiation. doi: 10.1016/j.celrep.2024.114536

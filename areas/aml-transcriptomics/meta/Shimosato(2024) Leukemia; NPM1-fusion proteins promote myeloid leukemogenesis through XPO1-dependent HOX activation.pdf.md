---
# --- identity ------------------------------------------------
id: 2024-01-01_shimosato-2024-leukemia-npm1-fusion-prot
id_basis: filename-year
source: Shimosato(2024) Leukemia; NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation.pdf
sha256: 2db0ca2da2e4246d5484868392fab47b5b73160903d6e5ee62fe571d6d66fd92
size_bytes: 2275790
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 124543

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-024-02438-w"
year: 2024
title: "NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Shimosato(2025) Leukemia; NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Two rare NPM1-fusion proteins found in pediatric AML, NPM1::MLF1 and NPM1::CCDC28A, are tested for oncogenic capacity. NPM1::MLF1 localises to both nucleus and cytoplasm and occasionally induces AML in mouse transplantation; NPM1::CCDC28A is more cytoplasmic, immortalises mouse bone marrow cells in vitro and efficiently induces AML in vivo. Both bind the HOX gene cluster and, like NPM1c, cause aberrant HOX upregulation in cooperation with XPO1. The XPO1 inhibitor selinexor suppressed HOX activation and colony formation driven by both fusions, and NPM1::CCDC28A cells were also sensitive to menin inhibition.

## Summary

Establishes that rare NPM1 rearrangements are genuine oncogenes rather than incidental findings, which matters because they had been reported in pediatric AML without functional testing. The finding that they converge on the same HOX activation as the far more common NPM1c mutation is what makes them therapeutically tractable - they inherit the treatment options developed for the common lesion.

The two fusions are not equivalent, and the difference tracks localisation: NPM1::CCDC28A is more cytoplasmic, transforms efficiently and produces a GMP-like population enriched for leukemia stem cells, while NPM1::MLF1 is partly nuclear, transforms only occasionally and yields diverse cell types including mature myeloid cells. That gradient supports the wider argument in this collection that cytoplasmic relocalisation of NPM1 is the leukemogenic event.

## Key points

- Provides the first functional evidence that NPM1::MLF1 and NPM1::CCDC28A are oncogenic, not incidental.
- Both bind the HOX cluster and drive HOX upregulation in cooperation with XPO1, like the common NPM1c mutation.
- Transforming potency tracks cytoplasmic localisation: NPM1::CCDC28A is more cytoplasmic and far more efficient than NPM1::MLF1.
- NPM1::CCDC28A produces a GMP-like population known to contain leukemia stem cells; NPM1::MLF1 yields more diverse cell types.
- Selinexor suppresses HOX activation and colony formation for both, and NPM1::CCDC28A is also sensitive to menin inhibition.

## Limitations

Retroviral overexpression in mouse bone marrow cells, so the fusions are expressed at non-physiological levels from a heterologous promoter rather than from the endogenous locus - a particular concern when the phenotype depends on relative abundance and localisation. NPM1::MLF1 induced AML only occasionally, which is reported but not explained. Therapeutic evidence is colony formation and HOX expression under selinexor in vitro, with no in vivo treatment experiment. These rearrangements are rare, so no patient cohort supports the clinical relevance beyond their original identification in a trial series. Menin sensitivity is shown for only one of the two fusions.

## Provenance

Located in the published literature, dropped into `inbox/` as `Shimosato(2025) Leukemia; NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-024-02438-w`; the prose sections were written here from the paper itself.

## Citation

Shimosato et al. Leukemia 2024. NPM1-fusion proteins promote myeloid leukemogenesis through XPO1-dependent HOX activation. doi: 10.1038/s41375-024-02438-w

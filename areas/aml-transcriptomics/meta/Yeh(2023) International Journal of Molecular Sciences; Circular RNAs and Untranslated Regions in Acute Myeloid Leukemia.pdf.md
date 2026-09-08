---
# --- identity ------------------------------------------------
id: 2023-01-01_yeh-2023-international-journal-of-molecu
id_basis: filename-year
source: Yeh(2023) International Journal of Molecular Sciences; Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia.pdf
sha256: ee056123750abeb5be1e23321abcd3c79654cecab12bf6390a51f68965930dc4
size_bytes: 1646749
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 100669

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.3390/ijms24043215"
year: 2023
title: "Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yeh(2023) Int J Mol Sci; Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of circular RNAs and non-coding untranslated regions in AML, prompted by the finding that approximately 97.5% of the human genome is transcribed into non-coding RNA. It discusses the cellular mechanisms of circRNAs, summarises studies of their biological roles in AML, reviews the contribution of 3' untranslated regions to disease progression through alternative polyadenylation, 3'UTR splicing and single nucleotide polymorphisms, and considers the potential of both as biomarkers for stratification and treatment response prediction and as targets for RNA-directed therapeutics.

## Summary

Most valuable for its methodological critique rather than its survey. The authors set out a specific technical problem with the circRNA literature: because a circRNA shares its sequence with the parental linear mRNA, RNA interference targeting the back-splice junction will partially complement and knock down the linear transcript too - so loss-of-function results attributed to a circRNA may reflect loss of its parent gene.

They name two solutions - LNA GapmeRs to minimise off-targeting, and CRISPR-Cas13 for circRNA-specific knockdown without disturbing cognate mRNAs - and note that neither has yet been used in AML. That is a direct caution for reading the circRNA papers elsewhere in this collection. They also argue the field has been narrow: circRNAs are almost always studied as miRNA sponges, while work in solid tumours shows roles in nuclear transcription and splicing and in cytoplasmic translational control that AML studies have not examined.

## Key points

- RNA interference against circRNA back-splice junctions partially knocks down the parental linear mRNA, confounding loss-of-function studies.
- LNA GapmeRs and CRISPR-Cas13 offer circRNA-specific knockdown but have not been applied in AML.
- AML circRNA research has focused almost exclusively on miRNA sponging, missing the nuclear and translational roles shown in solid tumours.
- Covers 3'UTR contributions through alternative polyadenylation, 3'UTR splicing and single nucleotide polymorphisms.
- circRNAs are proposed as non-invasive biomarkers for diagnosis, prognosis, relapse and subtype classification.

## Limitations

A narrative review with no systematic search or evidence appraisal, and its subject matter is one where the authors themselves judge the primary literature to be methodologically compromised - so much of what it summarises carries the caveat it raises. The therapeutic section is candid that limited research has explored circRNA as RNA therapeutics in AML, so the treatment framing is prospective. Biomarker claims are drawn from individual studies without meta-analysis or cross-validation. Coverage of 3'UTR biology is thinner than of circRNAs despite the title giving them equal weight.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yeh(2023) Int J Mol Sci; Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.3390/ijms24043215`; the prose sections were written here from the paper itself.

## Citation

Yeh et al. International Journal of Molecular Sciences 2023. Circular RNAs and Untranslated Regions in Acute Myeloid Leukemia. doi: 10.3390/ijms24043215

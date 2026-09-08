---
# --- identity ------------------------------------------------
id: 2021-01-01_swart-2021-experimental-hematology-the-r
id_basis: filename-year
source: Swart(2021) Experimental Hematology; The RUNX1 RUNX1T1 network translating insights into therapeutic options.pdf
sha256: 1aa80c88f0cfaea0a070d8837936525645c2691c87d8c08a6161c320f151e696
size_bytes: 1387537
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 54922

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.exphem.2020.11.005"
year: 2021
title: "The RUNX1/RUNX1T1 network: translating insights into therapeutic options"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Swart(2021) Exp Hematol; The RUNX1 RUNX1T1 network translating insights into therapeutic options.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of the RUNX1/RUNX1T1 regulatory network in the most common fusion gene of AML. It describes how perturbing fusion levels and DNA binding alters chromatin accessibility, transcription factor occupancy and gene expression at many loci; how targeted RNAi screens of that transcriptional program uncovered a crucial role in cell cycle progression through CCND2; and how this dependency creates vulnerability to CDK4 and CDK6 inhibitors. It also covers effects on ribosomal protein and rRNA expression, alternative promoter usage, and miRNA-mediated control of mRNA translation and stability.

## Summary

A well-organised account of how the t(8;21) field arrived at a druggable target, and useful for the conceptual correction it makes along the way. AML mutations are classically divided into class 1 kinase mutations driving proliferation and class 2 transcription factor fusions driving self-renewal and blocking differentiation - and the review argues that transcriptional network studies have blurred that distinction, since class 2 fusions also control growth factor and cell cycle genes including FLT3, CDK6 and CCND2. Given that self-renewal requires cell cycle progression, the separation was always artificial.

The methodological observation from the RNAi screen is worth keeping: the in vivo arm produced many more candidates than in vitro assays, matching a similar result in glioma - which is an argument against relying on culture-based screens for dependency discovery.

## Key points

- The class 1 / class 2 mutation distinction is blurred: transcription factor fusions also drive proliferation through FLT3, CDK6 and CCND2.
- Targeted RNAi screening of the RUNX1/RUNX1T1 program identified CCND2 and hence CDK4/6 inhibitor sensitivity.
- The in vivo screen arm yielded many more candidates than in vitro assays, paralleling a similar finding in glioma.
- RUNX1/RUNX1T1 also affects ribosomal protein and rRNA expression, binding rDNA repeats with the POL I factor UBF1.
- It controls alternative promoter usage (RPS6KA1, PARL) and a distinct miRNA signature including MIR126.

## Limitations

A narrative review by authors reporting largely on their own group's work, without systematic search or evidence appraisal. It states that how the observed changes affect ribosome biogenesis remains unclear, and notes a contradiction it cannot resolve - CBFB/MYH11 knockdown increased polysomes despite impaired rRNA transcription. The 133-gene self-renewal candidate set was deliberately restricted to genes downregulated by knockdown, which excludes derepressed genes that might matter equally. The review acknowledges that assigning regulatory elements to genes is difficult when distances span hundreds of kilobases. Published 2021, and the CDK4/6 inhibitor strategy it advocates remains preclinical in this subtype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Swart(2021) Exp Hematol; The RUNX1 RUNX1T1 network translating insights into therapeutic options.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.exphem.2020.11.005`; the prose sections were written here from the paper itself.

## Citation

Swart et al. Experimental Hematology 2021. The RUNX1/RUNX1T1 network: translating insights into therapeutic options. doi: 10.1016/j.exphem.2020.11.005

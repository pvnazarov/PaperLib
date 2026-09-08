---
# --- identity ------------------------------------------------
id: 2025-01-01_kim-2025-cell-mis-splicing-derived-neoan
id_basis: filename-year
source: Kim(2025) Cell; Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias.pdf
sha256: cd62e8a525411206c141c705d7f13fe9dbebb5f5d642084cd93b5346e6ad76ad
size_bytes: 3934656
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 187324

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2025.03.047"
year: 2025
title: "Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kim(2025) Cell; Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The authors identify neoantigens translated from highly stereotyped splicing alterations caused by neomorphic leukemia-associated splicing factor mutations, and use feature-barcoded peptide-MHC dextramers to isolate neoantigen-reactive T cell receptors from healthy donors, patients with active myeloid malignancy, and patients after curative allogeneic transplant. Neoantigen-reactive CD8+ T cells were present in the blood of patients with active disease but had a phenotype distinct from virus-reactive T cells, with defective NF-kB proinflammatory pathways and impaired cytotoxic function. T cells engineered with TCRs against SRSF2-mutant-induced neoantigens from mis-splicing of CLK3 and RHOT2 specifically recognised and killed SRSF2-mutant leukemia.

## Summary

Solves a structural problem in AML immunotherapy: AML has a low mutational burden and therefore few conventional neoantigens, and neoantigens that do exist are usually private to one patient. The insight here is that splicing factor mutations are neomorphic in a sequence-specific way, so they produce the same mis-splicing events across patients - which makes the resulting neoepitopes public and therefore worth engineering a TCR against. The authors make this contrast explicitly against other recurrent-neoantigen claims, where the molecular reason for sharing between patients is unclear.

The immunological finding is the sobering half. The T cells exist in patients and do not work - they carry defective NF-kB proinflammatory signalling and impaired cytotoxicity, unlike virus-reactive T cells in the same blood. That explains why endogenous immunity fails and argues for engineered rather than elicited responses, which is what the CLK3 and RHOT2 TCR experiments demonstrate.

## Key points

- Splicing factor mutations produce stereotyped mis-splicing, so the resulting neoantigens are shared across patients rather than private.
- The mechanism for recurrence is understood - sequence-specific effects on RNA recognition - unlike other reported recurrent neoantigens.
- Hundreds to thousands of potential neoepitopes per mutation raises the chance of presentation across diverse HLA alleles.
- Endogenous neoantigen-reactive CD8+ T cells exist in patients but have defective NF-kB signalling and impaired cytotoxicity.
- TCR-engineered T cells against SRSF2-induced CLK3 and RHOT2 neoantigens specifically kill SRSF2-mutant leukemia.

## Limitations

Proof-of-concept: the authors state that future studies are needed to test therapeutic efficacy and safety of these TCRs. Killing is demonstrated in vitro, with no in vivo model of engineered T cell therapy reported here. Each TCR is restricted to a particular HLA allele, so any single one serves only part of the patient population - the breadth argument rests on the number of candidate epitopes, not on validated TCRs. Donor-derived RHOT2-reactive T cells were found in one patient. Safety is the unaddressed concern: mis-splicing of CLK3 and RHOT2 occurs because of a splicing factor mutation, but whether the same isoforms arise at low level in normal tissue determines on-target off-tumour toxicity, and that is not established. Patient numbers for the immune phenotyping are limited.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kim(2025) Cell; Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2025.03.047`; the prose sections were written here from the paper itself.

## Citation

JunKim et al. Cell 2025. Mis-splicing-derived neoantigens and cognate TCRs in splicing factor mutant leukemias. doi: 10.1016/j.cell.2025.03.047

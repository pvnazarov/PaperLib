---
# --- identity ------------------------------------------------
id: 2024-01-01_liu-2024-journal-of-clinical-investigati
id_basis: filename-year
source: Liu(2024) Journal of Clinical Investigation; A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies.pdf
sha256: d3d2b34739808f26659a33c2c84f9a068fa114f416e7fe0152eb19eb72cd977e
size_bytes: 3938366
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 91641

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1172/JCI175619"
year: 2024
title: "A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Liu(2024) J Clin Invest; A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The pathogenic SRSF2 P95H mutation is shown to disrupt splicing of mitochondrial mRNAs, impair complex I function and robustly increase mitophagy. The authors identify a mitochondrial surveillance mechanism whereby mitochondrial dysfunction modifies splicing of the mitophagy activator PINK1 to remove a poison intron, increasing PINK1 mRNA stability and protein abundance; SRSF2 P95H-induced dysfunction raises PINK1 through this route, which is essential for mutant cell survival. Inhibiting splicing with a GSK-3 inhibitor promotes poison intron retention, impairing mitophagy and activating apoptosis in SRSF2 P95H cells.

## Summary

Connects two strands of this collection that are usually separate - splicing factor mutations and mitochondrial dependency - through a specific, satisfying circuit. The mutation mis-splices mitochondrial transcripts, damaging complex I; the damaged mitochondria must be cleared; clearance requires PINK1; and PINK1's own splicing is regulated by mitochondrial stress through a poison intron. So the cell survives its own splicing defect by using splicing to upregulate the repair pathway.

That makes the dependency exploitable in an unusual way. Rather than targeting the mutation, the therapeutic move is to push splicing further in the direction that retains the poison intron, cutting off PINK1 and leaving the cell with damaged mitochondria it cannot clear. The GSK-3 inhibitor is the tool used, and increased mitophagy doubles as a disease marker specific to SRSF2-mutant cases.

## Key points

- SRSF2 P95H mis-splices mitochondrial mRNAs, impairs complex I and markedly increases mitophagy - specifically compared with other AML and MDS.
- A mitochondrial surveillance mechanism: mitochondrial stress alters PINK1 splicing to remove a poison intron, raising PINK1 stability and protein.
- Elevated PINK1 through this route is essential for survival of SRSF2 P95H cells.
- A GSK-3 inhibitor promotes poison intron retention, blocking mitophagy and activating apoptosis in mutant cells.
- Increased mitophagy is proposed as both a disease marker and a therapeutic vulnerability in SRSF2-mutant MDS and AML.

## Limitations

GSK-3 inhibitors are pleiotropic - GSK-3 has many substrates and, as another paper in this collection shows, is being pursued for entirely different reasons in AML - so attributing the apoptotic effect specifically to PINK1 poison intron retention requires more than the correlation shown. Most mechanistic work is in K562 cells engineered to carry SRSF2 P95H, an isogenic system that is clean but is a chronic myeloid leukemia line rather than an AML or MDS model. Only the P95H hotspot is studied. The therapeutic strategy depends on a window between the mitophagy the mutant cell needs and the mitophagy normal cells need, which is not quantified. Efficacy is in vitro; no animal treatment experiment is reported in the summary evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Liu(2024) J Clin Invest; A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1172/JCI175619`; the prose sections were written here from the paper itself.

## Citation

Liu et al. Journal of Clinical Investigation 2024. A mitochondrial surveillance mechanism activated by SRSF2 mutations in hematologic malignancies. doi: 10.1172/JCI175619

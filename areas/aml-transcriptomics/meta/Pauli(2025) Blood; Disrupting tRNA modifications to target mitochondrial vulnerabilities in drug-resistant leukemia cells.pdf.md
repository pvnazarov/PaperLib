---
# --- identity ------------------------------------------------
id: 2025-01-01_pauli-2025-blood-disrupting-trna-modific
id_basis: filename-year
source: Pauli(2025) Blood; Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells.pdf
sha256: 17b54280ba9d8f3bc904151821703c807c1665193d317d1200cb40f9bc0cbae9
size_bytes: 4007526
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 180941

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2024027822"
year: 2025
title: "Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Pauli(2025) Blood; Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

CRISPR-based synthetic lethality screens exploring RNA modifications in resistance to antileukemic drugs identify TRMT5-mediated formation of N1-methylguanosine at position 37 of the tRNA anticodon loop as essential for tolerance to cytarabine and venetoclax in AML. TRMT5 methylates nearly all mitochondrial and nuclear tRNAs with a guanosine at position 37, but its role in drug tolerance depends specifically on its mitochondrial function: it is required for the dynamic upregulation of mitochondrial mRNA translation and oxidative phosphorylation that sustains tolerance. Lower expression of electron transport chain components correlates with therapy outcomes in patients, and TRMT5 inhibition prevents the OXPHOS upregulation and synergises with cytarabine and venetoclax.

## Summary

Supplies a mechanism for the OXPHOS switch that recurs throughout this collection. Several papers establish that drug-tolerant AML cells raise oxidative phosphorylation; this identifies what makes that possible - mitochondrial protein synthesis depends on a specific tRNA modification, and without TRMT5 the cells cannot mount the increase.

The experimental discrimination is the strong part. TRMT5 modifies both nuclear and mitochondrial tRNAs, so attributing the phenotype to mitochondria requires separating the two, and the rescue constructs do exactly that: wild-type TRMT5 restores respiration under cytarabine, an enzymatically dead mutant does not, and a mitochondria-targeting-sequence-deleted version does not either. That is a clean demonstration that both catalysis and mitochondrial localisation are required.

## Key points

- TRMT5-mediated m1G37 tRNA modification is required for cytarabine and venetoclax tolerance in AML.
- Explains how drug-tolerant cells achieve the OXPHOS upregulation reported across this collection - via mitochondrial mRNA translation.
- Rescue with enzymatically dead and mitochondria-targeting-deficient TRMT5 constructs shows both catalysis and mitochondrial localisation are needed.
- Electron transport chain component expression correlates with therapy outcome in patients.
- TRMT5 inhibition blocks the OXPHOS increase and synergises with both cytarabine and venetoclax.

## Limitations

No TRMT5 inhibitor exists; 'TRMT5 inhibition' here is genetic knockout, so the therapeutic proposal is unvalidated pharmacologically and the druggability of a tRNA methyltransferase is unaddressed. TRMT5 also modifies nuclear tRNAs and is required for normal mitochondrial function - germline TRMT5 mutations cause mitochondrial disease in humans - so the therapeutic window is a serious question the study does not answer. Work is in AML cell lines (OCI-AML2, OCI-AML3, MOLM13, Kasumi-1) with the patient link provided by expression-outcome correlation rather than by testing primary samples. Synergy is demonstrated in vitro; the summary evidence does not include an in vivo combination experiment.

## Provenance

Located in the published literature, dropped into `inbox/` as `Pauli(2025) Blood; Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2024027822`; the prose sections were written here from the paper itself.

## Citation

Pauli et al. Blood 2025. Disrupting tRNA modifications to target mitochondrial vulnerabilities in drug-resistant leukemia cells. doi: 10.1182/blood.2024027822

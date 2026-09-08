---
# --- identity ------------------------------------------------
id: 2024-01-01_fischer-2024-cell-reports-stag2-mutation
id_basis: filename-year
source: Fischer(2024) Cell Reports; STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia.pdf
sha256: c83632f8685c61d1f94b571201bd0d42b4e83296f41a6ab8b8046240b492c558
size_bytes: 16079499
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 232250

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2024.114498"
year: 2024
title: "STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Fischer(2024) Cell Rep; STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A characterisation of genetic, transcriptional and chromatin conformational changes in a sizable cohort of primary AML samples, addressing why STAG2 but not its paralog STAG1 is frequently mutated in myeloid malignancy. Specific loci show altered cohesin occupancy, gene expression and local chromatin activation that the remaining STAG1-cohesin does not compensate, linked to disrupted spatial chromatin looping. Depleting STAG2 or STAG1 in primary human CD34+ HSPCs reproduces STAG2-mutant AML-specific changes only for STAG2, and STAG2-deficient HSPCs show impaired differentiation and maintain HSPC-like gene expression.

## Summary

The paralog question is what this answers. Cohesin can carry either STAG1 or STAG2, yet only STAG2 is recurrently mutated, and the two possible explanations - that STAG2 is simply X-linked and therefore easier to inactivate with one hit, or that the paralogs do genuinely different jobs - are separable by depleting each in the same cells. Depleting STAG1 does not reproduce the AML phenotype, and no STAG1 mutations appear in over 300 patients, so the answer is functional difference, not just genetic accessibility.

Working in primary AML samples and primary CD34+ HSPCs rather than cell lines or mice is the methodological advance over the prior literature, and it yields a clinically useful by-product: STAG2 and RAD21 mutations occur at similar frequency, are mutually exclusive, and carry almost inverted co-mutation patterns, implying independent routes to leukemia through the same complex.

## Key points

- STAG2 loss, not STAG1 loss, reproduces AML-specific chromatin and expression changes in primary human HSPCs.
- The remaining STAG1-cohesin does not compensate at affected loci, and no STAG1 mutations were found in over 300 AML patients.
- STAG2 deficiency impairs differentiation and maintains an immature HSPC-like expression program.
- STAG2 and RAD21 mutations are mutually exclusive with almost inverted co-mutation patterns, implying independent leukemogenic mechanisms.
- STAG2-mutant cases form an epigenomically and transcriptionally coherent subgroup regardless of co-mutations.

## Limitations

Chromatin conformation assays on primary AML samples are technically demanding and were feasible only on a subset, so the looping conclusions rest on fewer samples than the cohort headline suggests. Knockdown in CD34+ HSPCs is not equivalent to the frameshift mutations seen in patients, and cultured HSPCs differentiate under artificial conditions. The candidate target genes are identified by association between altered looping and altered expression; none is functionally tested for a role in leukemogenesis. Primary AML samples vary in blast purity and cellular composition, which affects both conformation and expression measurements. Co-mutation associations come from cohort statistics and, for the newly reported IDH1 and CEBPA links, need independent confirmation.

## Provenance

Located in the published literature, dropped into `inbox/` as `Fischer(2024) Cell Rep; STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2024.114498`; the prose sections were written here from the paper itself.

## Citation

Fischer et al. Cell Reports 2024. STAG2 mutations reshape the cohesin-structured spatial chromatin architecture to drive gene regulation in acute myeloid leukemia. doi: 10.1016/j.celrep.2024.114498

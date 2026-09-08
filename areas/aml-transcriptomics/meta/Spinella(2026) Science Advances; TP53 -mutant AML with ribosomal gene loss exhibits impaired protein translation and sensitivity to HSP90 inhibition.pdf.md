---
# --- identity ------------------------------------------------
id: 2026-01-01_spinella-2026-science-advances-tp53-muta
id_basis: filename-year
source: Spinella(2026) Science Advances; TP53 -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition.pdf
sha256: 2711a799c50adc971b70ce82058b5bc872c5ea0601324db7e7390fda71279184
size_bytes: 11010213
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 106326

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/sciadv.aed7122"
year: 2026
title: "TP53 -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Spinella(2026) Sci Adv; -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using the Leucegene dataset of 691 AML specimens from 656 patients, the authors identify a subset of TP53-altered AML marked by recurrent deletions on chromosome 3p, present in over 20% of TP53-mutated cases. These frequently co-occur with del(5q) and encompass ribosomal protein genes, causing network-wide downregulation of the ribosome and reduced protein synthesis - a ribosomopathy-like phenotype most pronounced when RPG deletions occur on both 3p and 5q, suggesting cooperation. Chemical screening identified HSP90 inhibition as a selective vulnerability in AML with low ribosomal protein gene expression.

## Summary

Identifies a coherent subgroup inside TP53-mutant AML defined by a shared functional consequence rather than by a single lesion. Deletions on 3p and 5q each remove ribosomal protein genes, and when both occur the ribosomal network is downregulated enough to impair protein synthesis - which is why the authors describe it as ribosomopathy-like and draw the comparison to Diamond-Blackfan anemia, including the enrichment for M6 erythroid morphology.

The p53 connection is mechanistically necessary rather than incidental: ribosomal defects normally trigger a p53-dependent nucleolar stress response and growth arrest, so cells can only tolerate this state with p53 lost. That explains the co-occurrence. HSP90 inhibition emerging from a chemical screen fits a cell already struggling with protein homeostasis.

## Key points

- del(3p) occurs in over 20% of TP53-mutated AML and frequently co-occurs with del(5q).
- Both deletions remove ribosomal protein genes, and combined loss produces network-wide ribosomal downregulation and reduced protein synthesis.
- The ribosomopathy-like phenotype requires p53 loss, which allows escape from the nucleolar stress response ribosomal defects would otherwise trigger.
- The subgroup is enriched for M6 erythroid morphology, paralleling Diamond-Blackfan anemia biology.
- Chemical screening identified HSP90 inhibition as a selective vulnerability in low-RPG-expression AML.

## Limitations

Retrospective analysis of a single institutional dataset, with the therapeutic finding coming from ex vivo chemical screening rather than in vivo testing - no animal treatment experiment is described in the summary evidence. HSP90 inhibitors have an extensive history of clinical failure across cancers, largely on toxicity and modest efficacy, which the paper does not address. The proposed cooperative mechanism between 3p and 5q deletions is inferred from the phenotype being most pronounced when both are present, not from isolating each. The paradoxical shift from hypoproliferative to proliferative state that the authors invoke to reconcile reduced translation with leukemic growth is cited from other work rather than demonstrated here. No functional experiment tests whether restoring ribosomal protein expression reverses the phenotype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Spinella(2026) Sci Adv; -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/sciadv.aed7122`; the prose sections were written here from the paper itself.

## Citation

Spinella et al. Science Advances 2026. <i>TP53</i>
                    -mutant AML with ribosomal gene loss exhibits impaired protein translation and sensitivity to HSP90 inhibition. doi: 10.1126/sciadv.aed7122

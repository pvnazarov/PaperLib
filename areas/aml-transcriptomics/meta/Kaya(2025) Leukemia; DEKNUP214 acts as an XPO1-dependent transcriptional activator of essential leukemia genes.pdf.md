---
# --- identity ------------------------------------------------
id: 2025-01-01_kaya-2025-leukemia-deknup214-acts-as-an
id_basis: filename-year
source: Kaya(2025) Leukemia; DEKNUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.pdf
sha256: 0335409efe7ef462e61750178721936dba88ceacf16de19891c9dedf87c03374
size_bytes: 2377372
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 34884

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-025-02593-8"
year: 2025
title: "DEK::NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Kaya(2025) Leukemia; DEK NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A multi-omics comparison of 57 cytogenetically poor-risk primary AML samples - whole genome and targeted sequencing, transcriptomics, and drug screening with over 500 compounds - shows that t(6;9)/DEK::NUP214 cases respond selectively to the XPO1 inhibitors selinexor and eltanexor and carry a distinct transcriptomic signature with overexpression of FOXC1 and HOX genes. CUT&RUN demonstrates direct binding of DEK::NUP214 to the promoters of FOXC1 and the HOXA/B clusters, and both the expression of these genes and the fusion's binding at their regulatory regions are selectively reduced by XPO1 inhibition, identifying DEK::NUP214 as an XPO1-dependent transcriptional activator.

## Summary

Arrives at the same conclusion as Charles Cano in this collection - XPO1 dependency in DEK::NUP214 AML - from the opposite direction, starting from an unbiased drug screen across 57 poor-risk samples rather than from a hypothesis about the fusion. Two independent routes to the same target is stronger evidence than either alone, and the two papers together make a reasonable case for a trial in this rare entity.

The transcriptional detail adds something specific. HOXA overexpression is shared with NPM1-mutant and KMT2A-rearranged AML, but HOXB overexpression appears characteristic of t(6;9), and FOXC1 is strikingly overexpressed - a factor that independently confers a monocyte/macrophage differentiation block and poor outcome. Showing the fusion bound at those promoters, and losing that binding under XPO1 inhibition, ties the drug response to a mechanism rather than leaving it as a screen hit.

## Key points

- An unbiased screen of over 500 compounds across 57 poor-risk AML samples finds t(6;9) cases selectively sensitive to selinexor and eltanexor.
- t(6;9) AML shows a distinct signature: HOXA overexpression shared with other subtypes, HOXB overexpression more characteristic, and strong FOXC1 overexpression.
- CUT&RUN places DEK::NUP214 directly on the FOXC1 and HOXA/B promoters.
- XPO1 inhibition selectively reduces both the fusion's binding at these loci and the expression of the genes.
- Independently corroborates the XPO1 dependency reported for this entity, from a drug-screening rather than hypothesis-driven starting point.

## Limitations

Published as a Letter, so the experimental detail is compressed. Only four t(6;9) samples were available within the 57-patient cohort, which is inherent to a 1% entity but means the selective drug response rests on very few patients. Functional work leans on FKH-1, essentially the only available t(6;9) cell line, so cell-line-specific effects cannot be excluded. XPO1 inhibition has broad effects on nuclear export, and the observation that fusion binding at these promoters falls is consistent with the proposed mechanism without excluding indirect routes. FOXC1 knockdown establishes that the gene matters in FKH-1 by apoptosis, cell cycle and colony assays, but no in vivo efficacy experiment is reported here. The authors state that how these events are orchestrated remains unclear.

## Provenance

Located in the published literature, dropped into `inbox/` as `Kaya(2025) Leukemia; DEK NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-025-02593-8`; the prose sections were written here from the paper itself.

## Citation

Kaya et al. Leukemia 2025. DEK::NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes. doi: 10.1038/s41375-025-02593-8

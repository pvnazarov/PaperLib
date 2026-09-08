---
# --- identity ------------------------------------------------
id: 2025-01-01_liu-2025-british-journal-of-haematology
id_basis: filename-year
source: Liu(2025) British Journal of Haematology; Single‐cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8,21) acute myeloid leukaemia.pdf
sha256: 04bbb1f17e1e8209171e20d7eb74eed952bc7182d9e5399ba4c802627fcb5afb
size_bytes: 9720256
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 64935

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1111/bjh.70077"
year: 2025
title: "Single‐cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8;21) acute myeloid leukaemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Liu(2025) Br J Haematol; Single-cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8 21) acute myeloid leukaemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Single-cell RNA sequencing of t(8;21) AML characterises intratumoral heterogeneity and identifies an HSC-like subset as the most quiescent and primitive population, with IKZF2 as its master regulator. IKZF2 is upregulated in t(8;21) relative to other AML subtypes and is specifically targeted by AML1-ETO; primary samples and mouse models confirm its enrichment in primitive quiescent leukemic cells. IKZF2 knockout blocked accumulation of aberrant stem cells driven by AML1-ETO and promoted differentiation in vitro and in vivo. Markers of t(8;21) LSCs including IL5RA, CD69 and CPA3 are also reported.

## Summary

Addresses the specific clinical problem in t(8;21) AML - most patients enter remission and about 40% still relapse - by identifying the population most likely to be responsible and the factor that maintains it. IKZF2 sits downstream of AML1-ETO, which links the initiating lesion to the persistent cell.

The most interesting therapeutic observation is a possible dual effect the authors raise: IKZF2 (Helios) is important in regulatory T cells, so targeting it might simultaneously eradicate leukemic stem cells and reduce immune evasion. That same expression in T cells is also why they cannot relate IKZF2 levels to patient outcome using bulk transcriptomics - a limitation they state rather than work around, which is the honest handling of a confounded measurement.

## Key points

- An HSC-like subset is the most quiescent and primitive population in t(8;21) AML, and IKZF2 is its master regulator.
- IKZF2 is upregulated in t(8;21) relative to other AML subtypes and is a direct target of AML1-ETO.
- IKZF2 knockout blocks accumulation of AML1-ETO-driven aberrant stem cells and promotes differentiation in vitro and in vivo.
- New candidate t(8;21) LSC markers - IL5RA, CD69, CPA3 - are mostly specific to this subtype.
- Because IKZF2 also functions in regulatory T cells, targeting it might combine LSC eradication with reduced immune evasion.

## Limitations

The authors state their principal limitation directly: they could not establish a t(8;21) patient-derived xenograft capable of serial re-engraftment, so the in vivo disease-reinitiating potential of the HSC-like subset - the property that would make it the relapse-driving population - is not verified. They also cannot relate IKZF2 expression to patient outcome, because T cell IKZF2 confounds bulk transcriptomic measurement. In vivo work therefore rests on mouse AML1-ETO models rather than human disease. IKZF2's role in regulatory T cells cuts both ways: systemic inhibition would perturb immune tolerance, which the authors frame as an opportunity but which is equally a toxicity risk. The LSC markers are identified by expression, without functional validation that they enrich for leukemia-initiating capacity.

## Provenance

Located in the published literature, dropped into `inbox/` as `Liu(2025) Br J Haematol; Single-cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target IKZF2 in t(8 21) acute myeloid leukaemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1111/bjh.70077`; the prose sections were written here from the paper itself.

## Citation

Liu et al. British Journal of Haematology 2025. Single‐cell transcriptome profiling reveals blast cell heterogeneity and identifies novel therapeutic target <scp>IKZF2</scp> in t(8;21) acute myeloid leukaemia. doi: 10.1111/bjh.70077

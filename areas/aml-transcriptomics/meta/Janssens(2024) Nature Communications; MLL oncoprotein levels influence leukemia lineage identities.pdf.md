---
# --- identity ------------------------------------------------
id: 2024-01-01_janssens-2024-nature-communications-mll
id_basis: filename-year
source: Janssens(2024) Nature Communications; MLL oncoprotein levels influence leukemia lineage identities.pdf
sha256: d584fb62731916f7e1b7b24eaed8a4d50c823d4690cc0bb17f7615e4689636ad
size_bytes: 2128165
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 169401

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-024-53399-8"
year: 2024
title: "MLL oncoprotein levels influence leukemia lineage identities"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Janssens(2024) Nat Commun; MLL oncoprotein levels influence leukemia lineage identities.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Automated CUT&RUN profiling of oncoprotein target sites across 36 representative MLL-rearranged leukemia samples, including three that underwent lymphoid-to-myeloid lineage switching under therapy, shows that genomic enrichment of the oncoprotein is highly variable between samples and dynamically regulated. At high expression the oncoproteins preferentially activate either a pro-B-cell ALL program or a hematopoietic-stem-cell AML program, with fusion-partner-specific binding patterns correlating with each mutation's prevalence in ALL versus AML. In lineage-switching samples oncoprotein levels fall and binding shifts to granulocyte-monocyte progenitor genes; in one sample that switched during revumenib treatment, oncoprotein and menin became undetectable while the cofactor ENL persisted at many target loci including GMP-program genes.

## Summary

Lineage switching under therapy is one of the more alarming clinical phenomena in MLL-rearranged leukemia - a B-ALL returning as AML, which escapes lineage-directed treatment - and this measures the oncoprotein directly across patient samples before and after it happens.

The central claim is quantitative rather than qualitative: the same fusion protein specifies different lineages at different expression levels, high levels driving B-ALL or AML programs and reduced levels shifting binding to a GMP-like program. That makes lineage a dose-dependent property of the oncoprotein rather than a fixed consequence of the translocation. The revumenib observation is the therapeutically pointed one - with the oncoprotein and menin gone, ENL remains on target loci, suggesting a route by which the transcriptional program survives its supposed driver, and a candidate mechanism of menin inhibitor resistance.

## Key points

- 36 patient samples profiled by CUT&RUN, including three with therapy-induced lineage switching, spanning ages and fusion partners.
- Oncoprotein levels vary widely and are dynamically regulated; high levels drive either a pro-B-cell ALL or an HSC-like AML program.
- Fusion-partner-specific binding patterns correlate with how often each fusion is seen in ALL versus AML.
- Lineage switching is accompanied by reduced oncoprotein levels and redirected binding to a GMP-like program.
- After lineage switch on revumenib, oncoprotein and menin were undetectable but ENL persisted at target loci - a candidate resistance mechanism.

## Limitations

Chromatin occupancy profiling of patient samples is descriptive: nothing here manipulates oncoprotein levels to show that lowering them causes the lineage shift, so the direction of causation between reduced expression and switched lineage is inferred. The lineage-switching evidence rests on three samples, and the revumenib case on one. The authors set out the central unresolved alternative themselves - whether switching is trans-differentiation of B-ALL cells or selective outgrowth of a pre-existing multipotent clone - and conclude selective outgrowth is more likely, which would substantially change the interpretation of the binding data. CUT&RUN signal depends on cell number and quality, both variable in banked patient samples, and the samples span heterogeneous treatments and eras.

## Provenance

Located in the published literature, dropped into `inbox/` as `Janssens(2024) Nat Commun; MLL oncoprotein levels influence leukemia lineage identities.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-024-53399-8`; the prose sections were written here from the paper itself.

## Citation

Janssens et al. Nature Communications 2024. MLL oncoprotein levels influence leukemia lineage identities. doi: 10.1038/s41467-024-53399-8

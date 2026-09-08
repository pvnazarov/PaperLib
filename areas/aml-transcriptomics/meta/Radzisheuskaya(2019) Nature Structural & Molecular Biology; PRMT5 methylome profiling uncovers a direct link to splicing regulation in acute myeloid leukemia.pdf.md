---
# --- identity ------------------------------------------------
id: 2019-01-01_radzisheuskaya-2019-nature-structural-mo
id_basis: filename-year
source: Radzisheuskaya(2019) Nature Structural & Molecular Biology; PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia.pdf
sha256: dd244fb121dd359b0345b04f81b101f028817abcc10f645256b9276bf0134c7c
size_bytes: 5937561
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 146894

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41594-019-0313-z"
year: 2019
title: "PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Radzisheuskaya(2019) Nat Struct Mol Biol; PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using an enzymatically dead PRMT5 and a PRMT5-specific inhibitor, the authors show that PRMT5's catalytic activity is required for AML cell survival. Multiplexed quantitative proteomics identified PRMT5 substrates, and among those essential for AML proliferation, the splicing regulator SRSF1 was confirmed as a direct target whose function depends on PRMT5 methylation of three arginines. Loss of PRMT5 changes alternative splicing of multiple essential genes and alters SRSF1 binding to mRNAs and proteins, which explains the requirement for PRMT5 in leukemia cell survival and provides potential biomarkers of response to PRMT5 inhibitors.

## Summary

Connects a drug target already in clinical trials to a mechanism. PRMT5 inhibitors were being developed largely on the strength of the MTAP synthetic lethality in 9p21-deleted cancers; this asks what PRMT5 actually does in AML, and finds that its essential function runs through SRSF1 methylation and hence through splicing.

The methodology matters for the conclusion. The authors identify substrates by TMT-based multiplexed proteomics rather than SILAC, and note that a contemporaneous study using SILAC detected SRSF1 methylated peptides but could not confirm SRSF1 as a substrate because they appeared in only one replicate - a concrete illustration of how quantitation method determines which substrates are found. Focusing on substrates that are themselves essential for AML proliferation is the right filter for identifying which of many methylation events carries the phenotype.

## Key points

- PRMT5's catalytic activity, not merely its presence, is required for AML cell survival - shown with an enzymatically dead mutant and an inhibitor.
- SRSF1 is a direct PRMT5 substrate, methylated on three arginines, and its function depends on that methylation.
- PRMT5 loss changes alternative splicing of multiple essential genes and alters SRSF1 binding to mRNA and protein.
- Substrate identification used TMT multiplexed proteomics, which recovered SRSF1 where an earlier SILAC study could not.
- Provides candidate biomarkers of response for PRMT5 inhibitors already in clinical trials.

## Limitations

Work is in human AML cell lines bearing MLL-AF9, so a single genetic context, with supporting evidence from a published mouse model rather than from primary patient material here. The authors raise but do not test the most clinically interesting question their own mechanism suggests - whether AML patients with spliceosome mutations are especially sensitive to PRMT5 inhibition. PRMT5 has many substrates and methylates numerous splicing factors; SRSF1 is shown to be important but is not shown to account for the whole phenotype. Arginine methylation affects binding interactions broadly, so downstream splicing changes may arise through several substrates at once. The proposed biomarkers are candidates from this system, not validated against clinical response.

## Provenance

Located in the published literature, dropped into `inbox/` as `Radzisheuskaya(2019) Nat Struct Mol Biol; PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41594-019-0313-z`; the prose sections were written here from the paper itself.

## Citation

Radzisheuskaya et al. Nature Structural &amp; Molecular Biology 2019. PRMT5 methylome profiling uncovers a direct link to splicing regulation in acute myeloid leukemia. doi: 10.1038/s41594-019-0313-z

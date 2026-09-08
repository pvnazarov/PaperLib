---
# --- identity ------------------------------------------------
id: 2026-01-01_sgueglia-2026-cell-death-disease-dynamic
id_basis: filename-year
source: Sgueglia(2026) Cell Death & Disease; Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia.pdf
sha256: 759076b9fcff989f081bfcf8cd43fa30cbd0e942d449e50e2dc9ffb4106732ab
size_bytes: 1764863
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 53250

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41419-026-08594-4"
year: 2026
title: "Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Sgueglia(2026) Cell Death Dis; Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Two unbalanced isoforms of BCL2-associated transcription factor 1 (BCLAF1) are identified in AML cell lines - a full-length isoform with oncogenic properties and a short isoform that appears tumour-suppressive. Treatment with specific epidrugs re-establishes the physiological balance between them. ChIP analysis after SAHA treatment localised the regulation to exon 5 rather than the promoter, with increased acetylation and H3K4me3 and decreased H3K36me3 at specific regions, and co-immunoprecipitation showed that HDAC1 and DNMT3A interact under basal conditions and that this interaction is disrupted by SAHA, while DNMT3B binding is unchanged.

## Summary

An instance of the two-way traffic between chromatin and splicing that the field has increasingly recognised - histone marks affect RNA polymerase II processivity and splicing factor recruitment, and the marks here change at the exon rather than the promoter, which is where a genuine co-transcriptional splicing effect should appear.

The specificity of the finding is what supports it. Changes were confined to exon 5 regions R4 and R5, MRG15 was absent from the promoter regions as the model predicts, and DNMT3B binding was unaffected while the DNMT3A-HDAC1 interaction was disrupted by SAHA. The therapeutic framing is that an epidrug can restore an isoform balance rather than simply switching genes on or off, which is a more refined objective than most epigenetic therapy proposes.

## Key points

- BCLAF1 produces a full-length oncogenic and a short tumour-suppressive isoform, unbalanced in AML.
- Epidrug treatment restores the physiological isoform balance rather than simply altering gene expression.
- Regulation is localised to exon 5, not the promoter - consistent with co-transcriptional splicing control.
- SAHA increases acetylation and H3K4me3 and decreases H3K36me3 at specific exon 5 regions.
- HDAC1 and DNMT3A interact under basal conditions, and SAHA disrupts that interaction specifically, leaving DNMT3B unaffected.

## Limitations

Work is in AML cell lines, principally U937, with no primary patient samples or in vivo model, so the isoform imbalance is not established in patient disease. SAHA is a pan-HDAC inhibitor with pervasive effects on transcription and chromatin, so attributing the splicing change specifically to disrupting the DNMT3A-HDAC1 interaction requires more than the correlated ChIP changes shown. The functional characterisation of the two isoforms as oncogenic and tumour-suppressive is asserted from cell-line phenotypes; neither is tested in vivo. The proposed mechanism is described as operating 'at least in part' through HDAC1 and DNMT3A, which is an appropriate hedge for evidence of this kind. HDAC inhibitors have not succeeded clinically in AML, so restoring isoform balance with them remains hypothetical.

## Provenance

Located in the published literature, dropped into `inbox/` as `Sgueglia(2026) Cell Death Dis; Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41419-026-08594-4`; the prose sections were written here from the paper itself.

## Citation

Sgueglia et al. Cell Death &amp; Disease 2026. Dynamic epigenetic regulation of BCLAF1 splicing in acute myeloid leukemia. doi: 10.1038/s41419-026-08594-4

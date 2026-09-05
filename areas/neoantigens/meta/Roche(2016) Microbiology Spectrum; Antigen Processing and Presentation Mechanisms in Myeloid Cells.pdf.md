---
# --- identity ------------------------------------------------
id: 2016-01-01_roche-2016-microbiology-spectrum-antigen
id_basis: filename-year
source: Roche(2016) Microbiology Spectrum; Antigen Processing and Presentation Mechanisms in Myeloid Cells.pdf
sha256: 6f7b01e8918eca991561961ed4a9415657bf2691abcdb806c8349bd0abecd5b4
size_bytes: 2381212
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 136099

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1128/microbiolspec.MCHD-0008-2015"
year: 2016
title: "Antigen Processing and Presentation Mechanisms in Myeloid Cells"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as roche-cresswell-2016-antigen-processing-and-presentation-mechanisms-in-myeloid-cells.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A review of antigen processing and presentation in myeloid cells, particularly dendritic cells: antigen acquisition, proteolysis into fragments, peptide binding to MHC, and surface display of both MHC class I-peptide and class II-peptide complexes.

## Summary

This is the mechanistic background the prediction papers in this collection assume and rarely state. The dendritic cell focus matters because DCs are where cross-presentation happens - tumour antigens taken up from outside the cell reaching the MHC class I pathway - which is the route by which a vaccine or a dying tumour cell primes CD8 responses.

Covering class I and class II together is also useful, since the collection's computational work treats them as separate prediction problems while in a dendritic cell they are competing branches of one process.

## Key points

- Covers acquisition, proteolysis, MHC loading and surface display as one connected pathway.
- Myeloid and dendritic cell focus, which is where cross-presentation - the basis of vaccine priming - occurs.
- Treats class I and class II presentation together rather than as separate problems.
- Supplies the cell-biological context for the processing predictors elsewhere in this collection.

## Limitations

A review: every quantitative claim belongs to a cited study and must be traced there. It describes mechanisms without quantifying their relative contribution, so it cannot say how much of a tumour immunopeptidome arises by cross-presentation versus direct presentation. Published 2016, and the noncanonical antigen sources documented elsewhere in this collection have expanded the picture since.

## Provenance

Located in the published literature, dropped into `inbox/` as `roche-cresswell-2016-antigen-processing-and-presentation-mechanisms-in-myeloid-cells.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1128/microbiolspec.MCHD-0008-2015`; the prose sections were written here from the paper itself.

## Citation

Roche et al. Microbiology Spectrum 2016. Antigen Processing and Presentation Mechanisms in Myeloid Cells. doi: 10.1128/microbiolspec.MCHD-0008-2015

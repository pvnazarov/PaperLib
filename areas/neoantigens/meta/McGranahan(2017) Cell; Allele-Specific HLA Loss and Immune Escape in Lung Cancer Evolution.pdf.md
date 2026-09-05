---
# --- identity ------------------------------------------------
id: 2017-01-01_mcgranahan-2017-cell-allele-specific-hla
id_basis: filename-year
source: McGranahan(2017) Cell; Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution.pdf
sha256: 6369e896f1479cda4239017d754fa5491ce55457bb44a36b80d40b16c63608a9
size_bytes: 10941482
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 195981

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2017.10.001"
year: 2017
title: "Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2017_McGranahan_Cell_Allele_Specific_HLA_Loss_and_Immune_Escape_in_PMID29107330.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

LOHHLA, a tool for estimating allele-specific HLA copy number from sequencing data, is applied to 327 tumour and 100 matched normal exomes from 100 TRACERx NSCLC patients. Loss of heterozygosity at the HLA locus occurs in 40% of early-stage non-small-cell lung cancers, is associated with elevated subclonal neoantigen burden and immune activity, and is under strong selection.

## Summary

HLA LOH is an immune escape mechanism that is invisible to standard neoantigen pipelines: if a tumour has lost the allele that would present a predicted neoantigen, the prediction is wrong in a way no binding score can detect. Measuring allele-specific HLA copy number is therefore a prerequisite for accurate neoantigen prediction, not an optional refinement.

The evolutionary reading is that the immune system acts as a strong selection pressure during branched tumour development, and HLA loss marks where a tumour has responded to it.

## Key points

- LOH of the HLA locus in 40% of early-stage NSCLC - common enough that ignoring it biases neoantigen prediction systematically.
- HLA LOH is associated with high subclonal neoantigen burden and with immune activity, consistent with escape under pressure.
- No tumour showed homozygous HLA deletion, supporting the idea that one haplotype copy is mandatory to avoid NK-mediated lysis.
- LOHHLA makes allele-specific HLA copy number measurable from routine sequencing.

## Limitations

One tumour type in one cohort: the 40% figure is for early-stage NSCLC in TRACERx and should not be quoted for other cancers. Allele-specific copy number inference from exomes depends on purity and ploidy estimates and on the difficulty of mapping to the highly polymorphic HLA locus. The association between HLA LOH and neoantigen burden is correlative; the timing analysis infers rather than observes the order of events.

## Provenance

Located in the published literature, dropped into `inbox/` as `2017_McGranahan_Cell_Allele_Specific_HLA_Loss_and_Immune_Escape_in_PMID29107330.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2017.10.001`; the prose sections were written here from the paper itself.

## Citation

McGranahan et al. Cell 2017. Allele-Specific HLA Loss and Immune Escape in Lung Cancer Evolution. doi: 10.1016/j.cell.2017.10.001

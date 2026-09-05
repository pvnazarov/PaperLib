---
# --- identity ------------------------------------------------
id: 1999-01-01_mhcsequencingconsortium-1999-nature-comp
id_basis: filename-year
source: MHCsequencingconsortium(1999) Nature; Complete sequence and gene map of a human major histocompatibility complex.pdf
sha256: 69b1bcc0093d81460c193f0fda3f117bbbaacd4df598217ae587fdd8266a231b
size_bytes: 195310
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 61330

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/44853"
year: 1999
title: "Complete sequence and gene map of a human major histocompatibility complex"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 44853.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

The first complete sequence and gene map of a human MHC, the chromosome 6 region essential to the immune system. Of 224 identified gene loci, 128 are predicted to be expressed, and the authors estimate about 40% of expressed genes have immune system function. Over 50% of the MHC was sequenced twice in different haplotypes.

## Summary

This is the reference the whole field stands on. Every HLA typing tool, every allele-specific binding predictor and every analysis of HLA loss in this collection depends on a sequenced, mapped, annotated MHC - and this is where that came from.

Sequencing more than half the region in two haplotypes is what turned MHC polymorphism from a serological observation into sequence, which is the form the prediction tools need.

## Key points

- 224 gene loci identified, 128 predicted expressed, about 40% of expressed genes with immune function - so the MHC is not solely an immune locus.
- Over 50% sequenced in two different haplotypes, giving direct insight into the region's extraordinary polymorphism.
- Several class II and III genes trace by sequence similarity and synteny to over 700 million years ago, predating adaptive immunity by roughly 300 million years.
- The reference underpinning HLA typing, allele-specific prediction and HLA loss detection throughout this collection.

## Limitations

One MHC haplotype sequenced completely, with partial coverage of a second - and the MHC is the most polymorphic region of the human genome, so a single reference haplotype is a poor summary of it. Many of the 224 loci were of unknown function at the time and the 40% immune-function figure is an estimate. Reference bias from a single haplotype is precisely what makes HLA typing and read mapping at this locus hard, as the typing papers in this collection describe.

## Provenance

Located in the published literature, dropped into `inbox/` as `44853.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/44853`; the prose sections were written here from the paper itself.

## Citation

MHCsequencingconsortium et al. Nature 1999. Complete sequence and gene map of a human major histocompatibility complex. doi: 10.1038/44853

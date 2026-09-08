---
# --- identity ------------------------------------------------
id: 2023-01-01_klever-2023-blood-advances-aml-with-comp
id_basis: filename-year
source: Klever(2023) Blood Advances; AML with complex karyotype extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology.pdf
sha256: ffe8a70f2168d0c209ea3d14b9710c5d63fa40287b65d44deab2f115f65bc3d8
size_bytes: 1915330
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 148009

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/bloodadvances.2023010887"
year: 2023
title: "AML with complex karyotype: extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Klever(2023) Blood Adv; AML with complex karyotype extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

An integrative workflow combining Oxford Nanopore genomic long-read sequencing with high-throughput chromosome conformation capture (Hi-C) was applied to a defined cohort of complex-karyotype AML, identifying regions with extreme density of structural variants. These consist largely of focal amplifications enriched near mammalian-wide interspersed repeat elements, often producing oncogenic fusion transcripts such as USP7::MVD or deregulating driver genes, as confirmed by RNA-seq and direct cDNA sequencing. The authors name this pattern chromocataclysm, and show that combining the two technologies resolves complex rearrangements in regions that conventional sequencing handles poorly.

## Summary

Complex-karyotype AML has the worst outcome of any subtype and is only partly explained by TP53 mutation; the rest of the explanation has been inaccessible because short-read sequencing cannot resolve the rearrangements. Combining long reads with Hi-C is the methodologically sound answer, and the authors give the right reason for it - the two technologies do not share failure modes, so their intersection strongly suppresses false positives, while long reads span the repetitive regions where 58% of their breakpoints fall.

The substantive finding challenges a piece of received wisdom. Chromothripsis is generally understood as a single catastrophic event; here cases show extreme breakpoint clustering in some regions and much lower clustering elsewhere, with the events not physically linked - evidence that in individual cases multiple such events occurred independently.

## Key points

- Long-read sequencing plus Hi-C resolves complex-karyotype rearrangements that short-read sequencing cannot, with 58% of breakpoints in repetitive regions.
- The two technologies have different biases, so integrating them strongly reduces false-positive structural variant calls.
- Reveals regions of extreme structural variant density, largely focal amplifications enriched near MIR repeat elements - termed chromocataclysm.
- Rearrangements produce oncogenic fusion transcripts such as USP7::MVD, confirmed by RNA-seq and direct cDNA sequencing.
- Evidence that chromothripsis-like events can occur independently within one case, against the single-catastrophic-event model.

## Limitations

A small cohort - individual cases are discussed by name (CK2-Mut, CK3-Mut, CK4-Mut, CK6-Wt) - so 'chromocataclysm' is a pattern described in a handful of genomes rather than an established entity with defined frequency or prognostic meaning. Naming a new phenomenon on this basis is a strong move, and the authors themselves note their cases also show features of chromoplexy and chromoanasynthesis, so the categories overlap. The claim that chromothripsis events occurred independently is inferred from clustering patterns and lack of physical linkage, not from timing evidence. Functional impact is supported by expression changes and fusion transcript detection, but no fusion is functionally tested. Data are available on request from an author rather than deposited.

## Provenance

Located in the published literature, dropped into `inbox/` as `Klever(2023) Blood Adv; AML with complex karyotype extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/bloodadvances.2023010887`; the prose sections were written here from the paper itself.

## Citation

Klever et al. Blood Advances 2023. AML with complex karyotype: extreme genomic complexity revealed by combined long-read sequencing and Hi-C technology. doi: 10.1182/bloodadvances.2023010887

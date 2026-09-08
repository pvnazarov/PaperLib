---
# --- identity ------------------------------------------------
id: 2024-01-01_heikamp-2024-cell-reports-nup98-fusion-p
id_basis: filename-year
source: Heikamp(2024) Cell Reports; NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML.pdf
sha256: ddff38d94ba9f5d4195ae78198799fab2ee8f3e84c234a951714c47e0100bf92
size_bytes: 6420170
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 342768

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2024.114901"
year: 2024
title: "NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Heikamp(2024) Cell Rep; NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using menin-KMT2A inhibitors and targeted degradation of NUP98 fusion proteins, the authors define the relationship between NUP98 oncofusions and the non-canonical polycomb repressive complex PRC1.1. Evicting the NUP98 fusion-menin-KMT2A complex from chromatin is not sufficient to silence pro-leukemogenic genes: in the absence of PRC1.1 key oncogenes remain transcriptionally active, and transition to a repressed state requires accumulation of PRC1.1 and repressive histone modifications. PRC1.1 loss confers resistance to small-molecule menin-KMT2A inhibitors in vivo, so a critical function of these oncofusions is antagonising repressive chromatin complexes.

## Summary

A clinically pointed mechanistic result: removing the oncoprotein from chromatin is not the same as turning the oncogenes off. Silencing requires something to actively repress the locus afterwards, and PRC1.1 is that something - so a cell lacking PRC1.1 evicts the complex under menin inhibition and keeps expressing the genes anyway.

That directly predicts a resistance mechanism, demonstrated in vivo, and it matters because BCOR and BCORL1, PRC1.1 components, are recurrently mutated in AML. It also reframes what these oncofusions do: not only recruiting activating machinery but blocking repression. The authors are commendably explicit about what they have not shown, including that they do not demonstrate the complexes interacting on chromatin.

## Key points

- Eviction of the NUP98 fusion-menin-KMT2A complex is not sufficient to silence pro-leukemogenic genes.
- Silencing requires PRC1.1 accumulation and repressive histone modifications - active repression, not just loss of activation.
- PRC1.1 loss confers resistance to menin inhibitors in vivo, a mechanism relevant given recurrent BCOR/BCORL1 mutation in AML.
- A core function of these oncofusions is antagonising repressive polycomb complexes, not only recruiting activators.
- Menin inhibition affects Meis1 and other loci more than the Hox cluster, and why is unresolved.

## Limitations

The authors state several limits directly: they do not show the complexes interacting on chromatin, directly or indirectly; they cannot explain why menin-KMT2A inhibition evicts the complex and changes transcription at Meis1 while Hox cluster transcription remains relatively unchanged; and PRC1.1 inactivation alone does not much affect Hox/Meis expression at steady state, so the growth advantage of PRC1.1-deficient cells is not explained by these oncogenes and may work through a Hox/Meis-independent mechanism they have not defined. Most mechanistic work is in murine leukemia cell lines with degron systems, with PDX models used for the resistance experiment. The senior author holds a menin inhibition patent and multiple company relationships including research support from Syndax, the developer of revumenib.

## Provenance

Located in the published literature, dropped into `inbox/` as `Heikamp(2024) Cell Rep; NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2024.114901`; the prose sections were written here from the paper itself.

## Citation

Heikamp et al. Cell Reports 2024. NUP98 fusion proteins and KMT2A-MENIN antagonize PRC1.1 to drive gene expression in AML. doi: 10.1016/j.celrep.2024.114901

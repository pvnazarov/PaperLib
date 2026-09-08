---
# --- identity ------------------------------------------------
id: 2021-01-01_grinev-2021-nature-communications-runx1
id_basis: filename-year
source: Grinev(2021) Nature Communications; RUNX1 RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia.pdf
sha256: 2ce0a4612de15fdce13f5f097920623831cb23209c11102488309073d56f55e1
size_bytes: 4330543
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 95944

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-020-20848-z"
year: 2021
title: "RUNX1/RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Grinev(2021) Nat Commun; RUNX1 RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The fusion oncogene RUNX1/RUNX1T1 is shown to regulate alternative RNA splicing in leukemic cells. Comprehensive analysis of associated splicing events identifies two mechanisms: regulation of alternative transcription start site selection, which produces isoforms with alternative 5'-UTR structures, and direct or indirect control of genes encoding splicing factors, which generates alternative junctions between internal cassette and constitutive exons. The differential splicing affects several functional groups of genes and produces proteins with distinct conserved domain structures, establishing alternative splicing as a component of transcriptome reorganisation by an aberrant transcriptional regulator.

## Summary

The conceptual point is a boundary being crossed. Splicing dysregulation in leukemia is normally studied where splicing factors are mutated, and transcription factor oncogenes are studied for their effects on transcription; this shows a transcription factor fusion reorganising the transcriptome post-transcriptionally as well.

The two mechanisms are usefully distinct. One is not really post-transcriptional at all - by controlling where transcription starts, the fusion changes which 5' exons exist to be spliced, so an isoform change follows from a promoter choice. The other is indirect, through the expression of splicing factors themselves. The methodological warning the authors draw is worth keeping: total RNA-seq measurements in any transcription-factor study are affected by altered splicing and degradation, so transcription-centred analyses of such data are partly measuring something else.

## Key points

- A leukemic transcription factor fusion, not a mutated splicing factor, is shown to reorganise alternative splicing.
- Mechanism one: control of alternative transcription start site selection, yielding isoforms with different 5'-UTRs.
- Mechanism two: control of the expression of splicing factor genes, yielding new internal exon junctions.
- Differential splicing produces proteins with distinct conserved domain structures, illustrated for PARL.
- Implies that transcription-centred RNA-seq analyses of transcription factor oncogenes are confounded by splicing changes.

## Limitations

Based on siRNA knockdown of the fusion in two t(8;21) cell lines, Kasumi-1 and SKNO-1, with no primary patient samples or in vivo work, so the splicing program is established in a narrow system. Knockdown effects at 200 nM siRNA by electroporation are acute and could include stress-related splicing changes. Distinguishing direct from indirect effects is intrinsically hard here, and the second mechanism is by definition indirect. The functional consequence of the isoforms is largely inferential - domain structures are predicted from sequence, and only PARL is examined in any detail, with its isoform's function described as unknown. No isoform is shown to matter for the leukemic phenotype.

## Provenance

Located in the published literature, dropped into `inbox/` as `Grinev(2021) Nat Commun; RUNX1 RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-020-20848-z`; the prose sections were written here from the paper itself.

## Citation

Grinev et al. Nature Communications 2021. RUNX1/RUNX1T1 mediates alternative splicing and reorganises the transcriptional landscape in leukemia. doi: 10.1038/s41467-020-20848-z

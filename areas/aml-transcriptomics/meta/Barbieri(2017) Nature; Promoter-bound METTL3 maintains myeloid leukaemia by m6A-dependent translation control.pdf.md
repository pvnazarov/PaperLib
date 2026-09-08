---
# --- identity ------------------------------------------------
id: 2017-01-01_barbieri-2017-nature-promoter-bound-mett
id_basis: filename-year
source: Barbieri(2017) Nature; Promoter-bound METTL3 maintains myeloid leukaemia by m6A-dependent translation control.pdf
sha256: e9e9ca02b6736779dcdaaee0e735b4e599aa1d2bb3159e3792fedea5d69f87bc
size_bytes: 5021929
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 148590

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature24678"
year: 2017
title: "Promoter-bound METTL3 maintains myeloid leukaemia by m6A-dependent translation control"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Barbieri(2017) Nature; Promoter-bound METTL3 maintains myeloid leukaemia by mA-dependent translation control.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Two independent CRISPR screens - a genome-wide dropout screen in MLL-AF9/FLT3-ITD mouse primary leukemia cells and a custom domain-focused library - identify METTL3 as essential for AML growth. Knockdown causes cell cycle arrest, differentiation and failure to establish leukemia in immunodeficient mice. METTL3 associates with chromatin independently of METTL14 and localises to transcriptional start sites of active genes, the majority of which carry CEBPZ at the TSS, which is required for its recruitment. Promoter-bound METTL3 induces m6A within the coding region of the associated transcript and enhances translation by relieving ribosome stalling.

## Summary

The finding that makes m6A a chromatin story rather than only an RNA one. METTL3 is known as the catalytic half of a nuclear methyltransferase complex; here it is found on promoters without METTL14, recruited by CEBPZ, and marking the coding region of the transcript that promoter produces.

The consequence is translational, not transcriptional, which is the part worth holding onto: the m6A deposited co-transcriptionally relieves ribosome stalling on that mRNA, so a promoter-bound enzyme sets the translation efficiency of its own gene. Genes regulated this way are the ones AML needs, and the domain-focused second screen is a nice methodological touch - targeting catalytic domains separates enzymes whose activity is required from those merely needed as scaffolds.

## Key points

- METTL3 is essential for AML growth in two independent CRISPR screens, including one designed to test catalytic-domain dependence.
- It binds chromatin at active TSSs independently of METTL14, recruited by the CAATT-box binding protein CEBPZ.
- Promoter-bound METTL3 deposits m6A in the coding region of the associated mRNA and enhances its translation by relieving ribosome stalling.
- Knockdown produces cell cycle arrest, differentiation, and failure to establish leukemia in mice.
- Establishes an RNA-modifying enzyme as a chromatin-associated regulator and a therapeutic target in AML.

## Limitations

Effects on leukemia are shown by knockdown and engraftment failure, which cannot separate a requirement for leukemia initiation from a general growth requirement; normal hematopoiesis is not characterised in comparable depth, so the therapeutic window is unaddressed here. Much of the mechanism rests on MOLM13 with inducible shRNA, and m6A RIP-seq is antibody-based with limited resolution, so individual methylation sites are not mapped precisely. The CEBPZ dependency is shown by recruitment loss rather than by a structural interaction. Two senior authors declare founding and employment interests in a company developing RNA-modifying enzyme inhibitors, which is disclosed and relevant to how the 'novel therapeutic target' framing is read.

## Provenance

Located in the published literature, dropped into `inbox/` as `Barbieri(2017) Nature; Promoter-bound METTL3 maintains myeloid leukaemia by mA-dependent translation control.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature24678`; the prose sections were written here from the paper itself.

## Citation

Barbieri et al. Nature 2017. Promoter-bound METTL3 maintains myeloid leukaemia by m6A-dependent translation control. doi: 10.1038/nature24678

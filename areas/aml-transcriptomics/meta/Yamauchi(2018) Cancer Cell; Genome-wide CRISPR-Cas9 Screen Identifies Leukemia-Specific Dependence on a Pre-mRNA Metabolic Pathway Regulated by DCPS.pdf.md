---
# --- identity ------------------------------------------------
id: 2018-01-01_yamauchi-2018-cancer-cell-genome-wide-cr
id_basis: filename-year
source: Yamauchi(2018) Cancer Cell; Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS.pdf
sha256: 579f4be32606a4490ba3046b0cfaaf0e4d43d79091e07e6d3b491b09f1681974
size_bytes: 5510319
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 101096

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2018.01.012"
year: 2018
title: "Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yamauchi(2018) Cancer Cell; Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genome-wide CRISPR-Cas9 screening in AML cell lines, followed by a second screen in vivo, identified the mRNA decapping enzyme scavenger gene DCPS as essential for AML survival. Mass spectrometry showed DCPS interacting with components of pre-mRNA metabolic pathways including spliceosomes. RG3039, a DCPS inhibitor originally developed for spinal muscular atrophy, showed anti-leukemic activity by inducing pre-mRNA mis-splicing. Humans with germline biallelic DCPS loss-of-function mutations have no aberrant hematologic phenotype, indicating DCPS is dispensable for human hematopoiesis.

## Summary

The target selection strategy is the model contribution. Rather than taking screen hits at face value, the authors filtered them against chemical inhibitor databases and human genetic databases - ExAC, gnomAD, OMIM, ClinVar - explicitly inspired by how human loss-of-function variants guided PCSK9 drug development. That yields a target with both an existing inhibitor and direct human evidence of tolerability.

That human evidence is unusually strong. People carrying biallelic DCPS loss-of-function mutations have no hematologic abnormality, so the therapeutic window is established in humans before any trial - a far better basis than mouse tolerability. The screen design is also careful: mouse AML lines with normal karyotype and functionally normal Trp53, chosen to mimic primary human AML where TP53 is infrequently mutated, with an in vivo validation screen controlling for culture artefacts.

## Key points

- Screen hits were filtered against chemical inhibitor and human genetic databases to select actionable targets - a transferable strategy.
- Humans with biallelic DCPS loss-of-function have normal hematopoiesis, establishing the therapeutic window in humans directly.
- RG3039, developed for spinal muscular atrophy and already through phase I, has anti-leukemic activity by inducing pre-mRNA mis-splicing.
- DCPS interacts with spliceosome components, placing the dependency in pre-mRNA metabolism.
- Screening lines had normal karyotype and functional Trp53 to mimic primary AML, with an in vivo validation screen.

## Limitations

The authors report that genetic DCPS knockout or knockdown produces more potent anti-leukemic activity than RG3039 does - differentiation marker expression was more robust after knockdown - so the available inhibitor is not achieving the full effect, and domain mapping indicates residues outside the catalytic HIT sequence matter for AML survival. Their proposed remedy is a degradation approach, which is untested. The human tolerability evidence rests on rare individuals with one characterised allele, whose residual protein and activity are described as undetectable but who are few. Screens are in mouse AML lines with human validation, and RG3039's phase I safety was established for a different indication and dosing schedule.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yamauchi(2018) Cancer Cell; Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2018.01.012`; the prose sections were written here from the paper itself.

## Citation

Yamauchi et al. Cancer Cell 2018. Genome-wide CRISPR-Cas9 Screen Identifies Leukemia-Specific Dependence on a Pre-mRNA Metabolic Pathway Regulated by DCPS. doi: 10.1016/j.ccell.2018.01.012

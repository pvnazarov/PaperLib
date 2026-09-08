---
# --- identity ------------------------------------------------
id: 2018-01-01_tian-2018-journal-of-cellular-biochemist
id_basis: filename-year
source: Tian(2018) Journal of Cellular Biochemistry; AML1 ETO trans‐activates c‐KIT expression through the long range interaction between promoter and intronic enhancer.pdf
sha256: 32dd235ce18214a1242e84470a75706932e9ccde2aa3ec5197a2da0a772e2fc6
size_bytes: 1291604
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 52348

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1002/jcb.26587"
year: 2018
title: "AML1/ETO trans‐activates c‐KIT expression through the long range interaction between promoter and intronic enhancer"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tian(2018) J Cell Biochem; AML1 ETO trans-activates c-KIT expression through the long range interaction between promoter and intronic enhancer.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

AML1/ETO is documented mainly as a transcriptional repressor, and this study examines its transactivation mechanism at c-KIT, which is highly expressed in t(8;21) AML. ChIP-seq and motif scanning identified regulatory regions in the c-KIT promoter and an intronic enhancer, both enriched for AML1/ETO co-factors including AML1, CEBPe, c-Jun and c-Fos. Luciferase reporter assays show AML1/ETO transactivates the promoter through the AML1 motif with co-factors present, and that activity is reinforced by the intronic enhancer; ChIP-3C-qPCR verifies that AML1/ETO mediates DNA looping between the promoter and the intronic enhancer.

## Summary

Addresses the less-studied half of the fusion protein's function - how a protein characterised as a dominant-negative repressor activates genes - and answers it architecturally: AML1/ETO brings a distant intronic enhancer into contact with the promoter. c-KIT is a well-chosen target, since KIT mutations are the most common cooperating lesion in t(8;21) and KIT expression is characteristically high in this subtype.

The reporter experiments are systematic: promoter alone, intron alone, and the two joined, with and without AML1/ETO knockdown and with inducible AML1/ETO expression, all pointing the same way. The requirement for co-factors - AML1, CEBPe, c-Jun, c-Fos - to be co-transfected before activation is substantial is consistent with the wider finding in this collection that AP-1 factors cooperate with AML1/ETO at activated genes.

## Key points

- Explains how AML1/ETO activates rather than represses, at a gene central to t(8;21) biology.
- Both the c-KIT promoter and an intronic enhancer are bound by AML1/ETO and enriched for co-factors AML1, CEBPe, c-Jun and c-Fos.
- Transactivation requires the AML1 motif and the presence of co-factors, consistent with AP-1 cooperation reported elsewhere.
- The intronic enhancer reinforces promoter activity, and the combined construct outperforms either element alone.
- ChIP-3C-qPCR shows AML1/ETO mediates DNA looping between promoter and intronic enhancer.

## Limitations

Much of the functional evidence comes from luciferase reporter assays in HeLa cells - a cervical carcinoma line with no hematopoietic context - where transfected constructs on plasmids cannot reproduce native chromatin architecture, so the reporter results speak to sequence sufficiency rather than to what happens at the endogenous locus. The looping evidence rests on ChIP-3C-qPCR at a single locus, a targeted assay without genome-wide context. No functional consequence is tested: c-KIT expression is not shown to depend on the loop in leukemic cells, nor is disrupting the loop shown to affect growth. Published in a lower-profile journal with correspondingly limited experimental scope.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tian(2018) J Cell Biochem; AML1 ETO trans-activates c-KIT expression through the long range interaction between promoter and intronic enhancer.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1002/jcb.26587`; the prose sections were written here from the paper itself.

## Citation

Tian et al. Journal of Cellular Biochemistry 2018. AML1/ETO trans‐activates c‐KIT expression through the long range interaction between promoter and intronic enhancer. doi: 10.1002/jcb.26587

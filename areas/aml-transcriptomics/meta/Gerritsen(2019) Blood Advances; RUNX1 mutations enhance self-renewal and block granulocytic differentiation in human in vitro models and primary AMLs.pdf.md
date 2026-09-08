---
# --- identity ------------------------------------------------
id: 2019-01-01_gerritsen-2019-blood-advances-runx1-muta
id_basis: filename-year
source: Gerritsen(2019) Blood Advances; RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs.pdf
sha256: 678852419cdf9f8556f9e68f93091577b781c2655ac00e72e54919df7e5b6d7d
size_bytes: 2943800
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 146765

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/bloodadvances.2018024422"
year: 2019
title: "RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Gerritsen(2019) Blood Adv; RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The RUNX1-S291fs300X mutation was introduced into human CD34+ stem/progenitor cells and induced pluripotent stem cells. In both models it strongly impaired myeloid commitment while enhancing self-renewal, with increased long-term culture-initiating cell frequency and colony replating capacity; cord blood cultures continued beyond 100 days with an immature CD34+/CD123+/CD45RA+ granulocyte-macrophage progenitor-like phenotype, and the CD34+/CD38- HSC population appeared to be the cell of origin. CEBPA expression was reduced and its re-expression partly restored differentiation. RNA-seq on the models and primary patients confirmed the differentiation block, with upregulated targets enriched for nucleosome assembly and chromatin structure, and showed distinct genomic binding and differential expression for RUNX1mut versus AML1-ETO at genes including TCF4, MEIS1 and HMGA2.

## Summary

RUNX1 point mutations had been much less studied than the RUNX1 fusions despite being common and carrying a poor prognosis, and this addresses that directly in human rather than mouse cells. The mechanistic finding with the clearest handle is that CEBPA is reduced and that restoring it partly rescues differentiation, which puts a specific, familiar factor between the mutation and the phenotype.

The comparison with AML1-ETO is the more interesting contribution. Both lesions affect the same transcription factor and both block differentiation, yet RUNX1-mutant AML is poor-risk and AML1-ETO is good-risk. Showing that the two have different genomic binding distributions and different target genes offers a molecular basis for a prognostic difference that is otherwise just a clinical observation. Identifying the CD34+/CD38- HSC as the compartment where the mutation has most effect addresses cell of origin in a human system.

## Key points

- Models a RUNX1 point mutation in human CD34+ cells and iPSCs, where prior work concentrated on RUNX1 fusions and mouse models.
- The mutation blocks granulocytic differentiation and enhances self-renewal, with cultures sustained beyond 100 days in an immature GMP-like state.
- CEBPA is downregulated, and re-expressing it partially restores differentiation.
- The CD34+/CD38- HSC compartment is the most likely cell of origin.
- RUNX1mut and AML1-ETO have distinct genomic binding and target genes (TCF4, MEIS1, HMGA2), offering a basis for their opposite prognoses.

## Limitations

Overexpression of a mutant allele by transduction, not knock-in at the endogenous locus, so gene dosage and regulation differ from a patient's cell, and dominant-negative effects at supraphysiological levels are hard to exclude. A single mutation is tested, S291fs300X, while RUNX1 mutations are distributed across the protein with both missense and truncating classes that need not behave alike. The models produce a differentiation block and enhanced self-renewal but not leukemia, so this is transformation-adjacent rather than transformation. CEBPA rescue is partial. The primary-sample comparison rests on four RUNX1mut and three AML1-ETO AMLs, which is too few to support the prognostic interpretation; the authors present it as a potential explanation, which is the right strength.

## Provenance

Located in the published literature, dropped into `inbox/` as `Gerritsen(2019) Blood Adv; RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/bloodadvances.2018024422`; the prose sections were written here from the paper itself.

## Citation

Gerritsen et al. Blood Advances 2019. RUNX1 mutations enhance self-renewal and block granulocytic differentiation in human in vitro models and primary AMLs. doi: 10.1182/bloodadvances.2018024422

---
# --- identity ------------------------------------------------
id: 2019-01-01_ptasinska-2019-cell-reports-runx1-eto-de
id_basis: filename-year
source: Ptasinska(2019) Cell Reports; RUNX1-ETO Depletion in t(8,21) AML Leads to C EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction.pdf
sha256: 2a1690cc07984329597a0c455f03c3907f1c41c1e01fea38b3c35c2b5a3637d6
size_bytes: 4578398
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 109888

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.celrep.2019.08.040"
year: 2019
title: "RUNX1-ETO Depletion in t(8;21) AML Leads to C/EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ptasinska(2019) Cell Rep; RUNX1-ETO Depletion in t(8 21) AML Leads to C EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Promoter-Capture Hi-C, gene expression and transcription factor binding data are combined to construct a RUNX1-ETO-dependent dynamic gene regulatory network in t(8;21) AML. The approach links AML-specific cis-elements to their correct promoters and shows that RUNX1-ETO itself participates in cis-regulatory element interactions. After RUNX1-ETO depletion, gained interactions are associated with increased C/EBPalpha and RUNX1 binding while lost interactions involve loss of JUND and LDB1; gained interactions did not involve LMO2 or PU.1, and lost interactions did not involve CTCF. CITED2 is given as an example of a gene with a new C/EBPalpha-driven interaction, and CCND2 as a downregulated AP-1-dependent example.

## Summary

Adds the three-dimensional dimension to the t(8;21) regulatory network. Knowing which transcription factors bind where is not enough if the elements they bind are not connected to the right promoters, and promoter-capture Hi-C makes those assignments directly rather than by proximity.

The finding is that the interaction landscape is dynamic and transcription-factor-driven rather than structural. When the fusion is removed, new contacts form where C/EBPalpha binds and existing contacts are lost where AP-1 factors leave - and CTCF, the canonical architectural protein, is not involved in the lost interactions. That places the reorganisation under the control of lineage transcription factors rather than of the general looping machinery, which is a meaningful distinction. CCND2 appearing as an AP-1-dependent downregulated gene connects directly to the Martinez-Soria work in this collection.

## Key points

- Promoter-capture Hi-C assigns t(8;21) AML-specific cis-elements to their correct promoters, rather than inferring by proximity.
- RUNX1-ETO itself participates in cis-regulatory element interactions.
- Interactions gained after depletion are driven by C/EBPalpha and RUNX1; lost interactions involve loss of JUND and LDB1.
- CTCF is not involved in the lost interactions, so the reorganisation is transcription-factor-driven rather than architectural.
- CCND2 is a downregulated AP-1-dependent example, linking this to the CCND2 dependency reported separately in t(8;21) AML.

## Limitations

Published as a short Report, and based on siRNA knockdown in t(8;21) cell lines rather than primary patient blasts. Promoter-capture Hi-C at 5-kb resolution cannot resolve individual regulatory elements, and interaction calls from this technique are sensitive to normalisation and to sequencing depth - the correlation heatmaps presented are of merged replicates. Causation between transcription factor binding changes and interaction changes is inferred from their co-occurrence, not tested by manipulating the factors. Knockdown is transient, and the time course over 2 to 10 days means early direct effects and later secondary reorganisation are difficult to separate. No functional consequence of any specific interaction change is demonstrated.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ptasinska(2019) Cell Rep; RUNX1-ETO Depletion in t(8 21) AML Leads to C EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.celrep.2019.08.040`; the prose sections were written here from the paper itself.

## Citation

Ptasinska et al. Cell Reports 2019. RUNX1-ETO Depletion in t(8;21) AML Leads to C/EBPα- and AP-1-Mediated Alterations in Enhancer-Promoter Interaction. doi: 10.1016/j.celrep.2019.08.040

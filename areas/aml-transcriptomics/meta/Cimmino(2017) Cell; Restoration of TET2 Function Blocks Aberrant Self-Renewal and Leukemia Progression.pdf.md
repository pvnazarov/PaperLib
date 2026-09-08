---
# --- identity ------------------------------------------------
id: 2017-01-01_cimmino-2017-cell-restoration-of-tet2-fu
id_basis: filename-year
source: Cimmino(2017) Cell; Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression.pdf
sha256: ae5a0943e3fba26674860a2823b05c936cbd36613790d9d3c490ceb81199b936
size_bytes: 7350857
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 259069

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.cell.2017.07.032"
year: 2017
title: "Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Cimmino(2017) Cell; Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using a reversible transgenic RNAi mouse to model restoration of endogenous Tet2 expression, the authors show that Tet2 restoration reverses aberrant hematopoietic stem and progenitor cell self-renewal in vitro and in vivo, promoting DNA demethylation, differentiation and cell death. Vitamin C, a cofactor of Fe2+ and alpha-ketoglutarate-dependent dioxygenases, mimics restoration by enhancing 5-hydroxymethylcytosine generation and blocks leukemia progression, and it also sensitises leukemia cells to PARP inhibition.

## Summary

A rare experiment in cancer biology: switching a tumour suppressor back on and watching what happens. The reversible RNAi mouse makes TET2 loss a state rather than an event, and restoring it reverses aberrant self-renewal - establishing that continued TET2 deficiency is required to maintain the pre-leukemic state, not merely to initiate it.

The vitamin C result is what made the paper widely read, and the authors handle its awkward history well. High-dose vitamin C failed in trials decades ago; they argue the failures reflect oral bioavailability, since plasma cannot exceed about 150 microM orally while intravenous administration reaches far higher levels. They also test the mechanism honestly - combined Tet2/Tet3 deficiency abolishes vitamin C's effect, which is the control showing it works through TETs and that some residual TET activity is needed. The PARP inhibitor synergy follows from base excision repair being the route by which oxidised methylcytosines are removed.

## Key points

- A reversible RNAi mouse shows that restoring Tet2 reverses aberrant self-renewal - the pre-leukemic state requires ongoing TET2 deficiency.
- Vitamin C pharmacologically mimics TET2 restoration by boosting 5hmC generation, and works even with no functional Tet2, probably via TET3.
- Combined Tet2/Tet3 loss abolishes the vitamin C effect, establishing TETs as the mechanism and a minimum TET activity as a requirement.
- Restoring TET activity creates a new vulnerability: leukemia cells become more sensitive to PARP inhibitors.
- The historical failure of vitamin C trials is attributed to oral bioavailability; intravenous dosing reaches roughly 100-fold higher plasma levels.

## Limitations

Mouse genetics throughout, and the reversible RNAi model restores Tet2 uniformly and completely, which no drug does. Most patients carry mono-allelic TET2 loss, and the model's relevance to that state is argued rather than tested directly. Vitamin C's promise here rests on achieving intravenous pharmacologic concentrations in patients, which the paper does not attempt; the argument that prior trials failed for bioavailability reasons is plausible but retrospective, and high-dose intravenous vitamin C has since been tested in other cancers with modest results. Effects are on aberrant self-renewal and disease progression in models rather than on established AML. The PARP inhibitor synergy is preclinical. TET2 restoration also cannot address the additional mutations that accumulate in overt AML.

## Provenance

Located in the published literature, dropped into `inbox/` as `Cimmino(2017) Cell; Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.cell.2017.07.032`; the prose sections were written here from the paper itself.

## Citation

Cimmino et al. Cell 2017. Restoration of TET2 Function Blocks Aberrant Self-Renewal and Leukemia Progression. doi: 10.1016/j.cell.2017.07.032

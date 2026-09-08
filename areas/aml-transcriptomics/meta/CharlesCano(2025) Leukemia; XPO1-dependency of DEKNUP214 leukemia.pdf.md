---
# --- identity ------------------------------------------------
id: 2025-01-01_charlescano-2025-leukemia-xpo1-dependenc
id_basis: filename-year
source: CharlesCano(2025) Leukemia; XPO1-dependency of DEKNUP214 leukemia.pdf
sha256: 5b7c1e52d1747723bddf281de0feef0dc9ba3b6161ee0488fa86a558348c974b
size_bytes: 1701520
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 141932

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-025-02570-1"
year: 2025
title: "XPO1-dependency of DEK::NUP214 leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as CharlesCano(2025) Leukemia; XPO1-dependency of DEK NUP214 leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

DEK::NUP214 (t(6;9)) AML is evaluated for dependency on the nuclear export protein XPO1. Deleting XPO1 in DN-positive FKH-1 cells revealed strong dependency; the second-generation nuclear export inhibitor eltanexor reduced XPO1 expression, disrupted co-localisation of XPO1 with the fusion protein, and induced apoptosis and cell cycle arrest in primary and FKH-1 cells. XPO1 and DEK::NUP214 co-localise at chromatin, and inhibition strongly reduces that binding, downregulating fusion target genes and cell cycle and self-renewal pathways. In a patient-derived xenograft, eltanexor-treated mice showed molecular clearance in bone marrow after a median of 377 days while controls died after a median of 244 days.

## Summary

A precise mechanistic claim for a rare entity - DEK::NUP214 is about 1% of AML, affects younger adults, and is ELN adverse-risk with chemotherapy resistance, so a targeted option matters disproportionately. The mechanism inverts the usual reading of XPO1 inhibition: rather than trapping tumour suppressors in the nucleus, here XPO1 is shown to stabilise the fusion protein at chromatin, and removing it strips the oncoprotein off the DNA it needs to act on.

The in vivo result is unusually strong for this literature. Eltanexor-treated mice had no detectable hCD45+ cells in blood throughout treatment and for 26 weeks after the last control mouse died, with normal counts maintained, and the authors describe the PDX mice as cured. That is a durable clearance rather than a survival shift.

## Key points

- XPO1 is a genetic dependency in DEK::NUP214 AML, shown by deletion as well as by pharmacological inhibition.
- The mechanism is chromatin stabilisation: XPO1 and the fusion co-localise on chromatin, and inhibition removes both, silencing fusion target genes.
- Eltanexor, a second-generation selective inhibitor of nuclear export, induces apoptosis and cell cycle arrest in primary and cell-line DN AML.
- In a PDX model, eltanexor produced molecular clearance in marrow with normal blood counts and no detectable engraftment long after controls died.
- Gives a targeted option for a WHO/ICC-recognised entity that is ELN adverse-risk and chemotherapy-resistant.

## Limitations

DEK::NUP214 is rare, and the in vitro work rests almost entirely on a single cell line, FKH-1, which is one of very few available - so cell-line-specific effects cannot be excluded. The in vivo result comes from one PDX model, and one treated mouse had to be sacrificed at day 167, which is not fully accounted for in the summary claim. XPO1 inhibition is pleiotropic and eltanexor affects the export of many cargoes, so the chromatin mechanism, though supported by co-localisation, is not proven to be the therapeutic mechanism. Treatment continued for months with dose reduction after an interruption, so tolerability required adjustment. DEK::NUP214 frequently co-occurs with FLT3-ITD, and how that interacts with XPO1 dependency is not addressed.

## Provenance

Located in the published literature, dropped into `inbox/` as `CharlesCano(2025) Leukemia; XPO1-dependency of DEK NUP214 leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-025-02570-1`; the prose sections were written here from the paper itself.

## Citation

CharlesCano et al. Leukemia 2025. XPO1-dependency of DEK::NUP214 leukemia. doi: 10.1038/s41375-025-02570-1

---
# --- identity ------------------------------------------------
id: 2020-01-01_uckelmann-2020-science-therapeutic-targe
id_basis: filename-year
source: Uckelmann(2020) Science; Therapeutic targeting of preleukemia cells in a mouse model of NPM1 mutant acute myeloid leukemia.pdf
sha256: eb6535f736e1e4151000a0e6344be2dae086eac402acb38b7b788485bf6f6a7f
size_bytes: 893823
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 87680

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1126/science.aax5863"
year: 2020
title: "Therapeutic targeting of preleukemia cells in a mouse model of NPM1 mutant acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Uckelmann(2020) Science; Therapeutic targeting of preleukemia cells in a mouse model ofmutant acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

In Npm1c/Dnmt3a mutant knock-in mice, leukemia is preceded by extended myeloid progenitor proliferation and self-renewal. Npm1c induces stem-cell-associated gene expression, including Hoxa9, de novo in committed progenitors that normally lack self-renewal, and confers increased replating capacity; Dnmt3a mutation alone does not. This self-renewal is reversed by oral administration of the menin-MLL1 inhibitor VTP-50469, which rapidly represses stem cell genes including Meis1 and Pbx3 and induces differentiation. Meis1 knockout confirms it as a dependency, and Menin chromatin occupancy decreases globally while MLL1 and H3K4me3 are lost only at sites enriched for downregulated genes.

## Summary

Asks a question the field rarely tests: whether a targeted therapy can eradicate premalignant cells, not just treat established disease. AML is the right system because it is often preceded by clonal hematopoiesis or myelodysplastic syndrome, so a preventative window genuinely exists.

The biology underneath is that Npm1c can impose a stem cell programme on cells that do not have one - inducing Hoxa9 in granulocyte-monocyte progenitors, which normally lack self-renewal and express little Hox - and that this aberrant self-renewal is reversible with an oral drug. The chromatin analysis shows why the effect is selective: Menin is lost broadly, but MLL1 and H3K4me3 are lost only at the specific sites whose genes go down, which is the basis of the therapeutic window.

## Key points

- Tests whether targeted therapy can reverse a premalignant state, using a model where AML is preceded by progenitor self-renewal.
- Npm1c, not Dnmt3a mutation, induces Hoxa9 and a stem cell programme de novo in committed progenitors.
- Oral VTP-50469 reverses that self-renewal, repressing Meis1 and Pbx3 and inducing differentiation without significant apoptosis.
- Meis1 knockout independently confirms it as a dependency, and Meis1 expression protects cells from menin inhibition.
- Menin occupancy falls globally while MLL1 and H3K4me3 are lost only at downregulated genes - the basis of selectivity.

## Limitations

A mouse knock-in model with two defined mutations, whereas human clonal hematopoiesis and MDS are genetically heterogeneous and evolve over decades - so the preventative window modelled here is far cleaner than the clinical one. Reversing self-renewal is not the same as preventing leukemia, and the study does not follow treated animals to show that AML never develops. Any preventative strategy requires identifying high-risk individuals prospectively and treating them for years with an agent whose long-term toxicity is unknown, which the paper acknowledges only as a hypothesis worth testing. The finding that Meis1-expressing cells resist menin inhibition also identifies a resistance mechanism that would apply in the preventative setting.

## Provenance

Located in the published literature, dropped into `inbox/` as `Uckelmann(2020) Science; Therapeutic targeting of preleukemia cells in a mouse model ofmutant acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1126/science.aax5863`; the prose sections were written here from the paper itself.

## Citation

Uckelmann et al. Science 2020. Therapeutic targeting of preleukemia cells in a mouse model of
                    <i>NPM1</i>
                    mutant acute myeloid leukemia. doi: 10.1126/science.aax5863

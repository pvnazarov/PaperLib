---
# --- identity ------------------------------------------------
id: 2025-01-01_lv-2025-genome-biology-kat6a-chimeras-fo
id_basis: filename-year
source: Lv(2025) Genome Biology; KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL COMPASS to sustain AML.pdf
sha256: d71e3382e2639d59580adbee0b6a2c932cec0a861b47f442943fa97c2bee454b
size_bytes: 6589028
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 116811

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13059-025-03743-y"
year: 2025
title: "KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL/COMPASS to sustain AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lv(2025) Genome Biol; KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL COMPASS to sustain AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

KAT6A-CBP and KAT6A-P300 fusions are recurrent in AML with poor prognosis, but their size has impeded model development. Using a domain-focused truncation strategy, the authors generate de novo murine models that recapitulate the morphological, immunophenotypic and transcriptomic features of KAT6A-rearranged AML. The fusions preferentially localise to H3K4me2/3-marked regions, and KAT6A interacts with the Nucleosome Remodeling Factor (NURF), an H3K4me2/3 reader. Depleting or inhibiting the NURF subunit BPTF impairs fusion recruitment and disrupts MLL/COMPASS-mediated H3K4me2 deposition; CBP/P300 inhibition reduces acetylation and accessibility, further impairing recruitment, and combining the two is more effective than either alone.

## Summary

Solves a practical obstacle first. KAT6A fusion proteins are very large, which has prevented anyone building tractable models, and the domain-focused truncation strategy is what makes the rest of the work possible - a reminder that in this field the model is often the limiting reagent.

The biology is a genuine feedback loop rather than a linear pathway. The fusion is recruited to H3K4me2/3 by NURF; NURF supports MLL/COMPASS deposition of H3K4me2; the fusion's own CBP/P300 acetyltransferase activity opens chromatin and further aids recruitment. Each component reinforces the others, which explains both why the module is stable and why disrupting two points at once - BPTF and CBP/P300 - works better than either alone.

## Key points

- A domain-focused truncation strategy yields the first tractable murine models of the very large KAT6A-CBP and KAT6A-P300 fusions.
- The models recapitulate morphological, immunophenotypic and transcriptomic features of KAT6A-rearranged AML.
- KAT6A chimeras localise to H3K4me2/3 regions via interaction with NURF, an H3K4me2/3 reader.
- The module is self-reinforcing: NURF recruits the fusion, supports MLL/COMPASS H3K4me2 deposition, and CBP/P300 acetylation maintains the accessibility that permits recruitment.
- BPTF and CBP/P300 inhibition are each effective in K/C models and better in combination.

## Limitations

The models are built from truncated constructs retrovirally overexpressed in murine HSPCs, not from endogenous full-length fusions at native expression, so the recapitulation is phenotypic rather than genetic - and truncation was adopted for tractability, which means the models omit domains of the real oncoprotein. No primary human KAT6A-rearranged AML is tested. BPTF is a broadly required chromatin reader and CBP/P300 are essential acetyltransferases, so both interventions are pleiotropic and the therapeutic window is unaddressed; efficacy is measured in the murine leukemia models over short experiments. The self-reinforcing module is inferred from the effect of disrupting each component rather than from a direct demonstration that the components stabilise one another.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lv(2025) Genome Biol; KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL COMPASS to sustain AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13059-025-03743-y`; the prose sections were written here from the paper itself.

## Citation

Lv et al. Genome Biology 2025. KAT6A chimeras form a self-reinforcing epigenetic module with NURF and MLL/COMPASS to sustain AML. doi: 10.1186/s13059-025-03743-y

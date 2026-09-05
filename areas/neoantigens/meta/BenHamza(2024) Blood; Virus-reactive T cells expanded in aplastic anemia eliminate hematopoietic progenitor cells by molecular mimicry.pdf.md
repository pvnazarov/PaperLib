---
# --- identity ------------------------------------------------
id: 2024-01-01_benhamza-2024-blood-virus-reactive-t-cel
id_basis: filename-year
source: BenHamza(2024) Blood; Virus-reactive T cells expanded in aplastic anemia eliminate hematopoietic progenitor cells by molecular mimicry.pdf
sha256: 60c80e52fd81478aad5434d000c6ffc518fdb16cb1b0bb54a6481beba9b1e809
size_bytes: 2584550
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 188634

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2023023142"
year: 2024
title: "Virus-reactive T cells expanded in aplastic anemia eliminate hematopoietic progenitor cells by molecular mimicry"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Ben_Blood_Virus_reactive_T_cells_expanded_in_aplastic_an_PMID38277625.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

In 15 patients with acquired aplastic anaemia, single-cell sequencing and immunophenotyping showed oligoclonal expansion and effector differentiation of bone marrow CD8+ T cells. Re-expressing 28 dominant TCRs from 9 patients identified specificities for persistent viral antigens, and those same TCRs killed autologous haematopoietic progenitor cells through molecular mimicry.

## Summary

The disease has long been treated as T-cell mediated on the strength of its response to immunosuppression, but the antigens driving it were unknown. This work goes from expanded clone to reconstructed TCR to demonstrated target, which is the chain of evidence that was missing.

The mechanism is cross-reactivity: TCRs raised against epitopes of persistent viral infection also recognise epitopes presented on haematopoietic progenitors, and the resulting killing is sufficient to explain marrow failure.

## Key points

- 28 dominant TCRs from 9 of 15 patients were re-expressed in reporter lines to determine reactivity, rather than inferred from repertoire statistics.
- Virus-reactive clones eliminated autologous haematopoietic progenitor cells, establishing the mimicry as functional and not merely structural.
- Bone marrow CD8+ compartments showed oligoclonal expansion with effector differentiation.
- Gives a concrete, non-cancer instance of the self/non-self discrimination problem that neoantigen prediction runs into from the other direction.

## Limitations

Fifteen patients, with reconstructed TCRs from nine of them, is a small base for a mechanistic claim about a heterogeneous syndrome; the paper does not establish that mimicry accounts for most or even many cases. Reporter-line reactivity and in vitro progenitor killing are not the same as demonstrating that this drives marrow failure in a patient. The direction of causation between viral exposure and disease onset is not established here.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Ben_Blood_Virus_reactive_T_cells_expanded_in_aplastic_an_PMID38277625.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2023023142`; the prose sections were written here from the paper itself.

## Citation

BenHamza et al. Blood 2024. Virus-reactive T cells expanded in aplastic anemia eliminate hematopoietic progenitor cells by molecular mimicry. doi: 10.1182/blood.2023023142

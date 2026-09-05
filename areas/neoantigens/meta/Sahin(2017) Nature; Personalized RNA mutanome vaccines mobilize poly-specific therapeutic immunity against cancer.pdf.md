---
# --- identity ------------------------------------------------
id: 2017-01-01_sahin-2017-nature-personalized-rna-mutan
id_basis: filename-year
source: Sahin(2017) Nature; Personalized RNA mutanome vaccines mobilize poly-specific therapeutic immunity against cancer.pdf
sha256: ab61203bdf64b0aa9e83c202ab02bec6d6f8382e72bf50364ae1b7570d05f68e
size_bytes: 3065460
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 317901

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nature23003"
year: 2017
title: "Personalized RNA mutanome vaccines mobilize poly-specific therapeutic immunity against cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as nature23003.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A first-in-human study of individualised RNA mutanome vaccines, targeting each patient's own set of mutations. The premise is that T cells against mutant neo-epitopes drive cancer immunity but spontaneous recognition of mutations is inefficient, so vaccination is used to mobilise poly-specific responses that would not arise on their own.

## Summary

This is the origin of the RNA neoantigen vaccine platform that the pancreatic and melanoma mRNA trials in this collection are built on, and it establishes the manufacturing model: sequence the tumour, select mutations, synthesise a personalised RNA vaccine per patient.

The key word is poly-specific. Rather than choosing one strong target, the vaccine encodes many mutations at once, which hedges against individual predictions being wrong and against outgrowth of variants that lose a single targeted antigen.

## Key points

- First-in-human individualised RNA mutanome vaccine, the platform behind the later mRNA trials here.
- Poly-specific by design - many mutations per vaccine, hedging against prediction error and antigen loss.
- Rests on the observation that spontaneous immune recognition of mutations is inefficient, so the vaccine supplies what the tumour did not provoke.
- Demonstrated the sequence-to-personalised-vaccine workflow end to end in patients.

## Limitations

A small, single-arm first-in-human study: it establishes feasibility and immunogenicity, not efficacy, and no control arm allows clinical observations to be attributed to the vaccine. Mutation selection depended on 2017-era prediction tools. Which of the many encoded neoepitopes actually drove any observed response is not resolved by a poly-specific design - it is a deliberate trade of attribution for robustness.

## Provenance

Located in the published literature, dropped into `inbox/` as `nature23003.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nature23003`; the prose sections were written here from the paper itself.

## Citation

Sahin et al. Nature 2017. Personalized RNA mutanome vaccines mobilize poly-specific therapeutic immunity against cancer. doi: 10.1038/nature23003

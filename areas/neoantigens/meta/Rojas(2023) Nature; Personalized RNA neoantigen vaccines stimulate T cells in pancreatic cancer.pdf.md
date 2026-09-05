---
# --- identity ------------------------------------------------
id: 2023-01-01_rojas-2023-nature-personalized-rna-neoan
id_basis: filename-year
source: Rojas(2023) Nature; Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer.pdf
sha256: ba660cdfbff382f4d8928bb06205dadb40fa722598b6a465f6f933b5b8242014
size_bytes: 12626935
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 309248

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-023-06063-y"
year: 2023
title: "Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2023_Rojas_Nature_Personalized_RNA_neoantigen_vaccines_stimulate_PMID37165196.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A phase I trial of adjuvant autogene cevumeran, an individualised uridine mRNA-lipoplex neoantigen vaccine synthesised in real time from surgically resected pancreatic ductal adenocarcinoma. Vaccine-expanded T cells were induced in half the patients, and vaccine response correlated with delayed recurrence.

## Summary

PDAC is the hard case: lethal in 88% of patients, poorly inflamed, with immune-excluded or desert phenotypes. Demonstrating that an individualised mRNA vaccine can raise neoantigen-specific T cells here is a stronger result than the same demonstration in melanoma would be.

The operational achievement is manufacture within the post-surgical window - sequencing, neoantigen selection and mRNA synthesis fast enough to treat in the adjuvant setting.

## Key points

- Individualised mRNA neoantigen vaccine manufactured in real time from each patient's resected tumour.
- Approximately half of patients showed vaccine-expanded T cell responses; responders had delayed recurrence.
- Responder tumours were more clonal, consistent with immune-edited evolution seen in long-term PDAC survivors.
- Neoantigen quality, in the Luksza sense, correlated with immunogenicity - linking the computational and clinical strands of this collection.

## Limitations

The authors state the study was not powered to detect differences in biomarkers of vaccine response, so every biomarker observation here is hypothesis-generating. It is phase I, single-arm and small, and the recurrence correlation is not a randomised outcome. Whether mRNA neoantigen vaccines work in other non-inflamed cancers is explicitly left open, and the accompanying NeoPrecis paper notes that only 11% of targeted neoantigens actually induced a response.

## Provenance

Located in the published literature, dropped into `inbox/` as `2023_Rojas_Nature_Personalized_RNA_neoantigen_vaccines_stimulate_PMID37165196.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-023-06063-y`; the prose sections were written here from the paper itself.

## Citation

Rojas et al. Nature 2023. Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. doi: 10.1038/s41586-023-06063-y

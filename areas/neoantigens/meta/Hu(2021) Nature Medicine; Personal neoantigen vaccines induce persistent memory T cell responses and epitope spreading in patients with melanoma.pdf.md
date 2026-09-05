---
# --- identity ------------------------------------------------
id: 2021-01-01_hu-2021-nature-medicine-personal-neoanti
id_basis: filename-year
source: Hu(2021) Nature Medicine; Personal neoantigen vaccines induce persistent memory T cell responses and epitope spreading in patients with melanoma.pdf
sha256: fdb3c43985a82a7e7bcb841baf45ba8d378e7fda5e5356e12bc00c8589153d92
size_bytes: 20480623
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 207957

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41591-020-01206-4"
year: 2021
title: "Personal neoantigen vaccines induce persistent memory T cell responses and epitope spreading in patients with melanoma"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41591-020-01206-4.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Long-term follow-up of eight melanoma patients given a personal neoantigen vaccine shows persistent memory T cell responses and epitope spreading - responses to neoepitopes that were not in the vaccine - years after immunisation.

## Summary

Epitope spreading is the finding that matters, and it is the one the pancreatic mRNA trials in this collection looked for and did not detect. If vaccination against a handful of neoantigens broadens immunity to others released by tumour killing, the vaccine does more than the sum of its targets.

The authors report spreading not only in a patient with clinically evident metastases but also in one with no evidence of disease, which suggests it can occur against micro-metastatic disease.

## Key points

- Memory T cell responses persist long after vaccination, not just at peak immunisation.
- Epitope spreading to non-vaccine neoepitopes observed - contrast with Sethna (2025) in PDAC, where it was looked for and not found.
- Spreading occurred in a patient without evident disease as well as one with metastases.
- Long-term clinical and immunological follow-up of a peptide vaccine cohort, which is rare.

## Limitations

Eight patients, no control arm - this describes what happened, not what the vaccine caused. The authors state they cannot exclude that very-low-frequency T cells against the non-vaccine epitopes were present before vaccination and simply undetectable, which is the alternative explanation for apparent spreading. Melanoma is the most favourable setting for neoantigen vaccines, so these results are an upper bound rather than a typical case.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41591-020-01206-4.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41591-020-01206-4`; the prose sections were written here from the paper itself.

## Citation

Hu et al. Nature Medicine 2021. Personal neoantigen vaccines induce persistent memory T cell responses and epitope spreading in patients with melanoma. doi: 10.1038/s41591-020-01206-4

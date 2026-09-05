---
# --- identity ------------------------------------------------
id: 2018-01-01_keskin-2018-nature-neoantigen-vaccine-ge
id_basis: filename-year
source: Keskin(2018) Nature; Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial.pdf
sha256: 49e55aab341e5c5a081cf6b8a5903a5073111c7b1d061b7635c9e7352f9b4581
size_bytes: 41910415
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 180919

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41586-018-0792-9"
year: 2018
title: "Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as s41586-018-0792-9.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

A phase Ib trial of a personal neoantigen-targeting vaccine in glioblastoma, a tumour with low mutation burden and an immunologically cold microenvironment behind the blood-brain barrier. Vaccine-induced neoantigen-specific T cells were detected within the tumour itself, not only in circulation.

## Summary

Glioblastoma is close to the worst case for this approach: few mutations, profound local immunosuppression, and a site that circulating T cells reach poorly. Demonstrating intratumoral neoantigen-specific T cells is therefore a stronger claim than a peripheral blood response would be.

The intratumoral measurement is the methodological point. Peripheral response is what most vaccine trials can measure; whether those T cells reach and persist in the tumour is the question that decides whether the vaccine can work.

## Key points

- Vaccine-induced neoantigen-specific T cells found inside the tumour, not inferred from blood.
- Demonstrated in glioblastoma - low mutation burden, immunosuppressive, behind the blood-brain barrier.
- Patients not on dexamethasone showed the T cell responses, implicating steroid use as a confounder in this setting.
- Single-cell profiling links vaccine-induced clones to the intratumoral T cell landscape.

## Limitations

Phase Ib, small and single-arm: this establishes immunological feasibility, not clinical benefit, and glioblastoma outcomes were not improved. Intratumoral T cell detection requires resected tissue, so the finding is available only for patients who had surgery at the right moment. The dexamethasone observation is a subgroup comparison in a very small cohort and should be treated as a hypothesis.

## Provenance

Located in the published literature, dropped into `inbox/` as `s41586-018-0792-9.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41586-018-0792-9`; the prose sections were written here from the paper itself.

## Citation

Keskin et al. Nature 2018. Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial. doi: 10.1038/s41586-018-0792-9

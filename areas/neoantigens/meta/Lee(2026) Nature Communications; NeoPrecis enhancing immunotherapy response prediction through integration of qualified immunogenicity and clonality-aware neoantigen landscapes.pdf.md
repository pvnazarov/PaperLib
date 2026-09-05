---
# --- identity ------------------------------------------------
id: 2026-01-01_lee-2026-nature-communications-neoprecis
id_basis: filename-year
source: Lee(2026) Nature Communications; NeoPrecis enhancing immunotherapy response prediction through integration of qualified immunogenicity and clonality-aware neoantigen landscapes.pdf
sha256: d0244d93d7f7746c14deae45c9704ae46209e58e854b2b990442824c4cb112ed
size_bytes: 2526215
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 136690

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-026-68651-6"
year: 2026
title: "NeoPrecis: enhancing immunotherapy response prediction through integration of qualified immunogenicity and clonality-aware neoantigen landscapes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2026_Lee_Nat_Commun_NeoPrecis_enhancing_immunotherapy_response_pre_PMID41577704.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

NeoPrecis predicts immunotherapy response by refining neoantigen characterisation across both MHC-I and MHC-II pathways and incorporating tumour clonality, rather than relying on tumour mutation burden. Its interpretable T-cell-recognition model shows MHC molecules influence TCR recognition beyond presentation, and model-derived 'benefit' HLA alleles predict checkpoint-inhibitor outcomes in melanoma (p = 0.04) and NSCLC (p = 0.01).

## Summary

The critique of TMB is that it counts mutations without asking whether any of them are seen, and treats a subclonal neoantigen present in 5% of tumour cells the same as a clonal one present in all of them. NeoPrecis addresses both.

The framing quantity the authors cite is worth remembering: in the Rojas pancreatic vaccine trial the overall response rate was 50%, but only 11% of targeted neoantigens actually induced a T cell response. That gap between selecting a target and it working is what this framework is built to narrow.

## Key points

- Covers MHC-II as well as MHC-I, which most response-prediction metrics omit.
- Clonality-aware: subclonal and clonal neoantigens are weighted differently, which matters most in heterogeneous NSCLC.
- The recognition model attributes a role to the MHC molecule itself in TCR recognition, not just in presentation.
- Model-driven 'benefit' HLA alleles carry independent predictive power for checkpoint-inhibitor outcome.

## Limitations

Both outcome associations are around the conventional significance threshold (p = 0.04, p = 0.01) in retrospective cohorts, so this is a candidate stratifier rather than a validated one. 'Benefit' alleles identified by contribution analysis on the same data risk circularity unless validated on an independent cohort. Clonality estimates depend on purity and ploidy calls that carry their own error, and that error propagates into the landscape feature.

## Provenance

Located in the published literature, dropped into `inbox/` as `2026_Lee_Nat_Commun_NeoPrecis_enhancing_immunotherapy_response_pre_PMID41577704.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-026-68651-6`; the prose sections were written here from the paper itself.

## Citation

Lee et al. Nature Communications 2026. NeoPrecis: enhancing immunotherapy response prediction through integration of qualified immunogenicity and clonality-aware neoantigen landscapes. doi: 10.1038/s41467-026-68651-6

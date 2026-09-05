---
# --- identity ------------------------------------------------
id: 2026-01-01_xing-2026-jhep-reports-mass-spectrometry
id_basis: filename-year
source: Xing(2026) JHEP Reports; Mass spectrometry-based de novo sequencing reveals non-canonical neoantigens with antitumor efficacy in hepatocellular carcinoma.pdf
sha256: 887d4ca6424cf56cca79d15b41c13507dcc1d7656c97883a7dfb40d67c79a52e
size_bytes: 9955794
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 155586

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.jhepr.2026.101775"
year: 2026
title: "Mass spectrometry-based de novo sequencing reveals non-canonical neoantigens with antitumor efficacy in hepatocellular carcinoma"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as PIIS2589555926000467.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Mass-spectrometry de novo sequencing, rather than database search, is used to identify non-canonical neoantigens in hepatocellular carcinoma. Candidates were validated by ELISpot for immunogenicity and PRM targeted proteomics for endogenous expression, then tested as a peptide vaccine in subcutaneous and orthotopic mouse HCC models.

## Summary

De novo sequencing is the methodological choice that matters. Database search can only find peptides present in the reference it searches, so non-canonical antigens - from outside coding regions or unusual processing - are invisible to it by construction. Reading the spectrum directly removes that limit, at the cost of a harder inference.

The validation chain is unusually complete for this literature: predicted, then confirmed endogenously expressed by targeted proteomics, then shown immunogenic, then shown to have antitumour efficacy in two in vivo models.

## Key points

- De novo sequencing rather than database search, so non-canonical antigens are findable rather than excluded a priori.
- PRM targeted proteomics confirms the peptides are endogenously present, not just spectrally plausible.
- ELISpot for immunogenicity and two mouse HCC models - subcutaneous and orthotopic - for antitumour efficacy.
- A discovery-to-validation pipeline for a neoantigen class that prediction-based methods systematically miss.

## Limitations

De novo sequencing has a substantially higher error rate than database search, and its false discovery rate is harder to control - the very freedom that finds non-canonical peptides also produces spurious ones. Efficacy is in mouse HCC models, with the usual distance to human disease. The validated set is small, so this demonstrates a viable pipeline rather than establishing how much of the HCC immunopeptidome is non-canonical.

## Provenance

Located in the published literature, dropped into `inbox/` as `PIIS2589555926000467.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.jhepr.2026.101775`; the prose sections were written here from the paper itself.

## Citation

Xing et al. JHEP Reports 2026. Mass spectrometry-based de novo sequencing reveals non-canonical neoantigens with antitumor efficacy in hepatocellular carcinoma. doi: 10.1016/j.jhepr.2026.101775

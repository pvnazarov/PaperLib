---
# --- identity ------------------------------------------------
id: 2023-01-01_cerella-2023-leukemia-atp1a1-bcl2l1-pred
id_basis: filename-year
source: Cerella(2023) Leukemia; ATP1A1 BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides.pdf
sha256: 88952b52d937a9b6ef376d1fa58e771f57a6639e8271cc00b3d8abdb12b3d490
size_bytes: 4367373
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 268270

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-023-02076-8"
year: 2023
title: "ATP1A1/BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Cerella(2024) Leukemia; ATP1A1 BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Myelomonocytic and monocytic AML are intrinsically resistant to venetoclax-based regimens. The authors report that ex vivo response of AML patient blasts and in vitro sensitivity of cell lines to the hemi-synthetic cardiac glycoside UNBS1450 correlates with the ATP1A1/BCL2L1 expression ratio. Public AML datasets identify myelomonocytic/monocytic differentiation as the most robust prognostic feature for this response, alongside CBFB and KMT2A rearrangements and missense FLT3 mutations. Mechanistically BCL2L1 protects against cell death from the glycoside's stepwise ionic perturbation, protein synthesis inhibition and MCL1 downregulation; in vivo the compounds were tolerable and produced tumour growth inhibition to regression.

## Summary

An attempt to solve the specific reason cardiac glycoside repurposing has repeatedly failed in oncology - not lack of preclinical activity, of which there has been plenty, but the absence of a biomarker to say who should receive them. The proposed marker is a ratio rather than a single gene, which is coherent with the mechanism: ATP1A1 is the drug's target and BCL2L1 the protein that resists the death it triggers.

The clinical logic is neat. The subtypes that resist venetoclax are the ones predicted to respond here, so the two would be complementary rather than competing, and the authors propose glycoside/venetoclax/hypomethylating triplets with monocytic phenotype as an enrolment criterion. They also do something uncommon and useful: they warn that their own luciferase-expressing cell models show reprogrammed BCL2-family expression and may no longer represent their parental lines.

## Key points

- The ATP1A1/BCL2L1 expression ratio predicts response to cardiac glycosides in AML blasts ex vivo and cell lines in vitro.
- Targets exactly the myelomonocytic/monocytic subtypes that are intrinsically venetoclax-resistant, so the two approaches are complementary.
- Mechanism is stepwise: ionic perturbation, protein synthesis inhibition, then MCL1 downregulation, with BCL2L1 protecting against commitment to death.
- CBFB and KMT2A rearrangements and missense FLT3 mutations are additional associated features in public datasets.
- The authors caution that luciferase-modified cell lines show altered BCL2-family expression and may not represent their parental lines.

## Limitations

The biomarker is correlative and derived from ex vivo blast response and cell lines, with no prospective clinical validation; the authors themselves list open questions - whether mRNA or protein measurement should be used, and what co-variates influence the prediction. Cardiac glycosides have a narrow therapeutic index and well-known cardiac toxicity, and the paper notes that a venetoclax combination may need specific schedules to avoid drug-drug interaction and compounded toxicity; in vivo work shows tolerability in mice, which is weak reassurance for this drug class in humans. The efficacy range reported is 'tumour growth inhibition to regression', which is a wide spread. The clinical premise is itself contested - the paper acknowledges recent work questioning whether monocytic differentiation predicts venetoclax response in practice.

## Provenance

Located in the published literature, dropped into `inbox/` as `Cerella(2024) Leukemia; ATP1A1 BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-023-02076-8`; the prose sections were written here from the paper itself.

## Citation

Cerella et al. Leukemia 2023. ATP1A1/BCL2L1 predicts the response of myelomonocytic and monocytic acute myeloid leukemia to cardiac glycosides. doi: 10.1038/s41375-023-02076-8

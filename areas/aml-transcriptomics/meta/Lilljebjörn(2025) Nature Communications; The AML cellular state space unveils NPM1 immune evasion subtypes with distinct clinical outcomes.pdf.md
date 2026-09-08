---
# --- identity ------------------------------------------------
id: 2025-01-01_lilljebj-rn-2025-nature-communications-t
id_basis: filename-year
source: Lilljebjörn(2025) Nature Communications; The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes.pdf
sha256: f7b1d4260d1314d3c040b9116ad862a408e9500e4c49dd21e6fef808b71504b9
size_bytes: 2953512
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 238121

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-025-66546-6"
year: 2025
title: "The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lilljebjörn(2025) Nat Commun; The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genomic and transcriptomic characterisation of 120 AMLs including single-cell RNA sequencing reveals cellular heterogeneity that distorts bulk transcriptomic profiles. Examining the signatures of more than 90,000 immature AML cells selectively identifies four main clusters, extending current genomic classification. NPM1-mutated AML stratifies into two clinically relevant classes: NPM1 class I shows downregulation of MHC class II and excellent survival after hematopoietic stem cell transplantation, while NPM1 class II is resistant to allogeneic T cells in ex vivo co-culture and has dismal survival after transplant.

## Summary

The methodological premise is that bulk transcriptomes of AML are distorted by variable proportions of differentiated cells, so classification should be built from immature cells specifically - and doing that on over 90,000 such cells yields four clusters that extend rather than merely reproduce genomic classification.

The NPM1 result is clinically actionable and counterintuitive. NPM1-mutant AML is treated as one entity; here it splits into two classes with opposite responses to transplant, and the class that does well is the one with MHC class II downregulated - the opposite of what immune reasoning would predict, since less antigen presentation should mean worse graft-versus-leukemia. The authors support the direction with an ex vivo allogeneic T cell assay showing class II is the resistant one, and they take the practical next step of reducing the classifier to 30 genes so it could become a clinical assay.

## Key points

- Classification built from >90,000 immature AML cells, since bulk profiles are distorted by variable differentiated content.
- Four transcriptional clusters extend, rather than duplicate, existing genomic classification of AML.
- NPM1-mutant AML splits into two classes with opposite outcomes after allogeneic transplant.
- NPM1 class II is resistant to allogeneic T cells ex vivo and gains no survival advantage from transplant; class I benefits substantially.
- A 30-gene list reproduces the classification across datasets, a step toward a clinical assay.

## Limitations

The finding that NPM1 class I has MHC class II downregulated yet does better after transplant runs against the mechanism the paper invokes, and the ex vivo co-culture assay is the only functional evidence bearing on it - so the immune-evasion interpretation is less secure than the outcome association. The two classes differ substantially in co-mutations (IDH2, TET2, SRSF2 in class I; FLT3, DNMT3A, WT1, NRAS, PTPN11 in class II), so the classification may partly re-encode known prognostic genotypes even though the authors report the effect is not attributable to other factors. Survival analyses are retrospective across four datasets with transplant decisions made non-randomly, which biases any comparison of transplanted and non-transplanted patients. 120 AMLs, of which NPM1-mutant cases are a subset, gives modest numbers per class.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lilljebjörn(2025) Nat Commun; The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-025-66546-6`; the prose sections were written here from the paper itself.

## Citation

Lilljebjörn et al. Nature Communications 2025. The AML cellular state space unveils NPM1 immune evasion subtypes with distinct clinical outcomes. doi: 10.1038/s41467-025-66546-6

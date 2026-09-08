---
# --- identity ------------------------------------------------
id: 2021-01-01_ueda-2021-faseb-bioadvances-kdm4b-promot
id_basis: filename-year
source: Ueda(2021) FASEB BioAdvances; KDM4B promotes acute myeloid leukemia associated with AML1‐ETO by regulating chromatin accessibility.pdf
sha256: e7d761998eb29577c7a8c1c33de2b9208a882a5e2aa2c01ceb80289dbcd9be04
size_bytes: 1830593
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 64290

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1096/fba.2021-00030"
year: 2021
title: "KDM4B promotes acute myeloid leukemia associated with AML1‐ETO by regulating chromatin accessibility"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Ueda(2021) FASEB Bioadv; KDM4B promotes acute myeloid leukemia associated with AML1-ETO by regulating chromatin accessibility.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

KDM4B, a JmjC-domain histone demethylase, is found elevated specifically in t(8;21) AML. shRNA silencing reduced proliferation of t(8;21)-positive but not t(8;21)-negative lines, suppressed AML1-ETO-inducible gene expression, and perturbed chromatin accessibility at AML1-ETO binding sites with altered active enhancer marks. Transduction of murine KDM4B mutants showed that the double PHD or double Tudor methylated-histone binding modules, rather than catalytic function, support proliferation. Kdm4b conditional knockout mice showed attenuated AML1-ETO-mediated clonogenic potential and delayed leukemia progression in vivo.

## Summary

The domain-mapping result is the consequential one and cuts against the obvious therapeutic approach. KDM4B is a demethylase, so catalytic inhibition is what a drug programme would pursue - but the double PHD and double Tudor reader modules, not the catalytic activity, are what the leukemia needs. The authors' interpretation is that these modules act as scaffolds recruiting other chromatin components, which would make KDM4B a platform rather than an enzyme in this context.

The selectivity is well supported: KDM4B silencing does not affect t(8;21)-negative U937 and KG-1a cells, and chromatin accessibility at AML1-ETO binding sites is more dependent on KDM4B than accessibility at native AML1 sites - so the requirement tracks the fusion rather than the wild-type factor.

## Key points

- KDM4B is specifically elevated in t(8;21) AML and required for proliferation only in t(8;21)-positive lines.
- The double PHD and double Tudor reader modules, not the catalytic demethylase activity, support proliferation - against the obvious drug strategy.
- Chromatin accessibility at AML1-ETO binding sites depends on KDM4B more than accessibility at native AML1 sites.
- Kdm4b conditional knockout reduces AML1-ETO clonogenic potential and delays leukemia in vivo.
- AML1-ETO binding consensus sequences are present at the KDM4B promoter, suggesting a feed-forward loop.

## Limitations

The authors state that how KDM4B silencing changes chromatin occupancy and enhancer modification to produce anti-leukemic effects requires further study, and that the mechanism of KDM4B upregulation in t(8;21) AML remains to be clarified - the AML1-ETO binding at its promoter is inferred from published ChIP-seq rather than tested. With the catalytic domain dispensable, no obvious druggable module remains, so the therapeutic implication is limited. Work rests on shRNA in two t(8;21) lines plus mouse genetics, without primary patient samples in the functional experiments. Published in a lower-profile journal with correspondingly limited scope.

## Provenance

Located in the published literature, dropped into `inbox/` as `Ueda(2021) FASEB Bioadv; KDM4B promotes acute myeloid leukemia associated with AML1-ETO by regulating chromatin accessibility.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1096/fba.2021-00030`; the prose sections were written here from the paper itself.

## Citation

Ueda et al. FASEB BioAdvances 2021. KDM4B promotes acute myeloid leukemia associated with AML1‐ETO by regulating chromatin accessibility. doi: 10.1096/fba.2021-00030

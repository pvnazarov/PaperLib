---
# --- identity ------------------------------------------------
id: 2024-01-01_chuwdhury-2024-briefings-in-bioinformati
id_basis: filename-year
source: Chuwdhury(2024) Briefings in Bioinformatics; ImmuneMirror A machine learning-based integrative pipeline and web server for neoantigen prediction.pdf
sha256: 80f5631face27698e26a9495cf29d63332bc188943bb1e45c6ee35c4c24a0c55
size_bytes: 1551495
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 62896

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1093/bib/bbae024"
year: 2024
title: "ImmuneMirror: A machine learning-based integrative pipeline and web server for neoantigen prediction"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2024_Chuwdhury_Brief_Bioinform_ImmuneMirror_A_machine_learning_based_integrat_PMID38343325.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

ImmuneMirror is an open-source pipeline and web server that wraps a balanced random forest for neoantigen prediction and prioritisation, trained on immunogenic neopeptides collected from 19 published studies (test AUC 0.87). Applied to WES and RNA-seq from 805 gastrointestinal tumours, it identifies an MSI-high colorectal subgroup with high mutation burden but low neoantigen load.

## Summary

The stated gap is that binding-affinity tools ignore variant expression, HLA presentation, peptide processing and the eventual T-cell response, so they misrank in practice. ImmuneMirror integrates these into one pipeline rather than leaving the user to assemble them.

The clinical observation is the more interesting half: among MSI-high colorectal cancers - a group where PD-1 blockade is approved but roughly half do not respond - the authors find patients with significantly lower neoantigen load for both MHC-I and MHC-II, offering a candidate explanation for non-response.

## Key points

- Trained and tested on experimentally validated neopeptides pooled from 19 published studies; test AUC 0.87.
- Applied at scale: 805 tumours across colorectal, oesophageal squamous and hepatocellular cancer.
- Identifies MSI-high patients with >10 mutations/Mbp yet low neoantigen load (MHC-I P < 0.0001, MHC-II P = 0.0008), a possible non-responder subgroup.
- Reports a specific actionable candidate: YMCNSSCMGV from TP53 G245V restricted by HLA-A02 in oesophageal squamous cell carcinoma.

## Limitations

The 19 pooled studies differ in assay and reporting, so the training label is heterogeneous in a way a single AUC hides. Comparison with OpenVax found 45% of neoantigens identified by only one of the two tools, which the authors read as showing the limits of current pipelines generally - including their own. The MSI-high subgroup is a retrospective association with no outcome data linking low predicted load to actual non-response.

## Provenance

Located in the published literature, dropped into `inbox/` as `2024_Chuwdhury_Brief_Bioinform_ImmuneMirror_A_machine_learning_based_integrat_PMID38343325.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1093/bib/bbae024`; the prose sections were written here from the paper itself.

## Citation

SarwarChuwdhury et al. Briefings in Bioinformatics 2024. ImmuneMirror: A machine learning-based integrative pipeline and web server for neoantigen prediction. doi: 10.1093/bib/bbae024

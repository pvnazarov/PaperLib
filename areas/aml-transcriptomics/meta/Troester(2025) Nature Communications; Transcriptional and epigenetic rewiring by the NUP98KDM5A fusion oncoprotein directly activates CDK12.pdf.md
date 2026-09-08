---
# --- identity ------------------------------------------------
id: 2025-01-01_troester-2025-nature-communications-tran
id_basis: filename-year
source: Troester(2025) Nature Communications; Transcriptional and epigenetic rewiring by the NUP98KDM5A fusion oncoprotein directly activates CDK12.pdf
sha256: 84be621d9c4dc57d0ee1a1ae494dacfd6e0be0f1bec552736cae7051101f3d45
size_bytes: 6089583
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 332693

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-025-59930-9"
year: 2025
title: "Transcriptional and epigenetic rewiring by the NUP98::KDM5A fusion oncoprotein directly activates CDK12"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Troester(2025) Nat Commun; Transcriptional and epigenetic rewiring by the NUP98 KDM5A fusion oncoprotein directly activates CDK12.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

NUP98 fusion-expressing AML carries an epigenetic signature of increased accessibility at hematopoietic stem cell genes and enrichment of activating histone marks. Using an AML model for ligand-induced degradation of NUP98::KDM5A with CUT&Tag and nascent RNA-seq, the authors identify directly regulated epigenetic programmes and transcriptional targets; orthogonal genome-wide CRISPR screening narrows these to 12 direct target genes essential for AML growth. Among them CDK12 is validated as a druggable vulnerability - consistent with its role in transcribing DNA damage repair genes, small-molecule CDK12 inactivation increases DNA damage and kills NUP98::KDM5A AML cells.

## Summary

The filtering strategy is what makes the result usable. Degradation plus nascent transcription identifies genes the fusion directly regulates; a CRISPR screen identifies genes the cells need; intersecting the two leaves 12 candidates that are both direct targets and essential - which is a far stronger basis for picking a therapeutic target than either approach alone.

CDK12 is a good outcome because it is druggable, unlike most transcriptional targets, and because the mechanism is coherent: CDK12 transcribes DNA damage repair genes, so inhibiting it leaves cells unable to handle damage. The clinical motivation is specific to pediatric AML, where the mutational burden is low and the targeted therapies approved for adults are largely inapplicable.

## Key points

- NUP98 fusion AML shows increased accessibility at hematopoietic stem cell genes with enriched activating histone marks.
- Ligand-induced degradation with nascent RNA-seq separates direct targets from downstream consequences.
- Intersecting direct targets with a genome-wide CRISPR screen leaves 12 genes that are both directly regulated and essential.
- CDK12 is validated as a druggable vulnerability; its inhibition raises DNA damage and kills the cells.
- Addresses pediatric AML, where low mutational burden makes adult-derived targeted therapies largely unsuitable.

## Limitations

The models are murine fetal liver cells retrovirally co-transduced with NUP98::KDM5A and NrasG12D, so the fusion is overexpressed alongside an engineered cooperating oncogene rather than arising endogenously - and the degron tag requires further engineering. Human AML cell lines are used for comparison but not, in the summary evidence, for the degradation experiments. CDK12 inhibitors available are not fully selective, typically also hitting CDK13, and CDK12 is required for DNA damage repair transcription in normal cells, so the therapeutic window is not established. No in vivo treatment experiment with a CDK12 inhibitor is described. Twelve essential direct targets is a small set derived from one fusion, and generalisation across the 30-plus NUP98 partners is assumed.

## Provenance

Located in the published literature, dropped into `inbox/` as `Troester(2025) Nat Commun; Transcriptional and epigenetic rewiring by the NUP98 KDM5A fusion oncoprotein directly activates CDK12.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-025-59930-9`; the prose sections were written here from the paper itself.

## Citation

Troester et al. Nature Communications 2025. Transcriptional and epigenetic rewiring by the NUP98::KDM5A fusion oncoprotein directly activates CDK12. doi: 10.1038/s41467-025-59930-9

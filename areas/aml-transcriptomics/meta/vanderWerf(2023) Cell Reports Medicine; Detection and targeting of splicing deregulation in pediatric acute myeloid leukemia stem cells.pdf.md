---
# --- identity ------------------------------------------------
id: 2023-01-01_vanderwerf-2023-cell-reports-medicine-de
id_basis: filename-year
source: vanderWerf(2023) Cell Reports Medicine; Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells.pdf
sha256: 1d14a8775232542e9a21dbde4cee00cc8e299cec3b40dd4b4666b865548697d8
size_bytes: 4592129
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 204837

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.xcrm.2023.100962"
year: 2023
title: "Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as vanderWerf(2023) Cell Rep Med; Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Pediatric AML has high relapse rates and few somatic mutations, and splicing deregulation had not been studied there. Using single-cell proteogenomics, transcriptome-wide analysis of FACS-purified hematopoietic stem and progenitor cells with differential splicing analysis, dual-fluorescence lentiviral splicing reporter assays and humanized mouse models, the authors found transcriptomic splicing deregulation typified by differential exon usage, downregulation of the splicing regulator RBFOX2, and upregulation of a CD47 splice isoform. The splicing modulator Rebecsinib produced a therapeutic vulnerability in survival, self-renewal and splicing reporter assays.

## Summary

Extends to children a principle established in adults - that splicing deregulation drives therapy-resistant leukemia stem cells even without splicing factor mutations - and the reasoning for expecting it is sound: pediatric AML has few somatic mutations because children lack the DNA-damaging exposures and age-related clonal hematopoiesis that adults accumulate, so post-transcriptional mechanisms should carry proportionally more weight.

The study finds pediatric AML differs from adult disease rather than replicating it, which argues against extrapolating adult findings. RBFOX2 downregulation and CD47 isoform upregulation are the specific lesions, and CD47 is notable as the 'don't eat me' signal targeted by macrophage-directed immunotherapy - an isoform change there has immunological implications. Rebecsinib was previously shown to sensitise adult LSCs, so the therapeutic arm builds on established groundwork.

## Key points

- Pediatric AML's low mutational burden makes post-transcriptional mechanisms proportionally more important as drivers.
- Splicing deregulation is present in pediatric AML stem cells despite the near-absence of splicing factor mutations.
- RBFOX2 is downregulated and a CD47 splice isoform upregulated - the latter relevant to macrophage-directed immunotherapy.
- Pediatric AML splicing differs fundamentally from adult disease, arguing against extrapolating adult findings.
- The splicing modulator Rebecsinib creates a therapeutic vulnerability in survival, self-renewal and reporter assays.

## Limitations

The authors set out their own constraints: the paucity of samples for this rare disease and the study of rare stem cell populations made RNA-sequencing-based splicing analysis difficult; interpatient variability and cell-type-specific responses to splicing modulation are substantial; and a non-coding SF3B1 splicing mutation found in two patients has unclear clinical significance. They state that serial LSC transplantation with Rebecsinib, ADAR1 reporter studies linking splicing deregulation to RNA editing, and biomarkers of drug response all remain for future work - so durable in vivo efficacy and patient selection are unestablished. Splicing modulators inhibit an essential process, and the therapeutic window is not characterised here.

## Provenance

Located in the published literature, dropped into `inbox/` as `vanderWerf(2023) Cell Rep Med; Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.xcrm.2023.100962`; the prose sections were written here from the paper itself.

## Citation

vanderWerf et al. Cell Reports Medicine 2023. Detection and targeting of splicing deregulation in pediatric acute myeloid leukemia stem cells. doi: 10.1016/j.xcrm.2023.100962

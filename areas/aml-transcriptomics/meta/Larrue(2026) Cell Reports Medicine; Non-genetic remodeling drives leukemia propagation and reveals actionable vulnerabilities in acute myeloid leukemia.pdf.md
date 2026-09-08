---
# --- identity ------------------------------------------------
id: 2026-01-01_larrue-2026-cell-reports-medicine-non-ge
id_basis: filename-year
source: Larrue(2026) Cell Reports Medicine; Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia.pdf
sha256: 9c61f86e527ac933448344e539297d11fe3aa999befc69e593aaf6f12b0b3ae2
size_bytes: 6489907
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 138152

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.xcrm.2026.103017"
year: 2026
title: "Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Larrue(2026) Cell Rep Med; Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Serial patient-derived xenotransplantation establishes a longitudinal model in which leukemia-initiating capacity progressively increases. Integrated single-cell transcriptomics and multi-omics reveal a predominantly non-genetic trajectory following a conserved pattern across models, with coordinated changes across epigenetic, transcriptional and proteomic layers; ribosome profiling and rRNA 2'-O-methylation analysis show a stage-specific increase in translational activity with ribosome remodeling in advanced xenografts. A screen of 3247 compounds uncovers a limited set of vulnerabilities emerging during progression, including CRBN-dependent degradation of GSPT1 (CC-885) and IAP antagonism (AZD5582), both of which reduce burden, impair propagation and enhance cytarabine activity in vivo.

## Summary

Serial transplantation is used as a controlled model of disease evolution, and the key observation is that leukemia-initiating capacity rises without new genetic drivers - the trajectory is non-genetic and follows a conserved pattern across models, coordinated across chromatin, transcriptome and proteome.

The distinctive layer is translational. Ribosome profiling plus rRNA 2'-O-methylation mapping shows not just more translation but a remodelled ribosome, with specific methylation sites tracking translational output - a level of regulation almost never measured in AML. That the drug screen independently converges on translation-directed compounds (GSPT1 degradation, anisomycin) is a satisfying internal consistency, since the vulnerability was found by phenotype and the mechanism by molecular profiling.

## Key points

- Serial xenotransplantation gives a longitudinal model in which leukemia-initiating capacity progressively increases.
- The trajectory is predominantly non-genetic, conserved across models, and coordinated across epigenetic, transcriptional and proteomic layers.
- Advanced xenografts show increased translational activity with remodelling of specific rRNA 2'-O-methylation sites.
- A 3247-compound screen converges on a restricted set of vulnerabilities, notably GSPT1 degradation (CC-885) and IAP antagonism (AZD5582).
- Both agents reduce leukemic burden, impair propagation and enhance cytarabine activity in PDX models.

## Limitations

The authors state their own limits directly and unusually clearly. The therapeutic window of the identified vulnerabilities cannot be defined from this study: the framework was built to find dependencies, not to evaluate compounds preclinically, so the toxicity observations are preliminary and proper safety and selectivity assessment lies beyond its scope. GSPT1 degraders in particular are broadly cytotoxic, and the translation machinery is essential in normal cells. They also note that the xenograft assay reports whether cells can reinitiate disease but not which cells are responsible or how they change, and that resolving this needs longitudinal patient samples rather than serial mouse passage. Serial transplantation itself imposes selection that need not correspond to disease evolution in a patient. Nine matched trios, selected for prior engraftment capacity, is a small and non-representative sample.

## Provenance

Located in the published literature, dropped into `inbox/` as `Larrue(2026) Cell Rep Med; Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.xcrm.2026.103017`; the prose sections were written here from the paper itself.

## Citation

Larrue et al. Cell Reports Medicine 2026. Non-genetic remodeling drives leukemia propagation and reveals actionable vulnerabilities in acute myeloid leukemia. doi: 10.1016/j.xcrm.2026.103017

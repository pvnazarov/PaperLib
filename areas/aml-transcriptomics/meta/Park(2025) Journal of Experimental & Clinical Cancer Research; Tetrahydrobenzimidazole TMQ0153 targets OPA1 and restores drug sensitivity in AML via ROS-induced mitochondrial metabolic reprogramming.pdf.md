---
# --- identity ------------------------------------------------
id: 2025-01-01_park-2025-journal-of-experimental-clinic
id_basis: filename-year
source: Park(2025) Journal of Experimental & Clinical Cancer Research; Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming.pdf
sha256: ed6e62c08a12b3fc75dd29e3c2cadfeb7e880db588ccbb5a2d64101070cc2889
size_bytes: 10564829
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 137684

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1186/s13046-025-03372-0"
year: 2025
title: "Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Park(2025) J Exp Clin Cancer Res; Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

OPA1, the mitochondrial fusion protein, is upregulated in AML with adverse mutations and correlates with poor prognosis. The tetrahydrobenzimidazole derivative TMQ0153 reduced OPA1 and mitofusin-2 levels and disrupted mitochondrial morphology and function, increasing reactive oxygen species, inhibiting oxidative phosphorylation, depolarising the membrane potential and inducing caspase-dependent apoptosis. Metabolic profiling showed a shift from mitochondrial respiration to glycolysis with impaired respiratory chain activity and altered GSH/GSSG and NAD+/NADH ratios. TMQ0153 reduced tumour volume and weight in MV4-11 xenografts, and combinations with other AML drugs reduced leukemic burden and prolonged survival in NSG mice xenografted with U937 and MOLM-14 cells.

## Summary

Targets mitochondrial dynamics rather than mitochondrial metabolism directly - the shape and connectivity of the network rather than the enzymes running in it - on the observation that the fusion protein OPA1 is elevated in adverse-risk AML. Disrupting fusion fragments the network, and the metabolic consequences follow: ROS up, oxidative phosphorylation down, membrane potential lost, apoptosis.

It sits alongside the several other papers here arguing that AML depends on oxidative metabolism, and reaches the same vulnerability from a structural direction. The metabolic profiling with paired redox ratios is a more complete characterisation than most such studies attempt, and the combination experiments in two xenograft models with survival endpoints are the appropriate test of the resensitisation claim.

## Key points

- Targets mitochondrial dynamics via OPA1, rather than metabolic enzymes, in AML with adverse mutations where OPA1 is elevated.
- TMQ0153 lowers OPA1 and MFN2, disrupts mitochondrial morphology, raises ROS and inhibits oxidative phosphorylation.
- Cells shift from respiration to glycolysis, with altered GSH/GSSG and NAD+/NADH redox ratios.
- Single-agent activity in MV4-11 xenografts; combinations reduced burden and prolonged survival in two further xenograft models.
- Frames mitochondrial dynamics as a route to overcoming drug resistance in monocytic AML.

## Limitations

TMQ0153 is an early-stage compound with no clinical data, and the mechanism of OPA1 and MFN2 reduction is not established - whether the molecule binds OPA1 directly or lowers it indirectly matters for calling it an OPA1 inhibitor, and ROS induction is a common non-specific consequence of mitochondrial stress. OPA1 is essential for mitochondrial function in normal tissue, particularly in heart and optic nerve, where OPA1 mutations cause dominant optic atrophy - so on-target toxicity is a real concern not addressed by short mouse experiments. Efficacy rests on cell-line xenografts (MV4-11, U937, MOLM-14) with no primary patient-derived model. The prognostic association of OPA1 expression is correlative in public data. Combination benefit is reported without formal synergy analysis in the summary evidence.

## Provenance

Located in the published literature, dropped into `inbox/` as `Park(2025) J Exp Clin Cancer Res; Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1186/s13046-025-03372-0`; the prose sections were written here from the paper itself.

## Citation

JungPark et al. Journal of Experimental &amp; Clinical Cancer Research 2025. Tetrahydrobenzimidazole TMQ0153 targets OPA1 and restores drug sensitivity in AML via ROS-induced mitochondrial metabolic reprogramming. doi: 10.1186/s13046-025-03372-0

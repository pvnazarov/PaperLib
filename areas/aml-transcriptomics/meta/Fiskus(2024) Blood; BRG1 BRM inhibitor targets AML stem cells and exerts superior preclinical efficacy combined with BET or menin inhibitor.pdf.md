---
# --- identity ------------------------------------------------
id: 2024-01-01_fiskus-2024-blood-brg1-brm-inhibitor-tar
id_basis: filename-year
source: Fiskus(2024) Blood; BRG1 BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor.pdf
sha256: 9bfc4f4ea1af82bf16fd3d38e754218e0551d55d5ce028ef2d5a47c3cf347f43
size_bytes: 3615921
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 192814

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2023022832"
year: 2024
title: "BRG1/BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Fiskus(2024) Blood; BRG1 BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

FHD-286, an orally bioavailable selective inhibitor of the mutually exclusive BAF complex ATPases BRG1 (SMARCA4) and BRM (SMARCA2), is shown to induce differentiation and lethality in AML cells with MLL1 rearrangement or mutant NPM1, perturbing chromatin accessibility and repressing c-Myc, PU.1 and CDK4/6. Cotreatment with decitabine, a BET inhibitor, a menin inhibitor or venetoclax was synergistically lethal in vitro. In patient-derived xenografts, FHD-286 reduced AML burden, improved survival and attenuated the leukemia-initiating potential of stem-progenitor cells, and each combination significantly outperformed the single agents without significant toxicity.

## Summary

Aimed at a problem created by the success of menin inhibitors: most patients either fail to respond or relapse, some with menin mutations, so a mechanistically distinct partner is needed. Inhibiting the BAF ATPases attacks the same transcriptional dependency from a different angle - by closing the chromatin that the relevant transcription factors need to access - and repression of c-Myc and PU.1 is the shared downstream node.

The combination breadth is the practical contribution: FHD-286 with decitabine, BET inhibitor, menin inhibitor or venetoclax, each synergistic, each tested in patient-derived xenografts with survival and stem-progenitor readouts rather than viability alone. FHD-286 is in clinical development, so this is a rationale for combinations that could actually be run.

## Key points

- FHD-286 inhibits both BAF core ATPases (BRG1/SMARCA4 and BRM/SMARCA2) and is orally bioavailable and in clinical development.
- It induces differentiation and death in MLL1-rearranged and NPM1-mutant AML, repressing c-Myc, PU.1 and CDK4/6 with reduced chromatin accessibility.
- Targets AML stem/progenitor cells, reducing leukemia-initiating potential in xenografts.
- Synergises with decitabine, BET inhibitor, menin inhibitor and venetoclax in vitro and in PDX models.
- Addresses the clinical problem that most menin-inhibitor responses are incomplete or followed by relapse, sometimes with menin mutations.

## Limitations

Entirely preclinical. BRG1 and BRM are core chromatin remodellers required in normal tissue, and 'without inducing significant toxicity' rests on mouse tolerability over short experiments, which is a weak basis for a dual-ATPase inhibitor combined with four different agents. The stem-cell effect was inconsistent - phenotypically defined stem cell frequency fell in MLL1-rearranged samples but not in the mutant NPM1 sample - which undercuts the general stem-cell claim, and 'stem cells' here are a surface-marker phenotype rather than functionally defined by transplantation. Synergy is asserted from combination assays. Four authors are employees of Foghorn Therapeutics, which develops FHD-286, and the paper is effectively that company's preclinical combination package.

## Provenance

Located in the published literature, dropped into `inbox/` as `Fiskus(2024) Blood; BRG1 BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2023022832`; the prose sections were written here from the paper itself.

## Citation

Fiskus et al. Blood 2024. BRG1/BRM inhibitor targets AML stem cells and exerts superior preclinical efficacy combined with BET or menin inhibitor. doi: 10.1182/blood.2023022832

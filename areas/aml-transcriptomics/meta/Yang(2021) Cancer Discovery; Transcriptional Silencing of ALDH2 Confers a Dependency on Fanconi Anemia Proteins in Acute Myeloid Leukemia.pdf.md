---
# --- identity ------------------------------------------------
id: 2021-01-01_yang-2021-cancer-discovery-transcription
id_basis: filename-year
source: Yang(2021) Cancer Discovery; Transcriptional Silencing of ALDH2 Confers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia.pdf
sha256: 2d9c416202b2907696ee298e3ff2fec2bb77b5819809ed2a2cff7717b0b014d9
size_bytes: 6773963
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 224200

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1158/2159-8290.CD-20-1542"
year: 2021
title: "Transcriptional Silencing of ALDH2 Confers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Yang(2021) Cancer Discov; Transcriptional Silencing ofConfers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Domain-focused CRISPR screening of the ubiquitination machinery across cancer cell lines revealed the Fanconi anemia proteins UBE2T and FANCL as unique dependencies in AML. These dependencies arise from a synthetic lethal interaction between FA proteins and aldehyde dehydrogenase 2 (ALDH2), which function in parallel pathways counteracting the genotoxicity of endogenous aldehydes. DNA hypermethylation and silencing of ALDH2 occurs recurrently in human AML and is sufficient to confer FA pathway dependency, suggesting that targeting the ubiquitination reaction catalysed by FA proteins could eliminate ALDH2-deficient AML.

## Summary

Demonstrates a general principle with a clean example: epigenetic silencing can create a targetable dependency by disabling genetic redundancy. Hundreds of genes are aberrantly silenced in AML with unknown consequence, and this shows how one of them - ALDH2, silenced by hypermethylation - removes a parallel pathway and leaves the cell dependent on the Fanconi anemia machinery to handle endogenous aldehydes.

The authors are unusually forthright about what they cannot explain. Why ALDH2 is recurrently silenced is left open with three explicitly competing hypotheses: positive selection for a metabolic adaptation during early clonal expansion that no longer matters later; promotion of genetic evolution through aldehyde-induced mutation; or simply a passenger event at a methylation-susceptible locus. They also name the paradox their result creates - germline FA deficiency raises AML risk, yet FA proteins are what ALDH2-silenced AML depends on.

## Key points

- Epigenetic silencing creates a targetable dependency by disabling genetic redundancy - a general principle shown concretely.
- UBE2T and FANCL are AML-selective dependencies, synthetic lethal with ALDH2 loss.
- ALDH2 and the FA pathway act in parallel to counteract endogenous aldehyde genotoxicity.
- ALDH2 hypermethylation and silencing is recurrent in human AML and sufficient to confer the dependency.
- Why ALDH2 is silenced remains open, with three competing hypotheses set out by the authors.

## Limitations

The authors note the paradox that germline FA gene deficiency elevates AML risk, which complicates targeting the same pathway therapeutically - inhibiting FA proteins systemically would mimic a cancer-predisposing state. No FA pathway inhibitor exists, so the strategy rests on genetic evidence. Their observation that the ALDH2 locus is occupied by C/EBPalpha and AML1-ETO is reported as data not shown. Screening and validation are in cell lines, and the authors note that ALDH2 loss has no measurable fitness impact in those lines because FA proteins compensate - so the models may not capture why silencing occurred in the first place. Patient relevance rests on the recurrence of ALDH2 hypermethylation rather than on treated samples.

## Provenance

Located in the published literature, dropped into `inbox/` as `Yang(2021) Cancer Discov; Transcriptional Silencing ofConfers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1158/2159-8290.CD-20-1542`; the prose sections were written here from the paper itself.

## Citation

Yang et al. Cancer Discovery 2021. Transcriptional Silencing of
                    <i>ALDH2</i>
                    Confers a Dependency on Fanconi Anemia Proteins in Acute Myeloid Leukemia. doi: 10.1158/2159-8290.CD-20-1542

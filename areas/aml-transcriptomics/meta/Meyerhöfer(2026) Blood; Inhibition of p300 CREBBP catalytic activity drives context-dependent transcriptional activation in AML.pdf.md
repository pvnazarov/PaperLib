---
# --- identity ------------------------------------------------
id: 2026-01-01_meyerh-fer-2026-blood-inhibition-of-p300
id_basis: filename-year
source: Meyerhöfer(2026) Blood; Inhibition of p300 CREBBP catalytic activity drives context-dependent transcriptional activation in AML.pdf
sha256: 31d376d548a4c7ffcd68b59894069afbd8926bdfe1855088900be431d85d7d3a
size_bytes: 6487843
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 388641

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1182/blood.2025031924"
year: 2026
title: "Inhibition of p300/CREBBP catalytic activity drives context-dependent transcriptional activation in AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Meyerhöfer(2026) Blood; Inhibition of p300 CREBBP catalytic activity drives context-dependent transcriptional activation in AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

The acetyltransferase activity of p300/CREBBP has traditionally been linked to transcriptional activation via marks such as H3K27ac. Here, in AML, inhibiting p300/CREBBP catalysis paradoxically increases transcription at a subset of loci. Combining time-resolved nascent and total transcription with chromatin binding dynamics, chromatin pull-down and acetyl proteomics, motif enrichment, and genome-wide CRISPR dropout plus focused Perturb-seq screens, the authors show that catalytic inhibition traps p300/CREBBP at select regulatory elements, promoting cooperative transcription factor assembly and increased H3K27 acetylation. The effect is most pronounced at IRF motif-enriched loci, where it facilitates STAT1 recruitment and interferon-stimulated gene transcription, and combines synergistically with interferon-alpha.

## Summary

A genuinely counterintuitive result: inhibiting an acetyltransferase increases acetylation and transcription at particular sites. The explanation is that catalytic inhibition traps the enzyme on chromatin rather than removing it, and the trapped protein serves as a platform for cooperative transcription factor assembly - so the drug converts a catalytic activity into a scaffolding one.

The consequence is specific and exploitable. At IRF motif-enriched loci this drives STAT1 recruitment and interferon-stimulated gene expression, which the authors combine with interferon-alpha to synergistic effect in vivo. Distinguishing a catalytic inhibitor's behaviour from a degrader's is the right experimental control here, and using both is what separates trapping from loss of function - a distinction that matters for every chromatin enzyme now being targeted with inhibitors rather than degraders.

## Key points

- Inhibiting p300/CREBBP catalysis paradoxically increases transcription and H3K27 acetylation at a subset of regulatory elements.
- The mechanism is enzyme trapping: catalytic inhibition retains p300/CREBBP on chromatin, promoting cooperative transcription factor assembly.
- Matched inhibitors and a reference degrader are used to separate trapping from simple loss of function.
- The effect concentrates at IRF motif-enriched loci, facilitating STAT1 recruitment and interferon-stimulated gene transcription.
- Combining catalytic inhibition with interferon-alpha is synergistic and improves survival in AML mouse models.

## Limitations

The effect is context-dependent by the paper's own framing, so which loci respond and in which AML genotypes is not fully mapped - the IRF-enriched subset is characterised, the rest is not. Inducing interferon signalling in AML is double-edged: chronic interferon exposure impairs normal hematopoietic stem cells and drives inflammation, and the therapeutic window for the combination is not established beyond short mouse experiments. In vivo work uses MOLM-13 xenografts and an Npm1c/Flt3-ITD model, and the survival benefits shown are modest extensions rather than cures. p300/CREBBP are broadly required coactivators, so both inhibitor and degrader approaches carry substantial on-target toxicity concerns not addressed here. The trapping mechanism is inferred from chromatin binding dynamics rather than from a structural demonstration.

## Provenance

Located in the published literature, dropped into `inbox/` as `Meyerhöfer(2026) Blood; Inhibition of p300 CREBBP catalytic activity drives context-dependent transcriptional activation in AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1182/blood.2025031924`; the prose sections were written here from the paper itself.

## Citation

Meyerhöfer et al. Blood 2026. Inhibition of p300/CREBBP catalytic activity drives context-dependent transcriptional activation in AML. doi: 10.1182/blood.2025031924

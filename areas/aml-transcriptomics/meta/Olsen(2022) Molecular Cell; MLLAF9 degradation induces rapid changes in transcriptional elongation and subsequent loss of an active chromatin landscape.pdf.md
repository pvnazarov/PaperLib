---
# --- identity ------------------------------------------------
id: 2022-01-01_olsen-2022-molecular-cell-mllaf9-degrada
id_basis: filename-year
source: Olsen(2022) Molecular Cell; MLLAF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape.pdf
sha256: 77e2a455309a53c4a3dcb65335240fd2e72d43426e5f703868408adc278b50e5
size_bytes: 4196977
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 346806

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.molcel.2022.02.013"
year: 2022
title: "MLL::AF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Olsen(2022) Mol Cell; MLL AF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Using degradable MLL::AF9 models in which small molecules induce rapid degradation, the authors identify a core subset of target genes where degradation changes transcriptional elongation within 15 minutes, followed subsequently by loss of an active chromatin landscape. They use this ordering to assess small molecules targeting members of the MLL::AF9 complex: combined DOT1L and MENIN inhibition resembles MLL::AF9 degradation, whereas single-agent treatment has more modest effects on occupancy and gene expression. Combined inhibition releases the oncoprotein from chromatin globally.

## Summary

Establishes the order of events, which matters because chromatin and transcription are usually measured together and their causal sequence assumed. Degradation acting in minutes shows elongation changes first and chromatin changes after - so the active chromatin landscape at these loci is a consequence of transcription, not its cause.

The practical use is as a benchmark. Having defined what complete loss of the oncoprotein looks like, the authors can ask how close existing drugs come, and the answer is that single agents fall well short while DOT1L plus MENIN inhibition approximates it - with apoptosis in 2-3 days, against the much slower kinetics reported for either alone. Their inference is pointed: because single agents fail to phenocopy degradation, the incomplete and non-durable clinical responses to these drugs may reflect insufficient destabilisation of the complex rather than a wrong target.

## Key points

- Targeted degradation resolves the sequence: transcriptional elongation changes within 15 minutes, loss of active chromatin follows.
- Degradation provides a benchmark for what complete oncoprotein loss looks like, against which drugs can be measured.
- Combined DOT1L and MENIN inhibition approximates degradation; either alone has modest effects on occupancy and expression.
- The combination releases MLL::AF9 from chromatin globally and induces apoptosis in 2-3 days.
- Suggests that the non-durable clinical responses to DOT1L and MENIN inhibitors reflect incomplete complex destabilisation.

## Limitations

The authors state their principal limitation: the models use retroviral overexpression to define the MLL::AF9 transcriptional program, and both systems retain two wild-type MLL1 copies that could compensate on degradation - so the program measured may differ from that of an endogenous fusion at native expression. Degron systems require engineering the target, so this is not a study of patient cells or of any clinically usable degrader. The DOT1L/MENIN combination is supported in vitro; combining two chromatin-targeting agents raises toxicity concerns that these experiments do not address, and DOT1L inhibitors have separately underperformed clinically. Cell-line based throughout, with no primary sample or in vivo validation of the combination in this work.

## Provenance

Located in the published literature, dropped into `inbox/` as `Olsen(2022) Mol Cell; MLL AF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.molcel.2022.02.013`; the prose sections were written here from the paper itself.

## Citation

NaomiOlsen et al. Molecular Cell 2022. MLL::AF9 degradation induces rapid changes in transcriptional elongation and subsequent loss of an active chromatin landscape. doi: 10.1016/j.molcel.2022.02.013

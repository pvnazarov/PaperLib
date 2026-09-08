---
# --- identity ------------------------------------------------
id: 2021-01-01_stengel-2021-molecular-cell-definition-o
id_basis: filename-year
source: Stengel(2021) Molecular Cell; Definition of a small core transcriptional circuit regulated by AML1-ETO.pdf
sha256: ceded6512e459271937eafe690b9dec9f093a38de0eba5fa0c37b04585965903
size_bytes: 6402314
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 105576

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.molcel.2020.12.005"
year: 2021
title: "Definition of a small core transcriptional circuit regulated by AML1-ETO"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Stengel(2021) Mol Cell; Definition of a small core transcriptional circuit regulated by AML1-ETO.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Cell models were devised in which the AML1-ETO protein is rapidly degraded on addition of a small molecule. Combining that rapid kinetics with nascent transcript analysis by PRO-seq and genome-wide AML1-ETO binding by CUT&RUN identified the direct gene targets constituting a core AML1-ETO regulatory network, distinguishing them from secondary and compensatory changes. Derepression of this network was associated with RUNX1 DNA binding and triggered a transcriptional cascade ending in myeloid differentiation. GFI1B was reactivated on degradation in differentiating pre-leukemic CD34+ cultures but not in the t(8;21) cell line, where it is marked by H3K27me3.

## Summary

Makes a methodological point that applies across this literature: DNA binding is a poor predictor of regulatory activity, and existing datasets nominate far more binding sites than any single factor could plausibly regulate. Rapid degradation plus nascent transcription measurement separates the small set of genes the factor actually controls from the large set it merely sits near - and the authors report directly that most binding sites cannot be assigned a function.

The GFI1B result is the therapeutically interesting one. It is reactivated on AML1-ETO degradation in pre-leukemic CD34+ cells but not in Kasumi-1, where the locus carries H3K27me3 - so the leukemic cell has locked the gene closed by a mechanism beyond the fusion protein. Since GFI1 and GFI1B are the critical targets of LSD1 inhibition, that observation suggests a rational combination, and the paper follows it with LSD1 inhibitor plus degrader experiments.

## Key points

- Rapid degradation plus PRO-seq separates direct targets from secondary and compensatory transcriptional changes.
- Most AML1-ETO DNA binding sites cannot be assigned a transcriptional function - binding is a poor predictor of regulation.
- A small core regulatory circuit is defined, whose derepression involves RUNX1 binding and culminates in myeloid differentiation.
- GFI1B is reactivated on degradation in pre-leukemic CD34+ cells but silenced by H3K27me3 in the t(8;21) cell line.
- That difference motivates combining LSD1 inhibition, which acts through GFI1/GFI1B, with fusion protein removal.

## Limitations

The degron approach requires engineering an FKBP tag onto the fusion protein, so all work is in modified cell lines and transduced CD34+ cells rather than in patient blasts, and the CD34+ system expresses AML1-ETO ectopically rather than from a translocation. The core circuit is defined in one cell line, Kasumi-1, plus one pre-leukemic model, and the difference between them at GFI1B shows how much the result depends on cellular context. No in vivo work is reported. The LSD1 combination is supported by transcriptional and marker readouts in vitro, and LSD1 inhibitors have underperformed clinically. The authors note discrepancies with earlier studies explained by differences in experimental kinetics, which is a reminder that the target list depends on when you look.

## Provenance

Located in the published literature, dropped into `inbox/` as `Stengel(2021) Mol Cell; Definition of a small core transcriptional circuit regulated by AML1-ETO.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.molcel.2020.12.005`; the prose sections were written here from the paper itself.

## Citation

Stengel et al. Molecular Cell 2021. Definition of a small core transcriptional circuit regulated by AML1-ETO. doi: 10.1016/j.molcel.2020.12.005

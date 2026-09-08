---
# --- identity ------------------------------------------------
id: 2025-01-01_shi-2025-nature-communications-guanine-n
id_basis: filename-year
source: Shi(2025) Nature Communications; Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition.pdf
sha256: 43b5540d9afc205e179b58e6fd32d4d2fbc080e502dc87b81372d19cba8f5bd1
size_bytes: 5508776
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 361935

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-025-57544-9"
year: 2025
title: "Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Shi(2025) Nat Commun; Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Leukemia stem cells of MLL-rearranged AML show enhanced guanine nucleotide biosynthesis, and inhibiting it causes myeloid differentiation and sensitises cells to menin inhibitors. Targeting IMPDH2 reduces guanine nucleotides and rRNA transcription, lowering LEDGF and menin protein levels; consequently the MLL-fusion complex forms and binds chromatin less well, reducing MLL target gene expression. Inhibiting guanine nucleotide biosynthesis or rRNA transcription further suppresses MLL-rearranged AML when combined with a menin inhibitor.

## Summary

A metabolic route to a chromatin problem. Menin inhibitor resistance develops rapidly, so combinations are needed, and the mechanism proposed here is indirect but coherent: guanine nucleotides feed rRNA transcription, rRNA transcription supports translation of LEDGF and menin, and without enough of those proteins the MLL-fusion complex cannot assemble or hold chromatin. So a metabolic inhibitor destabilises the same complex the menin inhibitor blocks, from a different direction.

The translational appeal is that mycophenolate mofetil, an IMPDH inhibitor, has been used clinically as an immunosuppressant for nearly thirty years with an established safety profile - repurposing is far cheaper than developing. The authors also note the odd symmetry that both inhibiting and, in a separate report, supplying guanosine induce myeloid differentiation, suggesting the pathway needs to sit within a narrow range.

## Key points

- MLL-rearranged AML leukemia stem cells show enhanced guanine nucleotide biosynthesis, which sustains the MLL-fusion complex.
- IMPDH2 inhibition lowers guanine nucleotides and rRNA transcription, reducing LEDGF and menin protein and impairing complex formation.
- Reduced fusion complex binding is accompanied by increased myeloid transcription factor binding and differentiation.
- Combining guanine nucleotide or rRNA transcription inhibition with a menin inhibitor suppresses MLL-rearranged AML further.
- Mycophenolate mofetil, an established IMPDH inhibitor with a thirty-year clinical safety record, is the obvious repurposing candidate.

## Limitations

The authors name the central obstacle to their own proposal: neutropenia is a common side effect of mycophenolate mofetil, and that is precisely the toxicity that matters when treating a marrow malignancy with an already immunosuppressed patient at risk of infection. The mechanism is a long indirect chain - nucleotides to rRNA to protein levels to complex assembly - and each step is supported by correlated changes rather than by isolating the link. Work is in mouse models and cell lines with patient samples in xenografts, so the clinical genotype coverage is narrow. RNA polymerase I inhibitors, the second arm, are preclinical. Whether the therapeutic window separates leukemic from normal proliferating cells, which also need guanine nucleotides and rRNA, is not established.

## Provenance

Located in the published literature, dropped into `inbox/` as `Shi(2025) Nat Commun; Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-025-57544-9`; the prose sections were written here from the paper itself.

## Citation

Shi et al. Nature Communications 2025. Guanine nucleotide biosynthesis blockade impairs MLL complex formation and sensitizes leukemias to menin inhibition. doi: 10.1038/s41467-025-57544-9

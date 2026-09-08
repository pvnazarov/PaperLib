---
# --- identity ------------------------------------------------
id: 2021-01-01_issa-2021-leukemia-therapeutic-implicati
id_basis: filename-year
source: Issa(2021) Leukemia; Therapeutic implications of menin inhibition in acute leukemias.pdf
sha256: bd5fa19cb1495778425c2aada4bb398942b9c654c32147e900e63f2c9d93e519
size_bytes: 1098762
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 102209

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41375-021-01309-y"
year: 2021
title: "Therapeutic implications of menin inhibition in acute leukemias"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Issa(2021) Leukemia; Therapeutic implications of menin inhibition in acute leukemias.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of menin biology and menin inhibitors in acute leukemia. Menin acts as a tumour suppressor in endocrine glands - germline MEN1 mutations cause multiple endocrine neoplasia type 1 - yet is required for leukemogenesis in KMT2A-rearranged disease, an apparent contradiction explained by its several roles in gene regulation. The review covers the physiologic and malignant biology of menin, mechanisms in susceptible subsets including KMT2A rearrangement and mutant NPM1, HOX expression patterns as a potential response biomarker, other genotypes with similar transcriptional dependencies, and early clinical results with oral small-molecule menin inhibitors in relapsed acute leukemia.

## Summary

The conceptual map for the menin inhibitor story that the clinical trial results elsewhere in this collection later fill in. Its most useful contribution is the framing of susceptibility by transcriptional dependency rather than by genotype: the tabulated survey of lesions associated with HOXA/HOXB upregulation - NUP98 fusions, CALM-AF10, MN1-ETV6, EZH2, IDH1/2, ASXL1, CEBPA, trisomy 8 - defines a much larger candidate population than KMT2A rearrangement and NPM1 mutation alone.

The two forward-looking arguments both proved important. One is that HOX expression signature, not mutation, might be the right biomarker of response, since 75% of normal-karyotype AML expresses HOXA and HOXB including cases without NPM1 mutation. The other is that venetoclax resistance involves upregulation of HOXA9 and MEIS1 - a KMT2A-like signature at relapse - making menin inhibition a candidate after venetoclax failure, which the authors correctly flag as an untested hypothesis at the time.

## Key points

- Explains how menin can be a tumour suppressor in endocrine tissue and a leukemogenic requirement in KMT2A-rearranged disease.
- Extends the candidate population from KMT2A rearrangement and NPM1 mutation to any lesion producing HOXA/HOXB dependency, with a tabulated survey.
- Proposes a HOX gene expression signature, rather than genotype, as the biomarker of response.
- Notes that venetoclax resistance involves HOXA9/MEIS1 upregulation, suggesting menin inhibition after venetoclax failure.
- Reviews the early clinical proof-of-concept for oral menin inhibitors in relapsed acute leukemia.

## Limitations

A narrative review from 2021, before the mature clinical results, so its clinical section reports early proof-of-concept only and is now superseded. The authors note that because menin interacts with many other gene regulators, it is plausible that inhibition works by disrupting some other critical transcription factor rather than the KMT2A axis - so the mechanism underlying response is not settled, and no biomarker of response was established. The suggestion of menin inhibition after venetoclax failure is explicitly labelled an untested hypothesis. The tabulated genotypes rest on mixed evidence - patient samples, mouse models, and cell lines - which the table distinguishes but which means most entries are not clinically supported. No systematic search strategy or evidence appraisal.

## Provenance

Located in the published literature, dropped into `inbox/` as `Issa(2021) Leukemia; Therapeutic implications of menin inhibition in acute leukemias.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41375-021-01309-y`; the prose sections were written here from the paper itself.

## Citation

Issa et al. Leukemia 2021. Therapeutic implications of menin inhibition in acute leukemias. doi: 10.1038/s41375-021-01309-y

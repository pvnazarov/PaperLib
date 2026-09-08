---
# --- identity ------------------------------------------------
id: 2023-01-01_rosenquist-2023-journal-of-internal-medi
id_basis: filename-year
source: Rosenquist(2023) Journal of Internal Medicine; Novel precision medicine approaches and treatment strategies in hematological malignancies.pdf
sha256: 812caecdcb046c6d426e0998c310bea7193c54b0280eb87e650b77afe9676665
size_bytes: 1285391
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 178235

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1111/joim.13697"
year: 2023
title: "Novel precision medicine approaches and treatment strategies in hematological malignancies"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Rosenquist(2023) J Intern Med; Novel precision medicine approaches and treatment strategies in hematological malignancies.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

A review of precision diagnostics in hematological malignancies, covering how genetic testing has been implemented to guide treatment selection and improve survival in myeloid disease (myelodysplastic syndromes and AML) and lymphoid disease (acute lymphoblastic leukemia, diffuse large B-cell lymphoma and chronic lymphocytic leukemia). It discusses monitoring measurable residual disease with ultra-sensitive techniques - flow cytometry, quantitative and droplet digital PCR, and next-generation sequencing, each with stated advantages and limitations - to assess therapy response and detect early relapse, and surveys functional precision medicine combining ex vivo drug screening with omics technologies for patients with advanced disease.

## Summary

A broad orientation to how genomics actually reaches the clinic in blood cancers, written from a European implementation perspective. Its practical value in this collection is the measurable residual disease section, which lays out the methods against each other rather than advocating one: flow cytometry reaches 0.01-0.001% sensitivity and needs no prior knowledge of the patient's mutations but has lower specificity, while PCR and sequencing approaches are more specific and require knowing what to look for.

It also flags resistance mutations arising under targeted therapy - BTK and PLCG2 under BTK inhibitors, BCL2 under venetoclax - which is the argument for monitoring rather than assuming a response holds. The functional precision medicine section, pairing ex vivo drug screening with omics, is the direction several primary papers here pursue.

## Key points

- Surveys how disease subtypes in current classifications are defined by recurrent genetic alterations detected by cytogenetics, FISH and targeted sequencing.
- Compares MRD methods directly - flow cytometry, qPCR, ddPCR and NGS - with their sensitivity and specificity trade-offs.
- In AML, MRD level after initial therapy predicts relapse and can identify patients who benefit from allogeneic transplant.
- Resistance mutations emerge under targeted therapy: BTK and PLCG2 under BTK inhibitors, BCL2 under venetoclax.
- Functional precision medicine - ex vivo drug screening combined with omics - is presented as the route for advanced disease.

## Limitations

A narrative review from a symposium on European precision medicine implementation, with no systematic search or evidence grading, and covering five disease areas so that no single one is treated in depth. Published 2023, so it predates several developments in this collection including the menin inhibitor clinical data and the large epigenomic classification work. It is descriptive of practice and method rather than evaluative: MRD monitoring is discussed as informative largely within clinical trials, and the review does not resolve whether acting on MRD changes outcome. Functional precision medicine is presented as a promising avenue rather than an established one, and the ex vivo drug screening it describes has a well-known gap between assay result and clinical response.

## Provenance

Located in the published literature, dropped into `inbox/` as `Rosenquist(2023) J Intern Med; Novel precision medicine approaches and treatment strategies in hematological malignancies.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1111/joim.13697`; the prose sections were written here from the paper itself.

## Citation

Rosenquist et al. Journal of Internal Medicine 2023. Novel precision medicine approaches and treatment strategies in hematological malignancies. doi: 10.1111/joim.13697

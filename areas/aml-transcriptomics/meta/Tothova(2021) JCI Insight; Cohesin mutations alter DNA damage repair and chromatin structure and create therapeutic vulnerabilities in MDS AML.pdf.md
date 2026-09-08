---
# --- identity ------------------------------------------------
id: 2021-01-01_tothova-2021-jci-insight-cohesin-mutatio
id_basis: filename-year
source: Tothova(2021) JCI Insight; Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS AML.pdf
sha256: d9c546e3c17368089c690981ed81aa0afdbe16920b4c540a488e4229f9738b2d
size_bytes: 4275699
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 84879

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1172/jci.insight.142149"
year: 2021
title: "Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS/AML"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Tothova(2021) JCI Insight; Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS AML.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Genetic dependency screens in STAG2-mutant AML identified DNA damage repair and replication as dependencies in cohesin-mutant cells, with increased DNA damage and sensitivity to PARP inhibition. A mouse model of MDS in which Stag2 mutations arose as secondary lesions on a background of Tet2-driven clonal hematopoiesis showed selective depletion of cohesin-mutant cells with PARP inhibition in vivo, and talazoparib reduced disease burden and improved survival in STAG2- and RAD21-mutant AML patient-derived xenografts. Mechanistically, cohesin-mutant cells shift from STAG2- to STAG1-containing complexes, producing longer DNA loop extrusion, loss of insulation at TAD boundaries, intermixing of chromatin compartments, and increased interaction with PARP and replication protein A.

## Summary

Converts a structural observation into a therapy already in clinical use. Cohesin mutations are among the most frequent in myeloid malignancy, and the finding is that losing STAG2 shifts the complex to its paralog STAG1, which extrudes longer loops and, critically, interacts more with PARP and the replication protein A complex - so the architectural change and the DNA repair dependency are the same phenomenon.

The in vivo work is unusually thorough for a preclinical target paper: a mouse model in which Stag2 arises as a secondary lesion on Tet2 clonal hematopoiesis, mirroring the human sequence, plus patient-derived xenografts of two different cohesin genotypes. Showing that talazoparib selectively depletes the Stag2-mutant clone while leaving the Tet2-only clone intact is exactly the genotype-specific effect the strategy requires.

## Key points

- Cohesin-mutant AML depends on DNA damage repair and replication, carries increased DNA damage, and is sensitive to PARP inhibition.
- Loss of STAG2 shifts cohesin to STAG1-containing complexes, with longer loop extrusion, lost TAD insulation and compartment intermixing.
- STAG1-cohesin shows increased interaction with PARP and replication protein A, linking the architectural change to the repair dependency.
- In a Tet2/Stag2 mouse model mirroring the human mutation sequence, talazoparib selectively depleted the Stag2-mutant clone.
- Talazoparib reduced burden and improved survival in STAG2- and RAD21-mutant AML patient-derived xenografts.

## Limitations

PARP inhibitors carry a recognised risk of therapy-related myeloid neoplasm, which is an awkward property for a drug proposed to treat MDS and AML, and the paper does not address it. Blood count normalisation in treated Tet2/Stag2 mice was accompanied by persistent erythrophagocytosis, so the response was partial. Cohesin mutations are heterogeneous - STAG2, RAD21, SMC1A, SMC3 - and although two genotypes were tested in xenografts, whether all confer the same dependency is unestablished; other work in this collection reports that STAG2 and RAD21 mutations have inverted co-mutation patterns and may work through independent mechanisms. The chromatin architecture measurements are in engineered cell models. Several authors declare consulting and research relationships across multiple companies.

## Provenance

Located in the published literature, dropped into `inbox/` as `Tothova(2021) JCI Insight; Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS AML.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1172/jci.insight.142149`; the prose sections were written here from the paper itself.

## Citation

Tothova et al. JCI Insight 2021. Cohesin mutations alter DNA damage repair and chromatin structure and create therapeutic vulnerabilities in MDS/AML. doi: 10.1172/jci.insight.142149

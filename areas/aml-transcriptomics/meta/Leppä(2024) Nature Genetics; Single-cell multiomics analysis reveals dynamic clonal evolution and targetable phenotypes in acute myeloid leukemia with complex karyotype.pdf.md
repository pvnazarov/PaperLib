---
# --- identity ------------------------------------------------
id: 2024-01-01_lepp-2024-nature-genetics-single-cell-mu
id_basis: filename-year
source: Leppä(2024) Nature Genetics; Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype.pdf
sha256: 9a040a76357a1e0b573dc9c2e4fdc96659cc45336884bccb001a9f04178508bc
size_bytes: 15925353
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 343299

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41588-024-01999-x"
year: 2024
title: "Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Leppä(2024) Nat Genet; Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Combining structural variant discovery and nucleosome occupancy profiling with transcriptomic and immunophenotypic measurement in single cells, the authors study intratumoral heterogeneity in complex-karyotype AML. Individual cells show complex structural variant landscapes with linear and circular breakage-fusion-bridge cycles and chromothripsis. Three clonal evolution patterns are identified at diagnosis or salvage - monoclonal, linear and branched polyclonal - with 75% harbouring multiple subclones frequently undergoing ongoing karyotype remodeling. Patient-derived xenografts show varied clonal evolution of leukemic stem cells, and subclone-specific drug-response profiling identifies LSC-targeting therapies including BCL-xL inhibition; paired longitudinal samples reveal both genetic evolution and cell-type plasticity as mechanisms of progression.

## Summary

Measures genotype, epigenotype, phenotype and drug response in the same single cells, which is what complex-karyotype AML has needed: copy-number profiling alone cannot resolve copy-balanced and complex rearrangements, so the heterogeneity that drives this subtype's therapy resistance has been largely invisible.

The methodological payoff is subclone-specific pharmacology. Using CITE-seq data to design antibody panels that distinguish subclones, then measuring drug response per subclone by flow cytometry, answers a question bulk assays cannot - which clone survives which drug. The finding that LSC-enriched populations responded to azacitidine while bulk cells did not, and that one sample's LSCs responded where the bulk did not respond to venetoclax, is exactly the kind of discrepancy that explains clinical failure. The two case studies of progression are also instructive: one relapse driven by a new chromothripsis event, the other by cell-type plasticity within a persisting subclone.

## Key points

- Single-cell structural variants, nucleosome occupancy, transcriptome and immunophenotype measured together in complex-karyotype AML.
- 75% of cases harbour multiple subclones with ongoing karyotype remodelling; three evolution patterns - monoclonal, linear, branched polyclonal.
- Subclone-specific antibody panels allow drug response to be measured per clone rather than in bulk.
- LSC-enriched populations responded to azacitidine, and BCL-xL inhibition emerged as an LSC-targeting option.
- Longitudinal cases show both genetic evolution (a new chromothripsis event) and non-genetic cell-type plasticity as routes to progression.

## Limitations

Single-cell structural variant calling rests on very few cells in places - the refractory sample analysis is based on 21 cells, of which 3 and 18 define the two subclone fractions - so clonal proportions carry wide uncertainty. Drug-response profiling used three patient samples selected for available primary material, and is ex vivo by flow cytometry, which correlates imperfectly with clinical response. The BCL-xL finding inherits the thrombocytopenia problem that limits that drug class. Longitudinal conclusions come from individual patients presented as case studies, which illustrate mechanisms rather than establish their frequency. Nucleosome occupancy from single cells is sparse, limiting epigenotype resolution.

## Provenance

Located in the published literature, dropped into `inbox/` as `Leppä(2024) Nat Genet; Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41588-024-01999-x`; the prose sections were written here from the paper itself.

## Citation

Leppä et al. Nature Genetics 2024. Single-cell multiomics analysis reveals dynamic clonal evolution and targetable phenotypes in acute myeloid leukemia with complex karyotype. doi: 10.1038/s41588-024-01999-x

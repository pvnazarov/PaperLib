---
# --- identity ------------------------------------------------
id: 2016-01-01_lee-2016-nature-medicine-modulation-of-s
id_basis: filename-year
source: Lee(2016) Nature Medicine; Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins.pdf
sha256: 7ef994797c0eb029669be5904ddda334a43269c87bf53f64dd97216d2a5398cf
size_bytes: 1646953
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 238773

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/nm.4097"
year: 2016
title: "Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Lee(2016) Nat Med; Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Spliceosomal gene mutations in MDS and AML are always heterozygous and rarely co-occur, suggesting cells tolerate only partial deviation from normal splicing. Testing this, mice engineered to express Srsf2P95H in an inducible, hemizygous manner in hematopoietic cells rapidly succumbed to fatal bone marrow failure, showing that Srsf2-mutated cells depend on the wild-type allele. The spliceosome inhibitor E7107 substantially reduced leukemic burden specifically in isogenic mouse leukemias and patient-derived xenograft AMLs carrying spliceosomal mutations; E7107 caused widespread intron retention and exon skipping regardless of genotype, but the magnitude of splicing inhibition was greater in Srsf2-mutant cells.

## Summary

A therapeutic strategy derived from a genetic observation rather than a screen. Splicing factor mutations are invariably heterozygous and mutually exclusive - a pattern that only makes sense if cells can tolerate a partial but not a total deviation from normal splicing. That predicts a synthetic lethality, and the hemizygous mouse tests it directly: remove the wild-type allele and the animals die of marrow failure.

The pharmacological arm follows the same logic and reports its own complication honestly. E7107 inhibits splicing in every cell, mutant or not - the selectivity is quantitative, a matter of magnitude, not a difference in kind. That is a narrower therapeutic window than a truly synthetic-lethal interaction would give, and it is the reason spliceosome inhibitors have been difficult to develop.

## Key points

- Explains why spliceosomal mutations are always heterozygous and mutually exclusive: cells tolerate only partial deviation from normal splicing.
- Hemizygous Srsf2P95H mice die of bone marrow failure, proving dependence on the wild-type allele.
- The spliceosome inhibitor E7107 preferentially reduces burden in Srsf2-mutant mouse leukemias and mutant patient-derived xenografts.
- Selectivity is a matter of degree - E7107 causes intron retention and exon skipping regardless of genotype, but more so in mutant cells.
- Establishes further splicing perturbation as a therapeutic principle in spliceosome-mutant myeloid malignancy.

## Limitations

The selectivity is quantitative rather than absolute, which is the central weakness: E7107 inhibits splicing in wild-type cells too, and splicing is essential everywhere, so the therapeutic window depends on a difference in magnitude. E7107's clinical development was in fact halted for toxicity, including visual disturbance, which this preclinical work does not anticipate. The genetic model is hemizygous expression, a more severe perturbation than any drug achieves, so it establishes the principle rather than predicting drug behaviour. Mouse models plus PDX in immunodeficient mice; efficacy is reduction in burden rather than survival or cure. Only SRSF2 P95H is modelled, and whether U2AF1 and SF3B1 mutant cells behave identically is assumed from the shared genetic pattern rather than shown.

## Provenance

Located in the published literature, dropped into `inbox/` as `Lee(2016) Nat Med; Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/nm.4097`; the prose sections were written here from the paper itself.

## Citation

Chun-WeiLee et al. Nature Medicine 2016. Modulation of splicing catalysis for therapeutic targeting of leukemia with mutations in genes encoding spliceosomal proteins. doi: 10.1038/nm.4097

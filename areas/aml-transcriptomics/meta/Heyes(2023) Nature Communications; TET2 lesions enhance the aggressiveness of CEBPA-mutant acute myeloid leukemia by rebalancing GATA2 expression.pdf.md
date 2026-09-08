---
# --- identity ------------------------------------------------
id: 2023-01-01_heyes-2023-nature-communications-tet2-le
id_basis: filename-year
source: Heyes(2023) Nature Communications; TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression.pdf
sha256: 2bbad79842545873f568cb379be3160dc9043991c9201f77788f5333bcbeb47b
size_bytes: 2547390
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 212564

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1038/s41467-023-41927-x"
year: 2023
title: "TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Heyes(2023) Nat Commun; TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Combining transcriptomic and epigenomic analysis of CEBPA-TET2 co-mutated patients with mouse models, the authors identify GATA2 as the conserved target of the CEBPA-TET2 mutational axis. Elevated CEBPA levels driven by hypermorphic N-terminal mutations recruit TET2 to the Gata2 distal hematopoietic enhancer, increasing Gata2 expression; concurrent TET2 loss confers a competitive advantage by increasing Gata2 promoter methylation and rebalancing GATA2 levels. Demethylating treatment of Cebpa-Tet2 co-mutated AML restores Gata2 levels and prolongs disease latency.

## Summary

An unusually complete explanation of a co-mutation pattern, which is a class of question the field usually only describes. The logic is that the first lesion overshoots - CEBPA N-terminal mutations push GATA2 too high, which is itself suboptimal for the leukemia - and the second lesion corrects it. TET2 loss is therefore not an additional insult but a compensation, which explains why the two are found together and why TET2 and GATA2 mutations rarely co-occur in the same cases.

The therapeutic implication follows directly and is tested: if TET2 loss works by hypermethylating the Gata2 promoter, a demethylating agent should undo it, and 5-azacytidine restores Gata2 levels and prolongs latency. That is a rational, mechanism-derived use of a drug already standard in AML.

## Key points

- Explains a co-mutation pattern mechanistically: TET2 loss corrects the excessive GATA2 induced by hypermorphic CEBPA N-terminal mutations.
- CEBPA recruits TET2 to the Gata2 distal hematopoietic enhancer; losing TET2 raises Gata2 promoter methylation and lowers expression back to an optimal level.
- Consistent with the observation that TET2 and GATA2 mutations rarely co-occur in CEBPA-double-mutant AML.
- Extends beyond CEBPA-double-mutant cases: TET2 and GATA2 mutations are overrepresented wherever CEBPA expression is high.
- Demethylating treatment restores Gata2 levels and prolongs disease latency in the co-mutant mouse model.

## Limitations

The functional work is mouse genetics with a defined Cebpa-delta/p30 Tet2 model; human evidence is transcriptomic and epigenomic association in patient cohorts, so the causal chain is established in mice and inferred in people. Hypomethylating agents are profoundly non-specific, so restoration of Gata2 levels by 5-azacytidine is consistent with the model but far from proof that the Gata2 promoter is the therapeutically relevant site. The benefit measured is prolonged disease latency in mice, not cure or a survival benefit in an established leukemia. 'Optimal' GATA2 level is inferred from competitive advantage rather than measured against a defined functional optimum. Patient numbers for the co-mutated genotype are inevitably small, since CEBPA-double-mutant AML is itself uncommon.

## Provenance

Located in the published literature, dropped into `inbox/` as `Heyes(2023) Nat Commun; TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1038/s41467-023-41927-x`; the prose sections were written here from the paper itself.

## Citation

Heyes et al. Nature Communications 2023. TET2 lesions enhance the aggressiveness of CEBPA-mutant acute myeloid leukemia by rebalancing GATA2 expression. doi: 10.1038/s41467-023-41927-x

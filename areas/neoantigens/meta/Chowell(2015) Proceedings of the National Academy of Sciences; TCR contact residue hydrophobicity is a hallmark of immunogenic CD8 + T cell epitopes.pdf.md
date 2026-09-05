---
# --- identity ------------------------------------------------
id: 2015-01-01_chowell-2015-proceedings-of-the-national
id_basis: filename-year
source: Chowell(2015) Proceedings of the National Academy of Sciences; TCR contact residue hydrophobicity is a hallmark of immunogenic CD8 + T cell epitopes.pdf
sha256: b3667b915b49e496f2acbc2969fb9995188dc058b14cfdd52b749361f7d4db14
size_bytes: 1148358
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 75676

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1073/pnas.1500973112"
year: 2015
title: "TCR contact residue hydrophobicity is a hallmark of immunogenic CD8 + T cell epitopes"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as 2015_Chowell_Proc_Natl_Acad_Sci_U_S_TCR_contact_residue_hydrophobicity_is_a_hallma_PMID25831525.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Interrogating the biochemical properties of 9,888 MHC class I peptides, the authors find a strong bias toward hydrophobic amino acids specifically at TCR contact residues of immunogenic epitopes. They train a hydrophobicity-based neural network (ANN-Hydro) on this signal and validate it blind on 364 peptides from three HIV-1 Gag variants in vivo.

## Summary

The argument is that binding predictors were never trained to predict immunogenicity, so a large fraction of predicted binders will never provoke a response. Immunogenic epitopes must satisfy criteria beyond processing and MHC binding, and this paper proposes hydrophobicity at the exposed, TCR-facing positions as one of them.

Applied on top of existing peptide-MHC algorithms, the model consistently shrinks the candidate list across several antigens, and the authors suggest it may correlate with immunodominance.

## Key points

- The hydrophobicity bias is selective for exposed TCR contact residues, not the peptide as a whole - which is what makes it a mechanistic claim rather than a composition statistic.
- Validated blind in vivo on 364 overlapping peptides from three HIV-1 Gag protein variants.
- Used as a filter layered on existing binding predictors rather than as a replacement for them.
- Together with Calis (2013), establishes hydrophobic and aromatic TCR-facing residues as the classical immunogenicity signal.

## Limitations

The authors note the model was trained on 9-mers and that larger datasets are needed before longer or shorter epitopes are handled well. The negative class is non-immunogenic self peptides, which is an assumption about what was never tested rather than a measurement. Validation is in a single pathogen system (HIV-1 Gag) and in mice; nothing here establishes performance on cancer neoepitopes, where later benchmarks in this collection find such scores transfer poorly.

## Provenance

Located in the published literature, dropped into `inbox/` as `2015_Chowell_Proc_Natl_Acad_Sci_U_S_TCR_contact_residue_hydrophobicity_is_a_hallma_PMID25831525.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1073/pnas.1500973112`; the prose sections were written here from the paper itself.

## Citation

Chowell et al. Proceedings of the National Academy of Sciences 2015. TCR contact residue hydrophobicity is a hallmark of immunogenic CD8
                    <sup>+</sup>
                    T cell epitopes. doi: 10.1073/pnas.1500973112

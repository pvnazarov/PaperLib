---
# --- identity ------------------------------------------------
id: 2019-01-01_krivtsov-2019-cancer-cell-a-menin-mll-in
id_basis: filename-year
source: Krivtsov(2019) Cancer Cell; A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia.pdf
sha256: 537ee3c0cdf5572b82ef72e4dd90d4fff303dda3dd1ad9b4d706a6463d1ccdfd
size_bytes: 6118962
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-08'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 133702

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1016/j.ccell.2019.11.001"
year: 2019
title: "A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia"

# --- cross-area ----------------------------------------------
area: aml-transcriptomics
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Krivtsov(2019) Cancer Cell; A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia.pdf; ingested into area 'aml-transcriptomics' by scripts/ingest_inbox.py on 2026-09-08"
---

## Abstract

Structure-based design produced VTP50469, a potent, highly selective, orally bioavailable inhibitor of the menin-MLL interaction. MLL-rearranged cell lines were selectively responsive; the compound displaced menin from protein complexes and reduced MLL chromatin occupancy at select genes, leading to changes in gene expression, differentiation and apoptosis. Patient-derived xenografts of MLL-rearranged AML and ALL showed dramatic reductions in leukemia burden, and multiple mice engrafted with MLL-rearranged ALL remained disease free for more than a year after treatment.

## Summary

The other foundational menin inhibitor paper, and the one whose in vivo result is hardest to argue with: mice engrafted with human MLL-rearranged ALL that remain disease-free beyond a year after a course of a single agent are cured, not merely improved. The inclusion of infant MLL-rearranged ALL, where roughly 80% of cases carry the rearrangement and outcomes are dismal, is what gives the result its clinical weight.

The chromatin analysis contains the more subtle point. Loss of MLL occupancy is focal rather than global - restricted to a subset of target genes that need not include the HOXA cluster - and the authors argue that this focality is what creates the therapeutic window, since widespread loss of MLL binding would be damaging to most hematopoietic cells. The direct comparison with a selective DOT1L inhibitor is informative too: menin-MLL inhibition changes expression within 48 hours versus 7 days for DOT1L, implying mechanisms beyond DOT1L enzymatic activity, while the convergence of the two programs argues for combining them.

## Key points

- VTP50469 is a potent, selective, orally bioavailable menin-MLL inhibitor developed by structure-based design and X-ray co-crystallography.
- Single-agent treatment cured a substantial number of mice engrafted with human MLL-rearranged ALL - disease-free beyond one year.
- Loss of MLL chromatin occupancy is focal rather than global, which the authors argue explains the therapeutic window.
- The critical menin-MLL interaction is at a subset of target genes that do not necessarily include HOXA.
- Head-to-head with DOT1L inhibition: 48 hours versus 7 days to change expression, implying effects beyond DOT1L activity, with convergent programs supporting combination.

## Limitations

Preclinical. Patient-derived xenografts in immunodeficient mice omit the immune system, and 'cure' in that setting is a statement about engrafted human cells rather than about a patient's disease; the subsequent clinical experience with this drug class - modest complete remission rates, limited response duration, resistance through menin mutations - shows how much the models overstate. The mechanism is acknowledged as incomplete: the authors state that future studies will define why individual loci respond differently, and why menin-MLL inhibition acts faster and more broadly than DOT1L inhibition. Treatment was continuous drug in mouse chow over four weeks, and differentiation syndrome, the main clinical toxicity of this class, is not something these models detect. The efficacy claim is strongest in ALL, while most of this collection concerns AML.

## Provenance

Located in the published literature, dropped into `inbox/` as `Krivtsov(2019) Cancer Cell; A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia.pdf` and ingested into area **aml-transcriptomics** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1016/j.ccell.2019.11.001`; the prose sections were written here from the paper itself.

## Citation

Krivtsov et al. Cancer Cell 2019. A Menin-MLL Inhibitor Induces Specific Chromatin Changes and Eradicates Disease in Models of MLL-Rearranged Leukemia. doi: 10.1016/j.ccell.2019.11.001

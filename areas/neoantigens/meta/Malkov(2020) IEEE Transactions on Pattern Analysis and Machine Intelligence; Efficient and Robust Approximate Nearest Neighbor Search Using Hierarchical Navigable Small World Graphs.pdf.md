---
# --- identity ------------------------------------------------
id: 2020-01-01_malkov-2020-ieee-transactions-on-pattern
id_basis: filename-year
source: Malkov(2020) IEEE Transactions on Pattern Analysis and Machine Intelligence; Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs.pdf
sha256: e1f365b79d624eade77521332d660ae7c8b0a9bf2ec007de317b5da89081d48f
size_bytes: 1810429
media: pdf

# --- ingest --------------------------------------------------
processed: '2026-09-05'
processor: paperlib-ingest-1
status: ok
extraction:
  method: pdftotext
  ocr: false
  chars: 97314

# --- classification (LIH WI DC-909) --------------------------
type: paper
classification: Public
classification_basis: "published literature — publicly available at its venue"

# --- bibliographic -------------------------------------------
doi: "10.1109/TPAMI.2018.2889473"
year: 2020
title: "Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs"

# --- cross-area ----------------------------------------------
area: neoantigens
# also_in_areas: (none -- these bytes are held only here)
# --- provenance ----------------------------------------------
provenance: "located in the published literature and deposited by the data owner in inbox/ as Efficient_and_Robust_Approximate_Nearest_Neighbor_Search_Using_Hierarchical_Navigable_Small_World_Graphs.pdf; ingested into area 'neoantigens' by scripts/ingest_inbox.py on 2026-09-05"
---

## Abstract

Hierarchical NSW builds a multi-layer structure of proximity graphs over nested subsets of the stored elements, with an element's maximum layer chosen randomly under an exponentially decaying distribution. Searching from the top layer exploits scale separation to achieve logarithmic complexity, and a neighbour-selection heuristic improves performance at high recall and on clustered data.

## Summary

Infrastructure, like Faiss elsewhere in this collection, and increasingly the default index behind embedding-based similarity search. It is fully graph-based and needs no separate coarse-search structure, which is what makes it simple to deploy.

It earns its place here because peptide, TCR and protein-language-model methods all reduce to nearest-neighbour search over large vector sets, and the similarity-based components of several models in this collection are exactly this operation.

## Key points

- Fully graph-based: no auxiliary coarse-search structure, unlike most proximity-graph methods.
- Layer assignment by exponentially decaying probability separates links by distance scale, giving logarithmic search complexity.
- A neighbour-selection heuristic matters most at high recall and on highly clustered data - which is what biological embedding spaces are.
- General metric space method, so it applies to whatever distance a sequence or embedding model defines.

## Limitations

Nothing here concerns peptides, MHC or immunogenicity; any biological claim built on it needs its own evidence. Results are approximate by construction, and the recall/speed trade-off must be tuned per application. The authors note that comparing approximate nearest-neighbour algorithms is intrinsically difficult because the state of the art moves constantly, so the reported comparisons are dated even where the method is not.

## Provenance

Located in the published literature, dropped into `inbox/` as `Efficient_and_Robust_Approximate_Nearest_Neighbor_Search_Using_Hierarchical_Navigable_Small_World_Graphs.pdf` and ingested into area **neoantigens** by `scripts/ingest_inbox.py`. Title, venue, year and byline come from the publisher's registration for `10.1109/TPAMI.2018.2889473`; the prose sections were written here from the paper itself.

## Citation

Malkov et al. IEEE Transactions on Pattern Analysis and Machine Intelligence 2020. Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs. doi: 10.1109/TPAMI.2018.2889473

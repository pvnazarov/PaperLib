## How to read this

Every paper in the collection, clustered by subject. {n} papers, {t} topics in {parts} parts,
each paper in exactly one topic.

**The clustering is the only judgement in this document.** It was drawn by reading each paper's
title, abstract and key points and deciding where it belongs. The similarity vectors may
*propose* — per-topic cohesion, centroid overlap, papers that sit closer to another topic than
to their own — but proposing is all they do: they are TF-IDF over the summaries, so they group
by shared vocabulary rather than by subject, and vocabulary and subject part company more often
than is comfortable. Some topics here are deliberately low on vocabulary cohesion because their
subject is genuinely diverse.

**This is the FIRST clustering of this collection**, so there is no before-and-after to report.
When it is re-drawn, that revision belongs in `reports/` with the criteria written down *before*
any candidate taxonomy exists, and this block should be replaced with one that says so.

Everything else is mechanical:

| Element | Where it comes from |
|---|---|
| first author, year, journal, title | the publisher's own registration via Crossref or arXiv, keyed on a DOI or arXiv ID verified against the paper's bytes — or, for the papers that register nowhere, the paper's own first page |
| DOI / arXiv ID | the sidecar's `doi:` field |
| summary | the sidecar's `## Abstract` — written once at ingest from the source's own extracted text |
| `[src]` link | the source file in `raw/` |

**The summaries are paraphrases, not quotations, and this document is not a source.** Each entry
links the paper itself; a claim you intend to rely on must be checked there.

**Author lists are deliberately incomplete here.** Each entry names the registered first author
and `et al.`, never a reconstructed list. Full, verified lists exist for {with_authors} of {n}
papers, in `data/bib_cache.json` and searchable in the browser; they are not repeated here
because an entry heading is a citation, not a byline.

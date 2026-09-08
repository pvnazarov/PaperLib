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

**What the parts follow.** The six parts are ordered by the layer at which the disease is
dysregulated, working outward from the initiating lesion. **A** is the driver itself — the fusion
proteins and recurrent mutations, and the transcriptional networks they build. **B** is the
chromatin those networks act on: the regulators co-opted to hold the differentiation block, the
methylation landscape, and the three-dimensional organisation that decides which element reaches
which promoter. **C** is what happens to the RNA after it is transcribed — splicing, isoform
choice, chemical modification — a layer this collection covers unusually heavily because AML
turns out to be dysregulated there even in the large majority of patients who carry no splicing
factor mutation. **D** is metabolism and cell death, where most of the collection's therapeutic
vulnerabilities are, and where its single most consequential result sits: the cells that survive
chemotherapy are metabolically distinct rather than developmentally primitive. **E** is the
cellular population structure — stem cells, hierarchies, and what changes at relapse. **F** is
the clinical surface: how the disease is diagnosed and stratified, and how it evades the immune
system.

**Three choices worth stating.** First, **t(8;21) is split across two topics** rather than kept
whole. One holds the mechanism of the fusion protein, the other holds what the leukemia needs in
order to persist; they are different questions with different literatures, and merging them would
produce a nineteen-paper topic in which the therapeutic papers disappear among the mechanistic
ones.

Second, **metabolism is separated from the BCL2 family** even though venetoclax resistance is
substantially metabolic. The reason is that the venetoclax papers form a coherent argument with
each other — about who responds, and whether monocytic differentiation predicts it — and that
argument is legible only if they sit together.

Third, **functional genomics screens are a topic rather than a method note.** Five papers here
are read for what they say about screening itself: that an in vivo screen finds targets an in
vitro screen structurally cannot, that primary cells and cell lines give different answers, and
that filtering hits against human loss-of-function genetics before believing them is what
produced the one target in this collection whose therapeutic window is established in humans
rather than in mice.

**Where the seams are.** Six papers could defensibly sit elsewhere, and are named here rather
than left for a reader to notice. **Gerritsen (2019)** studies RUNX1 point mutations, not the
fusion, and is filed under t(8;21) dependencies because what it measures is the difference
between the two. **Saika (2026)** runs from a splicing factor mutation through chromatin to
ferroptosis and is filed under splicing rather than metabolism, because SF3B1 is where its causal
chain starts. **Chang (2024)** is a SETDB1 chromatin paper filed under immunotherapy, because the
dependency it finds exists only in an immunocompetent animal and is about NK recognition.
**Tirtakusuma (2022)** and **Mimura (2026)** are lymphoid diseases — an MLL/AF4 B-ALL and a T-ALL
— kept here for their lineage-switching and enhancer-hijacking mechanisms. **Zhou (2025)** is a
Data in Brief dataset description with no findings at all, filed under long-read transcriptomics
as the resource it is.

**Three files in `raw/` are not the papers.** Boët (2024), Fetsch (2026) and Lin (2017) are
one-page bibliographic records carrying a PubMed abstract, generated on 2026-09-08 by
`make_abstract_pdf.py` because no full text could be obtained. They say so in their own text,
their sidecars say so under Limitations, and nothing in their records can be checked against a
figure, a method or a reference list.

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

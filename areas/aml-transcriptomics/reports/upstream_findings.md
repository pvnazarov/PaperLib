# Upstream findings — aml-transcriptomics

Defects in the publishers' registered metadata. Recorded, never silently patched
(CLAUDE.md §2.4): a quiet fix is a fix nobody can see, and these are somebody
else's facts.

## Titles carrying a space no publisher wrote — OURS, and fixed 2026-09-08

Not an upstream defect, listed here because it looked like one for a while.
Crossref deposits inline markup on its own indented line:

    'Menin inhibition with revumenib for\n                    <i>NPM1</i>\n                    -mutated relapsed...'

`ingest_inbox.clean_title` removed the tag and collapsed the whitespace, which
turned the layout indentation into a real space: `NPM1 -mutated`. Ours to fix,
and fixed in `strip_markup()`; 8 titles across both areas were corrected in step
with the filenames built from them. See `2026-09-08_title_space_correction.md`.

## `single cell -omics` — Baronas(2025) — GENUINELY UPSTREAM, not patched

    registered_title: 'High-throughput single cell -omics using semi-permeable capsules'

No markup, no newlines: the space before `-omics` is in the registration itself.
It was in the first list of 11 candidates and was dropped on inspection — the
distinguishing test is whether the raw registration contains markup, not whether
the rendered string looks wrong. Left exactly as registered.

## `N 6 -Methyladenosine` — FTO paper — UPSTREAM, corrected 2026-09-08

    registered_title: 'FTO Plays an Oncogenic Role in Acute Myeloid Leukemia as a
                       N 6 -Methyladenosine RNA Demethylase'   (verbatim)

**Correcting an earlier entry in this file.** It first said this registered as
`N<sup>6</sup>-Methyladenosine` and was therefore half ours to fix. That was
inferred from the shape of the other cases and never checked against this one.
There is no markup here at all: both spaces are literally in the registration, so
`strip_markup()` leaves it untouched — correctly, since it has nothing to strip.
This belongs with Baronas above, not with the eight the ingest broke.

The paper itself prints `N6-Methyladenosine` (page 1; the 6 typeset as a
superscript, which `pdftotext` renders as `N6`), and `N6-methyladenosine`
throughout the body. The owner asked for it to be corrected, so the registered
title has been overridden — a bigger act than repairing our own bug, recorded as
its own ledger entry (seq 565) with the registration quoted verbatim so the
override stays visible and reversible.

## `MLLr + AML` — METTL3-YTHDC1 paper — thin spaces, deliberately left

    registered_title: '...chromatin TADs in MLLr + AML genome'

U+2009 THIN SPACE either side of the `+`. That is typography, not an error, and
the stored `MLLr + AML` is a fair rendering of it. The mechanical rule would have
produced the asymmetric `MLLr+ AML`, which is worse than what is there — the
reason this one was excluded rather than swept in with the rest.

## No registered venue

Three papers have no container-title in their registration and none recoverable
from the filename; `make audit` reports them on every run:

- `Baronas(2025) unknown; High-throughput single cell -omics using semi-permeable capsules`
- `Larrue(2023) unknown; Ferritinophagy is a Druggable Vulnerability...`
- `Miller(2026) unknown; Long-read cDNA sequencing reveals novel isoforms...`

Absent, not truncated (CLAUDE.md §3): they show as `unknown` rather than carrying
a venue reconstructed from the PDF.

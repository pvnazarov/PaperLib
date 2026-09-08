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

## `N 6 -Methyladenosine` — FTO paper — partly ours, deliberately left

    registered_title: '...as a N<sup>6</sup>-Methyladenosine RNA Demethylase'

The correct rendering is `N6-Methyladenosine`. Our fix takes it to
`N 6-Methyladenosine`: the space before the hyphen goes, but the one between `N`
and the former superscript `6` does not, because joining a superscript digit to
its letter is a different transformation and no rule for it has been measured.
Left as it is rather than half-guessed; `strip_markup`'s docstring says so too.

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

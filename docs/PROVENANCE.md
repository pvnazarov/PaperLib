# Provenance: what came from teamlibrary-toolkit and what changed

Source: `teamlibrary-toolkit-2026-09-05.tar.gz`, downloaded 2026-09-05 from
`http://files.sablab.net/copy/`. It was extracted from a working instance holding
340 papers, deployed inside an institute.

**The reference copy was removed on 2026-09-05 at the owner's request.** Every diff
line count below was measured against it while it was present. To re-check any of
them, re-download the archive from the URL above, unpack it beside this repository,
and diff `scripts/` against it — nothing in the pipeline reads it, so it is only
ever needed to verify these claims.

Every number below was measured on 2026-09-05, not estimated.

## The one change that made it multi-area

Every script computed `ROOT = Path(__file__).resolve().parent.parent` and hung
`raw/`, `meta/`, `outputs/`, `data/`, `dist/` off it. That single assumption was
the only thing making the toolkit single-collection.

`scripts/paperlib.py` (new) resolves `ROOT` to an **area** instead, from
`PAPERLIB_AREA`, or `PAPERLIB_AREA_ROOT`, or the only area when there is exactly
one. `areas/<name>/` therefore has exactly the shape the toolkit's root had, and
the pipeline runs inside one unchanged — own taxonomy, own `library.json`, own
UMAP layout, own page, for free.

## What was reused unchanged

| | |
|---|---|
| `src/` — `index.html`, `app.js`, `app.css` | **byte-identical**, 2321 lines. Shared by every area; a fix reaches all of them at once. |
| the sidecar format, the filename convention, the taxonomy-in-the-review design, the add-only rule, the refusal set, the determinism contract | unchanged |
| `docs/templates/` | the review-prose templates and the eval README, moved out of `annotations/` so a new area is seeded from them |

## What was changed, and by how much

Diff line counts against the original, `sort -rn`:

| script | ± lines | why |
|---|---|---|
| `ingest_inbox.py` | 227 | cross-area sha256 check and the `also_in_areas` field; `processor: paperlib-ingest-1`; provenance prose rewritten (upstream's described papers *circulated on a Webex thread*, which is not how papers arrive here) |
| `build.py` | 36 | area-aware `ROOT`; `area` and `also_in_areas` parsed into `library.json`; `paperlib.json` layered under each area's `project.json`; `has_roster` |
| `make_review.py` | 24 | `--taxonomy` was resolved against the working directory while `--out` was resolved against `ROOT`. In a single-collection tree those were the same place. Here they are not, and the mismatch wrote a review to `areas/x/areas/x/outputs/` that `make build` then reported as missing. Both are now area-relative, with a named fallback. |
| `selftest.py` | 20 | the fixture tree needs `paperlib.py` copied beside the scripts it copies, and `PAPERLIB_AREA_ROOT` set — otherwise the self-test resolves to the real collection and tests that instead. It caught this itself. |
| `render.py` | 9 | `data/` and `dist/` are the area's; `src/` is the project's |
| `make_example.py` | 49 | the `ROOT` one-liner, plus `--clean` — see the defect below |
| `audit.py` | 7 | the `ROOT` one-liner, plus `has_roster` |
| `fetch_bib.py` | 27 | the `ROOT` one-liner, plus `registered_first_family` — see below |
| `embed.py`, `edit_upstream.py`, `propose_topics.py`, `score_eval.py`, `ui_check.py` | 6 each | the `ROOT` one-liner, nothing else |
| `make_archive.py` | 8 | points at the project, **not yet multi-area aware** — its collection scan still assumes a single `root/meta`. Review before relying on it. |

## What is new — 662 lines

| script | |
|---|---|
| `paperlib.py` | area resolution, the area registry, the cross-area sha256 scan |
| `new_area.py` | scaffolds `areas/<name>/` and its `project.json` (dry run by default) |
| `route_inbox.py` | shared `inbox/` → `areas/<a>/inbox/`; reports cross-area duplicates; **never guesses an area** |
| `portal.py` | `index/registry.json` and `dist/index.html`, the front door |
| `write_prose.py` | installs the four prose sections into a sidecar; refuses anything not `prose-pending` without `--allow-overwrite`, round-trips line endings, records every edit in the ledger |
| `areas.py` | `make areas` — what exists and what each holds |

`Makefile`, `deploy.sh`, `CLAUDE.md` and `README.md` were rewritten for many areas.
`deploy.sh` keeps the original's symlink reasoning and its mode-fixing, per area.

## A defect found in the upstream toolkit

`RETARGETING.md` documents the example cleanup as:

```
rm raw/Example* meta/Example*
```

**It removes nothing.** `make_example.py` names its synthetic files after the
author's surname and puts the word "Example" inside the *venue*:
`Alvarez(2024) Journal of Example Methods; Distributional models….txt`. A person
following the runbook is told the example is gone and is left with 12 synthetic
papers in a real collection — which then reach the taxonomy, the map and the page.

Not patched silently: `make_example.py --clean` now removes exactly the files the
generator knows it wrote, and refuses to delete a `taxonomy.json` that is not the
generated one. `make demo-clean AREA=x` calls it. Reported here because the fix
lives in this copy and the defect lives upstream.

## Identity extraction, hardened against a real corpus

The first real ingest — 60 neoantigen papers, 2026-09-05 — put the upstream
identity code under conditions the 340-paper original had not produced. Four
defects were found, and each one produced a **well-formed string that was not the
right answer**, which is worse than finding nothing: nothing is refused loudly,
while a wrong identifier silently fetches a wrong registration.

**`find_doi` returned the first regex match.** Measured failures:

| what the paper prints | first match | correct |
|---|---|---|
| a DOI broken across a line (PLoS) | `10.1371/journal.` | `10.1371/journal.pcbi.1012511` |
| `.../suppl/doi:10.1073/pnas.2100542118/-/DCSupplemental` | the whole string | `10.1073/pnas.2100542118` |
| a per-figure DOI (PLoS mints one per figure and table) | `…pcbi.1003266.g001` | `…pcbi.1003266` |

Now: strip the `/-/` supplemental path and any `.g001`/`.t001`/`.s001` asset
suffix, then take the **most frequent** candidate, earliest first on a tie. The
article's own DOI is printed in the running header of every page, so frequency is
what separates it from everything printed beside it — read off the document rather
than guessed.

**Validated against ground truth, not asserted.** All 59 papers carrying a PMID
were resolved through NCBI's `esummary` and compared with what `find_doi` returned:

```
59 papers with a PMID · ground truth for 59
  agree      54
  disagree    2   (both: a published article whose PDF prints its PREPRINT DOI)
  not found   3   (fall back to --doi-map)
```

**The two disagreements needed a new mechanism.** `10.7554/eLife.93934.2` and
`10.1101/2025.04.04.647165` are both *registered* — as `posted-content` with no
venue — so `--doi-map`, which is deliberately only a fallback for when no DOI is
found, could not correct them. Filing them that way would have given the wrong
type, no venue, and for one the wrong year. Added `--doi-override`: a separate,
explicitly named flag that does beat the printed DOI, prints every use, and records
the reason in the sidecar's provenance. The upstream rule that the paper wins is
intact; this is a distinct, auditable exception.

**The first author's surname was being re-derived from a joined display name.**
`surname_key` took everything after the leading token, so `Juan C. Almagro` became
`CAlmagro` and `Jorg J. A. Calis` became `JACalis`. Crossref already returns
`given` and `family` separately and `fetch_bib.py` was joining them and throwing
the split away. It now carries `registered_first_family` through, and the ingest
uses it. Middle-initial dropping stays in `surname_key` as the fallback for
registrations with no structured family name (arXiv, consortium authors).

This matters more than it looks: the filename is the join key and `raw/` is
add-only, so a wrong surname is permanent. Checking all 60 generated names against
the surnames in the source filenames took the disagreements from 4 to 1 — and the
one that remains is `Łuksza`, where the *source* filename had dropped the `Ł` and
the registration is right.

## What was dropped, and why

- **`wiki/group.md` and the All / Ours / Shared switch.** It decides which papers
  the group co-wrote. This project collects published literature and writes none of
  it, so there is no distinction to draw. The absence is *declared*
  (`has_roster: false` in `paperlib.json`) rather than left to warn on every build
  forever — the check still exists for anyone who later wants a roster.

## Two names for "area"

Upstream already used the word: `duplicate_of_area` means a paper filed under a
second **topic** inside one review. This project's `area:` and `also_in_areas:`
mean the collection. They are deliberately different fields; do not merge them.

## Verified working, 2026-09-05

Against the 12-paper synthetic example, in `areas/neoantigens/`:

```
make example / make_review --from-sidecars / make build   -> 12 papers, 6 topics, 3 parts, no problems
make embed                                                -> 12 coords, 99.8% variance over 11 components
make render                                               -> 126 KB, three files
make audit                                                -> no problems, 13 notes
make verify                                               -> 12/12 hashes match
make test                                                 -> all checks passed
make portal                                               -> 1 area, 12 papers
```

Multi-area behaviour, tested with a temporary second area and then removed:

- `make build` with two areas and no `AREA=` → refuses, and names both.
- a file whose bytes are already in another area → routed, and reported as
  `[also held in: neoantigens]`.
- a loose file in `inbox/` with no `--area` → left where it is, and reported.

The example collection is synthetic and was deleted before the first real paper.

## Four more defects found by the first real corpus

Everything below was found by running the toolkit on 60 real papers on 2026-09-05,
and each was a case of the pipeline producing something well-formed and wrong.

**A registered title with markup and line breaks truncates its own frontmatter.**
Crossref returned `...immunogenic CD8\n <sup>+</sup>\n T cell epitopes` and the
ingest wrote it verbatim into a single-line `title: "..."`. The frontmatter regex is
line-anchored, so the parsed title stopped at the first newline. 1 of 60 papers.
Fixed with `clean_title()` in `ingest_inbox.py`, which strips markup and collapses
whitespace but - unlike `clean_component()` - keeps colons and semicolons, which are
legitimate in a title and only a problem in a filename. The affected sidecar was
repaired through `edit_upstream.py` with recorded approval.

**The upstream edit ledger has two incompatible shapes.** `ingest_inbox.py` and
`edit_upstream.py` write `{"_comment": [...], "edits": [...]}`; `build.py` reads
`doc.get("edits")`. A ledger writer that unwraps that to a bare list therefore
breaks the build - which is exactly what an early version of this project's
`write_prose.py` did, after 60 sidecars had already been written. The writer now
preserves the object and assigns `seq`; the damaged file was repaired in place with
no entry added or removed.

**`edit_upstream.py` replaces a field's LINE, not its VALUE.** Correcting a
multi-line frontmatter value leaves the continuation lines behind as orphans that
are not YAML keys and parse as nothing. Not fixed in the tool - it is a
line-oriented editor by design and its refusals depend on that - but recorded here,
because the failure is silent and looks like a clean edit in the tool's own diff.

**`make_example.py --clean` needed a guard scoped to writing.** The generator
refuses to run when `raw/` is non-empty, which is right for writing an example into
a real collection and wrong for removing one; `--clean` is now exempt.

## Two more defects, found by the second batch

**Duplicate checks compared only against the collection on disk, never against the
same run.** All three - sha256, DOI and target filename - loaded the collection's
holdings once and then planned every inbox file against that snapshot. Two
byte-identical files in one batch (`nature14426.pdf` and `nature14426-1.pdf`) both
passed, both planned the same `raw/` name, and `--apply` would have copied the
second over the first, taking the first paper's sidecar with it. That is a silent
add-only violation with no error anywhere. Batch 1 did not trigger it because it
contained no intra-batch duplicates. Fixed by tracking planned sha256s, DOIs and
target names across the plan loop; the re-run refuses exactly one file and names
the file it collides with.

**`--clear` trusted a stale `library.json`.** Upstream preferred `library.json`
when it existed and fell back to `meta/` only before the first build. But
`library.json` is a build product: ingesting 57 papers and running `--clear` before
the next `make build` compared the inbox against a 60-paper library, found none of
the new bytes, and kept all 58 files. It reads as "the copy failed" and invites
re-ingesting papers already in `raw/`. Now always read from `meta/`, which is the
ground truth, is always present, and is what `make verify` re-proves against the
bytes.

## First real ingest, 2026-09-05

60 papers (1995–2026) into `areas/neoantigens/`, 266 MB. 60 ingested, 0 refused;
`--doi-map` supplied 4 identifiers the PDFs do not print, `--doi-override`
corrected 2 preprint DOIs. All 60 sidecar hashes re-verified against the bytes in
`raw/` before the inbox was cleared.

`find_doi` was validated against ground truth rather than asserted: all 59 papers
carrying a PMID were resolved through NCBI `esummary` and compared with what the
extractor returned - 54 agree, 3 not found (supplied by `--doi-map`), 2 disagree
(both published articles whose PDFs print only their preprint DOI, corrected by
`--doi-override`).

**Prose and taxonomy, same day.** All 60 sidecars had their four prose sections
written by reading the papers, installed through the new `scripts/write_prose.py`.
The taxonomy is 14 topics in 5 parts, drawn by reading and following the pathway a
candidate neoantigen has to survive - presentation, recognition, discrimination and
escape, clinical translation, and the resources and benchmarks underneath. Final
state: 60 papers, 14 topics, 0 unfiled, `make audit` no problems, `make verify`
60/60 hashes intact, `make test` all checks passed.

## Second batch, 2026-09-05

57 more papers (1993-2026) from `lit2.7z`, 58 files of which one was refused as a
byte-identical duplicate. Ten had no usable DOI - publisher-internal filenames with
no PMID - and were resolved by reading each first page and matching the title
against Crossref, then fetching each candidate DOI back to confirm the registered
title matched the paper. Two of those ten were wrong-DOI extractions rather than
missing ones: a Zenodo software citation picked up instead of the article (MMseqs2),
and a truncated iScience DOI. Both unregistered at Crossref, so `--doi-map` covered
them and no override was needed.

Prose for all 57 written by reading. The taxonomy was then revised from 14 topics
over 60 papers to **18 topics over 117**, with criteria fixed in
`eval/reclustering.json` before the candidate existed and before the batch-2 papers
were read. Four topics are new, two were renamed, and **0 of the 60 batch-1 papers
changed topic**. Score: 6 MUSTs and 3 SHOULDs pass, 2 SHOULDs declared not measured
(one of them, cohesion, because the criteria file states its circularity in
advance). Full result and the caveats on two of the passes are in
`reports/2026-09-05_reclustering_score.txt`.

Final state: 117 papers, 18 topics, 0 unfiled, 117/117 hashes intact, `make audit`
no problems, `make test` all checks passed, 882 neighbour links on the map.

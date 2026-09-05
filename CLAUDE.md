# CLAUDE.md — how to work in this repository

**PaperLib**: several independent collections of published papers, each browsable
as a static web page with its own topics and its own similarity map. Read
`README.md` first if you have not; it is the runbook. This file is the standing
rules.

Derived from `teamlibrary-toolkit` (see `docs/PROVENANCE.md`), whose rules were
learned by getting things wrong. Where a rule has a scar, the scar is written next
to it, because a rule with no reason attached is a rule that gets optimised away by
the next person in a hurry.

---

## 1. The shape

```
scripts/   SHARED. One copy, every area.
src/       SHARED. The page: index.html, app.js, app.css. No framework, no bundler.
inbox/     SHARED drop point. inbox/<area>/paper.pdf names the area.
areas/<a>/ ONE COLLECTION, self-contained:
    raw/        the source files. ADD-ONLY.
    meta/       one sidecar per source: frontmatter + Abstract/Summary/Key points/Limitations
    outputs/    the literature review. THE TAXONOMY LIVES HERE, not in a config file.
    annotations/ the taxonomy spec, the review prose, the edit ledger
    data/       generated: library.json, similarity.json, bib_cache.json
    dist/       generated: three files, works over file:// with no server
    inbox/ reports/ eval/
index/     generated: registry.json — which areas hold which bytes
dist/      generated: the portal listing every area
```

`areas/<a>/` has exactly the shape the upstream toolkit's root had. That is why the
toolkit's scripts run inside one unchanged, and it is worth preserving: an area can
be tarred, handed to somebody, and used on its own.

`data/library.json` is the contract between the build and everything downstream.
Read `scripts/build.py`'s docstring; it is the specification.

---

## 2. The rules, in order of how much damage breaking them does

### 2.1 The area is never guessed

A subdirectory of `inbox/` names it, or `--area` does, or `AREA=` does. With
exactly one area it may be omitted because there is nothing to choose between;
with two, `scripts/paperlib.py` **refuses rather than picks**.

Filing a paper in the wrong area does not misplace it in a list. It puts it in a
different collection, under a different taxonomy, on a different map — and the
similarity map will then quietly place it among papers it has nothing to do with.
The toolkit's rule that the vectors may propose but must not decide applies here
with more force than it does to topics.

### 2.2 `raw/` is add-only

A new file may be added. **No existing file may be modified, renamed or deleted.**
Every `sha256:` in `meta/` is a claim about a byte sequence and `make verify`
re-proves those claims. Rename one file and that guarantee is gone for the whole
area, with no error anywhere.

The single permitted exception is `deploy.sh` changing file **modes** so nginx can
read them. No byte, no name, no hash changes.

### 2.3 Ask before writing to `meta/` or `outputs/`

These are the owner's words about the owner's papers. You may edit them — but
**ask every time**, and use `scripts/edit_upstream.py`, which refuses `raw/` by
name, refuses paths outside the editable directories, refuses to touch protected
identity fields, refuses to overwrite a filled field without `--allow-overwrite`,
refuses to run without approving words recorded in the plan, and round-trips line
endings byte-exactly.

That last one is not fussiness. A single careless read-modify-write turned nine
one-line field additions into a 663-insertion diff across a whole collection,
because the writer normalised CRLF to LF in every file it touched.

### 2.4 Report defects in the source data; never patch them silently

Wrong year, missing byline, truncated venue: write it in
`areas/<a>/reports/upstream_findings.md`. A quiet fix is a fix nobody can see.

### 2.5 Measure, never estimate

Every count, size or timing in a document, a docstring, a commit message or a reply
comes from a command that was actually run. If you have not measured it, write
**"not measured"**. If you cannot determine it, write **`UNVERIFIED`**. An
`UNVERIFIED` in a table is an honest deliverable; a confident wrong number survives
into a manuscript.

### 2.6 Deterministic builds

Same inputs, byte-identical outputs. There is deliberately no wall-clock timestamp
in `library.json` or `manifest.json`: both carry `data_as_of`, derived from the
inputs. An unchanged rebuild is then a no-op for git, so a dirty tree means the
data really moved rather than that somebody ran `make`.

### 2.7 The page must work from a clean directory

No server, no network, no build step. `dist/` is three files and the index is
**embedded** in the HTML rather than fetched, because `fetch()` is blocked over
`file://`. No CDN, no web fonts, no analytics. The check is
`make ui AREA=<a>` — which defaults to the `file://` URL for exactly this reason.

---

## 3. The register the page has to keep

The browser presents someone else's carefully hedged text. The hedges are content.

- **The summaries are paraphrases, not quotations, and the page is not a source.**
  Every record links the paper itself. This must stay visible on the page.
- **A paper being present is not an endorsement.** Where the notes record
  scepticism, preserve it as readily as praise.
- **Never fabricate.** No invented DOIs, counts, versions, sizes or timings.
- **Absent, not truncated.** A paper with no registered author list gets no author
  list — never a partial one reconstructed from a PDF byline. A byline parser was
  measured against a real corpus and rejected; the failure mode is that it looks
  right.

---

## 4. Things that are true and non-obvious

**Each area has its OWN map, and that is the point.** Neighbours are computed
within an area, so a paper's neighbours are the papers it is actually being read
against. One shared map across every area would put a neoantigen paper next to
whatever else happened to use the word "prediction".

**"area" means two different things, and only one of them is ours.** `area:` and
`also_in_areas:` are this project's: which collection a paper is in, and which
others hold the same bytes. `duplicate_of_area` is the upstream toolkit's, and
means a paper filed under a second **topic** inside one review. Do not merge them.

**A part LETTER is a position, not an identity.** Renumbering parts moves topics
between them silently. Every topic carries `part_name` beside `part` so the two can
be checked; `make_review.py` is fatal on a mismatch. In a real collection, dropping
one part and renumbering left three pure-mathematics papers filed under
cardiovascular medicine.

**The similarity map is TF-IDF over the summaries.** It groups by shared
vocabulary, which is not the same as subject. Anything that systematically appears
in the summaries becomes an axis of the space — including, in one real case, the
name of whoever circulated the paper.

**The neighbour lists come from the full space, never from the 2-D map.** The map
is a projection and loses information; two dots that look adjacent may not be
neighbours.

**The map's layout is cached per area and keyed by sha256**, so adding papers
*places* them into the existing layout rather than reshuffling it. A map that
rearranges itself every week cannot be learned.

**`make audit` reads data; it cannot see the page.** Both UI defects that reached a
real user — a facet showing 6 of 45 topics behind a scroll window, and a map that
lost height whenever a filter appeared — were invisible to every data check,
because nothing was wrong with the data. `make ui` renders the page and asserts
what a reader sees. Keep both.

---

## 5. Pitfalls

<!-- append here when a mistake is made twice -->

- **Sidecar frontmatter cannot be split on `---`.** The block itself contains
  comment rules like `# --- identity ---`. Match `^---\n(.*?)\n---\n` with DOTALL,
  or you will silently parse empty frontmatter for every file and report zero
  coverage for every field.
- **Source filenames are the join key** and contain spaces, parentheses,
  semicolons and non-ASCII characters. Never normalise them. Percent-encode for
  URLs, quote in the shell, use `<…>` in markdown links.
- **Path arguments are resolved relative to the AREA, not the working directory.**
  `--out outputs`, not `--out areas/x/outputs`. In a single-collection tree those
  were the same place; here they are not, and the second writes
  `areas/x/areas/x/outputs/`, which `make build` then reports as a missing review.
  Measured 2026-09-05, on the first run of this project.
- **A script copied into a fixture tree needs `paperlib.py` beside it and
  `PAPERLIB_AREA_ROOT` set.** Otherwise `selftest.py` either refuses to run or —
  much worse — resolves to the real collection and tests that instead.
- **An identifier read off a PDF can be well-formed and still wrong**, which is
  worse than absent: absent is refused loudly. Measured on 60 real papers — a DOI
  broken across a line yields a truncated prefix, PNAS appends `/-/DCSupplemental`,
  PLoS mints a DOI per figure, and a published article's PDF may print only its
  preprint DOI (`posted-content`, no venue). `find_doi` takes the most frequent
  candidate after normalising; `--doi-override` is the audited way to correct the
  last case, and `--doi-map` is still only a fallback for when nothing is found.
- **Never re-derive a surname by splitting a joined display name.** Crossref
  returns `given` and `family` separately; use `registered_first_family`. Splitting
  turned `Juan C. Almagro` into `CAlmagro` and `Mathias Fynbo Jensen` into
  `FynboJensen`. The filename is the join key and `raw/` is add-only, so a wrong
  surname is permanent — check generated names before `--apply`, never after.
- **Duplicate checks must compare against THIS RUN, not just the collection on
  disk.** Two byte-identical files in one inbox both passed sha256, DOI and
  filename checks, both planned the same `raw/` name, and the second would have
  overwritten the first with no error - an add-only violation that is silent.
- **`library.json` is a build product and goes stale the moment you ingest.**
  Anything asking what the collection holds must read `meta/`, which is the ground
  truth, is always present, and is what `make verify` re-proves against the bytes.
- **A width-derived size on a page whose height changes is a feedback loop.** The
  map's height came from its own width; its width depended on whether a scrollbar
  was present; the scrollbar depended on what was rendered below it. Fixed with
  `html { scrollbar-gutter: stable; }`.
- **A closed, scrolling list must say how many items it holds.** 45 topics behind a
  232 px window showed six, and the reader's reasonable conclusion was that the
  taxonomy was incomplete.
- **Pin the evaluation pool to one named review file.** Regenerating a review
  otherwise changes the denominator and scores move with nothing else changed.
- **`outputs/` is a dated snapshot, not a live view.** Never quote a number out of
  it as the current state; measure `meta/`.
- **A warning that fires on every build forever is how people learn to stop reading
  warnings.** `has_roster: false` in `paperlib.json` is why the missing
  `wiki/group.md` is a declared absence rather than a permanent complaint. Declare
  such things; do not delete the check.

---

## 6. Conventions

- **Python 3.12, standard library first.** `paperlib.py`, `build.py`, `render.py`,
  `audit.py`, `make_review.py`, `ingest_inbox.py`, `route_inbox.py`, `portal.py`,
  `new_area.py`, `areas.py` and `selftest.py` import nothing outside it, so a fresh
  clone can produce a page before pip has run. Only `embed.py` (numpy/scikit-learn/
  umap) and `ui_check.py` (playwright) need the venv. Ask before adding a
  dependency.
- **Comment the reason, not the mechanism.** `# increment i` is noise; `# the
  review writes the surname FIRST, so the last token is not the surname` is the
  comment that stops the bug coming back.
- **Writing scripts are DRY RUNS by default.** `new_area`, `route_inbox`, `inbox`,
  `example`, `edit` all print what they would do and write nothing until `--apply`.
  Discovering that a directory tree, or a collection, was created is worse than
  typing seven more characters.
- **Never force-push.**
- **Print the diff loudly and fail the build on `gone`.** A paper silently absent
  from a rebuild is the defect nobody notices.

---

## 7. Commands

Every collection-touching target takes `AREA=<name>`.

```
make help                 what every target does
make areas                list the areas and what each holds
make new-area NAME=x      scaffold a new area                    (DRY RUN; APPLY=1)
make all                  update every area, then the portal

make route                shared inbox/ -> areas/<a>/inbox/      (DRY RUN; APPLY=1)
make inbox AREA=x         DRY RUN over that area's inbox

make update AREA=x        build + embed + render (no network, idempotent)
make build AREA=x         meta/ + newest review -> data/library.json
make embed AREA=x         vectors, neighbours, that area's own 2-D map (needs venv)
make render AREA=x        library.json + shared src/ -> areas/x/dist/
make bib   AREA=x         Crossref/arXiv for new DOIs only        (NETWORK)

make review AREA=x        regenerate the literature review -> reports/ (a draft)
make topics AREA=x        propose topics for unfiled papers -> reports/ (a draft)
make audit  AREA=x        validate library.json against every other source
make verify AREA=x        re-hash every source against its sidecar
make ui     AREA=x        drive the built page in a real browser  (needs playwright)
make test                 build.py self-test against a synthetic fixture tree
make portal               index/registry.json + dist/index.html
make deploy               publish every built area + the portal
```

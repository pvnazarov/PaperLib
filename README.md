# PaperLib

Several independent collections of published papers — one per research **area** —
each browsable as a static web page: by topic, author, journal, year and type, with
a similarity map that places every paper next to the ones it resembles, and
full-text search over titles, author lists, abstracts, summaries and key points.

Each area's page is **three files** — `index.html`, `app.js`, `app.css` — that work
from a directory with no server, no network and no build step. No framework, no
bundler, no CDN, no analytics.

The first area is `neoantigens`. Adding the next one is a single command.

## What an area is

A complete collection, self-contained in `areas/<name>/`: its own papers, its own
taxonomy, its own similarity map, its own page. Areas are worked on independently
and do not share a taxonomy, so a paper's neighbours on the map are the papers it
is actually being read against.

The price of that independence: a paper relevant to two areas is stored in both.
The ingest detects it by sha256, says so, and records the other area in the sidecar
as `also_in_areas`, so the second copy never arrives without a trace of the first.

## How it fits together

```
inbox/<area>/            drop PDFs here
      │  make route                       decides WHICH collection — never guessed
      ▼
areas/<area>/inbox/
      │  make inbox AREA=<area>           dry run: DOI, registration, the new name
      │  ingest_inbox.py --apply
      ▼
areas/<area>/raw/        the source files, add-only, hashed
             meta/       one sidecar per paper: identity + four prose sections
                │                            ← written BY READING THE PAPER
                │  make review
                ▼
             outputs/<date>_literature_review.md    THE TAXONOMY LIVES HERE
                │  make build              ──▶ data/library.json
                │  make embed              ──▶ data/similarity.json  (this area's map)
                │  make render             ──▶ dist/  (the three files)
                ▼
      make portal  ──▶ dist/index.html     the front door, listing every area
      ./deploy.sh  ──▶ /var/www/html/paperlib/<area>/
```

`make update AREA=<a>` runs build + embed + render. It needs no network and is
idempotent: run it twice with nothing new and the second run changes no byte.
`make all` does that for every area, then rebuilds the portal.

## Start here

```bash
make areas                      # what exists and what each area holds
make help                       # every target
```

### Adding papers

```bash
cp some-paper.pdf inbox/neoantigens/
make route                                    # DRY RUN — read it
make route APPLY=1

make inbox AREA=neoantigens                   # DRY RUN — read it
python3 scripts/ingest_inbox.py --apply --approved "the owner said: go ahead"
```

The ingest renames each file to `Surname(YEAR) Venue; Title.ext`, copies it to
`raw/`, hashes it, and writes a sidecar with the identity fields and the registered
byline. **What it refuses, and why each refusal is right:**

| Refusal | Why |
|---|---|
| identical bytes already in this area | the same paper twice under two names is a duplicate you will not notice later |
| no DOI on pages 1–3 | the bibliography is keyed on an identifier; supply it with `--doi-map` |
| the DOI is not registered at Crossref | title, venue, year and byline come from the registration, so an unregistered DOI means those fields would be guesses |
| `raw/<name>` already exists | `raw/` is add-only |

Identical bytes **in another area** are not refused — they are reported and
recorded.

### Then write the prose

**This is the step that cannot be automated away, and the quality of everything
downstream is set here.** The ingest writes a placeholder and `status:
prose-pending`; the four sections have to be written by something that read the
paper. In `areas/<a>/meta/<name>.md`:

- **`## Abstract`** — 2–4 sentences. What the paper did. This is the text the
  similarity map is built from, so it decides where the paper lands.
- **`## Summary`** — a paragraph or three. What it found and how.
- **`## Key points`** — a `- ` list. Specific claims, not topic labels.
- **`## Limitations`** — what the paper does *not* support. Write this even when
  the paper does not; especially then.

Paraphrase, never quote: these summaries are read *instead of* the paper by people
in a hurry, the page says so in its footer, and that claim has to stay true.

```bash
grep -l 'status: prose-pending' areas/neoantigens/meta/*.md | wc -l
```

### Then decide the topics

The taxonomy is **parts** (broad, lettered) containing **topics** (what a reader
browses). Every paper sits in exactly one topic, and it lives in
`areas/<a>/annotations/taxonomy.json`. `make topics AREA=<a>` will propose some
from your own summaries — use the proposals to notice papers you have mis-filed,
not as an answer. TF-IDF groups by shared vocabulary, and vocabulary and subject
part company more often than is comfortable.

```bash
python3 scripts/make_review.py --from-sidecars \
        --taxonomy annotations/taxonomy.json --out outputs   # paths are AREA-relative
make update AREA=neoantigens
make audit  AREA=neoantigens
```

### Adding an area

```bash
make new-area NAME=immunopeptidomics            # DRY RUN
make new-area NAME=immunopeptidomics APPLY=1
```

From then on every collection-touching target needs `AREA=`, because with more
than one area the tool refuses to pick for you.

## Requirements

Measured on this machine, 2026-09-05:

- Python 3.12.3 — standard library only for everything except the two below.
- `make embed` needs numpy, scikit-learn and umap-learn: `make venv`.
- `make ui` needs playwright plus a Chromium download (`.venv/bin/playwright
  install chromium`, ~115 MB, separate from the pip package).
- `make inbox` needs `pdftotext` (poppler-utils, present) and network access to
  Crossref.

## What it is not

- **Not a reference manager.** It does not fetch PDFs, chase citations or manage a
  BibTeX file. It presents papers you already have.
- **Not automatic.** The four prose sections are written by reading the paper, the
  topics are decided by reading, and the area is named by a person. The similarity
  vectors may propose; they must not decide. That is a design position, not a
  limitation waiting to be lifted.
- **Not a search engine.** Everything is client-side over an embedded index, which
  is why it works offline and why it is not the right shape for a million papers.

## Provenance

Built on `teamlibrary-toolkit`, extracted from a working 340-paper instance. See
`docs/PROVENANCE.md` for what was reused, what was changed and why. `CLAUDE.md` is
the standing rules.

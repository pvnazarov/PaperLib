# Installing PaperLib on another machine

What a clone gives you, what it deliberately does not, and the order the two have
to be put together in.

The repository is **small and complete except for the papers**: ~6 MB, and it
already contains every sidecar, the literature review, the taxonomy,
`library.json` and `similarity.json`. So a fresh clone can render the full page —
map, facets, search, digest — before a single PDF is copied. What it cannot do is
link to a PDF, because the PDFs are not in git and never will be.

## What comes from where

| | Where it lives | Size | Notes |
|---|---|---|---|
| `scripts/`, `src/`, `Makefile`, `docs/` | git | — | the toolkit |
| `areas/*/meta/` | **git** | 548 KB | the sidecars. Tracked on purpose — see `.gitignore` |
| `areas/*/outputs/` | **git** | 356 KB | the literature review, i.e. the taxonomy. Tracked |
| `areas/*/annotations/`, `eval/` | git | — | taxonomy.json, the edit ledger |
| `areas/*/data/library.json`, `similarity.json`, `manifest.json`, `bib_cache.json` | git | 875 KB | deterministic, so an unchanged rebuild is a git no-op |
| **`areas/*/raw/`** | **copy by hand** | **551 MB, 125 files** | publisher PDFs. `.gitignore`d: large, and a git history cannot forget them |
| **`areas/*/data/embed_cache.npz`** | **copy by hand** | 358 KB | the per-paper vectors, keyed by sha256 |
| **`areas/*/data/embed_model.pkl`** | **copy by hand** | 449 KB | the *fitted* UMAP layout |
| `areas/*/dist/`, `dist/`, `index/registry.json` | regenerated | — | `make update` / `make portal` |
| `.venv/` | rebuilt | 6.1 GB | **do not copy it.** `make venv` |

`meta/` and `outputs/` are already in git, so copying them by hand is a harmless
no-op rather than a step — but the two files in `data/` above are easy to miss and
are not optional if you want the map to stay put (below).

### Why the two embed files matter

`similarity.json` is tracked, so the *existing* map transfers with the clone and
the page renders it correctly with no venv installed at all. But `embed_cache.npz`
and `embed_model.pkl` are what let a *new* paper be `.transform()`-ed into that
already-fitted layout. Without them, the next `make embed` has to refit from scratch, which costs two
things. It produces a **different map** — every paper's position and neighbour
list moves at once, and a map that rearranges itself cannot be learned. And it
needs **network access to HuggingFace**: `embed.py` builds the encoder with
`SentenceTransformer("NeuML/pubmedbert-base-embeddings")` and no local-files
guard, so a machine that has never run it downloads the model (the cache here is
1.7 GB in `~/.cache/huggingface`, outside the repo and not part of any copy).

Copy the two files.

## The order matters

Copy `raw/` **before** the first `make build`. `build.py` checks each sidecar's
`source:` against the bytes in `raw/` and writes the result into `library.json` as
`file_ok`; `src/app.js` only renders a paper's PDF link when `file_ok` is true. So
a build run against an empty `raw/` flips all 125 records to `file_ok: false`,
which shows up as a 125-line diff on a tracked file and a page with no PDF links
that otherwise looks perfect.

It is recoverable — `git checkout areas/*/data/library.json`, or just rebuild once
the PDFs are there — but it is much easier not to do.

## Steps

### 1. Clone

```bash
git clone https://github.com/pvnazarov/PaperLib.git paperlib
cd paperlib
```

SSH (`git@github.com:pvnazarov/PaperLib.git`) works too and is what you want if
you intend to push back from the work server.

Requirements on the target: **Python 3.12+** (3.12.3 here), `make`, and
`poppler-utils` for `pdftotext` — that last one only for `make inbox`. Everything
in `make build` / `make render` is standard library only.

### 2. Copy the papers

Use `rsync`, not a shell loop and not a zip round-trip through a non-UTF-8
filesystem: the filenames carry spaces, semicolons, parentheses and non-ASCII
(`Keşmir`, `Łuksza`, `Koşaloğlu-Yalçın`, and a curly apostrophe in `O’Brien`).
Those are the names the sidecars' `source:` fields and the sha256 manifest are
keyed on, so a mangled filename is a broken paper. If they do get mangled anyway,
`make fix-names` repairs it: it hashes every file in `raw/`, looks the sha256 up
in the sidecars, and renames each file to the `source:` its own bytes prove it
should have. It names the cause it found (normalisation vs truncation), is a dry
run unless `APPLY=1`, and refuses any rename that would overwrite an existing
file. That is a rename inside add-only `raw/` and the exception is narrow: it
runs only where the join is *already* broken, and it restores the name the
sidecar declares rather than inventing one. `make verify` afterwards is the proof.

Two mangles seen in practice: **NFD normalisation**, when `raw/` is copied via a
machine whose filesystem decomposes accents (macOS) while `meta/` came from `git
clone`, which stores NFC — the two then disagree even though both look identical
in a terminal. And **truncation**: the longest sidecar name here is 253 bytes,
which fits ext4 and APFS but not eCryptfs (~143) or a Windows path.

```bash
# from the source machine, for each area:
rsync -av --progress \
  ~/ai/paperlib/areas/neoantigens/raw/ \
  user@work-server:/path/to/paperlib/areas/neoantigens/raw/

rsync -av \
  ~/ai/paperlib/areas/neoantigens/data/embed_cache.npz \
  ~/ai/paperlib/areas/neoantigens/data/embed_model.pkl \
  user@work-server:/path/to/paperlib/areas/neoantigens/data/
```

`raw/` and `areas/*/inbox/` do not exist in a clone; `rsync` creates `raw/` on the
way in. The inbox directories are created by the ingest when you need them, and
`make route` / `make inbox` say "no inbox/ — nothing to do" until then rather than
failing.

If this installation already existed and you are bringing it up to date rather
than creating it, the filenames in `raw/` may be behind the sidecars — see
`docs/PROPAGATING-CORRECTIONS.md`, which is one `make fix-names APPLY=1` per area.

### 3. Prove the copy

```bash
make verify AREA=neoantigens   # re-reads and re-hashes every PDF against its sidecar
make areas                     # 'src' column should now read 125, not 0
```

`make verify` is the real check: it re-proves that every sha256 in `meta/` matches
the bytes that arrived. If it passes, the collection is byte-identical to the
source machine and nothing else about the transfer can be wrong.

A failure reading ``sidecar `source:` does not resolve in raw/`` is the filename
problem above, not a missing paper: the bytes arrived, under a name the sidecar
does not recognise. `make fix-names` reports which files drifted and why, and
`make fix-names APPLY=1` puts them back. A `sha256 MISMATCH` is the other thing
entirely — those bytes really are different, and no rename will fix it.

### 4. Build the page

```bash
make build  AREA=neoantigens
make render AREA=neoantigens
make portal
git status --short              # expect: clean
```

A clean tree here is the whole point of the tracked, deterministic build outputs:
it says the rebuild on the new machine produced the same bytes as the old one. A
dirty `library.json` means something really differs — check `file_ok` first
(step 3 skipped or incomplete).

Then open it with no server at all:

```
file:///path/to/paperlib/areas/neoantigens/dist/index.html
```

PDF links resolve through a relative `pdf/` base, so they only work once the page
is served with `pdf/` pointing at `raw/` — see step 6. Everything else (map,
facets, search, digest) works from `file://`.

### 5. The venv — only if you will add papers

Not needed to build or serve the existing collection.

```bash
make venv                              # numpy, scikit-learn, umap-learn, sentence-transformers
.venv/bin/playwright install chromium  # only for `make ui`; ~115 MB, separate
```

`requirements.txt` pulls `sentence-transformers` and through it torch — the venv
here measures 6.1 GB, and the first `make embed --refit` adds a ~1.7 GB
HuggingFace model cache under `~/.cache/huggingface` on top of that. Only `make embed`, `make topics` and `make ui` need it;
`make build`, `make render`, `make portal`, `make verify` and `make test` are
standard library only and will run on a machine with nothing installed.

Sanity check without any of it:

```bash
make test    # build.py self-test against a synthetic fixture tree
```

### 6. Serving it

Three options, cheapest first.

**a. Don't.** `file://` on the built `index.html` is a complete, working page for
everything but the PDF links.

**b. `deploy.sh` — copy into a web root.** Publishes `dist/` per area and makes
`<area>/pdf` a **symlink** to `raw/`, then verifies over HTTP that nginx really
follows it:

```bash
./deploy.sh --dest /var/www/html        # the default
./deploy.sh --check                     # verify only, change nothing
```

It also `chmod o+x` the `raw/` directory and `o+r` any file that arrived mode 600,
because nginx runs as `www-data` and cannot otherwise read them. Modes only — no
byte, name or hash changes, so `make verify` still passes afterwards. The web root
must be writable by whoever runs it.

**c. `nginx-install.sh` — serve by alias, no copy.** It generates one pair of
`location` blocks per area by looping over `areas/*/`, so a new area is picked up
by re-running it — but it is still **partly specific to the home server**: it
appends to `/etc/nginx/snippets/alcmaeon-common.conf`, a file that exists only
there, and prints `https://hatkapina.cc/...` at the end. Before running it
elsewhere, set:

- `SNIPPET=` → whichever nginx conf file the work server actually includes
- the closing URLs it prints → cosmetic, but wrong

**Re-run it after adding an area.** Until you do, the new area's URL 404s while
every existing one keeps working, because the installed block does not mention it.

`X-Robots-Tag: noindex, nofollow` in that block keeps the collection out of search
indexes; `nginx-noindex.conf` does the same job for the `deploy.sh` model, in one
prefix location that covers current and future areas. Pick one model, not both.
Either way it is **not access control** — anyone with the URL reads everything. If
the work server is internet-facing, that distinction is the thing to decide before
publishing a few hundred publisher PDFs, not after.

## Note on what is public

The GitHub repository is **public**: `meta/` (all 125 summaries) and `outputs/`
(the literature review) are world-readable, which is why step 1 needs no
credentials. The PDFs are not there — `raw/` is `.gitignore`d — so no publisher
bytes are being redistributed. If the summaries should not be public either, that
is a repository-visibility change, not an install step.

## If something is wrong

| Symptom | Cause |
|---|---|
| page renders, no PDF links | `make build` ran before `raw/` was copied → `file_ok: false`. Copy, rebuild |
| `make verify` reports a hash mismatch | the transfer mangled a filename or truncated a file. Re-`rsync` that one |
| `make areas` shows `src 0` | `raw/` is empty or in the wrong place |
| `make embed` says "no installed venv" | `make venv` — numpy/sklearn/umap are not system-wide |
| the map reshuffles after adding a paper | `embed_cache.npz` / `embed_model.pkl` were not copied, so it refit |
| PDFs 404 through nginx, page fine | `raw/` lost `o+x`/`o+r`, or nginx is not following the symlink. `./deploy.sh` fixes the modes |
| `make build` refuses to pick an area | expected, once there are two. Pass `AREA=` |

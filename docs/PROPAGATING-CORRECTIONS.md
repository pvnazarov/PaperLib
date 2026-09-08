# Propagating the 2026-09-08 title corrections to another installation

Ten titles were corrected on 2026-09-08, and nine of them changed a filename in
`raw/`. **`raw/` is not in git**, so a `git pull` brings the corrected sidecars
to another installation and leaves its PDFs under the old names — every one of
which then fails to resolve. This is the procedure that closes that gap.

It is two commands, and the second one is the whole point:

```bash
git pull
make fix-names AREA=<area> APPLY=1     # for each area
make verify    AREA=<area>             # must say: no problems
make render    AREA=<area>
make portal
```

## Why `make fix-names` is the right tool and a rename script is not

It matches each PDF to its sidecar **by sha256**, then renames the file to the
name that hash proves it should carry. It never guesses from string similarity,
so it repairs any drift — these corrections, an older naming convention, a
transfer that mangled a name — without being told what changed.

Verified on this machine, 2026-09-08, by simulating exactly the state another
installation will be in:

```
renamed one PDF back to its pre-correction name
make verify      ->  2 failures ("sidecar `source:` does not resolve in raw/")
make fix-names   ->  correct 185 · to rename 1 · orphan 0 · absent 0
                     RENAME ...MLLr + AML genome.pdf
                         -> ...MLLr+ AML genome.pdf
                            differs in title (older naming convention?)
make fix-names APPLY=1  ->  renamed 1
make verify      ->  no problems
```

## What travels in the pull, and what does not

| | Travels? | Note |
|---|---|---|
| `scripts/ingest_inbox.py` (`strip_markup`) | **yes** | the actual bug fix; future ingests are clean |
| `areas/*/meta/*.md` — titles **and filenames** | **yes** | tracked, so renames arrive as git renames |
| `areas/*/outputs/`, `annotations/taxonomy.json` | **yes** | tracked |
| `annotations/upstream_edits.json` | **yes** | the ledger, incl. the repointed entries |
| `data/library.json`, `manifest.json`, `similarity.json` | **yes** | tracked and deterministic |
| `reports/upstream_findings.md` + the correction reports | **yes** | why each case was or was not touched |
| **`areas/*/raw/` filenames** | **NO** | `.gitignore`d — this is what `make fix-names` repairs |
| `data/embed_cache.npz`, `embed_model.pkl` | no | **unaffected**: keyed by sha256, and no PDF byte changed, so the map does not move |
| `areas/*/dist/`, `dist/` | no | regenerate with `make render` + `make portal` |

## Check it landed

```bash
make verify    AREA=<area>     # no problems
make audit     AREA=<area>     # 0 problems  <- see below
make fix-names AREA=<area>     # nothing to do
```

**Run `make audit`, not just `make verify`.** Renaming a file orphans every edit
ledger entry that names it, and `build.py` does not notice: it only complains
when it *finds* the file and the hash differs. During this work `make verify`
passed both areas clean while `make audit` found 4 problems in one and 12 in the
other. The pull carries the repointed ledger, so a plain pull + `fix-names`
should be clean — but audit is the check that would say otherwise.

## The corrections themselves

Eight were **ours**: `ingest_inbox.clean_title` stripped Crossref's inline markup
with a bare `re.sub` and then collapsed whitespace, so the XML pretty-printing
indentation survived as a real space.

    NPM1 -mutated      -> NPM1-mutated        Arellano(2025)     aml
    NPM1 -mutant       -> NPM1-mutant         Damaskou(2025)     aml
    TP53 -mutant       -> TP53-mutant         Spinella(2026)     aml
    TP53 -Y220C–mutant -> TP53-Y220C–mutant   Carter(2025)       aml
    NUP98 -rearranged  -> NUP98-rearranged    Michmerhuizen(2020) aml
    FLT3 -Mutant       -> FLT3-Mutant         Sabatier(2023)     aml
    CD8 +              -> CD8+                Chowell(2015)      neoantigens
    ProsperousPlus :   -> ProsperousPlus:     Li(2023)           neoantigens   [title only]

Two were **upstream overrides** — no markup involved, the space is in the
registration itself, so these override a publisher's deposited title and are
recorded individually in the ledger with the registration quoted verbatim:

    N 6 -Methyladenosine -> N6-Methyladenosine   Li(2017)   aml   seq 565
    MLLr + AML           -> MLLr+ AML            Fu(2025)   aml   seq 566

One candidate was **deliberately not corrected**: `single cell -omics`
(Baronas 2025). Its space is in the registration and no evidence was found that
the publisher meant otherwise. See `areas/aml-transcriptomics/reports/upstream_findings.md`.

`ProsperousPlus` is title-only: filenames strip colons, so its filename never
carried the artifact and `make fix-names` will not touch it.

## If the other installation has papers this one does not

`make fix-names` reports them as `orphan` (a PDF with no matching sidecar) or
`absent` (a sidecar whose bytes are missing) and renames neither. Both counts
were 0 here. An `orphan` is not an error by itself — it is a PDF this repository
has no record of, and it wants a person, not a rename.

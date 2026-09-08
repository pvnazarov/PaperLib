# raw/ filename correction on import, 2026-09-08

**What happened.** `raw.7z` (files.sablab.net/copy, 1,032,620,022 bytes, 186 files)
was unpacked into this area's empty `raw/`. All 186 papers were present and
**byte-perfect** — every `sha256:` in `meta/` matched a file in the archive, 0
missing — but 143 of them carried an earlier naming convention that used
abbreviated venues, so the filename join to the sidecars failed for those 143:

    Abla(2024) Blood Adv; ...        (archive)
    Abla(2024) Blood Advances; ...   (sidecar `source:`)

`make verify` reported 143 × "sidecar `source:` does not resolve in raw/". Nothing
was wrong with the bytes; only the names were stale.

**What was done, and under what approval.** The 143 files were renamed to their
sidecar `source:` values. `raw/` is add-only (CLAUDE.md §2.2), so this is a
recorded deviation, not a routine step. The owner approved it explicitly:

> "file names of sidecars and paper PDF should match. It is allowed to use short
> names for journals. If needed with a permission it is allowed to correct raw.
> please go on"

**Why the rename is safe rather than a guess.** Every rename was chosen by exact
sha256 identity, not by string similarity: each file's hash selected exactly one
sidecar, and that sidecar's `source:` supplied the new name. Checked before
renaming — all 186 target names unique, and no target collided with a different
file's current name, so a direct rename needed no temp-name pass. No byte was
touched; only names changed, and the hash claims they are keyed on still hold.

**Evidence it worked.**

    make verify AREA=aml-transcriptomics   ->  build: no problems
    make build                              ->  186/186 file_ok true
                                                library.json byte-identical to git
    git status                              ->  clean

A clean tree is the strong result: this copy now reproduces the build made on the
machine the area was created on, byte for byte.

**Defect noted, not patched (CLAUDE.md §2.4).** One sidecar's registered title
carries a stray space that the rename has now propagated into a filename:

    Arellano(2025) Blood; Menin inhibition with revumenib for NPM1 -mutated ...
                                                                    ^

The archive's older name had `NPM1-mutated`. The sidecar value came from the
Crossref registration and is what the join key must match, so it was followed
rather than silently "fixed". Correcting it means changing the sidecar and the
filename together, which is an upstream edit and needs its own approval.

**The 143 renames in full:** `2026-09-08_raw_rename_map.json` beside this file,
one record per file with its sha256, old name and new name.

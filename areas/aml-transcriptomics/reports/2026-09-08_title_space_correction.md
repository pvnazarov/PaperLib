# Title/filename space correction, 2026-09-08

**The report.** The owner pointed at one filename — `NPM1 -mutated` — carrying a
space no publisher wrote. It turned out to be one instance of a systematic ingest
defect affecting **8 titles across both areas**, and the filenames built from them.

**The cause, measured not guessed.** Crossref deposits inline markup on its own
indented line inside the registered title:

    'Menin inhibition with revumenib for\n                    <i>NPM1</i>\n                    -mutated relapsed...'

`ingest_inbox.clean_title` did `re.sub(r"<[^>]+>", "", s)` and then collapsed
whitespace. Removing the tag alone leaves the XML indentation behind, and the
collapse turns it into one real space — so `<i>NPM1</i>` followed by `-mutated`
became `NPM1 -mutated`. `audit.py:506` had already noted this class of thing;
what was missing was that it reached the stored title and the filename.

**The fix.** `strip_markup()` marks where each tag stood instead of deleting it
blind, then decides per boundary: a boundary hugging punctuation that attaches to
the preceding word was layout and takes no space; anywhere else it is a word gap,
and only if it actually carried whitespace. Deliberately narrow — it fires only
where a tag stood, so a legitimate spaced dash in an unmarked title is untouched.

Proven against every registered title on disk: **8 of 312 change, and they are
exactly the intended 8.** The `single cell -omics`, `MLLr + AML` and
`N 6 -Methyladenosine` cases are all left alone; see `upstream_findings.md` for
why each was excluded.

**What was changed, per paper.** `title:` and `source:` in the sidecar, the
`meta/` and `raw/` filenames where the artifact was in them, `taxonomy.json`, and
the two `outputs/` documents. `ProsperousPlus` was title-only: filenames strip
colons, so its filename never carried the artifact.

    NPM1 -mutated      -> NPM1-mutated        Arellano(2025)
    NPM1 -mutant       -> NPM1-mutant         Damaskou(2025)
    TP53 -mutant       -> TP53-mutant         Spinella(2026)
    TP53 -Y220C–mutant -> TP53-Y220C–mutant   Carter(2025)
    NUP98 -rearranged  -> NUP98-rearranged    Michmerhuizen(2020)
    FLT3 -Mutant       -> FLT3-Mutant         Sabatier(2023)
    CD8 +              -> CD8+                Chowell(2015)      [neoantigens]
    ProsperousPlus :   -> ProsperousPlus:     Li(2023)           [neoantigens]

**Approval.** `raw/` is add-only (§2.2) and `meta/`/`outputs/` are the owner's
words (§2.3). The owner asked for the NPM1 fix, was shown that it was 1 of 11
candidates, and chose "the 9 unambiguous ones + fix the ingest". Baronas was then
dropped from that 9 on inspection, leaving 8.

**The ledger.** Renaming a file orphans every ledger entry naming it, and
`build.py` does not notice — it only shouts when it *finds* the file and the hash
differs. `make audit` does notice, and reported 4 problems in one area and 12 in
the other that the build had passed. Both directions were then resolved: 23
orphaned entries were repointed at the paths their files now live under, new
entries record the correction itself, and the two `outputs/` entries were
refreshed with the hashes those files now carry.

**Worth knowing:** run `make audit`, not just `make verify`, after anything that
renames a file. The build passed all of this in silence.

**Evidence.**

    strip_markup vs the old code, over all 312 registered titles   8 changed
    make verify   both areas                                       no problems
    make audit    both areas   5,925 checks                        0 problems
    make build    both areas                                       DIFF all zero

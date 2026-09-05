#!/usr/bin/env bash
#
# Publish the portal and every built area to the nginx web root.
#
#     /var/www/html/paperlib/index.html          the portal   (dist/index.html)
#     /var/www/html/paperlib/<area>/             one area's page
#     /var/www/html/paperlib/<area>/pdf  ->  areas/<area>/raw    A SYMLINK
#
# THE SYMLINK IS THE POINT. The sources are NOT copied: a copy is a second copy
# that silently diverges from raw/ after every add-only update, while the symlink
# is current the moment the ingest finishes. The cost is three real failure modes,
# each handled here rather than left to be discovered:
#
#   1. `rsync --delete` would remove the symlink, because it does not exist in
#      dist/. Every PDF link would 404 while the page rendered perfectly. It is
#      excluded below.
#   2. nginx has to be following symlinks. It does by default and no
#      `disable_symlinks` directive need be set -- but that is a server-level
#      setting this repo cannot control, so --check VERIFIES it with a real HTTP
#      request instead of trusting the default.
#   3. Moving or renaming this repository breaks every PDF link at once, silently.
#      If the repo moves, re-run this script.
#
# THE ONE THING THAT REACHES BACK INTO THE COLLECTION: nginx runs as www-data and
# PDFs commonly arrive mode 600, so www-data cannot read them and the page returns
# 404 with `stat() failed (13: Permission denied)` in nginx's error log. This
# grants the minimum:
#
#     chmod o+x  areas/<area>/raw/      traverse, but NOT o+r -- no directory listing
#     chmod o+r  the unreadable files   read a known filename
#
# MODES ONLY. No byte, no name and no sha256 changes, so `make verify` still
# re-proves the collection is byte-intact. It runs every time because new files
# keep arriving 600.
#
# Usage:
#   ./deploy.sh                    publish every built area + the portal, then verify
#   ./deploy.sh --area neoantigens just that area (and the portal)
#   ./deploy.sh --check            verify only; publish nothing
#   ./deploy.sh --dest /some/dir   publish somewhere else (testing)
#
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHECK_ONLY=0
ONE_AREA=""
DEST_ROOT="/var/www/html"
PREFIX="$(python3 -c "import json;print(json.load(open('$SRC/paperlib.json')).get('site_dir_prefix','paperlib'))")"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --check) CHECK_ONLY=1 ;;
        --area)  ONE_AREA="${2:?--area needs a name}"; shift ;;
        --dest)  DEST_ROOT="${2:?--dest needs a path}"; shift ;;
        -*)      echo "deploy: unknown option $1" >&2; exit 2 ;;
        *)       DEST_ROOT="$1" ;;
    esac
    shift
done

BASE="$DEST_ROOT/$PREFIX"
URL_BASE="http://localhost/$PREFIX"

fail=0
say()  { printf '%s\n' "$*"; }
ok()   { printf '  ok    %s\n' "$*"; }
bad()  { printf '  FAIL  %s\n' "$*"; fail=1; }

if [[ -n "$ONE_AREA" ]]; then
    AREAS=("$ONE_AREA")
else
    AREAS=()
    for d in "$SRC"/areas/*/; do
        [[ -d "$d" ]] || continue
        AREAS+=("$(basename "$d")")
    done
fi
[[ ${#AREAS[@]} -gt 0 ]] || { echo "deploy: no areas to publish" >&2; exit 1; }

# ── publish ──────────────────────────────────────────────────────────────────
if [[ "$CHECK_ONLY" -eq 0 ]]; then
    [[ -d "$DEST_ROOT" && -w "$DEST_ROOT" ]] || {
        echo "deploy: $DEST_ROOT is not writable by $(whoami)" >&2; exit 1; }
    mkdir -p "$BASE"

    published=0
    for area in "${AREAS[@]}"; do
        adist="$SRC/areas/$area/dist"
        araw="$SRC/areas/$area/raw"
        if [[ ! -f "$adist/index.html" ]]; then
            say "deploy: SKIP $area -- no dist/index.html (run: make update AREA=$area)"
            continue
        fi
        dest="$BASE/$area"
        mkdir -p "$dest"
        # --delete so a removed file disappears from the site; `pdf` is the symlink
        # above and must survive it.
        rsync -a --delete --exclude 'pdf' "$adist/" "$dest/"

        # Recreate the symlink only when it is wrong, so a deploy does not churn it.
        if [[ -L "$dest/pdf" && "$(readlink -f "$dest/pdf")" == "$(readlink -f "$araw")" ]]; then
            :
        else
            rm -rf "$dest/pdf"
            ln -s "$araw" "$dest/pdf"
            say "deploy: (re)created $dest/pdf -> $araw"
        fi

        # Modes only; idempotent; reported.
        if [[ -d "$araw" ]]; then
            before=$(stat -c '%a' "$araw")
            [[ "$before" == *7 || "$before" == *5 || "$before" == *1 ]] || chmod o+x "$araw"
            after=$(stat -c '%a' "$araw")
            [[ "$before" == "$after" ]] || \
                say "deploy: $area raw/ mode $before -> $after (o+x to traverse; still no o+r, so no listing)"
            n=$(find "$araw" -maxdepth 1 -type f ! -perm -o+r -printf . | wc -c)
            if [[ "$n" -gt 0 ]]; then
                find "$araw" -maxdepth 1 -type f ! -perm -o+r -exec chmod o+r {} +
                say "deploy: $area made $n source file(s) world-readable (modes only)"
            fi
        fi
        say "deploy: published $area -> $dest"
        published=$((published + 1))
    done

    # The portal last: it reports per-area counts, so it must not be published
    # ahead of the pages it counts.
    if [[ -f "$SRC/dist/index.html" ]]; then
        cp "$SRC/dist/index.html" "$BASE/index.html"
        say "deploy: published the portal -> $BASE/index.html"
    else
        say "deploy: no dist/index.html -- run 'make portal'"
    fi
    say "deploy: $published area(s) published"
fi

# ── verify ───────────────────────────────────────────────────────────────────
say ""
say "deploy: verifying $BASE"
[[ -f "$BASE/index.html" ]] && ok "portal index.html present" || bad "portal index.html missing"

for area in "${AREAS[@]}"; do
    dest="$BASE/$area"
    [[ -d "$dest" ]] || { say "  skip  $area not published"; continue; }
    [[ -f "$dest/index.html" && -f "$dest/app.js" && -f "$dest/app.css" ]] \
        && ok "$area: the three files present" || bad "$area: page files missing"
    [[ -L "$dest/pdf" ]] && ok "$area: pdf is a symlink" || bad "$area: pdf is not a symlink"
    [[ -d "$dest/pdf" ]] && ok "$area: pdf resolves to a directory" || bad "$area: pdf does not resolve"

    # An absolute asset path would break the page under a subdirectory, and every
    # area lives under one.
    if grep -qE 'src="/|href="/[^/]' "$dest/index.html" 2>/dev/null; then
        bad "$area: index.html has absolute paths -- it would break under /$PREFIX/$area/"
    else
        ok "$area: no absolute asset paths"
    fi

    if command -v curl >/dev/null; then
        code=$(curl -s -o /dev/null -w '%{http_code}' "$URL_BASE/$area/" || echo 000)
        [[ "$code" == 200 ]] && ok "$area: GET $URL_BASE/$area/ -> 200" \
                             || bad "$area: GET $URL_BASE/$area/ -> $code"
        # A real source file, url-encoded the way the page links it. Proves nginx
        # follows the symlink rather than assuming it.
        # -print -quit rather than `| head -1`: under `set -o pipefail`, head
        # closing the pipe early makes find die of SIGPIPE and take the script down.
        sample=$(find -L "$dest/pdf" -maxdepth 1 -type f ! -name '.*' -print -quit)
        if [[ -n "$sample" ]]; then
            enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" \
                  "$(basename "$sample")")
            code=$(curl -s -o /dev/null -w '%{http_code}' "$URL_BASE/$area/pdf/$enc" || echo 000)
            if [[ "$code" == 200 ]]; then
                ok "$area: GET a source through the symlink -> 200 (nginx IS following symlinks)"
            else
                bad "$area: GET a source through the symlink -> $code"
                say "        'Permission denied' in nginx's error log means raw/ or its files"
                say "        lost o+x / o+r; this script fixes that on the next run."
            fi
        fi
    fi
done
[[ $(command -v curl) ]] || say "  skip  curl not installed; nothing verified over HTTP"

say ""
if [[ "$fail" -eq 0 ]]; then
    say "deploy: all checks passed — $URL_BASE/"
else
    say "deploy: CHECKS FAILED — see above" >&2
    exit 1
fi

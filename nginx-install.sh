#!/usr/bin/env bash
#
# Install (or remove) the nginx routes for PaperLib.
#
# The pages are served by ALIAS from this repository, the same way /gol/ and
# /venn/ are -- nothing is copied into the web root, so `make update` is the
# deploy and the served page is current the moment it is rendered.
#
# Deliberately NOT linked from the homepage (owner, 2026-09-05): reachable by
# link only. `X-Robots-Tag: noindex, nofollow` is what makes "by link" stay true
# rather than the collection turning up in search results. It is NOT access
# control: anyone with the URL can read everything. See --help.
#
# Safe to re-run: it refuses to append a second copy of the block, backs the
# snippet up before touching it, and RESTORES the backup if `nginx -t` fails.
#
#   sudo ./nginx-install.sh            install, test, reload, verify
#   sudo ./nginx-install.sh --remove   take the routes out again
#        ./nginx-install.sh --check    verify over HTTP; change nothing (no root)
#
set -euo pipefail

SNIPPET=/etc/nginx/snippets/alcmaeon-common.conf
MARK_BEGIN="# >>> paperlib (managed by nginx-install.sh) >>>"
MARK_END="# <<< paperlib <<<"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE=install

for a in "$@"; do
    case "$a" in
        --remove) MODE=remove ;;
        --check)  MODE=check ;;
        -h|--help) sed -n '2,26p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "unknown option: $a" >&2; exit 2 ;;
    esac
done

say() { printf '%s\n' "$*"; }
ok()  { printf '  ok    %s\n' "$*"; }
bad() { printf '  FAIL  %s\n' "$*"; FAIL=1; }
FAIL=0

# ---------------------------------------------------------------- verify --
verify() {
    say ""
    say "verifying over HTTP"
    command -v curl >/dev/null || { say "  skip  curl not installed"; return 0; }

    urls=(http://localhost/paperlib/)
    for d in "$REPO"/areas/*/; do
        [[ -d "$d/dist" ]] && urls+=("http://localhost/paperlib/$(basename "$d")/")
    done
    for url in "${urls[@]}"; do
        code=$(curl -s -o /dev/null -w '%{http_code}' "$url" || echo 000)
        [[ "$code" == 200 ]] && ok "GET $url -> 200" || bad "GET $url -> $code"
    done

    # A real paper through the alias, percent-encoded the way the page links it.
    # -print -quit rather than `| head -1`: under `set -o pipefail`, head closing
    # the pipe early makes find die of SIGPIPE and take the script with it.
    sample_area=""
    for d in "$REPO"/areas/*/; do
        if find "$d/raw" -maxdepth 1 -name '*.pdf' -print -quit 2>/dev/null | grep -q .; then
            sample_area="$d"; break
        fi
    done
    sample=$(find "$sample_area/raw" -maxdepth 1 -name '*.pdf' -print -quit 2>/dev/null)
    if [[ -n "$sample" ]]; then
        enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" \
              "$(basename "$sample")")
        read -r code ctype < <(curl -s -o /dev/null \
            -w '%{http_code} %{content_type}\n' \
            "http://localhost/paperlib/$(basename "$sample_area")/pdf/$enc" || echo "000 -")
        if [[ "$code" == 200 ]]; then
            ok "GET a paper through the alias -> 200 ($ctype)"
        else
            bad "GET a paper through the alias -> $code"
            say "        'Permission denied' in nginx's error log means www-data cannot"
            say "        traverse $REPO; check the mode of every directory on that path."
        fi
    fi

    # "By link only" is a claim this script makes on the page's behalf; check it.
    # Checked on every page AND on a PDF: a .pdf cannot carry a robots meta tag,
    # so for the papers the header is the only thing standing between the
    # collection and a search index. Google does index PDF text.
    for url in "${urls[@]}" "http://localhost/paperlib/$(basename "$sample_area")/pdf/$enc"; do
        hdr=$(curl -s -I "$url" | tr -d '\r' | grep -i '^x-robots-tag:' || true)
        [[ -n "$hdr" ]] && ok "noindex on ${url#http://localhost} (${hdr#*: })" \
                        || bad "NO X-Robots-Tag on ${url#http://localhost} -- indexable"
    done

    # The homepage must not have grown a link to it.
    if curl -s http://localhost/ | grep -qi 'paperlib'; then
        bad "the homepage mentions paperlib -- it was meant to stay unlinked"
    else
        ok "homepage does not link it (link access only, as intended)"
    fi
}

if [[ "$MODE" == check ]]; then
    verify
    say ""
    [[ "$FAIL" -eq 0 ]] && say "all checks passed" || { say "CHECKS FAILED" >&2; exit 1; }
    exit 0
fi

# ------------------------------------------------------------ preflight --
[[ "$(id -u)" -eq 0 ]] || { echo "nginx-install: needs root -- run with sudo" >&2; exit 1; }
[[ -f "$SNIPPET" ]] || { echo "nginx-install: $SNIPPET not found" >&2; exit 1; }

BACKUP="${SNIPPET}.bak.$(date +%Y%m%d-%H%M%S)"
cp -p "$SNIPPET" "$BACKUP"
say "nginx-install: backed up -> $BACKUP"

restore_and_die() {
    cp -p "$BACKUP" "$SNIPPET"
    echo "nginx-install: nginx -t FAILED; snippet restored from the backup. Nothing changed." >&2
    exit 1
}

# ------------------------------------------------------------- remove --
if [[ "$MODE" == remove ]]; then
    if ! grep -qF "$MARK_BEGIN" "$SNIPPET"; then
        say "nginx-install: the paperlib block is not present; nothing to remove."
        rm -f "$BACKUP"
        exit 0
    fi
    python3 - "$SNIPPET" "$MARK_BEGIN" "$MARK_END" <<'PY'
import sys
p, b, e = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(p, encoding="utf-8").read()
i, j = t.index(b), t.index(e) + len(e)
open(p, "w", encoding="utf-8").write((t[:i].rstrip("\n") + "\n" + t[j:].lstrip("\n")))
PY
    nginx -t || restore_and_die
    systemctl reload nginx
    say "nginx-install: routes removed and nginx reloaded."
    exit 0
fi

# ------------------------------------------------------------ install --
if grep -qF "$MARK_BEGIN" "$SNIPPET"; then
    say "nginx-install: the paperlib block is already installed -- not appending a second copy."
    say "               (use --remove first if you want to reinstall it)"
    rm -f "$BACKUP"
    nginx -t >/dev/null && systemctl reload nginx && say "nginx-install: reloaded anyway."
    verify
    say ""
    [[ "$FAIL" -eq 0 ]] && say "all checks passed" || { say "CHECKS FAILED" >&2; exit 1; }
    exit 0
fi

# One pair of location blocks per area, GENERATED. This used to name
# neoantigens literally, which meant a second area was served by the catch-all:
# no X-Robots-Tag on its pages or its PDFs, and .md digests downloaded instead
# of opening. "All areas are noindex" is a claim that has to be generated from
# what is on disk, not typed once and left behind by the next area.
AREA_BLOCKS=""
for dir in "$REPO"/areas/*/; do
    [[ -d "$dir/dist" ]] || continue
    area=$(basename "$dir")
    AREA_BLOCKS+="
# --- $area ---
# The papers themselves. autoindex stays OFF: a directory listing would
# enumerate the whole collection, and this route exists to serve a filename the
# page already links, not to browse.
location /paperlib/$area/pdf/ {
        alias $REPO/areas/$area/raw/;
        add_header X-Robots-Tag \"noindex, nofollow\" always;
}

location /paperlib/$area/ {
        alias $REPO/areas/$area/dist/;
        index index.html;
        add_header X-Robots-Tag \"noindex, nofollow\" always;

        # The reading digest is markdown, and nginx's default map has no entry
        # for .md -- it falls through to application/octet-stream, so clicking
        # the sidebar link DOWNLOADS the file instead of opening it. Declaring
        # types inside a location REPLACES the map for that location, so all
        # four types dist/ actually contains are listed here; the PDFs are
        # served by the separate /pdf/ block above and are unaffected.
        types {
                text/html       html;
                text/css        css;
                text/javascript js;
                text/plain      md;
        }
        # REQUIRED alongside the types block above. Declaring \`types\` replaces the
        # map for this location, and nginx's built-in fallback for anything not
        # listed is text/plain -- which would serve a several-hundred-megabyte
        # .tar.gz as text and break the download offer.
        default_type application/octet-stream;
        charset utf-8;
}
"
done
[[ -n "$AREA_BLOCKS" ]] || { echo "nginx-install: no areas with dist/ -- run make render first" >&2; exit 1; }

cat >> "$SNIPPET" <<CONF

$MARK_BEGIN
# PaperLib -- literature browser, one page per research area.
#
# Aliased from $REPO like /gol/ and /venn/,
# so there is no copy in the web root to drift: \`make update\` is the deploy.
# /pdf/ aliases raw/ directly, which is add-only and sha256-hashed, so what is
# served is provably the ingested bytes and there is no second copy of 266 MB.
#
# NOT linked from the homepage: link access only. X-Robots-Tag keeps it out of
# search indexes, which is what makes that true. It is NOT access control.
#
# nginx picks the LONGEST matching prefix location, so these three resolve
# independently of the order they appear in.

location = /paperlib {
        return 301 /paperlib/;
}

$AREA_BLOCKS
# The portal listing every area. Shortest prefix, kept last by convention
# because it is the one most easily mistaken for a catch-all.
location /paperlib/ {
        alias $REPO/dist/;
        index index.html;
        add_header X-Robots-Tag "noindex, nofollow" always;
}
$MARK_END
CONF

say "nginx-install: appended the paperlib block to $SNIPPET"
nginx -t || restore_and_die
systemctl reload nginx
say "nginx-install: nginx -t passed and nginx reloaded."
verify
say ""
if [[ "$FAIL" -eq 0 ]]; then
    say "nginx-install: all checks passed"
    say ""
    # Listed from the SAME areas/*/ scan, under the SAME dist/ predicate, that
    # generated the blocks above. A hardcoded pair of lines here went on saying
    # "neoantigens" for as long as a second area was being served -- reporting
    # a route that had just been installed as though it did not exist. That is
    # the drift AREA_BLOCKS was introduced to end, and the summary has to be
    # driven by the same scan or it reintroduces it one print statement later.
    w=6
    for dir in "$REPO"/areas/*/; do
        [[ -d "$dir/dist" ]] || continue
        n=$(basename "$dir")
        if (( ${#n} > w )); then w=${#n}; fi
    done
    printf '  %-*s https://hatkapina.cc/paperlib/\n' "$w" portal
    for dir in "$REPO"/areas/*/; do
        [[ -d "$dir/dist" ]] || continue
        area=$(basename "$dir")
        printf '  %-*s https://hatkapina.cc/paperlib/%s/\n' "$w" "$area" "$area"
    done
else
    say "nginx-install: CHECKS FAILED -- see above. Backup kept at $BACKUP" >&2
    exit 1
fi

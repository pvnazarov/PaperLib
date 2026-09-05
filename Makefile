# PaperLib -- many areas, one toolkit. See CLAUDE.md for the rules these implement.
#
# EVERY target that touches a collection needs to know WHICH one. Pass AREA=<name>;
# with exactly one area it may be omitted, because with one area there is nothing
# to choose between. With two it is required, and scripts/paperlib.py refuses
# rather than picks -- `make build` guessing an area is how a taxonomy gets written
# into the wrong collection.
#
#   make update AREA=neoantigens      build + embed + render for that area
#   make all                          the same for every area, then the portal
#
# `update` needs NO network and is idempotent. `bib` and `inbox` are the only
# networked targets: separate, explicitly invoked, and advisory.

export PAPERLIB_AREA = $(AREA)

# A venv counts only once `make venv` has finished INSTALLING into it. Keying on
# .venv/bin/python instead was a real trap: a half-made venv (python symlinks, no
# pip) satisfied the check, so numeric targets silently ran against an interpreter
# with no numpy and looked like they had worked.
VENV_READY := $(wildcard .venv/.installed)
PY := $(if $(VENV_READY),.venv/bin/python,python3)
AREAS := $(notdir $(wildcard areas/*))

.PHONY: help all areas new-area portal update build render embed bib test verify \
        deploy clean venv topics audit edit review route inbox ui example demo demo-clean

help:
	@echo "AREA=<name> selects the collection. Omit it only if there is exactly one."
	@echo ""
	@echo "  make areas             list the areas and what each holds"
	@echo "  make new-area NAME=x   scaffold a new area            (DRY RUN; APPLY=1)"
	@echo "  make all               update every area, then the portal"
	@echo "  make portal            index/registry.json + dist/index.html"
	@echo ""
	@echo "  make route             shared inbox/ -> areas/<a>/inbox/  (DRY RUN; APPLY=1)"
	@echo "  make inbox AREA=x      DRY RUN over that area's inbox -- runbook in CLAUDE.md"
	@echo ""
	@echo "  make update AREA=x     build + embed + render  (no network, idempotent)"
	@echo "  make build AREA=x      meta/ + newest review -> data/library.json"
	@echo "  make embed AREA=x      vectors, neighbours, this area's own 2-D map"
	@echo "                         REFIT=1 refits everything (Tier $$(TIER), $$(STMODEL))"
	@echo "  make render AREA=x     library.json + shared src/ -> areas/x/dist/"
	@echo "  make bib   AREA=x      Crossref/arXiv for new DOIs only        (NETWORK)"
	@echo ""
	@echo "  make review AREA=x     regenerate the literature review -> reports/ (a draft)"
	@echo "  make topics AREA=x     propose topics for unfiled papers -> reports/ (a draft)"
	@echo "  make audit  AREA=x     validate library.json against every other source"
	@echo "  make verify AREA=x     re-hash every source against its sidecar"
	@echo "  make ui     AREA=x     drive the built page in a real browser (playwright)"
	@echo "  make test              build.py self-test against a synthetic fixture tree"
	@echo "  make example AREA=x    a synthetic collection, to run the pipeline dry"
	@echo "  make demo AREA=x       that example, built into a page, in one command"
	@echo "  make demo-clean AREA=x remove it again"
	@echo "  make edit   AREA=x PLAN=p.json   a recorded edit to meta//outputs/"
	@echo ""
	@echo "  make venv              create .venv and install requirements.txt"
	@echo "  make deploy            publish every built area + the portal"
	@echo ""
	@echo "areas present: $(if $(AREAS),$(AREAS),none yet)"

# ------------------------------------------------------------------ areas --

areas:
	@python3 scripts/areas.py

new-area:
	@test -n "$(NAME)" || { echo "make new-area: pass NAME=<lowercase-name>"; exit 1; }
	python3 scripts/new_area.py "$(NAME)" $(if $(APPLY),--apply,)

portal:
	python3 scripts/portal.py

# Each area is built in full before the next starts, so a failure names the area it
# failed in rather than leaving a half-updated set with no indication which.
all:
	@test -n "$(AREAS)" || { echo "make all: no areas yet -- make new-area NAME=x APPLY=1"; exit 1; }
	@for a in $(AREAS); do \
	   echo "=== $$a ==="; \
	   $(MAKE) --no-print-directory update AREA=$$a || exit 1; \
	 done
	@$(MAKE) --no-print-directory portal

# ------------------------------------------------------------- one area --

update: build embed render

# build.py and render.py are stdlib-only on purpose: a fresh clone can produce
# library.json and a page before anything is installed.
build:
	python3 scripts/build.py

render:
	python3 scripts/render.py

# Depends on build: fetch_bib reads data/library.json to find which papers are new,
# so a paper copied in a minute ago has to be in that file before it can be looked
# up. Without this, a cold `make bib` silently skips every new paper.
bib: build
	python3 scripts/fetch_bib.py
	python3 scripts/build.py

# Its own vectors, its own neighbours, its own UMAP layout, cached per area and
# keyed by sha256 so adding papers PLACES them in the existing map rather than
# reshuffling it. A map that rearranges itself every week cannot be learned.
# TIER and STMODEL are the measured choice for this collection, not defaults.
# A plain `make embed` loads the saved model and keeps whatever tier it was fitted
# at, so these matter on a REFIT -- without them a refit would silently drop back
# to Tier 0 TF-IDF and undo the change. Evidence:
# areas/neoantigens/reports/2026-09-05_embedding_slate.txt
TIER    ?= 1
STMODEL ?= pubmedbert
embed:
	@test -n "$(VENV_READY)" || { \
	  echo "make embed: no installed venv. Run 'make venv' first --"; \
	  echo "            numpy/scikit-learn/umap-learn are not present system-wide."; \
	  exit 1; }
	$(PY) scripts/embed.py $(if $(REFIT),--refit --tier $(TIER) --st-model $(STMODEL),) $(EMBEDFLAGS)

# ------------------------------------------------------------- ingestion --

# Both are DRY RUNS by default. Routing decides which COLLECTION a paper joins, and
# that is not a thing to discover having happened.
route:
	python3 scripts/route_inbox.py $(if $(AREA),--area $(AREA),) $(if $(APPLY),--apply,)

# Dry run only, on purpose. Ingesting writes to raw/ and meta/, needs the prose
# written by a person, and needs the owner's approval recorded -- so the apply step
# is spelled out in full in CLAUDE.md rather than hidden behind a target that looks
# harmless.
inbox:
	python3 scripts/ingest_inbox.py

# ------------------------------------------------------------- checking --

audit:
	python3 scripts/audit.py $(AUDITFLAGS)

# Re-reads and re-hashes every source. Proves the copy is byte-intact, and is what
# shows that deploy.sh's chmod changed modes and nothing else.
verify:
	python3 scripts/build.py --verify-bytes

test:
	python3 scripts/selftest.py

# The only target that RENDERS the page instead of reading data. `make audit`
# cannot see that a facet is a long list behind a short window, or that a filter is
# hidden inside a collapsed section -- both of those shipped, and the owner found
# them. Point it at the built file to also prove the page needs no server.
URL ?= file://$(CURDIR)/areas/$(AREA)/dist/index.html
ui:
	$(PY) scripts/ui_check.py '$(URL)'

# ------------------------------------------------------------- drafting --

# Writes a DRAFT into reports/. Nothing reads it there. Installing it in outputs/ is
# what makes it the taxonomy, and that is an upstream write -- so it goes through
# scripts/edit_upstream.py with recorded approval, not by cp.
review:
	python3 scripts/make_review.py $(if $(TAXONOMY),--taxonomy $(TAXONOMY),)

# Deliberately NOT part of `update`. It writes a draft for a person to read; if
# anything in data/ ever read it, that would be a second taxonomy.
topics:
	@test -n "$(VENV_READY)" || { \
	  echo "make topics: no installed venv. Run 'make venv' first."; exit 1; }
	$(PY) scripts/propose_topics.py

# Dry run unless APPLY=1 -- and APPLY=1 is what "always ask" gates: show the
# dry-run diff and get a yes first. The tool refuses to run without approving words
# in the plan, and copies that string into the ledger so "I asked" is auditable.
edit:
	@test -n "$(PLAN)" || { echo "make edit: pass PLAN=<plan.json> (see scripts/edit_upstream.py)"; exit 1; }
	python3 scripts/edit_upstream.py --plan "$(PLAN)" $(if $(APPLY),--apply,) $(EDITFLAGS)

example:
	$(PY) scripts/make_example.py $(APPLY)

# A whole working page over 12 synthetic papers, in one command. It exists so the
# pipeline can be run before any real paper is committed to it, which is what
# separates "the tool is broken" from "my data is not ready" -- two states that are
# otherwise impossible to tell apart at the last step.
# The synthetic sources are all named Example*, which is what makes demo-clean
# able to remove exactly them and nothing else.
demo:
	@test -n "$(AREA)" || { echo "make demo: pass AREA=<name>"; exit 1; }
	$(PY) scripts/make_example.py --apply
	python3 scripts/make_review.py --from-sidecars \
	        --taxonomy annotations/taxonomy.json --out outputs
	$(MAKE) --no-print-directory build AREA=$(AREA)
	$(MAKE) --no-print-directory render AREA=$(AREA)
	@echo ""
	@echo "open file://$(CURDIR)/areas/$(AREA)/dist/index.html"
	@echo "add the map with: make embed AREA=$(AREA) && make render AREA=$(AREA)"
	@echo "remove it with:   make demo-clean AREA=$(AREA)"

# Driven by the generator, which is the only thing that knows what it wrote --
# NOT by a glob. See the note in make_example.py.
demo-clean:
	@test -n "$(AREA)" || { echo "make demo-clean: pass AREA=<name>"; exit 1; }
	$(PY) scripts/make_example.py --clean --apply
	rm -f areas/$(AREA)/outputs/*_literature_review.md
	rm -f areas/$(AREA)/dist/* areas/$(AREA)/data/* areas/$(AREA)/reports/build_*.txt
	@# `rm -f dir/*` and not `rm -rf dir`: the glob does not match .gitkeep, so the
	@# directory and its note survive. Recreating the directory loses both.
	@echo "demo-clean: $(AREA) is empty again"

# ------------------------------------------------------------ publishing --

deploy:
	./deploy.sh $(if $(AREA),--area $(AREA),)

venv:
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	touch .venv/.installed
	@echo "venv ready: $$(.venv/bin/python -V)"
	@echo "for 'make ui' also: .venv/bin/playwright install chromium  (~115 MB, separate)"

# Removes only what is regenerable, and only for the named area. bib_cache.json is
# NOT removed: it caches network round trips keyed by sha256, and losing it costs a
# full refetch.
clean:
	@test -n "$(AREA)" || { echo "make clean: pass AREA=<name>"; exit 1; }
	rm -rf areas/$(AREA)/dist/ areas/$(AREA)/data/*.npy areas/$(AREA)/data/*.npz

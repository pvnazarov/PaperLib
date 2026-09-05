/* TeamLibrary Browser — the whole app.
 *
 * Reads the index from the <script type="application/json" id="library"> block that
 * render.py embeds. It is embedded rather than fetched because fetch() is blocked
 * over file://, and CLAUDE.md §8.1 requires the page to work from a clean directory
 * with no server and no network.
 *
 * No framework, no bundler, no dependencies.
 */
(function () {
  'use strict';

  var DATA = JSON.parse(document.getElementById('library').textContent);
  var PAPERS = DATA.papers;
  var PDF_BASE = document.body.dataset.pdfBase || 'pdf/';
  /* Optional: absent on a clone where `make embed` has never run. Every use of it
   * is guarded, so the page loses the map and the neighbour lists and keeps
   * working -- it must never be the reason the library will not open. */
  var SIM = DATA.similarity || null;
  /* What this instance calls itself (project.json, via render.py). The page
   * retitles itself as the reader moves, so the name is needed at runtime and
   * not only in the template. */
  var NAME = (DATA.project && DATA.project.name) || 'Library';
  var PART_OF = {};   // part letter -> index, for the map's colour key

  /* ── folding: search must survive accents and name variants ──────────
   * 'Binkowski' has to match a query typed without the diacritic, and
   * 'Chepeleva' has to match 'Maryna Chepeleva', 'Marina Chepeleva' AND
   * 'M. Chepeleva' — all three spellings occur in this corpus. Folding to
   * unaccented lowercase and matching on substrings handles both without a
   * name-normalisation table to maintain. */
  var COMBINING = /[̀-ͯ]/g;
  function fold(s) {
    return (s || '').normalize('NFKD').replace(COMBINING, '').toLowerCase();
  }

  /* WHO SHARED A PAPER IS NOT IN THIS HAYSTACK, and is not a facet either.
   *
   * Owner, 2026-09-03: "does not matter who shared" (D5). So the browser indexes
   * and browses papers by what they ARE and who WROTE them. The sharer is still
   * recorded on each record, because it is a fact about the item, but it is not a
   * way of navigating the library. */
  /* `hay_drop` names the spans of the summary that describe how the paper
   * ARRIVED rather than what it says -- "Circulated by <a colleague> as ...".
   * They are cut from the searched text and left in the displayed text:
   * searching a colleague's name must find what they WROTE, not what they
   * forwarded (D5). Without this, one member's surname matched 83 papers where
   * 41 are theirs. build.py
   * computes the spans; see its "circulation sentences" note. */
  function searchable(summary, drop) {
    if (!summary || !drop || !drop.length) return summary || '';
    var out = '', at = 0;
    for (var i = 0; i < drop.length; i++) {
      out += summary.slice(at, drop[i][0]);
      at = drop[i][1];
    }
    return out + summary.slice(at);
  }

  PAPERS.forEach(function (p, i) {
    p._i = i;
    p._hay = fold([
      p.title, p.first_author, (p.authors || []).join(' '), p.venue, p.topic, p.part,
      p.abstract, searchable(p.summary, p.hay_drop),
      (p.key_points || []).join(' '), p.limitations,
      p.doi, p.arxiv, p.source
    ].join('  '));
  });

  /* Authors, as a browsable dimension (D5). Built here rather than at build time
   * because it is derived from `authors` and costs nothing.
   *
   * Full names, never collapsed to surnames: 93 papers in this corpus carry an
   * author surnamed Wang and they are not one person. A surname facet would merge
   * strangers and report a confident wrong count. */
  var AUTHORS = (function () {
    var n = {};
    PAPERS.forEach(function (p) {
      var seen = {};
      (p.authors || []).forEach(function (a) {
        if (seen[a]) return;          // a name listed twice on one paper counts once
        seen[a] = 1;
        n[a] = (n[a] || 0) + 1;
      });
    });
    return Object.keys(n).map(function (a) {
      return { who: a, count: n[a], fold: fold(a) };
    }).sort(function (x, y) {
      return y.count - x.count || x.who.localeCompare(y.who);
    });
  })();

  /* Journals, preprint servers and conferences alike -- the owner's framing:
   * bioRxiv and its kin ARE the venue for the papers published there, and a facet
   * that only listed peer-reviewed journals would hide 44 of 234 papers.
   * build.py folds `arXiv:2506.03373` back to `arXiv`, so the 19 arXiv papers are
   * one venue rather than 19 singletons. */
  var VENUES = (function () {
    var n = {};
    PAPERS.forEach(function (p) { if (p.venue) n[p.venue] = (n[p.venue] || 0) + 1; });
    return Object.keys(n).map(function (v) {
      return { name: v, count: n[v], fold: fold(v) };
    }).sort(function (x, y) {
      return y.count - x.count || x.name.localeCompare(y.name);
    });
  })();

  var TYPES = uniq(PAPERS.map(function (p) { return p.type; })).sort();
  var YEARS = uniq(PAPERS.map(function (p) { return p.year; }))
    .filter(function (y) { return y; }).sort(function (a, b) { return b - a; });

  /* Not a facet since D7 (owner: "section FLAGS is useless for the moment"). The
   * definitions stay for two reasons: `state.flags` is still the filter the unfiled
   * banner sets, and the per-paper BADGES that mark these papers stay -- §9 needs
   * the 7 filename titles labelled, and that is the badge, not the facet. */
  var FLAGS = [
    { key: 'unfiled', label: 'Unfiled — no topic yet',
      test: function (p) { return p.unfiled; } },
    { key: 'fnametitle', label: 'Title from the filename',
      test: function (p) { return p.title_from_filename; } },
    { key: 'noauthors', label: 'No registered author list',
      test: function (p) { return !p.authors || !p.authors.length; } }
  ];

  var state = { q: '', scope: 'all', topics: [], authors: [], authorq: '', venues: [],
                venueq: '', years: [], types: [], flags: [], sort: 'year',
                view: 'list', focus: null,
                /* `sel` is the lasso HIGHLIGHT -- transient, map-only, not a
                 * filter. `lasso` is the filter it becomes once Keep only or
                 * Exclude is pressed. Two steps on purpose: a freehand loop over
                 * a scatter plot is imprecise, so you see what you caught before
                 * it changes what you are looking at. Same shape as the
                 * dhe-explorer UMAP, which offers Keep only / Exclude /
                 * Restore beside its Bokeh lasso. */
                sel: null, lasso: null,
                /* Which facets the reader has opened. All five start CLOSED
                 * (owner, 2026-09-03), and this has to be remembered across
                 * renders or the panel would slam shut on every click:
                 * renderSidebar() rebuilds the <details> from scratch, so a
                 * hardcoded default would re-apply itself after each
                 * selection and make multi-select unusable. */
                facetOpen: {},
                /* And which of the Topic facet's nine PARTS. Keyed by part
                 * NAME, never by letter: a letter is a position and gets
                 * renumbered when the taxonomy changes -- that is exactly how
                 * the maths papers ended up under Cardiovascular on
                 * 2026-09-04 -- while the name is the claim. */
                partOpen: {} };

  /* The roster is only shipped when wiki/group.md parsed and somebody on it
   * co-authored something here, so this is also the switch's on/off test. */
  var GROUP = DATA.group || [];

  var BY_ID = {};
  PAPERS.forEach(function (p) { BY_ID[p.id] = p; });
  DATA.taxonomy.forEach(function (part, i) { PART_OF[part.letter] = i; });

  /* Eight hues, one per part, distinguishable in both themes. Not a gradient:
   * parts are categories and a sequential ramp would imply an order they do not
   * have. */
  /* One colour per part. The values live in app.css as --part-1..--part-9, in
   * TWO palettes -- the dark one reads on #14161a, and on white those same
   * values are muddy and converge into "a dark dot" (§7.3). Reading them from
   * CSS rather than hard-coding them is what makes the map follow the theme
   * toggle at all.
   *
   * The array below is a FALLBACK, for a tenth part that CSS has no variable
   * for and for the case where getComputedStyle returns nothing. It is the
   * light palette: a wrong-but-visible colour beats no colour. */
  var PART_COLOURS = ['#2b6ff0', '#ef6c11', '#10a862', '#e0247c', '#8348e8',
                      '#b58400', '#0fa6b8', '#6aa314', '#e83a3a'];
  var NO_PART = '#8b93a3';

  /* Resolved once per paint, not once per dot: getComputedStyle is a layout
   * read, and doing it 338 times inside the draw loop is how a repaint on
   * every pointermove of a lasso becomes visibly slow. */
  var PALETTE = PART_COLOURS.slice();

  function readPalette() {
    var cs = getComputedStyle(document.documentElement);
    PALETTE = PART_COLOURS.map(function (fallback, i) {
      var v = (cs.getPropertyValue('--part-' + (i + 1)) || '').trim();
      return v || fallback;
    });
  }

  function partColour(p) {
    var i = PART_OF[p.part_letter];
    if (i === undefined) return NO_PART;
    return PALETTE[i] || PART_COLOURS[i % PART_COLOURS.length];
  }
  function nearOf(p) {
    return (SIM && SIM.papers[p.id] && SIM.papers[p.id].near) || [];
  }
  function xyOf(p) {
    return (SIM && SIM.papers[p.id] && SIM.papers[p.id].xy) || null;
  }

  /* ── filtering ────────────────────────────────────────────────────── */

  function terms(q) {
    return fold(q).split(/\s+/).filter(Boolean);
  }

  function matches(p, ts) {
    for (var i = 0; i < ts.length; i++) {
      if (p._hay.indexOf(ts[i]) === -1) return false;   // AND across terms
    }
    return true;
  }

  /* Each facet's counts are computed against the OTHER facets' results, so its own
   * options stay meaningful: a facet counted after applying itself would show every
   * option as 0 the moment one was chosen. `skip` names the facet to leave out. */
  function pass(p, skip) {
    if (skip !== 'q' && state.q && !matches(p, terms(state.q))) return false;
    if (skip !== 'scope' && state.scope !== 'all' &&
        (state.scope === 'own') !== !!p.own) return false;
    if (skip !== 'lasso' && state.lasso) {
      var inSel = state.lasso.ids.indexOf(p.id) !== -1;
      if (inSel !== (state.lasso.mode === 'keep')) return false;
    }
    if (skip !== 'topics' && state.topics.length &&
        state.topics.indexOf(p.topic) === -1) return false;
    if (skip !== 'venues' && state.venues.length &&
        state.venues.indexOf(p.venue) === -1) return false;
    if (skip !== 'years' && state.years.length &&
        state.years.indexOf(p.year) === -1) return false;
    if (skip !== 'types' && state.types.length &&
        state.types.indexOf(p.type) === -1) return false;
    if (skip !== 'authors' && state.authors.length) {
      var list = p.authors || [];
      // OR within the facet: picking two authors shows either's papers, which is
      // what "papers by these people" means. AND would mean co-authorship only.
      var hit = state.authors.some(function (who) { return list.indexOf(who) !== -1; });
      if (!hit) return false;
    }
    if (skip !== 'flags' && state.flags.length) {
      var all = state.flags.every(function (k) {
        var f = FLAGS.filter(function (x) { return x.key === k; })[0];
        return f && f.test(p);
      });
      if (!all) return false;
    }
    return true;
  }

  /* Lifted out of results() so the map's selection list can sort the same way.
   * Two lists on one page ordered by different rules is a small thing that
   * makes a page feel broken. */
  var SORTERS = {
    year: function (a, b) { return (b.year || 0) - (a.year || 0) || cmpTitle(a, b); },
    title: cmpTitle,
    author: function (a, b) {
      return String(a.first_author || '~').localeCompare(String(b.first_author || '~')) ||
             cmpTitle(a, b);
    },
  };

  function sorter() { return SORTERS[state.sort] || SORTERS.year; }

  function results() {
    return PAPERS.filter(function (p) { return pass(p, null); }).sort(sorter());
  }

  function cmpTitle(a, b) {
    return String(a.title || a.source).localeCompare(String(b.title || b.source));
  }
  function countIf(skip, test) {
    var n = 0;
    for (var i = 0; i < PAPERS.length; i++) {
      if (test(PAPERS[i]) && pass(PAPERS[i], skip)) n++;
    }
    return n;
  }

  /* ── dom helpers ──────────────────────────────────────────────────── */

  function el(tag, attrs, kids) {
    var e = document.createElement(tag);
    for (var k in attrs || {}) {
      if (k === 'text') e.textContent = attrs[k];
      else if (k === 'html') e.innerHTML = attrs[k];
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
    }
    (kids || []).forEach(function (c) {
      if (c) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
    });
    return e;
  }
  function esc(s) {
    return String(s === null || s === undefined ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function uniq(a) {
    return a.filter(function (v, i) { return a.indexOf(v) === i; });
  }
  function toggle(list, v) {
    var i = list.indexOf(v);
    if (i === -1) list.push(v); else list.splice(i, 1);
  }

  /* ── the sidecar prose is markdown, and must be rendered as such ─────
   *
   * `## Limitations` is a bullet list upstream and topic descriptions carry
   * **emphasis**. Rendered as plain text they came out as one run-on paragraph
   * full of literal `-` and `**`, which misrepresents the source: two separate
   * limitations read as one sentence.
   *
   * Everything is ESCAPED FIRST and only the tags generated below are ever
   * introduced, so no corpus text can become markup. */
  /* Three sidecar titles carry real markup from the publisher's record:
   * `m<sup>6</sup>Am`, `[<sup>18</sup>F]FDG`, `<i>GATA3</i>`. Rendered as text
   * they read as literal tags; STRIPPED they read as `m6Am`, a different
   * molecule. So exactly these six attribute-less formatting tags are let back
   * through AFTER escaping, and nothing else is: every other `<...>` anywhere in
   * the corpus stays inert text. */
  function fmtTags(escaped) {
    return escaped.replace(/&lt;(\/?)(i|em|b|strong|sup|sub)&gt;/g, '<$1$2>');
  }

  function mdInline(escaped) {
    return fmtTags(escaped)
      // code first, so its contents are not then emphasised
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^*\w])\*([^*\n]+)\*(?!\w)/g, '$1<em>$2</em>')
      .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
               '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  }

  /* Highlight inside text only, stepping over the tags mdInline produced — a
   * match that straddled a tag boundary would otherwise corrupt the markup. */
  function highlightHtml(html) {
    if (!terms(state.q).length) return html;
    return html.split(/(<[^>]+>)/).map(function (chunk) {
      return chunk.charAt(0) === '<' ? chunk : markText(chunk);
    }).join('');
  }

  /* Prose: escape, render markdown, then highlight. */
  function rich(s) {
    return highlightHtml(mdInline(esc(s)));
  }

  /* Block-level: paragraphs and bullet lists. Returns DOM nodes. */
  function mdBlocks(text) {
    var nodes = [], buf = [], list = null;
    function flushP() {
      if (buf.length) { nodes.push(el('p', { html: rich(buf.join(' ')) })); buf = []; }
    }
    function flushL() {
      if (list) {
        nodes.push(el('ul', {}, list.map(function (i) {
          return el('li', { html: rich(i) });
        })));
        list = null;
      }
    }
    String(text || '').split('\n').forEach(function (line) {
      var m = /^\s*[-*+]\s+(.*)$/.exec(line);
      if (m) {
        flushP();
        list = list || [];
        list.push(m[1]);
      } else if (!line.trim()) {
        flushP(); flushL();
      } else if (list) {
        list[list.length - 1] += ' ' + line.trim();   // wrapped bullet
      } else {
        buf.push(line.trim());
      }
    });
    flushP(); flushL();
    return nodes;
  }

  /* Plain fields — titles, names, venues. Escaped and highlighted, but NOT
   * markdown-rendered: an asterisk in an author name is an asterisk. */
  /* Titles and other short strings: escape, restore the formatting tags, then
   * highlight. NOT rich() -- a title is not markdown, and `*` in a chemical
   * name should stay a `*`. */
  function hl(s) {
    return highlightHtml(fmtTags(esc(s)));
  }

  function markText(out) {
    var ts = terms(state.q);
    if (!ts.length) return out;
    var folded = fold(out), marks = [];
    ts.forEach(function (t) {
      var from = 0, at;
      while ((at = folded.indexOf(t, from)) !== -1) {
        marks.push([at, at + t.length]);
        from = at + t.length;
      }
    });
    if (!marks.length) return out;
    marks.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [marks[0]];
    for (var i = 1; i < marks.length; i++) {
      var last = merged[merged.length - 1];
      if (marks[i][0] <= last[1]) last[1] = Math.max(last[1], marks[i][1]);
      else merged.push(marks[i]);
    }
    var res = '', pos = 0;
    merged.forEach(function (m) {
      res += out.slice(pos, m[0]) + '<mark>' + out.slice(m[0], m[1]) + '</mark>';
      pos = m[1];
    });
    return res + out.slice(pos);
  }

  /* ── sidebar ──────────────────────────────────────────────────────── */

  function optBtn(label, n, on, click, cls) {
    return el('button', {
      'class': 'opt' + (cls ? ' ' + cls : '') + (n === 0 && !on ? ' zero' : ''),
      type: 'button', 'aria-pressed': on ? 'true' : 'false', onclick: click,
      disabled: n === 0 && !on ? '' : null
    }, [el('span', { text: label }), el('span', { 'class': 'n', text: String(n) })]);
  }

  /* One place decides whether a facet is open, so the five cannot drift apart.
   * `openByDefault` applies only until the reader touches it. */
  /* `n` is how many options the facet holds, shown in the summary.
   *
   * Not decoration. The facets are CLOSED by default (D12) and the Topic facet
   * scrolls, so a reader saw six of forty-five topics through a short window and
   * reasonably concluded the list was incomplete -- the owner did, on 2026-09-04:
   * "текущие топики не полные". A count is the cheapest way for a closed,
   * scrolling list to say how much of itself you are looking at. */
  function facetShell(title, openByDefault, body, n) {
    var open = state.facetOpen[title];
    if (open === undefined) open = !!openByDefault;
    var head = [el('span', { text: title })];
    if (n) head.push(el('span', { 'class': 'facetn', text: String(n) }));
    var det = el('details', { 'class': 'facet', open: open ? '' : null },
      [el('summary', {}, head), body]);
    // `toggle` fires on both open and close, and on the keyboard too
    det.addEventListener('toggle', function () { state.facetOpen[title] = det.open; });
    return det;
  }

  function facet(title, openByDefault, bodyKids, scroll, n) {
    return facetShell(title, openByDefault, el(
      'div', { 'class': 'facet-body'
        + (scroll ? ' facet-scroll' : '')
        + (scroll === 'tall' ? ' facet-tall' : '') }, bodyKids), n);
  }

  /* ── own vs shared ─────────────────────────────────────────────────
   *
   * Two different libraries live in this one: 234 papers the team READ and
   * circulated, and 104 the team WROTE. They answer different questions, and
   * mixing them silently makes both worse -- "what have we published on
   * methylation" and "what have we read about it" are not the same query.
   *
   * `own` means a member of the roster in wiki/group.md is a CO-AUTHOR. It is
   * deliberately not "who circulated it" (D5) and not the sidecar's own
   * provenance line, which was measured to over-claim -- see
   * reports/upstream_findings.md. */
  var SCOPES = [
    { key: 'all',    label: 'All' },
    { key: 'own',    label: 'Ours' },
    { key: 'shared', label: 'Shared' }
  ];

  function scopeSwitch() {
    if (!GROUP.length) return null;
    var kids = SCOPES.map(function (s) {
      var n = countIf('scope', function (p) {
        return s.key === 'all' ? true : (s.key === 'own') === !!p.own;
      });
      return el('button', {
        'class': 'seg' + (state.scope === s.key ? ' on' : ''), type: 'button',
        role: 'radio', 'aria-checked': state.scope === s.key ? 'true' : 'false',
        onclick: function () { state.scope = s.key; render(); }
      }, [el('span', { text: s.label }), el('span', { 'class': 'n', text: String(n) })]);
    });
    var names = GROUP.map(function (m) { return m.name; }).join(', ');
    return el('div', { 'class': 'scope' }, [
      el('div', { 'class': 'segs', role: 'radiogroup', 'aria-label': 'Which papers' }, kids),
      el('p', { 'class': 'hint', title: names,
        text: '“Ours” = co-authored by someone on the group roster (' +
              GROUP.length + ' members appear here). Not who circulated it.' })
    ]);
  }

  function renderSidebar() {
    var aside = document.getElementById('facets');
    aside.textContent = '';

    var sw = scopeSwitch();
    if (sw) aside.appendChild(sw);

    /* Each part of the taxonomy is its own <details>, nested inside the Topic
     * facet's. Nine part names fit in a glance where 45 topics are 2,124px of
     * scrolling -- and a partial view of a list reads as a partial LIST, which
     * is what the owner reported on 2026-09-04 ("текущие топики не полные").
     *
     * The parts start CLOSED, like the facets themselves (D12). That would hide
     * an active filter, so two things stop it: a part holding selected topics
     * says so in its summary even while shut, and it opens itself unless the
     * reader has explicitly closed it. Note the ORDER of those two -- the badge
     * is what makes the collapse safe, the auto-open is only a convenience, and
     * dropping the badge to rely on auto-opening would put a live filter behind
     * a closed triangle the moment a reader collapsed a part by hand.
     *
     * The swatch is the map's colour for that part, read from the same CSS
     * variable the dots use (not the JS fallback), so the sidebar and the map
     * cannot disagree after a theme change. */
    var partEls = [], nTopics = 0;
    DATA.taxonomy.forEach(function (part, i) {
      var partN = countIf('topics', function (p) { return p.part_letter === part.letter; });
      var picked = part.topics.filter(function (t) {
        return state.topics.indexOf(t.name) !== -1;
      }).length;
      nTopics += part.topics.length;

      var kids = part.topics.map(function (t) {
        var n = countIf('topics', function (p) { return p.topic === t.name; });
        return optBtn(t.name, n, state.topics.indexOf(t.name) !== -1, function () {
          toggle(state.topics, t.name); render();
        }, 'child');
      });

      var open = state.partOpen[part.name];
      if (open === undefined) open = picked > 0;
      var det = el('details', {
        'class': 'part' + (partN === 0 && !picked ? ' zero' : ''),
        open: open ? '' : null
      }, [
        el('summary', {}, [
          el('span', { 'class': 'swatch',
            style: 'background:var(--part-' + (i + 1) + ',' +
                   PART_COLOURS[i % PART_COLOURS.length] + ')' }),
          el('span', { 'class': 'part-name',
            text: part.letter + '. ' + part.name }),
          picked ? el('span', { 'class': 'facetn on', title:
            picked + (picked === 1 ? ' topic' : ' topics') + ' in this part '
            + 'are filtering the library', text: picked + ' on' }) : null,
          el('span', { 'class': 'facetn', title: partN + ' matching papers',
            text: String(partN) })
        ]),
        el('div', { 'class': 'part-body' }, kids)
      ]);
      det.addEventListener('toggle', function () {
        state.partOpen[part.name] = det.open;
      });
      partEls.push(det);
    });

    /* Collapsing by default takes something away: the flat list could be
     * SCANNED. Nine clicks is not a substitute, so one control opens or shuts
     * the lot. `anyOpen` is read off the elements just built, which is the same
     * thing the reader is looking at. */
    var anyOpen = partEls.some(function (d) { return d.open; });
    var allBtn = el('button', {
      'class': 'partall', type: 'button',
      title: anyOpen ? 'Collapse all nine parts' : 'Open all nine parts',
      onclick: function () {
        DATA.taxonomy.forEach(function (part) {
          state.partOpen[part.name] = !anyOpen;
        });
        render();
      }
    }, [el('span', { text: anyOpen ? 'Collapse all' : 'Expand all' })]);

    /* `tall`: the Topic facet is the primary navigation. Collapsed it is nine
     * lines, but a reader who expands several parts is back to a long list, so
     * it keeps the generous cap. Author and Journal keep the short one -- they
     * hold hundreds of entries and have their own search box. */
    aside.appendChild(facet('Topic', false, [allBtn].concat(partEls), 'tall', nTopics));

    aside.appendChild(authorFacet());

    aside.appendChild(venueFacet());

    aside.appendChild(facet('Year', false, YEARS.map(function (y) {
      var n = countIf('years', function (p) { return p.year === y; });
      return optBtn(String(y), n, state.years.indexOf(y) !== -1, function () {
        toggle(state.years, y); render();
      });
    }), false, YEARS.length));

    aside.appendChild(facet('Type', false, TYPES.map(function (t) {
      var n = countIf('types', function (p) { return p.type === t; });
      return optBtn(t, n, state.types.indexOf(t) !== -1, function () {
        toggle(state.types, t); render();
      });
    }), false, TYPES.length));

  }

  /* 4,459 distinct authors is far too many to list, and the long tail is mostly
   * single papers. So: the frequent ones are listed, and a filter box reaches all
   * of them. Only the visible rows get a count computed, so typing stays cheap. */
  var AUTHOR_ROWS = 40;

  function authorFacet() {
    var body = el('div', { 'class': 'facet-body' });
    var box = el('input', {
      'class': 'authorq', type: 'search', placeholder: 'Filter authors…',
      autocomplete: 'off', spellcheck: 'false', value: state.authorq
    });
    var list = el('div', { 'class': 'facet-scroll' });

    var timer = null;
    box.addEventListener('input', function () {
      state.authorq = box.value;
      clearTimeout(timer);
      // Only the list is repainted, not the sidebar -- rebuilding the sidebar
      // would destroy this input and the caret inside it on every keystroke.
      timer = setTimeout(function () { paintAuthors(list); }, 90);
    });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { box.value = ''; state.authorq = ''; paintAuthors(list); }
    });

    body.appendChild(box);
    body.appendChild(list);
    paintAuthors(list);

    return facetShell('Author', false, body, AUTHORS.length);
  }

  function paintAuthors(list) {
    list.textContent = '';
    var q = fold(state.authorq).trim();
    var picked = AUTHORS.filter(function (a) { return state.authors.indexOf(a.who) !== -1; });
    var pool = AUTHORS.filter(function (a) {
      return state.authors.indexOf(a.who) === -1 &&
             (!q || a.fold.indexOf(q) !== -1);
    });
    var rows = picked.concat(pool.slice(0, AUTHOR_ROWS));

    rows.forEach(function (a) {
      var n = countIf('authors', function (p) {
        return (p.authors || []).indexOf(a.who) !== -1;
      });
      list.appendChild(optBtn(a.who, n, state.authors.indexOf(a.who) !== -1, function () {
        toggle(state.authors, a.who);
        render();
      }));
    });

    var more = pool.length - Math.min(pool.length, AUTHOR_ROWS);
    if (more > 0) {
      list.appendChild(el('p', { 'class': 'hint', style: 'margin:6px 6px 2px',
        text: q ? more + ' more match — keep typing to narrow'
                : 'Showing the ' + AUTHOR_ROWS + ' most frequent of ' +
                  AUTHORS.length + ' authors. Type to find any of them.' }));
    } else if (!rows.length) {
      list.appendChild(el('p', { 'class': 'hint', style: 'margin:6px',
        text: 'No author matches “' + state.authorq + '”.' }));
    }
  }

  /* 77 venues is more than a comfortable list and fewer than the 4,459 authors, so
   * this uses the same shape as the Author facet but shows more rows before it
   * needs the filter box. */
  var VENUE_ROWS = 25;

  function venueFacet() {
    var body = el('div', { 'class': 'facet-body' });
    var box = el('input', {
      'class': 'authorq', type: 'search', placeholder: 'Filter journals…',
      autocomplete: 'off', spellcheck: 'false', value: state.venueq
    });
    var list = el('div', { 'class': 'facet-scroll' });
    var timer = null;
    box.addEventListener('input', function () {
      state.venueq = box.value;
      clearTimeout(timer);
      timer = setTimeout(function () { paintVenues(list); }, 90);
    });
    box.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { box.value = ''; state.venueq = ''; paintVenues(list); }
    });
    body.appendChild(box);
    body.appendChild(list);
    paintVenues(list);
    return facetShell('Journal', false, body, VENUES.length);
  }

  function paintVenues(list) {
    list.textContent = '';
    var q = fold(state.venueq).trim();
    var picked = VENUES.filter(function (v) { return state.venues.indexOf(v.name) !== -1; });
    var pool = VENUES.filter(function (v) {
      return state.venues.indexOf(v.name) === -1 && (!q || v.fold.indexOf(q) !== -1);
    });
    picked.concat(pool.slice(0, VENUE_ROWS)).forEach(function (v) {
      var n = countIf('venues', function (p) { return p.venue === v.name; });
      list.appendChild(optBtn(v.name, n, state.venues.indexOf(v.name) !== -1, function () {
        toggle(state.venues, v.name);
        render();
      }));
    });
    var more = pool.length - Math.min(pool.length, VENUE_ROWS);
    if (more > 0) {
      list.appendChild(el('p', { 'class': 'hint', style: 'margin:6px 6px 2px',
        text: q ? more + ' more match — keep typing to narrow'
                : 'Showing the ' + VENUE_ROWS + ' most common of ' + VENUES.length +
                  ' journals and preprint servers. Type to find any of them.' }));
    } else if (!picked.length && !pool.length) {
      list.appendChild(el('p', { 'class': 'hint', style: 'margin:6px',
        text: 'No journal matches “' + state.venueq + '”.' }));
    }
  }

  /* ── result list ──────────────────────────────────────────────────── */

  function badges(p) {
    var b = [el('span', { 'class': 'badge type', text: p.type })];
    if (p.own) {
      var who = (p.own_members || []).map(function (i) {
        for (var k = 0; k < GROUP.length; k++) if (GROUP[k].initials === i) return GROUP[k].name;
        return i;
      });
      b.push(el('span', { 'class': 'badge own', title:
        (who.length ? who.join(', ') : 'a group member') + ' — co-author' +
        (who.length > 1 ? 's' : '') + ' on this paper' +
        (p.own_basis === 'filename'
          ? '. Matched on the filename\u2019s first-author surname, because the ' +
            'publisher registered no author list; the surname belongs to nobody ' +
            'else in this library.'
          : p.own_basis === 'author-initial'
          ? '. Matched on a given-name initial, accepted because the surname ' +
            'belongs to nobody else in this library.' : '.'),
        text: 'ours' }));
    }
    if (p.title_from_filename) {
      b.push(el('span', { 'class': 'badge warn', title:
        'No registered record exists to check this title against — it comes from ' +
        'the filename, and filenames were truncated at 98 characters upstream.',
        text: 'title from filename' }));
    }
    if (p.unfiled) {
      b.push(el('span', { 'class': 'badge warn', title:
        'No entry in the newest literature review yet, so this paper has no topic. ' +
        'It is left blank rather than guessed at.', text: 'unfiled' }));
    }
    if (!p.authors || !p.authors.length) {
      b.push(el('span', { 'class': 'badge', title:
        'The publisher registered no usable author list for this paper. None is ' +
        'shown rather than a partial one, which would look complete.',
        text: 'no author list' }));
    }
    return el('span', { 'class': 'badges' }, b);
  }

  function hitEl(p) {
    return el('li', {}, [
      el('article', { 'class': 'hit', tabindex: '0', role: 'link',
        onclick: function () { go(p); },
        onkeydown: function (e) {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(p); }
        }
      }, [
        el('h3', { html: hl(p.title) }),
        el('p', { 'class': 'byline', html:
          hl([p.first_author, p.year, p.venue].filter(Boolean).join(' · ')) }),
        el('p', { 'class': 'crumb' }, [
          p.topic
            ? el('span', { html: hl(p.part_letter + '. ' + p.part + ' → ' + p.topic) })
            : el('span', { text: 'no topic yet' }),
          document.createTextNode('  '),
          badges(p)
        ]),
        authorLine(p)
      ])
    ]);
  }

  /* The card's second line is the byline, so this one carries the rest of the
   * author list -- the thing D2 fetched and the thing the Author facet browses. */
  function authorLine(p) {
    var a = p.authors || [];
    if (a.length < 2) return null;
    var q = terms(state.q).concat(state.authors.map(fold));
    // Show the matching co-authors first when there is a reason to: a hit found
    // through an author deserves to say which one.
    var hits = a.slice(1).filter(function (name) {
      var f = fold(name);
      return q.some(function (needle) { return needle && f.indexOf(needle) !== -1; });
    });
    var rest = a.slice(1, 6).join(', ');
    var text = hits.length
      ? 'with ' + hits.slice(0, 4).join(', ')
      : 'with ' + rest + (a.length > 6 ? ' and ' + (a.length - 6) + ' more' : '');
    return el('p', { 'class': 'crumb', html: hl(text) });
  }

  function renderList() {
    var main = document.getElementById('main');
    main.textContent = '';
    var hits = results();

    main.appendChild(el('div', { 'class': 'resulthead' }, [
      el('h2', {}, [
        el('span', { text: String(hits.length) + (hits.length === 1 ? ' paper' : ' papers') }),
        hits.length !== PAPERS.length
          ? el('span', { 'class': 'of', text: ' of ' + PAPERS.length }) : null
      ]),
      el('span', { 'class': 'spacer' }),
      el('label', { 'class': 'sortby' }, [
        document.createTextNode('sort '),
        el('select', { onchange: function (e) { state.sort = e.target.value; render(); } },
          [['year', 'newest paper'], ['author', 'first author'],
           ['title', 'title']].map(function (o) {
            return el('option', { value: o[0], text: o[1],
              selected: state.sort === o[0] ? '' : null });
          }))
      ])
    ]));

    var chips = activeChips();
    if (chips) main.appendChild(chips);

    var unfiled = unfiledBanner();
    if (unfiled) main.appendChild(unfiled);

    if (!hits.length) {
      main.appendChild(el('p', { 'class': 'empty', text:
        'Nothing matches. Try fewer filters, or a shorter search.' }));
      return;
    }
    main.appendChild(el('ol', { 'class': 'hits' }, hits.map(hitEl)));
  }

  /* CLAUDE.md §4.3 requires unfiled papers to be VISIBLE, not merely counted in
   * build.py's output: a paper that arrived after the latest literature review has
   * no topic, and one silently absent from the tree is the defect nobody notices.
   * D7 removed the Flags facet, which was where that lived, so this replaces it --
   * it renders NOTHING when the count is zero, which is the normal state, and
   * appears only when there is something to act on. */
  function unfiledBanner() {
    if (state.flags.indexOf('unfiled') !== -1) return null;   // already showing them
    var n = PAPERS.filter(function (p) { return p.unfiled; }).length;
    if (!n) return null;
    return el('p', { 'class': 'notice', style: 'margin:0 0 10px' }, [
      el('strong', { text: n === 1 ? '1 paper has no topic yet.'
                                   : n + ' papers have no topic yet.' }),
      document.createTextNode(' They arrived after the latest literature review, so ' +
        'they are searchable and on the map but unplaced in the topic tree. Nothing ' +
        'has been guessed. '),
      el('button', { 'class': 'chip', type: 'button', text: 'Show them',
        onclick: function () { reset(); state.flags = ['unfiled']; render(); } })
    ]);
  }

  function activeChips() {
    var out = [];
    function chip(label, undo) {
      out.push(el('button', { 'class': 'chip', type: 'button', onclick: undo },
        [el('span', { text: label }), el('span', { 'class': 'x', text: '×' })]));
    }
    if (state.q) chip('“' + state.q + '”', function () { setQuery(''); });
    // The scope narrows the result list exactly as a facet does, so it gets a
    // removable chip like one. Without it, choosing "Ours" and scrolling away
    // left the list filtered with nothing in the results area saying so, and
    // `clear all` only appears once two chips exist -- so there was no way back
    // short of finding the switch again.
    if (state.scope !== 'all') {
      chip(state.scope === 'own' ? 'ours only' : 'shared only',
           function () { state.scope = 'all'; render(); });
    }
    if (state.lasso) {
      chip((state.lasso.mode === 'keep' ? 'lassoed on the map: ' : 'lassoed out: ') +
           state.lasso.ids.length,
           function () { state.lasso = null; render(); });
    }
    state.topics.forEach(function (t) {
      chip(t, function () { toggle(state.topics, t); render(); });
    });
    state.authors.forEach(function (w) {
      chip(w, function () { toggle(state.authors, w); render(); });
    });
    state.venues.forEach(function (v) {
      chip(v, function () { toggle(state.venues, v); render(); });
    });
    state.years.forEach(function (y) {
      chip(String(y), function () { toggle(state.years, y); render(); });
    });
    state.types.forEach(function (t) {
      chip(t, function () { toggle(state.types, t); render(); });
    });
    state.flags.forEach(function (k) {
      var f = FLAGS.filter(function (x) { return x.key === k; })[0];
      chip(f ? f.label : k, function () { toggle(state.flags, k); render(); });
    });
    if (out.length < 2) return out.length ? el('div', { 'class': 'chips' }, out) : null;
    out.push(el('button', { 'class': 'chip clear-all', type: 'button',
      text: 'clear all', onclick: reset }));
    return el('div', { 'class': 'chips' }, out);
  }

  /* ── record view ──────────────────────────────────────────────────── */

  /* Full list or none, per D2: a partial author list is not shown, because a
   * truncated list looks complete. The `and N more` control below is display
   * folding of a list we DO have in full, which is a different thing. */
  function authorsEl(p) {
    if (!p.authors || !p.authors.length) {
      return el('p', { 'class': 'authors' }, [
        el('span', { text: p.first_author || 'authors not recorded' }),
        el('span', { 'class': 'badge', style: 'margin-left:6px', title:
          'The publisher registered no usable author list for this paper, so none is ' +
          'shown. A partial list is not shown either — it would look complete.',
          text: 'no registered author list' })
      ]);
    }
    var CUT = 12, wrap = el('p', { 'class': 'authors' });
    function paint(showAll) {
      wrap.textContent = '';
      var list = showAll ? p.authors : p.authors.slice(0, CUT);
      wrap.appendChild(el('span', { html: hl(list.join(', ')) }));
      if (p.authors.length > CUT) {
        wrap.appendChild(document.createTextNode(showAll ? ' ' : ' … '));
        wrap.appendChild(el('button', { 'class': 'moreauthors', type: 'button',
          text: showAll ? 'show fewer' : 'and ' + (p.authors.length - CUT) + ' more',
          onclick: function () { paint(!showAll); } }));
      }
    }
    paint(false);
    return wrap;
  }

  function pdfHref(p) {
    return PDF_BASE + encodeURIComponent(p.source);
  }

  function renderRecord(p) {
    var main = document.getElementById('main');
    main.textContent = '';
    var kids = [
      el('button', { 'class': 'back', type: 'button', text: '← back to the list',
        onclick: function () { location.hash = ''; } }),
      el('h2', { html: hl(p.title) })
    ];
    if (p.title_from_filename) {
      kids.push(el('p', { 'class': 'warnbox', text:
        'Title from the filename; no registered record exists to check it against. ' +
        'Filenames were truncated at 98 characters upstream and the truncation is ' +
        'invisible, so this title may be incomplete.' }));
    }
    kids.push(authorsEl(p));
    kids.push(el('p', { 'class': 'meta' }, [
      el('span', { html: hl([p.venue, p.year].filter(Boolean).join(' · ')) }),
      document.createTextNode(' '), badges(p)
    ]));

    var acts = [];
    if (p.file_ok) {
      acts.push(el('a', { 'class': 'btn', href: pdfHref(p), target: '_blank',
        rel: 'noreferrer', text: (p.media === 'docx' ? 'Open DOCX' : 'Open PDF') }));
    }
    if (p.doi) {
      acts.push(el('a', { 'class': 'btn secondary', href: 'https://doi.org/' + p.doi,
        target: '_blank', rel: 'noreferrer', text: 'DOI ↗' }));
    } else if (p.arxiv) {
      acts.push(el('a', { 'class': 'btn secondary', href: 'https://arxiv.org/abs/' + p.arxiv,
        target: '_blank', rel: 'noreferrer', text: 'arXiv:' + p.arxiv + ' ↗' }));
    }
    if (p.topic) {
      acts.push(el('button', { 'class': 'btn secondary', type: 'button',
        text: 'All in “' + p.topic + '”', onclick: function () {
          reset(); state.topics = [p.topic]; location.hash = ''; render();
        } }));
    }
    kids.push(el('div', { 'class': 'actions' }, acts));

    if (p.topic) {
      kids.push(el('h3', { text: 'Topic' }));
      kids.push(el('p', { text: p.part_letter + '. ' + p.part + ' → ' + p.topic }));
      var td = topicDescription(p.topic);
      if (td) kids.push(el('p', { 'class': 'crumb', html: rich(td) }));
    }
    if (p.summary) {
      kids.push(el('h3', { text: 'Summary' }));
      mdBlocks(p.summary).forEach(function (n) { kids.push(n); });
    }
    if (p.key_points && p.key_points.length) {
      kids.push(el('h3', { text: 'Key points' }));
      kids.push(el('ul', {}, p.key_points.map(function (k) {
        return el('li', { html: rich(k) });
      })));
    }
    if (p.limitations) {
      kids.push(el('h3', { text: 'Limitations' }));
      mdBlocks(p.limitations).forEach(function (n) { kids.push(n); });
    }
    var sim = similarEl(p, 5);
    if (sim) kids.push(sim);

    kids.push(el('details', { 'class': 'tech' }, [
      el('summary', { text: 'Source record' }),
      el('dl', {}, [
        ['file', p.source], ['sha256', p.sha256], ['id', p.id],
        ['classification', p.classification],
        ['size', p.size_bytes ? (p.size_bytes / 1048576).toFixed(1) + ' MB' : null],
        ['extracted characters', p.extraction_chars ? String(p.extraction_chars) : null],
        ['author list from', sourceLabel(p.authors_source)],
        ['DOI from', p.doi ? sourceLabel(p.doi_source || 'sidecar') : null],
        ['venue from', p.venue ? sourceLabel(p.venue_source) : null]
      ].reduce(function (acc, kv) {
        acc.push(el('dt', { text: kv[0] }));
        acc.push(el('dd', { text: kv[1] || '—' }));
        return acc;
      }, []))
    ]));

    main.appendChild(el('article', { 'class': 'record' }, kids));
    document.title = (p.title) + ' — ' + NAME;
    window.scrollTo(0, 0);
  }

  // Where a field came from, in words rather than in field values. `pdf-byline`
  // and `posted-content` are our vocabulary, not a reader's -- and this block is
  // the one place §9's "say what is known AND how" is answered per record, so it
  // has to be legible. An unrecognised value is passed through rather than
  // hidden: a label we forgot to translate is better than a fact we dropped.
  var SOURCE_LABELS = {
    crossref: 'Crossref — the publisher\u2019s own registration',
    arxiv: 'arXiv',
    'pdf-byline': 'the paper\u2019s own first page, read here',
    pdf: 'the paper\u2019s own first page, read here',
    sidecar: 'the sidecar, as upstream shipped it',
    'sidecar-written-here': 'the paper\u2019s own first page, read here and '
      + 'written into the sidecar',
    review: 'the literature review',
    filename: 'the filename (nothing registered)'
  };

  function sourceLabel(v) {
    if (!v) return null;
    return SOURCE_LABELS[v] || v;
  }

  /* What this line used to say: `tier 0 (TF-IDF + TruncatedSVD) · layout v4`.
   * That is the build's vocabulary, not a reader's -- it named the vectoriser and
   * an internal version counter, neither of which a reader can act on (owner,
   * 2026-09-04: "perhaps we can just keep update date"). The tier and the layout
   * version are still in data/similarity.json, where the operator and ADR 0004
   * need them; they simply are not the page's business.
   *
   * The DATE is worth keeping for a reason the version numbers never had: when
   * it disagrees with the library's own date, the map was built from older data,
   * so papers added since are MISSING FROM IT -- a reader looking for one would
   * otherwise conclude it is not in the library. render.py warns the operator
   * about this at build time; this is the same fact told to the reader. */
  function mapAsOf() {
    var mapDate = SIM && SIM.data_as_of;
    if (!mapDate) return el('span', { 'class': 'sortby', text: '' });
    if (DATA.data_as_of && mapDate !== DATA.data_as_of) {
      return el('span', {
        'class': 'sortby stale',
        title: 'The map was built from the library as it stood on ' + mapDate
             + ', but the library is now dated ' + DATA.data_as_of
             + '. Papers added since are not plotted. Run `make embed`.',
        text: 'map from ' + mapDate + ' \u2014 older than the library'
      });
    }
    return el('span', { 'class': 'sortby', text: 'updated ' + mapDate });
  }

  function topicDescription(name) {
    var d = null;
    DATA.taxonomy.forEach(function (part) {
      part.topics.forEach(function (t) { if (t.name === name) d = t.description; });
    });
    return d;
  }

  /* ── the map ──────────────────────────────────────────────────────────
   *
   * Plain canvas. 234 points needs no plotting library and no WebGL (§10).
   *
   * Two rules from §7.1, both of which look like implementation details and are
   * not:
   *   - the "similar papers" list is the top-k computed in the FULL embedding
   *     space by embed.py, NEVER the points that happen to look close here;
   *   - the notice below is part of the content, because this is a map of the
   *     summaries and two papers can sit together for having been summarised in
   *     the same words.
   */
  var MAP = { w: 0, h: 0, pad: 26, dpr: 1, pts: [], path: null };

  /* Ray casting. The lasso is a freehand polygon, so there is nothing cheaper
   * that is also correct -- and at 338 points a full test costs nothing. */
  function inPolygon(x, y, poly) {
    var inside = false;
    for (var i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      var xi = poly[i][0], yi = poly[i][1], xj = poly[j][0], yj = poly[j][1];
      if ((yi > y) !== (yj > y) &&
          x < (xj - xi) * (y - yi) / (yj - yi) + xi) inside = !inside;
    }
    return inside;
  }

  function renderMap() {
    var main = document.getElementById('main');
    main.textContent = '';

    if (!SIM) {
      main.appendChild(el('p', { 'class': 'empty', text:
        'No map: this build has no data/similarity.json. Run `make embed`.' }));
      return;
    }

    var hits = results();
    var shown = {};
    hits.forEach(function (p) { shown[p.id] = true; });

    main.appendChild(el('div', { 'class': 'resulthead' }, [
      el('h2', {}, [
        el('span', { text: String(hits.length) + ' of ' + PAPERS.length + ' shown' })
      ]),
      el('span', { 'class': 'spacer' }),
      mapAsOf()
    ]));
    var chips = activeChips();
    if (chips) main.appendChild(chips);

    /* §7 requires the page to say that this is a map of the SUMMARIES. It said
     * so in a three-sentence bordered card above the plot, which is a lot of
     * prose to put between a reader and a scatter plot (owner, 2026-09-03:
     * "users are not so interested"). The claim stays -- it is the difference
     * between a map you can trust and one you cannot -- but as one line of
     * small print, with the full wording on hover. */
    main.appendChild(el('p', { 'class': 'hint maphint', title: SIM.notice, text:
      'Built from the summaries, not the papers — two can sit together for being '
      + 'described alike. Neighbour lists come from the full space, not from this map.' }));

    main.appendChild(lassoBar(hits));

    var wrap = el('div', { 'class': 'mapwrap' });
    var canvas = el('canvas', { 'class': 'map', id: 'map' });
    wrap.appendChild(canvas);
    var tip = el('div', { 'class': 'maptip', id: 'maptip', hidden: '' });
    wrap.appendChild(tip);
    // live count while the loop is being drawn, so you can tell what you have
    // before you let go
    wrap.appendChild(el('div', { 'class': 'lassolive', id: 'lassolive', hidden: '' }));
    main.appendChild(wrap);

    // colour key
    main.appendChild(el('div', { 'class': 'mapkey' }, DATA.taxonomy.map(function (part, i) {
      var on = state.topics.length === 0 ||
        part.topics.some(function (tp) { return state.topics.indexOf(tp.name) !== -1; });
      return el('button', {
        'class': 'keyitem' + (on ? '' : ' off'), type: 'button',
        title: 'Show only ' + part.name,
        onclick: function () {
          var names = part.topics.map(function (tp) { return tp.name; });
          var already = names.every(function (n) { return state.topics.indexOf(n) !== -1; });
          state.topics = already ? [] : names;
          render();
        }
      }, [
        el('span', { 'class': 'swatch',
          // the CSS variable, not the JS fallback, so the key and the dots
          // cannot disagree after a theme change
          style: 'background:var(--part-' + (i + 1) + ',' +
                 PART_COLOURS[i % PART_COLOURS.length] + ')' }),
        el('span', { text: part.letter + '. ' + part.name })
      ]);
    })));

    if (state.focus && BY_ID[state.focus]) main.appendChild(focusPanel(BY_ID[state.focus]));

    var below = selectionList(hits);
    if (below) main.appendChild(below);

    drawMap(canvas, shown);
    window.addEventListener('resize', onResize);
  }

  /* Step two of the lasso: the highlight becomes a filter only when asked.
   *
   * `Keep only` and `Exclude` are dhe-explorer's own two verbs, and they are the
   * two that matter -- "show me this cluster" and "show me everything but this
   * cluster". Both leave a removable chip, so the filter is never invisible, and
   * both work on IDS rather than on the polygon: the map may be redrawn at a
   * different size, and a selection that silently meant something else after a
   * resize would be worse than no selection at all. */
  function lassoBar(hits) {
    var n = selCount();
    if (!n) {
      return el('p', { 'class': 'hint maphint', text:
        'Drag on the map to lasso a group of papers, or filter on the left, and they '
        + 'are listed below. Click a paper to focus it and see its true nearest '
        + 'neighbours.' });
    }
    var ids = Object.keys(state.sel);
    function apply(mode) {
      state.lasso = { ids: ids, mode: mode };
      // `Keep only` KEEPS the highlight: the selection is now exactly what is
      // shown, so the dimming is uniform and the list at the bottom of the page
      // goes on answering "what am I looking at". `Exclude` drops it, because a
      // list of the papers you just hid is not what you asked to see.
      state.sel = mode === 'keep' ? state.sel : null;
      state.focus = null;
      render();
    }
    return el('div', { 'class': 'lassobar' }, [
      el('strong', { text: n + (n === 1 ? ' paper selected' : ' papers selected') }),
      el('span', { 'class': 'spacer' }),
      el('button', { 'class': 'chip', type: 'button', title:
        'Filter everything -- the list, the facets and the map -- to these papers',
        onclick: function () { apply('keep'); } }, [el('span', { text: 'Keep only' })]),
      el('button', { 'class': 'chip', type: 'button', title:
        'Hide these papers and keep the rest',
        onclick: function () { apply('exclude'); } }, [el('span', { text: 'Exclude' })]),
      el('button', { 'class': 'chip', type: 'button',
        onclick: function () { state.sel = null; render(); } },
        [el('span', { text: 'Clear' })])
    ]);
  }

  /* What the bottom of the map page is for: the papers you just enclosed.
   *
   * Sorted the way the list view sorts, and each row opens the record -- so a
   * lasso is a way of reading a cluster, not just of counting it. */
  /* Is the reader looking at a NARROWED library? Mirrors reset() field for
   * field on purpose -- these two are the same list of things read from two
   * directions, and a facet added to one and forgotten in the other would leave
   * a filter that silently does not count as one. `sel` is excluded: the lasso
   * HIGHLIGHT is not a filter until Keep only or Exclude turns it into `lasso`
   * (see the note on state.sel). */
  function filtersActive() {
    return !!(state.q || state.scope !== 'all' || state.lasso
      || state.topics.length || state.authors.length || state.venues.length
      || state.years.length || state.types.length || state.flags.length);
  }

  /* What sits under the map. Three cases, and the middle one is the owner's ask
   * of 2026-09-04: "when I filter by left panel (author, topic, etc) and Map
   * view, the list of papers should appear under the map, like when you do
   * lasso". Before this, filtering in the map view repainted the dots and left
   * the area below saying only "Lasso a group of points above" -- so the reader
   * could see THAT eleven papers matched but had no way to find out WHICH
   * without switching to the list view and losing the map.
   *
   * A lasso selection still wins where both exist: it is the more specific and
   * more recent act, and it is what the reader just did with the mouse.
   *
   * The unfiltered case deliberately does NOT list all 338 -- that is the list
   * view's job, and dumping the whole library under the plot would bury it. */
  function selectionList(hits) {
    var n = selCount();
    if (n) {
      var picked = PAPERS.filter(function (p) { return state.sel[p.id]; });
      picked.sort(sorter());
      return listPanel(n + (n === 1 ? ' selected paper' : ' selected papers'), picked);
    }
    if (filtersActive()) {
      return listPanel(hits.length === 1 ? '1 matching paper'
                                         : hits.length + ' matching papers', hits);
    }
    /* Nothing selected and nothing filtered: say NOTHING here. lassoBar()
     * already prints the instruction above the canvas, and a second hint below
     * repeating it just put two near-identical sentences around the plot. */
    return null;
  }

  function listPanel(heading, papers) {
    if (!papers.length) {
      return el('p', { 'class': 'hint', style: 'margin:14px 2px 0', text:
        'Nothing matches. Remove a filter above.' });
    }
    return el('section', { 'class': 'selpanel' }, [
      el('div', { 'class': 'resulthead' }, [
        el('h2', {}, [el('span', { text: heading })]),
        el('span', { 'class': 'spacer' }),
        el('span', { 'class': 'sortby', text:
          state.sort === 'title' ? 'by title'
            : state.sort === 'author' ? 'by first author' : 'newest first' })
      ]),
      el('ol', { 'class': 'hits' }, papers.map(hitEl))
    ]);
  }

  var resizeTimer = null;
  function onResize() {
    if (state.view !== 'map') { window.removeEventListener('resize', onResize); return; }
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(render, 150);
  }

  /* Sizing and point positions. Separate from paint() because a lasso drag
   * repaints on every pointermove and must not re-measure or re-lay-out. */
  function layoutMap(canvas) {
    var rect = canvas.getBoundingClientRect();
    MAP.dpr = window.devicePixelRatio || 1;
    MAP.w = Math.max(320, Math.round(rect.width));
    MAP.h = Math.max(260, Math.round(Math.min(620, rect.width * 0.62)));
    canvas.width = MAP.w * MAP.dpr;
    canvas.height = MAP.h * MAP.dpr;
    canvas.style.height = MAP.h + 'px';

    var pad = MAP.pad;
    MAP.pts = [];
    PAPERS.forEach(function (p) {
      var xy = xyOf(p);
      if (!xy) return;
      MAP.pts.push({
        p: p,
        x: pad + xy[0] * (MAP.w - 2 * pad),
        // canvas y grows downward; flip so the layout is not mirrored
        y: pad + (1 - xy[1]) * (MAP.h - 2 * pad)
      });
    });
  }

  function paintMap(canvas, shown) {
    readPalette();
    var css = getComputedStyle(document.body);
    var ctx = canvas.getContext('2d');
    ctx.setTransform(MAP.dpr, 0, 0, MAP.dpr, 0, 0);
    ctx.clearRect(0, 0, MAP.w, MAP.h);

    var sel = state.sel;
    var focus = state.focus ? BY_ID[state.focus] : null;
    var nearIds = {};
    if (focus) nearOf(focus).forEach(function (n) { nearIds[n.id] = n.sim; });

    // links from the focused paper to its true (full-space) neighbours
    if (focus) {
      var fp = MAP.pts.filter(function (q) { return q.p.id === focus.id; })[0];
      if (fp) {
        ctx.lineWidth = 1;
        MAP.pts.forEach(function (q) {
          if (!nearIds[q.p.id]) return;
          ctx.globalAlpha = 0.25 + 0.55 * Math.min(1, nearIds[q.p.id]);
          ctx.strokeStyle = css.getPropertyValue('--ink') || '#000';
          ctx.beginPath();
          ctx.moveTo(fp.x, fp.y);
          ctx.lineTo(q.x, q.y);
          ctx.stroke();
        });
        ctx.globalAlpha = 1;
      }
    }

    MAP.pts.forEach(function (q) {
      var visible = shown[q.p.id];
      var isFocus = focus && q.p.id === focus.id;
      var isNear = !!nearIds[q.p.id];
      var isSel = sel && sel[q.p.id];
      // While a selection exists, everything outside it recedes -- the same
      // move as dhe-explorer's nonselection_alpha, and the only way a lasso
      // over a few hundred points reads at a glance.
      ctx.globalAlpha = !visible ? 0.1
        : sel ? (isSel ? 1 : 0.12)
        : (focus && !isFocus && !isNear ? 0.34 : 1);
      ctx.beginPath();
      ctx.arc(q.x, q.y, isFocus ? 7.5 : (isSel ? 6 : (isNear ? 6 : 4.6)), 0, 6.2832);
      ctx.fillStyle = partColour(q.p);
      ctx.fill();
      if (isFocus || isNear || isSel) {
        ctx.lineWidth = isFocus ? 2.5 : 1.5;
        ctx.strokeStyle = isSel
          ? (css.getPropertyValue('--ink') || '#000')
          : (css.getPropertyValue('--panel') || '#fff');
        ctx.stroke();
      }
    });
    ctx.globalAlpha = 1;

    // the loop being drawn
    if (MAP.path && MAP.path.length > 1) {
      ctx.save();
      ctx.lineWidth = 1.5;
      ctx.strokeStyle = css.getPropertyValue('--accent') || '#2f63e0';
      ctx.fillStyle = ctx.strokeStyle;
      ctx.globalAlpha = 0.08;
      ctx.beginPath();
      ctx.moveTo(MAP.path[0][0], MAP.path[0][1]);
      for (var i = 1; i < MAP.path.length; i++) ctx.lineTo(MAP.path[i][0], MAP.path[i][1]);
      ctx.closePath();
      ctx.fill();
      ctx.globalAlpha = 0.9;
      ctx.setLineDash([4, 3]);
      ctx.stroke();
      ctx.restore();
    }
  }

  function drawMap(canvas, shown) {
    layoutMap(canvas);
    paintMap(canvas, shown);
    bindMap(canvas, shown);
  }

  /* A drag shorter than this is a click, not a lasso. Without a threshold every
   * click becomes a one-point polygon that selects nothing and wipes the
   * focused paper. */
  var DRAG_MIN = 8;

  function bindMap(canvas, shown) {
    var drag = null, suppressClick = false;

    canvas.onmousemove = function (ev) {
      if (drag) return;                       // no tooltips mid-lasso
      var r = canvas.getBoundingClientRect();
      var hit = pick(ev.clientX - r.left, ev.clientY - r.top);
      var tipEl = document.getElementById('maptip');
      if (!hit) { tipEl.hidden = true; canvas.style.cursor = 'crosshair'; return; }
      canvas.style.cursor = 'pointer';
      tipEl.hidden = false;
      tipEl.textContent = (hit.p.title || hit.p.source);
      var tx = Math.min(hit.x + 12, MAP.w - 260);
      tipEl.style.left = Math.max(4, tx) + 'px';
      tipEl.style.top = (hit.y + 14) + 'px';
    };
    canvas.onmouseleave = function () { document.getElementById('maptip').hidden = true; };

    canvas.onclick = function (ev) {
      if (suppressClick) { suppressClick = false; return; }   // that was a lasso
      var r = canvas.getBoundingClientRect();
      var hit = pick(ev.clientX - r.left, ev.clientY - r.top);
      state.focus = hit ? hit.p.id : null;
      render();
    };

    function at(ev) {
      var r = canvas.getBoundingClientRect();
      return [ev.clientX - r.left, ev.clientY - r.top];
    }

    canvas.onpointerdown = function (ev) {
      if (ev.button !== 0) return;
      drag = { moved: 0, last: at(ev) };
      MAP.path = [drag.last];
      document.getElementById('maptip').hidden = true;
      // So the drag keeps reporting even when the pointer leaves the canvas --
      // a lasso around the edge points is exactly when that happens.
      // Guarded: capture throws on a pointer id the browser does not consider
      // active, and a throw here would kill the lasso outright.
      try { canvas.setPointerCapture(ev.pointerId); } catch (e) { /* not fatal */ }
    };

    canvas.onpointermove = function (ev) {
      if (!drag) return;
      var pt = at(ev);
      var dx = pt[0] - drag.last[0], dy = pt[1] - drag.last[1];
      if (dx * dx + dy * dy < 9) return;      // 3px, so the path stays short
      drag.moved += Math.sqrt(dx * dx + dy * dy);
      drag.last = pt;
      MAP.path.push(pt);
      paintMap(canvas, shown);
      var live = document.getElementById('lassolive');
      if (live && drag.moved > DRAG_MIN) {
        live.hidden = false;
        live.textContent = countIn(MAP.path, shown) + ' selected';
      }
    };

    canvas.onpointerup = function (ev) {
      if (!drag) return;
      var wasDrag = drag.moved > DRAG_MIN;
      var poly = MAP.path;
      drag = null;
      MAP.path = null;
      var live = document.getElementById('lassolive');
      if (live) live.hidden = true;
      if (!wasDrag) { paintMap(canvas, shown); return; }   // a click; onclick handles it
      suppressClick = true;
      var ids = MAP.pts.filter(function (q) {
        return shown[q.p.id] && inPolygon(q.x, q.y, poly);
      }).map(function (q) { return q.p.id; });
      // An empty loop clears rather than selecting nothing -- that is what
      // drawing a circle round the whitespace obviously means.
      state.sel = null;
      if (ids.length) {
        state.sel = {};
        ids.forEach(function (id) { state.sel[id] = true; });
      }
      render();
    };
    canvas.onpointercancel = canvas.onpointerup;
  }

  function countIn(poly, shown) {
    var n = 0;
    MAP.pts.forEach(function (q) {
      if (shown[q.p.id] && inPolygon(q.x, q.y, poly)) n++;
    });
    return n;
  }

  function selCount() {
    return state.sel ? Object.keys(state.sel).length : 0;
  }

  function pick(x, y) {
    var best = null, bestD = 144;   // 12px radius
    MAP.pts.forEach(function (q) {
      var d = (q.x - x) * (q.x - x) + (q.y - y) * (q.y - y);
      if (d < bestD) { bestD = d; best = q; }
    });
    return best;
  }

  /* The panel under the map when a point is selected. */
  function focusPanel(p) {
    return el('div', { 'class': 'record focus' }, [
      el('button', { 'class': 'back', type: 'button', text: '× clear selection',
        onclick: function () { state.focus = null; render(); } }),
      el('h2', { style: 'font-size:16px', html: hl(p.title) }),
      el('p', { 'class': 'meta' }, [
        el('span', { text: [p.first_author, p.year, p.venue].filter(Boolean).join(' · ') }),
        document.createTextNode(' '), badges(p)
      ]),
      el('div', { 'class': 'actions' }, [
        el('button', { 'class': 'btn', type: 'button', text: 'Open the record',
          onclick: function () { go(p); } })
      ]),
      similarEl(p, 5)
    ]);
  }

  /* Nearest neighbours, from embed.py's full-space top-k. The cosine and the
   * shared terms are shown deliberately: a match joined by nothing but
   * "machine, learning" should look as thin as it is (ADR 0002). */
  function similarEl(p, limit) {
    if (!SIM) return null;
    var near = nearOf(p).slice(0, limit || 5);
    var kids = [el('h3', { text: 'Similar papers' })];
    if (!near.length) {
      kids.push(el('p', { 'class': 'crumb', text:
        'No paper in the library is close enough to this one to list (cosine below ' +
        SIM.min_sim + '). Nothing is shown rather than something thin.' }));
      return el('div', {}, kids);
    }
    kids.push(el('ul', { 'class': 'simlist' }, near.map(function (n) {
      var q = BY_ID[n.id];
      if (!q) return null;
      return el('li', {}, [
        el('button', { 'class': 'simhit', type: 'button',
          onclick: function () { go(q); } }, [
          el('span', { 'class': 'simtitle', text: q.title }),
          el('span', { 'class': 'simmeta', text:
            [q.first_author, q.year].filter(Boolean).join(' · ') })
        ]),
        el('span', { 'class': 'simscore', title:
          'Cosine similarity in the full 128-d embedding space, not from the map.',
          text: n.sim.toFixed(2) }),
        n.terms && n.terms.length
          ? el('span', { 'class': 'simterms', text: 'shared: ' + n.terms.join(', ') })
          : null
      ]);
    }).filter(Boolean)));
    kids.push(el('p', { 'class': 'crumb', text:
      'Computed in the full embedding space, not from positions on the map — ' +
      'neighbours read off a projection are partly an artefact of it.' }));
    return el('div', {}, kids);
  }

  /* ── routing ──────────────────────────────────────────────────────── */

  function go(p) { location.hash = '#/p/' + encodeURIComponent(p.id); }

  function current() {
    var m = /^#\/p\/(.+)$/.exec(location.hash || '');
    if (!m) return null;
    var id = decodeURIComponent(m[1]);
    return PAPERS.filter(function (p) { return p.id === id; })[0] || null;
  }

  function render() {
    renderSidebar();
    syncViewButtons();
    var p = current();
    if (p) {
      renderRecord(p);
    } else if (state.view === 'map') {
      renderMap();
      document.title = 'Map — ' + NAME;
    } else {
      renderList();
      document.title = NAME;
    }
  }

  function syncViewButtons() {
    var box = document.getElementById('viewtoggle');
    if (!box) return;
    Array.prototype.forEach.call(box.children, function (b) {
      b.setAttribute('aria-pressed', b.dataset.view === state.view ? 'true' : 'false');
    });
  }

  function setQuery(v) {
    state.q = v;
    var box = document.getElementById('q');
    if (box.value !== v) box.value = v;
    render();
  }

  function reset() {
    state.scope = 'all';
    state.sel = null; state.lasso = null;
    state.topics = []; state.authors = []; state.authorq = '';
    state.venues = []; state.venueq = '';
    state.years = []; state.types = []; state.flags = [];
    setQuery('');
  }

  /* ── theme: the same storage key as workpage, so the choice is shared ─ */

  function initTheme() {
    var KEY = 'vennkit.theme.v1';   // deliberately workpage's key; same origin
    var box = document.getElementById('theme');
    /* A canvas is not CSS. Everything else on the page restyles itself when the
     * theme attribute changes; the map is PAINTED, so its colours are whatever
     * the theme was at paint time and it has to be told. That was already true
     * of the neighbour links and the dot outlines, which read --ink and
     * --panel; it became impossible to miss once the part colours moved into
     * CSS too, because switching to light left nine dark dots on white. */
    function repaintIfMap() {
      if (state.view === 'map' && !current() && document.getElementById('map')) {
        render();
      }
    }
    function apply(pref) {
      if (pref === 'system') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', pref);
      Array.prototype.forEach.call(box.children, function (b) {
        b.setAttribute('aria-pressed', b.dataset.pref === pref ? 'true' : 'false');
      });
      repaintIfMap();
    }
    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) { saved = null; }
    apply(saved === 'light' || saved === 'dark' ? saved : 'system');
    box.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-pref]');
      if (!b) return;
      try { localStorage.setItem(KEY, b.dataset.pref); } catch (err) { /* private mode */ }
      apply(b.dataset.pref);
    });
    window.addEventListener('storage', function (e) {
      if (e.key === KEY) apply(e.newValue || 'system');
    });
    /* And on `system`, the OS can change under us with no click at all. */
    if (window.matchMedia) {
      var mq = window.matchMedia('(prefers-color-scheme: dark)');
      var onScheme = function () {
        if (!document.documentElement.hasAttribute('data-theme')) repaintIfMap();
      };
      if (mq.addEventListener) mq.addEventListener('change', onScheme);
      else if (mq.addListener) mq.addListener(onScheme);
    }
  }

  /* ── boot ─────────────────────────────────────────────────────────── */

  var box = document.getElementById('q');
  var timer = null;
  box.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { state.q = box.value; render(); }, 90);
  });
  box.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { box.value = ''; setQuery(''); }
  });
  document.getElementById('clearq').addEventListener('click', function () {
    box.value = ''; setQuery(''); box.focus();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && e.target !== box) { e.preventDefault(); box.focus(); }
  });
  window.addEventListener('hashchange', render);

  var vt = document.getElementById('viewtoggle');
  if (vt) {
    if (!SIM) {
      // No embed step has run: do not offer a view that cannot work.
      vt.hidden = true;
    } else {
      vt.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-view]');
        if (!b) return;
        state.view = b.dataset.view;
        if (location.hash) location.hash = ''; else render();
      });
    }
  }

  // The link back to the landing page is meaningless over file://, so it is hidden
  // in the HTML and revealed only when a server is actually serving this.
  var up = document.getElementById('uplink');
  if (up && location.protocol.indexOf('http') === 0) up.hidden = false;

  initTheme();
  render();
})();

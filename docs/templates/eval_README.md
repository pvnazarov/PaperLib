# eval/ — expectations written down before the answers

Nothing in this directory is required to build the library. It exists because two
questions have a way of being answered after the fact, and both are load-bearing:

1. **Does the search find the right paper?**
2. **Is this clustering better than the one it replaced?**

The discipline is the same for both: **commit the criteria before you look at the
results.** A threshold chosen after seeing the number it has to clear is not a
threshold, and a "MUST" that was demoted to a "SHOULD" when it failed is not a
criterion. Both of those are easy to do by accident and impossible to detect later.

## Two files

**`expectations.json`** — search queries with the papers that should come back.

```json
{
  "pool_review": "2026-01-15_literature_review.md",
  "queries": [
    {
      "q": "single-cell foundation model",
      "must_include": ["Surname(2025) Nature; Some title.pdf"],
      "hit_topics": ["Foundation models for cells and omics"],
      "note": "why this query is a fair test, in one line"
    }
  ]
}
```

`pool_review` pins the evaluation to ONE review file. Pin it, and keep it pinned.
A pool that follows "whatever the newest review is" silently changes the
denominator every time a review is regenerated: in one real case the pool grew
from 234 to 338 papers and a score moved from 38/55 to 37/55 with **no vector and
no query changed**. The score looked like a regression; nothing had regressed.

When a regenerated review renames the topics an expectation refers to, the fix is
to read the labels out of the pinned review — **never** to rewrite the expectation.
Editing ground truth after seeing the answers is the failure this whole directory
exists to prevent, and it is indistinguishable from an honest edit a week later.

**`reclustering.json`** — MUST and SHOULD criteria for a change to the taxonomy,
written before any candidate taxonomy exists.

```json
{
  "written_before": "any candidate taxonomy existed",
  "circularity": "state it here: the vectors that measure cohesion are the same
                  vectors that proposed the clusters, so cohesion cannot be an
                  independent test of them",
  "must":   [{"id": "coverage", "claim": "every paper is in exactly one topic"}],
  "should": [{"id": "cohesion", "claim": "median within-topic cohesion does not fall"}]
}
```

Say the circularity out loud. If the same vectors both propose and score the
clustering, cohesion measures agreement with the proposer, not quality — and a
document that does not admit that is inviting the reader to over-trust it.

## Reporting

`scripts/score_eval.py` reads these and prints what passed and what failed. Report
the failures. A criterion that failed and was reported is a finding; a criterion
that failed and was quietly dropped is a defect in the evaluation, not in the
thing evaluated.

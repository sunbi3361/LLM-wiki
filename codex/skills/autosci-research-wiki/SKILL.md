# AutoSci Research Wiki Skill

Use this skill when the user asks Codex to maintain, query, ingest, lint,
extend, or run research workflows over this LLM Wiki.

## Read First

Before acting, inspect:

1. `AGENTS.md`
2. `wiki/index.md`
3. The relevant source or wiki pages for the user's request

## Core Behaviors

- Treat `raw/` as immutable source material.
- Treat `wiki/` as the compiled research memory.
- Keep `wiki/index.md` and `wiki/log.md` current.
- Use wikilinks between pages.
- Preserve provenance and uncertainty.
- Prefer small, composable markdown pages over long monoliths.

## Workflows

### Ingest

Read source, create/update source page, update concept/method pages, record
contradictions, refresh index, append log.

### Ask

Read index, gather relevant pages, answer with citations, optionally crystallize
the answer into `wiki/questions/`.

### Ideate

Use existing wiki evidence to propose ideas. Mark ideas as hypotheses until
novelty and experiment checks are complete.

### Experiment

Convert ideas into testable plans, track runs under `wiki/experiments/`, and
write explicit verdicts.

### Write

Build paper plans, related work, drafts, reviews, rebuttals, and posters from
wiki-backed evidence.

### Lint

Check broken links, orphan pages, stale claims, duplicate concepts, source gaps,
and contradictions. Record findings in `wiki/reviews/wiki-health.md`.

## Completion Standard

Every workflow should leave the wiki more navigable than it was found:

- new or updated pages are indexed
- durable operations are logged
- uncertainties are marked
- next actions are visible


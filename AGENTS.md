# Codex Wiki Librarian Instructions

You are the maintainer of this LLM Wiki. Treat the repository as a persistent
research memory, not as a transient chat workspace.

## Core Architecture

The wiki has three layers:

- `raw/`: immutable source material curated by the user.
- `wiki/`: compiled markdown knowledge authored and maintained by Codex.
- `AGENTS.md` plus `codex/skills/`: the schema and operating procedure.

The user curates sources and asks questions. Codex handles summarization,
cross-linking, synthesis, contradiction tracking, logging, and maintenance.

## Write Discipline

- Do not modify files under `raw/` unless the user explicitly asks.
- Update `wiki/index.md` whenever pages are added, renamed, or materially changed.
- Append to `wiki/log.md` for every ingest, query crystallization, lint pass, or research-stage transition.
- Prefer `[[wikilinks]]` for wiki-to-wiki references.
- Preserve provenance. If a claim comes from a source, name the source page or raw file.
- Mark uncertain claims with `Status: hypothesis`, `Status: needs-source`, or `Status: conflict`.
- When a new source contradicts old knowledge, do not silently overwrite. Add a note under "Contradictions / Tensions" and link both sources.
- Keep pages compact but connected. Split pages when a concept, method, paper, experiment, or idea becomes independently reusable.

## Wiki Page Types

Use these directories:

- `wiki/foundations/`: stable background concepts and domain primers.
- `wiki/papers/`: one page per paper or source document.
- `wiki/concepts/`: reusable concepts, mechanisms, entities, systems, datasets, and metrics.
- `wiki/methods/`: algorithms, workflows, implementation patterns, and experimental methods.
- `wiki/ideas/`: research ideas, hypotheses, project proposals, and novelty checks.
- `wiki/experiments/`: experiment plans, runs, results, and verdicts.
- `wiki/manuscripts/`: outlines, paper plans, drafts, figures, and submission artifacts.
- `wiki/reviews/`: reviews, rebuttal notes, critique passes, and decision logs.
- `wiki/questions/`: crystallized answers to user questions.

## Ingest Workflow

When asked to ingest:

1. Inspect `wiki/index.md` first to understand existing coverage.
2. Read the target raw source.
3. Create or update a `wiki/papers/` source page with summary, claims, methods, results, limitations, and links.
4. Update relevant concept, method, idea, and experiment pages.
5. Add contradictions, gaps, or follow-up questions where needed.
6. Update `wiki/index.md`.
7. Append an entry to `wiki/log.md`.

## Query Workflow

When asked a question:

1. Read `wiki/index.md`.
2. Open the smallest relevant set of wiki pages.
3. Answer with citations to wiki pages or raw sources.
4. If the answer is durable, ask whether to crystallize it, or do so directly when requested.

## Lint Workflow

When asked to lint or health-check:

- Find orphan pages, stale claims, missing source links, broken wikilinks, duplicate pages, contradictions, and unindexed pages.
- Write findings to `wiki/reviews/wiki-health.md`.
- Update `wiki/log.md`.

## AutoSci-Style Research Lifecycle

For research projects, organize work through these stages:

1. Literature memory: ingest and consolidate sources.
2. Ideation: generate ideas grounded in the wiki.
3. Experiment design: turn ideas into testable plans.
4. Experiment execution and evaluation: record runs and verdicts.
5. Writing: produce paper plans, drafts, reviews, rebuttals, and posters.
6. Evolution: fold feedback back into the wiki schema and memory.


# Runtime Directory Chart

> On-demand reference for the current Codex LLM-Wiki layout. This is adapted
> from AutoSci's runtime chart, but reflects the lighter structure currently
> present in this repository.

```text
.
├── AGENTS.md          ← Codex runtime schema and wiki-maintenance rules
├── README.md          ← project orientation and first-use guide
├── .gitignore
├── codex/
│   └── skills/
│       └── autosci-research-wiki/
│           └── SKILL.md
│                         ← reusable Codex skill for ingest/query/lint/research workflows
├── docs/
│   ├── commands.md    ← natural-language command menu for Codex
│   ├── codex-autosci-adapter.md
│   │                  ← mapping between AutoSci ideas and this Codex wiki
│   └── runtime-directory-structure.md
│                      ← this file
├── tools/
│   └── wiki_status.py ← lightweight broken-link and index status checker
├── raw/
│   ├── README.md      ← source-layer rules
│   ├── papers/        ← user-owned paper lists, PDFs, TeX, bibliographies
│   ├── notes/         ← user-owned notes and research scraps
│   ├── web/           ← clipped web pages and saved articles
│   ├── data/          ← datasets, result tables, configs, metadata
│   └── assets/        ← images and attachments
└── wiki/
    ├── index.md       ← markdown content catalog
    ├── log.md         ← chronological log (append-only)
    ├── overview.md    ← current whole-wiki synthesis
    ├── foundations/   ← stable background concepts and local design rules
    ├── papers/        ← structured paper/source summaries
    ├── concepts/      ← reusable concepts, mechanisms, entities, datasets, metrics
    ├── methods/       ← algorithms, workflows, implementation patterns
    ├── ideas/         ← research ideas, hypotheses, novelty checks
    ├── experiments/   ← experiment plans, runs, results, verdicts
    ├── manuscripts/   ← outlines, paper plans, drafts, figures, submission artifacts
    ├── reviews/       ← wiki health checks, critique passes, decision logs
    ├── questions/     ← durable answers crystallized from chat
    └── templates/     ← page templates for papers, ideas, and experiments
```

## Current Wiki Layer

```text
wiki/
├── index.md           ← markdown content catalog
├── log.md             ← chronological log (append-only)
├── overview.md        ← current whole-wiki synthesis
├── papers/            ← structured paper summaries
├── concepts/          ← reusable technical concepts
├── ideas/             ← research ideas (with lifecycle status)
├── experiments/       ← experiment records (wiki pages)
├── methods/           ← cross-paper reusable method entities
├── foundations/       ← background knowledge and local design rules
├── manuscripts/       ← paper plans, drafts, figures, submission artifacts
├── reviews/           ← health checks, reviews, rebuttal notes, decision logs
├── questions/         ← crystallized answers to user questions
└── templates/         ← reusable page templates
```

## Current Raw Layer

```text
raw/
├── README.md          ← source-layer guidance
├── papers/            ← user-owned .tex / .pdf sources and paper search notes
├── notes/             ← user-owned .md notes
├── web/               ← user-owned HTML / Markdown
├── data/              ← datasets, tables, configs, metadata
└── assets/            ← images and attachments
```

## Fast Reminders

- `raw/papers/`, `raw/notes/`, and `raw/web/` are user-owned inputs.
- `raw/data/` and `raw/assets/` are also source-layer inputs; Codex should not rewrite them unless explicitly asked.
- The runtime schema for Codex is `AGENTS.md`; the local reusable workflow is `codex/skills/autosci-research-wiki/SKILL.md`.
- `wiki/index.md` should be updated whenever pages are added, renamed, or materially changed.
- `wiki/log.md` should receive an append-only entry for every ingest, query crystallization, lint pass, or research-stage transition.
- `tools/wiki_status.py` checks broken wikilinks and unindexed wiki pages.

## AutoSci Items Not Currently Present

The following AutoSci runtime directories are intentionally not part of the
current lightweight scaffold yet:

- `wiki/CLAUDE.md`
- `wiki/topics/`
- `wiki/people/`
- `wiki/Summary/`
- `wiki/outputs/`
- `wiki/graph/`
- `raw/discovered/`
- `raw/tmp/`
- `config/`

Add these later only when the wiki needs closer AutoSci compatibility, generated
graph artifacts, remote experiment configuration, or larger automated ingest
pipelines.

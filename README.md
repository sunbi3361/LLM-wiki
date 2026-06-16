# LLM Wiki Preview

This directory is a Codex-maintained LLM Wiki scaffold inspired by Karpathy's
LLM Wiki pattern and AutoSci's research-memory workflow.

The working model is simple:

1. Put immutable sources in `raw/`.
2. Ask Codex to ingest, query, lint, or extend the wiki.
3. Codex maintains the compiled knowledge layer in `wiki/`.
4. The operating rules live in `AGENTS.md` and `codex/skills/autosci-research-wiki/SKILL.md`.

## Directory Map

- `raw/` - source-of-truth materials. Codex reads these but does not rewrite them.
- `wiki/` - LLM-authored markdown memory with pages, cross-links, logs, and open questions.
- `docs/` - operator-facing docs, command examples, and design notes.
- `codex/skills/` - reusable local Codex skill instructions for this wiki.
- `tools/` - lightweight helper scripts for checking wiki status.

## First Moves

Add sources to one of these folders:

- `raw/papers/` for PDFs, TeX, paper notes, and bibliographies.
- `raw/notes/` for meeting notes, hypotheses, scraps, and research journals.
- `raw/web/` for clipped articles and web pages.
- `raw/data/` for datasets, result CSVs, configs, and metadata.

Then ask Codex:

- "raw/papers에 있는 논문들을 ingest 해줘"
- "이 wiki에서 GPU SSD 연구 방향을 요약해줘"
- "새 아이디어를 만들어서 novelty check까지 해줘"
- "wiki health check 해줘"

See `docs/commands.md` for a fuller command menu.

## Design Principles

- Raw sources are immutable.
- Wiki pages are compiled, linked, and revised as knowledge improves.
- Every non-obvious claim should point back to a source or be marked as a hypothesis.
- Important answers from chat should be crystallized back into `wiki/`.
- Logs are append-only so the project history stays auditable.


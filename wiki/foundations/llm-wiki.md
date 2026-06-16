# LLM Wiki

Status: foundation

The LLM Wiki pattern separates knowledge work into three layers:

- immutable raw sources
- an LLM-maintained markdown wiki
- a schema file that teaches the agent how to maintain the wiki

The central idea is that useful synthesis should compound. Instead of
re-reading raw documents from scratch for every question, Codex should compile
knowledge once, link it, revise it when new sources arrive, and preserve the
reasoning trail.

## Local Rules

- `raw/` is the source of truth.
- `wiki/` is the compiled memory.
- `AGENTS.md` is the operating schema.
- `wiki/index.md` is the navigation map.
- `wiki/log.md` is the chronological record.

## Maintenance Checks

- Are new pages indexed?
- Do important claims cite sources?
- Are contradictions explicitly flagged?
- Are there orphan pages with no inbound links?
- Did a useful chat answer get crystallized into `wiki/questions/`?

## Links

- [[../overview]]
- [[autosci]]


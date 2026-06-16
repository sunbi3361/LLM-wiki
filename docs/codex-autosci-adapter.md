# Codex AutoSci Adapter

This repository adapts AutoSci's research-memory architecture to Codex.

AutoSci contributes the lifecycle shape:

- memory-centered research workspace
- literature ingest
- idea generation
- experiment design and execution
- paper writing and review
- evolving procedures over time

Karpathy's LLM Wiki contributes the core substrate:

- immutable `raw/` sources
- LLM-maintained `wiki/` pages
- a schema file that teaches the agent how to behave

This scaffold keeps the implementation lightweight: markdown and shell-friendly
files first, optional tools second.

## Mapping

| AutoSci idea | This repo |
| --- | --- |
| SciMem long-term memory | `wiki/foundations/`, `wiki/concepts/`, `wiki/methods/` |
| Active research memory | `wiki/ideas/`, `wiki/experiments/`, `wiki/manuscripts/`, `wiki/reviews/` |
| SciFlow lifecycle | command menu in `docs/commands.md` |
| SciDAG operators | future reusable workflows under `codex/skills/` |
| SciEvolve | updates to `AGENTS.md`, skill files, and wiki health reviews |

## Operating Boundary

This is not a full AutoSci clone. It is a wiki-first Codex workspace that can
grow toward AutoSci-like automation as sources, experiments, and manuscript
artifacts accumulate.


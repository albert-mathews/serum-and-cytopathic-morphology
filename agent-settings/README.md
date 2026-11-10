# agent-settings/ — central agent guidance

This folder is the tracked, human-readable home for the guidance every stream agent follows. It is written
for two audiences: **the agents** (who load these rules) and **repo readers** (who want to see what the
agents are told without hunting through local tooling).

| File | What it is |
|------|-----------|
| `README.md` | This index |
| `agents.md` | The stream → agent manifest and the shared behavior contract |
| `research-strategy.md` | The standard literature workflow (search → full text → `<STREAM>_pdf_wishlist.md`) |
| `environment.md` | The single shared Python venv and how agents use it |

## Shared repositories of truth (top level)

| File | Role |
|------|------|
| [`../CLAIMS.md`](../CLAIMS.md) | Argument claims register (`C###` IDs, proof-style kinds, Mermaid dependency graph) |
| [`../CONVENTIONS.md`](../CONVENTIONS.md) | Repo-wide working language: evidence tags, Mermaid, role codes, stream discipline, file placement |
| [`../P4_P7_index.md`](../P4_P7_index.md) | Formalized prediction extensions P4–P7 |
| [`../TODO.md`](../TODO.md) | Shared research roadmap |

## Local-only (gitignored, not committed)

These frame *how* research is conducted but must never appear in a public surface:

- `grok.md`, `grok_guardrails.md`, `interpretive_lens.md` (repo root, gitignored)
- `.opencode/agents/*.md` (the runtime prompts OpenCode loads — mirrors the manifest in `agents.md`)

Everything in this folder is tracked; nothing here names real raters/freelancers/CRO staff, and nothing here
contains participant-identifying or briefing-condition detail.
# P3 Step 1 — Sequence origin / confirmation mapping (protocol)

**Updated:** 2026-09-21 (evidentiary-bar clarification; USER 2026-09-21).

**Goal.** For named viruses, reconstruct the **documented link** between (a) how the sequenced sample was produced and (b) the genome that was deposited / published as the reference. Learn what fraction of first (and major confirming) public genetic sequences rest on **cell culture ± CPE** vs clinical-direct, eggs, animal-only, other, or unclear paths. Exploration, not advocacy.

**Core research question.** How many viral genome origins were produced by sampling biologic material claimed to be a virus isolate by means of **cell culture ± CPE** — versus clinical-direct sequencing, eggs, animal-only passage, other, or unclear?

**Core framing.** Before any virus was sequenced there were zero viral contigs. Then someone sequenced *something* and claimed a viral genome. That thread should document, as far as ordinary scientific records allow:

1. **Sample production** — what biologic material was input, and how it was produced (clinical specimen; culture ± CPE/plaques/syncytia; eggs; animal passage; etc.)
2. **Sequencing** — tools and results
3. **Viral warrant** — how they concluded the sequence is viral
4. **Deposit** — accession / GenBank / published sequence that became the reference

## Evidentiary bar (mandatory — USER 2026-09-21)

We are **NOT** seeking forensic A→B→C custody of a physical tube.

We need **adequate documented evidence** linking **method by which the sequenced sample was produced** ↔ **genome deposited**, within reasonable (scientific) doubt — not chain-of-custody paperwork.

**Acceptable patterns include (EXAMPLES ONLY — not an exclusive list):**

1. Researchers publish a repeatable isolate-production method; later depositors use that method/stock and deposit the first known genetic sequence.
2. The depositing paper itself reports the exact method used to produce the sample that was sequenced.
3. An upstream isolate / stock / vaccine-seed paper clearly used for the sequenced material states culture ± CPE (or another path).
4. A methods-citation chain, GenBank/paper Methods block, seed-lot history, or any other ordinary scientific record that adequately shows how the sequenced material was produced.

Use common sense and imagination for **any** documentary pattern that adequately makes the method↔deposit link. If that link is clear in Methods quotes (deposit paper and/or clearly used upstream papers), set `chain_closed` and assign `path_score`. **Do NOT** keep chains open awaiting hospital paperwork, intermediate handoff logs, or forensic custody of aliquots.

If method is only “purified RNA from lab stock” with **no** usable upstream production record, keep chasing open pointers — but close when the production path for the sequenced material is adequately stated.

## Constraints
- No phage. No HIV (unless user lifts the park).
- Prefer OA/PMC; paywalled PDFs only if user supplies them into gitignored `refs/sequence_origins/`.
- Never invent Methods. Never close a chain on trust-me-bro with zero documentary link.
- Tracked artifacts under `p3_genetics/sequence_origins/`; PDFs only under gitignored `refs/sequence_origins/`.
- Dozens of virus families is the target scale; five was a starter spine, not a ceiling.

## Event types
- **Origin (O):** first/defining complete (or near-complete) sequence report that established the public sequence ontology for that named virus/strain.
- **Confirmation (C):** later resequence / independent complete genome / major correction of the same type material.
- **Provenance node (P):** upstream paper that does **not** itself deposit the genome but supplies the sample/stock/RNA/DNA used by an O or C event. Link with `feeds_event_id`.

## Qualifying origin/confirmation paper
Must speak to (1) methods for material sequenced, (2) sequencing outcome, and ideally (3) deposit/accession or published sequence that became reference. Abstract-only is allowed only with `access` noted and chain left open where Methods are missing — unless another ordinary record (GenBank Methods, clearly used upstream isolate paper, vaccine-seed history, etc.) adequately closes the method↔deposit link.

## Provenance chain rules (mandatory)
1. Start at the O/C paper. Quote the exact sample-prep sentence(s).
2. Extract every citation that supplies RNA/DNA/virions/stock/cells.
3. Open those papers when needed. Follow until sample production for the sequenced material is adequately documented **or** the chain honestly ends in `provenance_gap`.
4. Record the chain as ordered `event_id` / `P` nodes. Depth may be 1 paper (deposit Methods suffice) or 2–6+.
5. **path_score applies to the sequenced material’s production path** once the method↔deposit link is adequate — not to wording pedantry on the genome paper alone.
6. Codes for chain status: `chain_closed` | `chain_open` | `provenance_gap` (cited source unavailable / circular cite / no wet prep ever stated).

## path_score (closed set — scored when chain is closed enough to choose)
| Code | Meaning |
|------|---------|
| `culture_cpe` | Sequenced material ultimately from cell culture; at least one paper in the resolved record documents CPE / plaques / syncytia (or clear CPE-equivalent morphology) as part of isolate assertion or stock production for that material |
| `culture_no_cpe` | Culture/propagated stock clearly documented; CPE/plaques never stated anywhere in the resolved record |
| `clinical_direct` | Sequenced directly from clinical specimen without culture passage for the sequenced material |
| `other` | Eggs, animal-only passage, synthetic/clone assembly, etc. |
| `unclear` | Even after chasing available records, Methods still insufficient to choose — use sparingly; do not default everything to unclear |

**Important:** Do **not** mark `culture_no_cpe` merely because the genome paper omitted CPE while citing a culture stock that itself documents CPE upstream — score `culture_cpe`. Do **not** leave `chain_open` solely because intermediate custody paperwork is missing when production method for the sequenced material is otherwise clear.

## Deliverables
1. Per-family `family_<name>.md` — narrative + **provenance chains** for each O/C
2. `P3_sequence_origin_events.csv` (O/C rows)
3. `P3_sequence_provenance_nodes.csv` (P rows + `feeds_event_id`)
4. Bibliography + search log
5. PDFs when OA or user-supplied
6. `P3_step1_family_expansion_list.md` — working list of dozens of families
7. `P3_step1_progress_summary.md` — honest fractions; never claim “done” while major chains are open

## CSV columns (events)
`event_id,family,virus,strain,event_type,year,first_author,title,journal,pmid,doi,accession,path_score,chain_status,culture_system,cpe_evidence,sample_prep_quote,upstream_cites,access,pdf_local,notes`

## CSV columns (provenance nodes)
`node_id,feeds_event_id,year,first_author,title,pmid,doi,role,prep_summary,cpe_stated,access,pdf_local,notes`

event_id pattern: `POL-O1`, `POL-O4` (Kitamura), `POL-C1`, `MEA-O1`, …

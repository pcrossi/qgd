# AGENTS.md - Brain protocol for GDQ

This folder is the structured memory layer for the GDQ project.

It complements, but does not replace, the manuscript, `memory.md`, or the
question files. The goal is to preserve a clean hierarchy of facts, proofs,
status, and open work so the project can be resumed without re-deriving the
same context.

## 1. Role of `brain/`

Use `brain/` as the canonical structured index for:

- axioms;
- definitions;
- theorems;
- lemmas;
- hypotheses;
- conditional results;
- numerical results;
- decisions;
- open problems;
- future ideas;
- notes and references.

Each important claim should have one canonical home in `brain/` and, when
needed, supporting notes in adjacent files.

## 2. Canonical hierarchy

Recommended top-level structure:

- `brain/index.md`
- `brain/axioms/`
- `brain/definitions/`
- `brain/theorems/`
- `brain/lemmas/`
- `brain/hypotheses/`
- `brain/conditional-results/`
- `brain/open-problems/`
- `brain/numerics/`
- `brain/decisions/`
- `brain/notes/`
- `brain/future/`
- `brain/references/`
- `brain/templates/`

Each substantive item should have:

- one `index.md` as the canonical summary;
- one `status.md` if the item has a live status;
- one `proof.md` or `derivation.md` if the argument is nontrivial;
- one `notes.md` if there are auxiliary observations.

## 3. Status vocabulary

Use the following statuses consistently:

- `axiomatic`
- `defined`
- `demonstrated`
- `conditionally_demonstrated`
- `structurally_closed`
- `numerically_supported`
- `exploratory`
- `open`
- `future`
- `superseded`

Do not declare an item closed if a hypothesis, boundary condition, or numeric
calibration remains essential.

## 4. Relation to `agentmemory`

The MCP memory should store compact, durable facts only:

- decisions;
- stable derivations;
- status changes;
- key numerical outcomes;
- file paths to the canonical documents.

The detailed hierarchy remains in `brain/`. Use memory entries as an index,
not as a substitute for the document tree.

When saving a memory entry, include:

- stable concepts;
- the canonical file path(s);
- the present status;
- whether the result is foundational, conditional, numeric, or future work.

## 5. Writing rules

- Keep the canonical statement short and explicit.
- Separate theorem statement from proof.
- Separate derivation from numerical check.
- Separate closed results from open dependencies.
- Preserve historical material; do not overwrite the provenance of a result.
- If a claim is only conditional, say so in the title and the status.

## 6. Search and recovery

To recover context, search in this order:

1. `brain/index.md`
2. the specific topic folder
3. `memory.md`
4. `faltas.md`, `faltas_plano.md`, and `faltas_mapa.md`
5. the manuscript and question files
6. `agentmemory` for historical context and file-level traces

## 7. Minimal template for an item

Suggested fields:

- `title`
- `status`
- `scope`
- `assumptions`
- `statement`
- `proof`
- `checks`
- `limitations`
- `dependencies`
- `references`


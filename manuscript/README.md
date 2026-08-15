	# Quantum Geometrodynamics — GDQ

Welcome to the restructured edition of the **Quantum Geometrodynamics (GDQ)** manuscript.

This directory gathers the version intended for continuous reading and publication with Obsidian and Quartz. Historical material, audits, exploratory calculations, and simulations remain in the working repository but are not automatically treated as proven parts of the manuscript.

## What is the proposal about?

GDQ investigates the possibility of describing matter, quantum phenomena, and their classical limits from a dynamic complex geometry, equipped with flow, weighted measure, boundaries, and torsion.

Instead of assuming point particles inserted in a rigid geometric background, the program explores the hypothesis that matter and its observable properties can correspond to localized configurations, circulations, and defects of the geometry itself.

The initial problem arises from the comparison between two path integrals:

- the Wiener integral, based on a positive probability measure and associated with diffusion;
- the Feynman integral, based on complex oscillatory amplitudes and associated with quantum interference.

The manuscript seeks to determine whether these regimes can be reconstructed as compatible aspects of the same geometric dynamics, without improperly identifying probabilities with amplitudes or treating Wick rotation as an automatic equivalence.

## An experiment in iterative construction with artificial intelligence

In addition to the physical proposal, this repository records an atypical development method. Intuitions, conceptual connections, and drafts accumulated over time are organized and tested iteratively with the help of artificial intelligence models.

Development primarily uses two AI environments:

- **Codex/GPT, from OpenAI**;
- **Antigravity/Gemini, from Google**.

There is no fixed division of functions between them. Depending on the stage of the work, either of the two can be used to organize the manuscript, propose ideas, develop derivations, build numerical tests, research alternative routes, or critically review a result. At other times, one system is used to check, correct, or expand the work produced by the other. Relevant responses are subsequently compared with the documents, with the official action, with numerical tests, and with available references.

AI is used as an intellectual amplification tool to:

- organize fragments and dependencies;
- make previously implicit hypotheses explicit;
- develop and check algebraic steps;
- build numerical tests;
- locate contradictions and gaps;
- separate results from conjectures and parameter fits.

Codex/GPT and Antigravity/Gemini participate in this work as intellectual collaboration systems, contributing to organization, calculation, and critical review. The value of each contribution is determined by its consistency, traceability, and capacity to resist verification, regardless of whether it was initially formulated by the author or by one of the AI systems. No isolated response constitutes scientific validation or replaces proof, experimental evidence, or independent review.

## Scientific status of the work

This is a research manuscript in development, produced as an independent intellectual project. Theoretical physics and advanced mathematics are not the author's professional fields of practice. The text should, therefore, be read as a construction open to criticism, correction, and external verification.

To prevent a hypothesis from being confused with a conclusion, the restructured edition distinguishes:

- definition and axiom;
- derivation and conditional theorem;
- effective reduction;
- hypothesis and future program;
- consistency test;
- fit or reverse engineering;
- phenomenological comparison;
- prediction without post-adjustment.

A numerical agreement, on its own, does not demonstrate that a result was derived from the fundamental action. Wherever a link is missing between the action, the background, the operator, the boundary conditions, and the observable, this dependency must remain explicit.

## Organization of this edition

The directory is structured as an Obsidian vault compatible with Quartz:

- [`index.md`](index.md): public index of the edition;
- `01_initial_problem/`: Chapter 1 and its sections;
- `02_geometrization/`: geometrization of matter and official action;
- `03_complex_causality/`: complex causality and continuation;
- `04_action_consistency/`: variational principle and quantum consistency;
- `05_equations_conservation/`: equations of motion and Noether;
- `06_global_local_bridge/`: bridge from Einstein's Universe to the laboratory;
- `07_classical_limit/`: classical limit and the correspondence principle;
- `08_hilbert_quantization_uncertainty/` to `13_holonomies_ab_sagnac/`: quantum reconstruction, measure, spin, transport, and holonomies;
- `14_geometric_particle_taxonomy/` to `21_cp_hopf_monopoles/`: taxonomy, masses, effective fields, confinement, electroweak, gravitation, and topology;
- `22_hydrogen_atom/` to `25_astrophysics_cosmology/`: atomic, nuclear, astrophysical, and cosmological applications;
- `26_logical_status/` to `28_technical_faq/`: logical status, numerical protocol, and technical FAQ;
- `ref/`: bibliographical sources, full OCR, and OCR per page;
- `notes/`: pedagogical notes intended to explain mathematical language;
- `scripts/`: transversal editorial checkers;
- `formal/`, at the project root: Lean library and index of formal certifications.

Directory names are written in English and without special characters to preserve stable URLs. Public titles in Portuguese are defined in the `title` field of the YAML header of each `index.md`.

Equations follow the Quartz convention: short expressions are written in inline math; highlighted equations use double dollar sign delimiters on their own lines.

## How to read

The entry point is the [Main index of the manuscript](index.md). Sequential reading begins in [01. The initial problem](01_initial_problem/index.md), which formulates the divergence between the Feynman and Wiener integrals before introducing the geometrization of matter.

Pedagogical notes can be consulted without interrupting the main path. They explain concepts and notations, but do not replace the technical proofs, which will be kept in the corresponding chapters or appendices.

The transversal integrity of the edition can be checked in the [reproducible report](notes/editorial/final_transversal_audit.md). This report checks structure, links, Quartz conventions, Python syntax, literal preservation of the official action, and traceability of the scripts; it does not replace scientific or physical review.

## Criticism and collaboration

Mathematical criticisms, independent tests, identification of hidden hypotheses, and attempts at refutation are welcome. The objective of this publication is not to present a completed theory by decree, but to make its logical chain visible enough so that it can be examined.

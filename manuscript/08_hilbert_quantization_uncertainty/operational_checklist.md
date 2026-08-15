---
title: "Operational checklist — Chapter 8"
---

# Operational checklist — Chapter 8

This checklist records the status of Chapter 8.

## 1. Statement

Show that the physical Hilbert space, circulation quantization, and uncertainty inequalities emerge as sectorial operational reconstructions of GDQ, not as primary axioms.

## 2. Logical Status

| Block | Status | Observation |
|---|---|---|
| Physical Hilbert space | Structurally closed | Conditioned on sectorial reflection positivity. |
| Inner product | Structural | $\langle [F],[G]\rangle=\langle\Theta F\,G\rangle_E$. |
| States, observables, and composition | Structurally closed | Vectors, rays, density matrices, spectral projectors, and tensor product after the physical quotient. |
| Unitariety in $t$ | Conditional theorem | If $H=H^\dagger$, then $U(t)=e^{-itH/\hbar}$ is unitary; decay in a projected sector is effective open theory. |
| Wallstrom | Structurally closed | Integrality comes from $S^1$ phase and $U(1)$ bundle. |
| Heisenberg | Closed in the regular sector | Cauchy-Schwarz applied to the Madelung fluid. |
| Robertson--Schrödinger | Closed in the reconstructed Hilbert | Hermitian positivity. |
| BBM/GUP/global Fubini--Study | Future program | Do not use as closed proof. |

## 3. Deductive Chain

$$
\mathcal S_{\rm GDQ}
\to
\text{positive effective sector}
\to
\mathcal H_{\rm phys}
\to
\text{self-adjoint operators}
\to
\text{unitariety}
\to
\text{circular phase}
\to
\text{Wallstrom}
\to
\text{uncertainty}.
$$

## 4. Preservation Points

- Hilbert is operational, not primary ontology.
- Do not use $t=-i\tau$ as proof of physical time.
- Poisson does not derive quantization; it presupposes integer sectors.
- Non-integer states are not admissible global sections.
- Strict Kähler only in the torsion-free sector; the general geometry is Hermitian/KT.
- Fubini--Study belongs to the reconstructed Hilbert space.
- GUP and BBM remain as conditional extensions.

## 5. Optional Scripts

The scripts in `scripts/` are illustrations of consistency, not new proofs.

| Script | Classification |
|---|---|
| `test_gaussian_uncertainty.py` | Direct evaluation of Heisenberg in Gaussians. |
| `verify_wallstrom_circulation.py` | Symbolic/topological test of integer circulation and integer Chern flux. |
| `verify_hilbert_positivity.py` | Toy model of positivity and quotient by zero norm. |
| `verify_operational_hilbert.py` | Toy model of states, observables, unitary evolution, and tensorization in the physical quotient. |
| `verify_unitary_physical_time.py` | Toy model of unitariety in $t$, Euclidean contraction, and projected decay. |

## 6. Technical Proofs Referenced

- [[notes/construction_gdq_hilbert_quantization|GDQ construction of the physical Hilbert and quantization]]
- [[notes/states_observables_composition_hilbert|States, observables, and composition in the reconstructed Hilbert]]
- [[notes/unitary_physical_time_and_open_sectors|Unitariety in physical time and open sectors]]
- [[notes/wallstrom_u1_line_bundle|Proof of circulation quantization by U(1) bundle]]

## Didactic Revision of 2026-07-19

Chapter 8 was checked during the scientific/didactic revision phase. Section `08.9` was rewritten to present BBM, GUP, global Fubini--Study, and torsional corrections as future extensions of the manuscript itself, without requiring knowledge of historical versions. The Wallstrom note was adjusted to avoid the impression that GDQ adds an external single-valuedness condition: integrality comes from the global geometric admissibility of a section of a $U(1)$ bundle.

The scripts in the chapter remain as consistency illustrations: positivity/Hilbert quotient, integer circulation, and uncertainty in Gaussians. None of them replace the sectorial reconstruction nor use an experimental target.

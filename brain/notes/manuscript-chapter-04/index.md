---
title: Manuscript chapter 04
status: active
concepts:
  - manuscript
  - chapter 04
  - official action
  - variational principle
  - Hessian
  - loops
  - ghosts
  - Landau pole
---

# Manuscript chapter 04

## Scope

This entry indexes the fourth manuscript chapter:

`manuscrito/04_action_consistency/`

The chapter establishes the official GDQ action as the organizing functional
for geometry, density, phase, measure, boundary data, symmetries and
quadratic fluctuations. It also defines what “loop” means inside GDQ:
not imported perturbation theory, but the determinant of the physical Hessian
of the official action on an admissible background.

## Main chain

1. A single action is required to keep density, phase, metric, measure,
   boundary terms and symmetries compatible.
2. The official action is preserved exactly; reductions to Einstein-Hilbert,
   Yang-Mills, Dirac, Pauli or other external functionals are only reductions
   or audit languages.
3. The local bulk is `R^4 x T^4` with real dimension eight and complex
   dimension four.
4. `Lambda_C` in the official action is a dimensionless cutoff number in
   Cartan-normalized coordinates. Physical scales are `ell_C`, `k_C` and
   `E_C`.
5. The measure `U` is constitutive:
   `U = rho/(4 pi z_tau)^n`. It must vary with the density sector.
6. The variational problem uses fields `(g,f,bar f)`, optionally rewritten as
   `(rho,S_R)`, plus declared domain, regularity, boundary and normalization
   data.
7. Phase shifts are a global symmetry and yield a Noether current on shell.
   Local gauge redundancy is not inserted by analogy.
8. Boundary terms are part of the theory. Stomata, excisions, horizons and
   apparatuses require boundary/interface data or source terms.
9. The fundamental one-loop object is
   `Gamma_GDQ^(1) = 1/2 Tr_phys ln Hess S_GDQ`.
10. Ghosts are not GDQ ontology. When used, they represent the Jacobian of a
    gauge section of the physical quotient.
11. Ward identities and Slavnov-Taylor identities are recovered as spectral
    covariance identities of the reduced operator.
12. In the declared U(1) heat-kernel comparison sector, polarization saturates
    in the ultraviolet and the Landau pole is absent under an explicit
    spectral inequality.

## Current status

Chapter 4 is structurally closed as a statement of the action, variational
domain and perturbative meaning of loops. It does not prove universal
non-perturbative finiteness of GDQ, nor does it prove stability of every
background. Those tasks require the physical Hessian, vertices and domains of
the concrete sector under study.

## Detailed memory

- [Full Chapter 4 details](details.md)
- [Called notes and audits](called-notes.md)

## Canonical linked entries

- [Official GDQ action](../../axioms/official-gdq-action/index.md)
- [Dimensional consistency of official action](../../conditional-results/official-action-dimensional-consistency/index.md)
- [GDQ variational data](../../definitions/gdq-variational-data/index.md)
- [Physical Hessian and loops](../../definitions/physical-hessian-loops/index.md)
- [Physical quotient and ghosts](../../conditional-results/physical-quotient-ghosts/index.md)
- [Heat-kernel U(1) polarization](../../conditional-results/heat-kernel-u1-polarization/index.md)
- [Perturbative all-orders finiteness](../../open-problems/perturbative-all-orders-finiteness/index.md)

## Manuscript files

- `manuscrito/04_action_consistency/index.md`
- `manuscrito/04_action_consistency/04.1 - Por que precisamos de uma ação.md`
- `manuscrito/04_action_consistency/04.2 - A ação oficial da GDQ.md`
- `manuscrito/04_action_consistency/04.3 - Campos, medida e dados estruturais.md`
- `manuscrito/04_action_consistency/04.4 - Como ler cada termo da ação.md`
- `manuscrito/04_action_consistency/04.5 - O princípio variacional e suas equações.md`
- `manuscrito/04_action_consistency/04.6 - Simetrias, conservação e bordos.md`
- `manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md`
- `manuscrito/04_action_consistency/04.8 - Alcance e limites do capítulo.md`
- `manuscrito/04_action_consistency/preservation_map.md`

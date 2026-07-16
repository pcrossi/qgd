---
title: Manuscript chapter 05
status: active
concepts:
  - manuscript
  - chapter 05
  - equations
  - conservation
  - Noether
  - Bohm
  - Madelung
---

# Manuscript chapter 05

## Scope

This entry indexes the fifth manuscript chapter:

`manuscrito/05_equations_conservation/`

The chapter executes the first variational pass through the official GDQ
action. It derives the phase current, the density equation with the Bohm
operator, the weighted metric equation, Noether identities and boundary
conditions. It also separates these direct bulk results from the still
conditional reconstruction of the laboratory Madelung system.

## Main chain

1. Start from the official action and vary `U`, `L_0` and `dV_g`; omitting any
   of them changes the equations.
2. Rewrite the complex field as `(rho,S_R)` with `rho>0`.
3. Phase variation leaves the measure fixed and yields a conserved bulk
   phase current.
4. Density variation changes the measure and produces the operator
   `Delta sqrt(rho)/sqrt(rho)`.
5. Metric variation gives a weighted metric-dilatonic equation with
   derivatives of `U`.
6. Noether is proved explicitly: continuous symmetries give off-shell
   identities and on-shell conservation laws.
7. Integrated charge conservation requires no lateral flux or explicit
   interface balance.
8. Boundary conditions arise from the same first variation as the bulk
   equations.
9. The usual Bohm potential and Hamilton-Jacobi-Bohm equation are recovered
   only after the physical reduction fixes the mass/kinetic normalization and
   the canonical term.
10. The identity `Pi_{S_R}=rho` is not an off-shell identity of the official
    action; it is a conditional physical polarization/reduction.

## Current status

Chapter 5 is directly closed for the first variation of the official action
in the declared bulk/Hermitian class. It remains conditional for the
laboratory Madelung dynamics because the pullback, canonical term and
selection of the physical state-space polarization are handled by the
global-local bridge and measurement theory.

## Detailed memory

- [Full Chapter 5 details](details.md)
- [Called notes and audits](called-notes.md)

## Canonical linked entries

- [Phase current and Noether](../../conditional-results/phase-current-noether/index.md)
- [Density equation and Bohm operator](../../conditional-results/density-equation-bohm-operator/index.md)
- [Weighted metric equation](../../conditional-results/weighted-metric-equation/index.md)
- [Boundary conditions from variation](../../definitions/boundary-conditions-variation/index.md)
- [Madelung canonical sector](../../conditional-results/madelung-canonical-sector/index.md)
- [Canonical Madelung selection](../../open-problems/canonical-madelung-selection/index.md)

## Manuscript files

- `manuscrito/05_equations_conservation/index.md`
- `manuscrito/05_equations_conservation/05.1 - Da ação estacionária às equações.md`
- `manuscrito/05_equations_conservation/05.2 - Densidade e fase como variáveis independentes.md`
- `manuscrito/05_equations_conservation/05.3 - Variação da fase e conservação do fluxo.md`
- `manuscrito/05_equations_conservation/05.4 - Variação da densidade e equilíbrio dinâmico.md`
- `manuscrito/05_equations_conservation/05.5 - Variação métrica e resposta geométrica.md`
- `manuscrito/05_equations_conservation/05.6 - Noether, vínculos e condições de bordo.md`
- `manuscrito/05_equations_conservation/05.7 - O que foi demonstrado e o que depende da reconstrução física.md`

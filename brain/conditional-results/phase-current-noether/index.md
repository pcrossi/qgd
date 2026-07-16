---
title: Phase current and Noether
status: active
concepts:
  - phase current
  - Noether
  - conservation
---

# Phase current and Noether

## Statement

The global phase-shift symmetry of the official GDQ action yields a conserved
bulk phase current on shell.

## Symmetry

$$
S_R\mapsto S_R+S_0.
$$

Equivalently:

$$
f\mapsto f+\frac{iS_0}{\hbar},
\qquad
\bar f\mapsto\bar f-\frac{iS_0}{\hbar}.
$$

This leaves `rho` and `U` invariant.

## Current

With the action normalization:

$$
\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U
g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

On shell:

$$
\nabla_\mu\widehat J_S^\mu=0.
$$

## Noether identity

For a continuous symmetry:

$$
\nabla_aJ_\xi^a
=-\mathcal E_A\Delta_\xi\Phi^A.
$$

Conservation follows only when the fields satisfy the Euler-Lagrange
equations.

## Charge condition

Integrated charge conservation also requires no lateral leakage or explicit
interface balance.

## Sources

- `manuscrito/05_equations_conservation/05.3 - Variação da fase e conservação do fluxo.md`
- `manuscrito/05_equations_conservation/05.6 - Noether, vínculos e condições de bordo.md`
- `manuscrito/notes/equations/Derivação da corrente de fase.md`

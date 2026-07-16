---
title: Wick rotation as a conditional bridge
status: conditionally_demonstrated
concepts:
  - Wick rotation
  - analytic continuation
  - Wiener integral
  - Feynman integral
  - boundary terms
  - Euclidean reconstruction
---

# Wick rotation as a conditional bridge

## Statement

Wick rotation relates oscillatory quantum evolution to heat-like Euclidean
evolution only when the operator, domain, boundary data, analytic continuation,
spectral assumptions, positivity, and causal prescription are all controlled.

## What is demonstrated in Chapter 1

If `H` is self-adjoint and bounded below, the unitary group

$$
U(t)=e^{-itH/\hbar}
$$

admits the formal Euclidean continuation

$$
U(-i\tau)=e^{-\tau H/\hbar},
\qquad
\tau>0.
$$

This explains why heat kernels and Wiener-type functionals can represent
Euclidean sectors of quantum problems under suitable hypotheses.

## Limitation

The rotation is not an automatic equivalence between Wiener and Feynman
integrals. Boundary phases, total derivatives, gauge transformations, domains,
and positivity conditions must transform coherently.

## Required conditions

- analytic continuation exists in the required domain;
- singularities and cuts are not crossed incorrectly;
- the operator domain is specified;
- boundary conditions are carried through the continuation;
- positivity is sufficient for Euclidean reconstruction;
- the return to physical time has a causal prescription.

## Source

- `manuscrito/01_initial_problem/01.4 - Rotação de Wick e continuação analítica.md`
- `manuscrito/01_initial_problem/01.5 - Calibre, termos de contorno e rotação de Wick.md`


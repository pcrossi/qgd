---
title: Question 25 - Fermionic sign problem
status: partially_resolved
source: questoes/q25/questao_25.md
updated: 2026-07-16
---

# Question 25 - Fermionic sign problem

Q25 asks whether GDQ has really solved the fermionic sign problem.

Current answer: not as a computational algorithm.

What is structurally established:

$$
\rho=e^{-(f+\bar f)/2}>0
$$

and fermionic antisymmetry is stored in the phase/holonomy:

$$
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar
\quad
(\mathrm{mod}\ 2\pi\hbar).
$$

Thus the sign is not in the positive measure $\rho$, but in monodromy of the
phase bundle.

This is a geometric/structural reformulation, not yet an algorithmic solution.

To close computationally, GDQ needs:

1. explicit estimator for phase-sensitive observables;
2. variance bound;
3. mixing/autocorrelation analysis;
4. asymptotic complexity by class of Hamiltonians;
5. benchmark suite;
6. nodal/holonomy control with error estimates.

A promising route is domain decomposition plus transmission/reflection
matrices across surgery interfaces, but this is a future algorithmic program.

## Status

Q25 is closed only as a distinction: structural geometric reformulation yes;
official algorithmic resolution no.


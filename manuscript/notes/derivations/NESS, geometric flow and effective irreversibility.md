---
title: "NESS, geometric flow and effective irreversibility"
---

# NESS, geometric flow and effective irreversibility

## 1. Three evolutions that must not be identified

In GDQ, three distinct structures appear:

1. the parameter $\tau$ of the geometric flow;
2. the physical time $t$ reconstructed on the laboratory sheet;
3. the reduced evolution of macroscopic variables after a projection.

The flow in $\tau$ can possess monotonic functionals. The closed physical evolution in $t$, when reconstructed by a self-adjoint Hamiltonian, preserves the norm:

$$
\frac{d}{dt}\lVert\Psi(t)\rVert^2=0.
$$

These statements do not contradict each other because they refer to different generators and state spaces.

## 2. Projection and reduced dynamics

If $P$ projects onto monitored observables and $Q=1-P$, the formal elimination of the $Q$ sector produces a Nakajima--Zwanzig type equation:

$$
\frac{d}{dt}P\varrho(t)
=PLP\varrho(t)
+\int_0^tK(t-s)P\varrho(s)\,ds
+I(t),
$$

where $L$ is the microscopic generator, $K$ is a memory kernel, and $I$ depends on unmonitored initial correlations. Even if $L$ generates a reversible evolution, the projected equation can be dissipative.

In the short-memory limit, the kernel can reduce to a local term. The macroscopic entropy can then satisfy:

$$
\frac{dS_{\rm macro}}{dt}\ge0,
$$

without the microscopic norm ceasing to be conserved.

## 3. Operational definition of NESS

A NESS is a reduced state $\varrho_{\rm ss}$ such that:

$$
\frac{d}{dt}\langle O_a\rangle_{\rm ss}=0
$$

for the chosen set of macroscopic observables, but which can sustain currents:

$$
J_a\neq0.
$$

"Stationary" does not mean thermodynamic equilibrium or absence of flow. It also does not mean that the block-universe literally evolves in a fifth physical dimension.

## 4. Correct use in GDQ

GDQ provides natural candidates for the elements of the reduction:

- the measure $\mathcal U$ and Noether currents define the conserved quantities;
- the Hessian separates slow, fast, bound, and continuous modes;
- the apparatus and the interface determine which degrees of freedom are monitored;
- the causal mobility provides the time scale in $t$;
- the flow in $\tau$ organizes geometric relaxation but does not prove physical irreversibility on its own.

Therefore, NESS is an admissible effective reduction of GDQ. For a specific apparatus, dissipation must be derived from the coupling and the influence kernel, not postulated by the simple monotonicity of Perelman.

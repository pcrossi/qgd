---
title: "Measures and integrals in path spaces"
type: note
---

# Measures and integrals in path spaces

## Intuitive idea

A common integral sums contributions associated with points. A path integral sums contributions associated with entire functions. Instead of asking how much a function is worth at each position $x$, we ask how much a functional $F[x]$ is worth for each possible trajectory $x(t)$.

The set of all these trajectories is an infinite-dimensional space. Therefore, symbols like

$$
\int F[x]\mathcal D x
$$

need a construction that explains which paths are admitted, how they are weighted, and in what sense the limit exists.

## Positive measure

A positive measure assigns a number $\mu(A)\geq0$ to each admissible set $A$. If $\mu$ is a probability measure,

$$
\mu(\Omega)=1,
$$

where $\Omega$ is the space of all possible outcomes.

The expectation of a variable $F$ is

$$
\mathbb E[F]
=\int_{\Omega} F\,d\mu.
$$

The Wiener measure is of this type. It is constructed so that the increments of the Brownian path have compatible Gaussian distributions in all temporal partitions.

## Why Brownian trajectories do not have ordinary velocity

For a small temporal increment $\Delta t$, Brownian motion has a typical scale

$$
|\Delta x|\sim\sqrt{\Delta t}.
$$

The quotient attempting to define a velocity behaves as

$$
\frac{|\Delta x|}{\Delta t}
\sim\frac1{\sqrt{\Delta t}},
$$

and grows as $\Delta t$ tends to zero. This does not prevent the definition of the measure: it only shows that the continuous notation involving $\dot x^2$ is a formal representation of the construction by increments, not a classical energy calculated path by path.

## Oscillatory integral

In the Feynman integral, the weight is complex:

$$
e^{iS[x]/\hbar}.
$$

It does not define a positive probability. The final value depends on phase cancellations. One possible construction begins with a sequence of integrals in discrete time steps and defines the limit as an oscillatory integral. Other constructions use operators, Euclidean continuation, or spectral methods.

## Application in the manuscript

The initial problem of GDQ is not to demonstrate that Wiener and Feynman are the same integral. It is to explain how the diffusive and oscillatory sectors can belong to a common dynamics without losing, respectively, positivity and phase information.

## Common error

Formally replacing $t$ with $-i\tau$ can transform the appearance of an equation, but does not prove on its own:

- convergence of the integral;
- preservation of boundary conditions;
- positivity of the Euclidean theory;
- reconstruction of a unitary dynamics.

These properties must be verified in the problem under consideration.

[[index|← Analysis and Probability]]

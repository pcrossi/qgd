---
title: Question 06 - Meaning of tau
status: closed
source: questoes/q06/questao_06.md
updated: 2026-07-16
---

# Question 06 - Meaning of tau

## Enunciation

Q6 asks what $\tau$ is. The original ambiguity was that $\tau$ appeared as
flow time, area-like variable, diffusive time, logarithmic scale and imaginary
coordinate associated with physical time.

## Current answer

The fundamental definition is

$$
\tau\in\mathbb R_+,
\qquad
[\tau]=L^2.
$$

$\tau$ is the real geometric/diffusive flow parameter of GDQ. It is physical as
a flow/resolution parameter, but it is not the chronological time measured in
the local physical spacetime.

The physical chronological time is

$$
t.
$$

The causal complex variable is

$$
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0},
$$

so that $[\nu_0]=L^2/T$ and $[z_\tau]=L^2$.

## Heat-kernel scaling

In real dimension $d=2n$, the heat kernel scales as

$$
K(\tau)\sim(4\pi\tau)^{-d/2}.
$$

For the official GDQ bulk,

$$
n=4,
\qquad
d=8,
$$

therefore

$$
K(\tau)\sim(4\pi\tau)^{-4}.
$$

Old formulas using $\tau^{-2}$ are admissible only in a reduced real 4D sector
or as historical drafts, not as the fundamental 8D bulk kernel.

## Logarithmic scale

$d\tau/\tau$ is dimensionless and implements logarithmic scale measure on the
causal contour. It does not make $\tau$ dimensionless.

The dimensionless variable is

$$
\widehat\tau=\frac{\tau}{\ell_C^2}.
$$

The logarithmic scale is

$$
s=\log\widehat\tau
=
\log\left(\frac{\tau}{\ell_C^2}\right),
\qquad
\frac{\partial}{\partial s}
=
\tau\frac{\partial}{\partial\tau}.
$$

For a momentum/energy scale $\mu$,

$$
\widehat\tau
\sim
\frac{1}{\mu^2\ell_C^2},
\qquad
s\sim -2\log(\mu\ell_C).
$$

Thus $\tau\neq\log\mu$.

## Correct replacements for old text

- Replace $\tau+it$ by $z_\tau=\tau+i\nu_0t$.
- Replace $t=-i\tau$ by causal continuation in the $z_\tau$ plane.
- Replace dimensionless $\tau$ by $\widehat\tau=\tau/\ell_C^2$.
- Replace $\ln\mu\to\tau$ by

$$
s=\log\left(\frac{\tau}{\ell_C^2}\right),
\qquad
s\sim-2\log(\mu\ell_C).
$$

- Replace $(4\pi\tau)^{-n/2}$, when $n$ means complex dimension, by
  $(4\pi\tau)^{-n}$.

## Status

Q6 is closed as the definition and dimensional map of $\tau$. Maps to
$\epsilon$, $s$ and RG language are reductions/conventions, not new
fundamental meanings of $\tau$.


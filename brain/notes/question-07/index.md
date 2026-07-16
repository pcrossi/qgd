---
title: Question 07 - Lorentzian time
status: conditionally_closed
source: questão_7.md
updated: 2026-07-16
---

# Question 07 - Lorentzian time

Q7 asks how Lorentzian time emerges in GDQ.

The answer separates two problems: Lorentzian signature of the physical metric
and quantum Lorentzian reconstruction with Hilbert space, positive norm,
self-adjoint Hamiltonian and unitary time evolution.

## Signature layer

For $X:N\to M$,

$$
q=X^*g,
$$

with clock form

$$
u=X^*\omega,
\qquad
s=q^{-1}(u,u)>0,
$$

the physical metric is

$$
h_{\mu\nu}
=
q_{\mu\nu}
-2\frac{u_\mu u_\nu}{s}.
$$

In a $q$-orthonormal frame adapted to $u$,

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

## OS reconstruction layer

For effective Euclidean GDQ Schwinger functions satisfying OS1--OS5,

$$
(F,G)=\langle\Theta F\,G\rangle_E,
\qquad
\mathcal H=\overline{\mathcal D_+/\mathcal N}.
$$

Positive Euclidean time translations yield

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger\ge0.
$$

The Lorentzian evolution is

$$
U(t)=e^{-itH/\hbar}.
$$

## Relation to GDQ causal variables

$$
z_\tau=\tau+i\nu_0t,
\qquad
\gamma\subset\mathbb C_{z_\tau}.
$$

OS gives $(\mathcal H,H,U(t))$. Sudarshan gives the compatible causal contour
prescription in $z_\tau$.

## Status

Q7 is closed as an OS criterion for Lorentzian time emergence. It is
conditional, sector by sector, on the effective Euclidean GDQ Schwinger
functions satisfying OS1--OS5.


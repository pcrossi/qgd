---
title: "Spectral continuation from unitary group to semigroup"
type: derivation
status: theorem-under-hypotheses
---

# Spectral continuation from unitary group to semigroup

## 1. Hypotheses

Let $H$ be self-adjoint on a Hilbert space and bounded below. After a constant shift, we can assume $H\geq0$. By the spectral theorem,

$$
H=\int_0^\infty\lambda\,dE_H(\lambda),
$$

where $E_H$ is the projection-valued spectral measure.

## 2. Real evolution

For $t\in\mathbb R$,

$$
U(t)
=e^{-itH/\hbar}
=\int_0^\infty
e^{-it\lambda/\hbar}\,dE_H(\lambda).
$$

Since the integrand has unit modulus,

$$
U(t)^*U(t)=I
$$

and

$$
U(t+s)=U(t)U(s).
$$

Therefore, $U(t)$ is a strongly continuous unitary group.

## 3. Continuation in the lower half-plane

For

$$
z=t-i\tau,
\qquad
\tau>0,
$$

we define

$$
U(z)
=\int_0^\infty
e^{-iz\lambda/\hbar}\,dE_H(\lambda).
$$

Since

$$
|e^{-iz\lambda/\hbar}|
=e^{-\tau\lambda/\hbar}\leq1,
$$

the operator is bounded and analytic in the interior of the half-plane. On the negative imaginary axis,

$$
U(-i\tau)=e^{-\tau H/\hbar}.
$$

Furthermore,

$$
e^{-(\tau_1+\tau_2)H/\hbar}
=e^{-\tau_1H/\hbar}e^{-\tau_2H/\hbar},
$$

but only $\tau\geq0$ is contractive. We have a semigroup, not a unitary group.

## 4. What does not follow automatically

The functional argument alone does not guarantee:

1. a representation via Wiener measure;
2. reflection positivity;
3. continuation through cuts or singularities;
4. correspondence of boundary domains;
5. unique causal reconstruction.

These items require additional hypotheses about the operator, the potential, the fields, and the physical domain.

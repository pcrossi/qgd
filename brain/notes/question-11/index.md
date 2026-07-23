---
title: Question 11 - Hamilton-Jacobi-Bohm equation
status: conditionally_closed
source: questoes/q11/questao_11.md
updated: 2026-07-16
---

# Question 11 - Hamilton-Jacobi-Bohm equation

Q11 asks whether the action produces the Hamilton--Jacobi equation with Bohm
potential.

In the Madelung/canonical reduction fixed by Q10, variation with respect to
$\rho$ gives

$$
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
+Q
=0,
$$

with

$$
Q
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

Therefore

$$
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

## Variational source

The reduced action is

$$
I_{\rm Mad}
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac{|\nabla S_R|^2}{2m}
+V
\right)
+\frac{\hbar^2}{8m}
\frac{|\nabla\rho|^2}{\rho}
\right]d^dx.
$$

The Fisher term satisfies

$$
\frac{\delta}{\delta\rho}
\left[
\frac{\hbar^2}{8m}
\int
\frac{|\nabla\rho|^2}{\rho}
d^dx
\right]
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

## Correction

$Q$ enters the Hamilton--Jacobi equation without an extra derivative. The
gradient $\nabla Q$ appears only after taking the gradient of the
Hamilton--Jacobi equation to obtain the Euler/Madelung force equation.

## Status

Q11 is conditionally closed in the same sector as Q10: the Madelung canonical
reduction and boundary conditions are required.


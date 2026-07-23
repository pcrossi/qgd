---
title: Question 10 - Continuity equation
status: conditionally_closed
source: questoes/q10/questao_10.md
updated: 2026-07-16
---

# Question 10 - Continuity equation

Q10 asks whether the action produces the continuity equation.

The continuity equation is produced in the Madelung/canonical reduction of the
GDQ contour action, not by a naive static variation of the geometric integrand
alone.

Decompose

$$
f
=
-\frac{S_I-iS_R}{\hbar},
\qquad
\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2}.
$$

In the reduced Madelung sector,

$$
I_{\rm Mad}
=
\int d\lambda
\int_{\Sigma_\lambda}
\rho
\left[
\partial_\lambda S_R
+\frac12G^{AB}
\partial_A S_R
\partial_B S_R
+V_{\rm eff}
\right]
d\mu_g.
$$

Varying $S_R$ gives

$$
\partial_\lambda\rho+\nabla_A(\rho v^A)=0,
\qquad
v^A=G^{AB}\partial_BS_R.
$$

With variable measure,

$$
\partial_\lambda(\rho\sqrt g)
+\partial_A(\rho v^A\sqrt g)
=0.
$$

The same conservation law is the Noether current of
$S_R\mapsto S_R+\hbar\alpha$.

## Limitation

The identity $\Pi_{S_R}=\rho$ and the term
$\rho\,\partial_\lambda S_R$ are not universal off-shell identities of the
official action. They belong to the physical Madelung polarization/reduction,
later refined by the global--local/measurement/Routh argument.

## Status

Q10 is conditionally closed: once the Madelung canonical sector is selected,
variation in $S_R$ produces continuity with the stated boundary conditions.


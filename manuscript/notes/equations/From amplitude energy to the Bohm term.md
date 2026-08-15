---
title: "Note — From amplitude energy to the Bohm term"
---

# From amplitude energy to the Bohm term

Let

$$
R=\sqrt\rho.
$$

Then

$$
\ln\rho=2\ln R
$$

and

$$
\nabla\ln\rho=2\frac{\nabla R}{R}.
$$

Applying the divergence again,

$$
\Delta\ln\rho
=2\frac{\Delta R}{R}
-2\frac{|\nabla R|^2}{R^2}.
$$

Since

$$
|\nabla\ln\rho|^2
=4\frac{|\nabla R|^2}{R^2},
$$

we obtain the identity

$$
\boxed{
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=\frac12\Delta\ln\rho
+\frac14|\nabla\ln\rho|^2.
}
$$

In the non-relativistic normalization where the amplitude energy has coefficient $\hbar^2/(8m)$, its variation with respect to $\rho$ yields:

$$
\boxed{
Q_B
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
$$

The sign depends on the convention of the Laplacian. Here, $\Delta=\nabla^i\nabla_i$ is positive on convex functions in Euclidean space. GDQ determines the physical normalization only after the pullback to the laboratory chart; the prior geometric identity is independent of this step.

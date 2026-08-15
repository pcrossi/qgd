---
title: "Identity between osmotic velocity and quantum potential"
type: derivation
status: exact-identity-under-hypotheses
---

# Identity between osmotic velocity and quantum potential

## 1. Differential identity

For $\rho>0$, write $R=\sqrt\rho$. Since

$$
\ln R=\frac12\ln\rho,
$$

we have

$$
\frac{\Delta R}{R}
=\Delta\ln R+|\nabla\ln R|^2
=\frac12\Delta\ln\rho
+\frac14|\nabla\ln\rho|^2.
$$

If

$$
u=\nu\nabla\ln\rho,
$$

then

$$
\nabla\cdot u=\nu\Delta\ln\rho
$$

and

$$
|u|^2=\nu^2|\nabla\ln\rho|^2.
$$

Consequently,

$$
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
=2m\nu^2\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

For

$$
\nu=\frac{\hbar}{2m},
$$

it follows that

$$
\boxed{
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
=\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
}
$$

Thus, the quantum potential can be written as

$$
\boxed{
Q[\rho]
=-\left(
m\nu\nabla\cdot u+\frac{m}{2}|u|^2
\right).
}
$$

## 2. Sign and interpretation

$Q$ is not universally positive nor universally repulsive. Its sign depends on the local curvature of $\sqrt\rho$. What is universal is its differential form. The associated force is $-\nabla Q$ and can also change direction.

In certain localized profiles or near density zeros, this term can act as a barrier. This property must be demonstrated for the profile in question; it cannot be inferred from the name "quantum pressure" alone.

## 3. Geometric generalization

On a Riemannian manifold, $\nabla$ is replaced by the covariant derivative and $\Delta$ by the Laplace--Beltrami operator. With weighted measure or torsion, additional terms may arise. Therefore, the flat identity is the limit that the GDQ reduction needs to reproduce, not the complete expression in every background.

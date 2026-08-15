---
title: "Wall impedance by Schur"
---

# Wall impedance by Schur

Status: reduced variational derivation.

## Partition of the Hessian

If the well mode lives at the interface $Y$ and the wall degrees of freedom live in $I$, we write the quadratic form:

$$
Q[y,u]
=
\frac{1}{2}
\begin{pmatrix}
y\\u
\end{pmatrix}^{\!T}
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}
\begin{pmatrix}
y\\u
\end{pmatrix}.
$$

Variation with respect to $u$ gives:

$$
K_{II}u+K_{IY}y=0.
$$

If $K_{II}$ is invertible in the physical subspace:

$$
u_\ast=-K_{II}^{-1}K_{IY}y.
$$

Substituting back:

$$
Q_{\rm eff}[y]
=
\frac{1}{2}y^T
\left(
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}
\right)y.
$$

Therefore:

$$
\mathsf R_{\rm wall}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

## One-dimensional homogeneous wall

In the wall:

$$
-u''+(V_0-E)u=0.
$$

With a Dirichlet external face at thickness $d$:

$$
u(s)=A\sinh\left(\kappa(d-s)\right),
\qquad
\kappa=\sqrt{V_0-E}.
$$

The Dirichlet--Neumann map at the interface is:

$$
\lambda(E)
=
\kappa\coth(\kappa d).
$$

This is the impedance used in the numerical script.

## Symmetric spectral condition

For a well of length $L=1$ with equal impedance on both faces:

$$
\left(\lambda^2-k^2\right)\sin k
+
2k\lambda\cos k
=0,
\qquad
k=\sqrt E.
$$

The roots give the Robin/DtN spectrum.

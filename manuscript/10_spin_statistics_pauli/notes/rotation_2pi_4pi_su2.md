---
title: "Rotation of 2pi and 4pi in SU(2)"
---

# Rotation of $2\pi$ and $4\pi$ in $SU(2)$

## Statement

In the spatial spinor representation:

$$
U(\theta)
=
\exp\left(
-i\frac{\theta}{2}\mathbf n\cdot\boldsymbol\sigma
\right),
$$

we have:

$$
U(2\pi)=-I,
\qquad
U(4\pi)=I.
$$

## Proof

For a unit vector $\mathbf n$:

$$
(\mathbf n\cdot\boldsymbol\sigma)^2=I.
$$

Thus:

$$
\exp(-i a\,\mathbf n\cdot\boldsymbol\sigma)
=
\cos a\,I
-i\sin a\,\mathbf n\cdot\boldsymbol\sigma.
$$

Taking $a=\theta/2$:

$$
U(\theta)
=
\cos\frac\theta2\,I
-i\sin\frac\theta2\,\mathbf n\cdot\boldsymbol\sigma.
$$

For $\theta=2\pi$:

$$
U(2\pi)
=
\cos\pi\,I
-i\sin\pi\,\mathbf n\cdot\boldsymbol\sigma
=
-I.
$$

For $\theta=4\pi$:

$$
U(4\pi)
=
\cos2\pi\,I
-i\sin2\pi\,\mathbf n\cdot\boldsymbol\sigma
=
I.
$$

## Scope

This is the mathematical realization of the spinor half-turn. GDQ interprets this structure through Hopf, circulation, and torsion, but the sign comes from the double covering $SU(2)\to SO(3)$.

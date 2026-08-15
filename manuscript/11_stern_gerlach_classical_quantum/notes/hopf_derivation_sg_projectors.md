---
title: "Hopf derivation of Stern-Gerlach projectors"
---

# Hopf derivation of Stern-Gerlach projectors

## Statement

The normal link $S^3\subset\mathbb C^2$ of the stoma induces rank-one projectors in $\mathbb C^2$:

$$
P(u)=uu^\dagger.
$$

They can be written as:

$$
P(u)=\frac12(I+\mathbf n\cdot\sigma).
$$

## Proof

Let:

$$
u=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\qquad
u^\dagger u=1.
$$

Then:

$$
P=uu^\dagger
$$

satisfies:

$$
P^2=P,
\qquad
P^\dagger=P,
\qquad
\operatorname{Tr}P=1.
$$

Every $2\times2$ Hermitian matrix can be decomposed in the basis:

$$
I,\sigma_1,\sigma_2,\sigma_3.
$$

Since $\operatorname{Tr}P=1$, there exists $\mathbf n$ such that:

$$
P=\frac12(I+\mathbf n\cdot\sigma).
$$

From the condition $P^2=P$ it follows:

$$
|\mathbf n|^2=1.
$$

Thus $\mathbf n\in S^2$.

The complementary projector is:

$$
I-P=\frac12(I-\mathbf n\cdot\sigma).
$$

Hence, for the axis of the apparatus:

$$
P_{\mathbf n}^{\pm}
=
\frac12(I\pm\mathbf n\cdot\sigma).
$$

## Scope

This is a local derivation of the two-channel structure. The metrological selection of the axis comes from the magnetic field of the apparatus.

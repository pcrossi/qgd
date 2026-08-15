---
title: "Local APS index, Hopf and Bismut"
---

# Local APS index, Hopf and Bismut

This note records the local part of the generational construction. It does not use the Standard Model as input. The goal is to show that a co-oriented primitive stoma carries a unit of chiral index.

## 1. The local link of the stoma

An isolated stoma is modeled locally by a complex normal neighborhood. After excision of the core, the normal boundary is:

$$
\partial B^4\simeq S^3.
$$

Since:

$$
H^2(S^3,\mathbb Z)=0,
$$

the first Chern of an abelian line does not literally live in $S^3$. It is read via the Hopf fibration:

$$
S^1\longrightarrow S^3\longrightarrow S^2.
$$

On the base $S^2$, a primitive flux is described by:

$$
A_N=\frac m2(1-\cos\theta)d\varphi,
$$

$$
A_S=-\frac m2(1+\cos\theta)d\varphi.
$$

At the equator:

$$
A_N-A_S=m\,d\varphi,
$$

hence the transition function is:

$$
g_{NS}=e^{im\varphi}.
$$

The curvature is:

$$
F=dA_N=\frac m2\sin\theta\,d\theta\wedge d\varphi.
$$

Therefore:

$$
c_1(L_m)
=
\frac{1}{2\pi}\int_{S^2}F
=
m.
$$

The primitive stoma corresponds to:

$$
|m|=1.
$$

## 2. Tangential operator on the $S^3$ link

On the round link of radius $a$, the untwisted tangential Dirac operator has a symmetric spectrum:

$$
\lambda_n^\pm
=
\pm\frac{n+\frac32}{a},
\qquad
d_n=(n+1)(n+2).
$$

The Hopf connection can be written, in a basis of invariant forms $\sigma_i$, as:

$$
A_m=-\frac m2\sigma_3.
$$

The topological contribution that matters for the APS condition is the transgression:

$$
\frac{1}{4\pi^2}\int_{S^3}A_m\wedge dA_m
=
-m^2.
$$

Thus, the reduced eta has fractional part:

$$
\bar\eta(A_m)
\equiv
-\frac{m^2}{2}
\pmod{\mathbb Z}.
$$

For $|m|=1$:

$$
-\bar\eta(A_m)\equiv\frac12\pmod{\mathbb Z}$.
$$

This half-integer term is the spectral signature of the primitive Hopf flux on the boundary.

## 3. Role of Bismut torsion

GDQ does not use the bare Dirac operator as a fundamental action. The spinorial operator appears as a reconstructed or effective operator of the Hessian in the local sector. The correct connection is the Hermitian connection with Bismut torsion.

On the boundary $S^3$, the parallelizing torsion shifts the tangential operator. In the normalization used in this construction, the physical torsional coupling is:

$$
\beta=-\frac32
$$

for the chosen orientation.

A reduced spectral model of the tangential sector is:

$$
D_{m,B}^{(j)}
=
\frac1a
\left(
2\,\boldsymbol\sigma\cdot\mathbf L^{(j)}
-m\sigma_3
\right).
$$

The torsional kernel associated with the primitive flux has dimension:

$$
h_m=|m|+1.
$$

Hence:

$$
h_1=2.
$$

These two modes are the dual internal degree of freedom that is later separated by boundary/apparatus or by the choice of effective chiral sector.

## 4. APS filling and index unit

Consider a filling $X^4=B^4$ with boundary $S^3$ and a smooth extension:

$$
A=f(r)A_m.
$$

By the Chern term:

$$
\int_{X^4}{\rm ch}_2(L_m)
=
\frac{1}{8\pi^2}\int_{X^4}F\wedge F
=
-\frac{m^2}{2}.
$$

Without torsion, the fractional part of the volume term and the boundary eta cancel each other out. Local chirality does not automatically appear.

With Bismut torsion adiabatically turned on, the tangential operator undergoes spectral flow. For the primitive sector $m=1$, there is a simple eigenvalue crossing on the physical Bismut path. With the APS convention:

$$
\Delta{\rm ind}_{\rm APS}
=
-{\rm SF}.
$$

Since the physical spectral flow has:

$$
{\rm SF}=-1,
$$

it follows:

$$
{\rm ind}_{\rm APS}D_{1,B}^+=1.
$$

This is the local generation unit:

$$
\boxed{
{\rm ind}_{\rm stoma}=1
}.
$$

## 5. What this unit does not mean

It is not:

- a hypercharge;
- a fractional Chern;
- a generation inserted by a table;
- an already massive particle.

It is a local unit of chiral index. Hypercharges belong to the line $L_Y$ and to the global quotient $\mathbb Z_6$. Masses and mixings belong to subsequent chapters, where the physical Hessian of the material background is diagonalized.

## 6. Computational verification

The script:

$$
{\tt scripts/aps_index_hopf_bismut.py}
$$

verifies the discrete invariants used in this note: flux $c_1=m$, fractional part of $\bar\eta$, dimension of the torsional kernel, and primitive APS unit.

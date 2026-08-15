---
title: "Hermitian structure, Kähler and Bismut connection"
type: derivation
status: geometric-definition
---

# Hermitian structure, Kähler and Bismut connection

## 1. Hermitian structure

An almost-complex structure is an endomorphism

$$
J:TM\to TM
$$

such that

$$
J^2=-I.
$$

When its Nijenhuis tensor vanishes, $J$ is integrable. A metric $g$ is Hermitian when

$$
g(JX,JY)=g(X,Y).
$$

The associated fundamental form is

$$
\omega_H(X,Y)=g(JX,Y).
$$

It is antisymmetric because compatibility implies

$$
g(JX,Y)=-g(X,JY).
$$

## 2. Kähler case

The Hermitian structure is Kähler when

$$
d\omega_H=0.
$$

In this case, the Levi--Civita connection preserves $J$ and has no torsion.

## 3. Bismut connection

On an integrable Hermitian manifold, there exists a unique connection that preserves $g$ and $J$ and whose torsion is totally antisymmetric. This is the Bismut connection. Schematically,

$$
\nabla^B=\nabla^{\rm LC}+\frac12g^{-1}H,
$$

with the sign depending on the convention, and

$$
H=d_J^c\omega_H.
$$

If $d\omega_H=0$, then $H=0$ in the usual convention. Thus,

$$
H\neq0
\quad\Longrightarrow\quad
\text{the sector is not strictly Kähler}.
$$

## 4. Pluriclosed sector

An additionally considered condition is often

$$
dH=0,
$$

equivalent, under usual conventions, to a pluriclosed or strong KT condition. It does not follow from the Hermitian definition alone and must be imposed by the sector or demonstrated by the dynamics.

## 5. Status in GDQ

In the current official action, the varied fields are $g$, $f$, and $\bar f$; $J$ is the structure of the theory and $H$ is derived from the Hermitian structure according to the adopted convention. If a reduction treats $H$ as an auxiliary variable, this must be identified as an effective formulation, not as a silent alteration of the fundamental action.

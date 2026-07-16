---
title: Causal complex variable
status: defined
concepts:
  - z_tau
  - tau
  - physical time
  - nu_0
  - causal variable
---

# Causal complex variable

## Definition

GDQ separates:

- `t`: physical time reconstructed in the Lorentzian sector;
- `tau`: geometric flow parameter with dimension of area;
- `z_tau`: causal complex variable.

Since:

$$
[\tau]=L^2,
\qquad
[t]=T,
$$

the sum `tau+i t` is dimensionally invalid. Introduce:

$$
[\nu_0]=L^2T^{-1}.
$$

The causal variable is:

$$
\boxed{
z_\tau=\tau+i\nu_0t.
}
$$

## Conditional uniqueness

Inside the minimal affine class:

$$
z=a\tau+ibt,
$$

with `a,b` real and `a != 0`, rescaling gives:

$$
z/a=\tau+i(b/a)t.
$$

Setting:

$$
\nu_0=b/a
$$

recovers `z_tau`. Under time reversal:

$$
t\mapsto -t
\quad\Longrightarrow\quad
z_\tau\mapsto\bar z_\tau.
$$

## Status

Defined, with conditional uniqueness in the affine minimal class. Nonlinear
causal variables are future extensions, not current requirements.

## Source

`manuscrito/03_complex_causality/03.2 - Três variáveis que não devem ser confundidas.md`


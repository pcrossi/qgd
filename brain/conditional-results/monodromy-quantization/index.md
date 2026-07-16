---
title: Monodromy quantization
status: conditionally_demonstrated
concepts:
  - monodromy
  - circulation
  - quantization
  - holonomy
  - integral class
---

# Monodromy quantization

## Statement

Circulation quantization follows from holonomy and integral class conditions,
not from residue calculus alone.

Locally:

$$
p=dS_R.
$$

For:

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar},
$$

transport around a cycle `C` gives:

$$
\exp\left(
\frac{i}{\hbar}\oint_Cp
\right).
$$

Trivial monodromy requires:

$$
\exp\left(
\frac{i}{\hbar}\oint_Cp
\right)=1.
$$

Therefore:

$$
\oint_Cp=2\pi n\hbar=nh,
\qquad
n\in\mathbb Z.
$$

For spinorial holonomy:

$$
\exp\left(
\frac{i}{\hbar}\oint_Cp
\right)=-1,
$$

so:

$$
\oint_Cp
=2\pi\hbar\left(n+\frac12\right).
$$

## Integral class form

For a line bundle connection:

$$
\left[
\frac{F_A}{2\pi}
\right]
\in H^2(M,\mathbb Z).
$$

## Status

Conditionally demonstrated after the relevant holonomy and normalization are
specified. Selection of the spin antiperiodic sector belongs to the spin
chapter, not to Chapter 3.

## Source

`manuscrito/03_complex_causality/03.6 - Circulação, monodromia e quantização.md`


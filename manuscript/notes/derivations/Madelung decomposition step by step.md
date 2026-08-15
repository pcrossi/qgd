---
title: "Madelung decomposition step by step"
type: derivation
status: exact-identity
---

# Madelung decomposition step by step

## 1. Hypotheses and domain

Consider the non-relativistic Schrödinger equation

$$
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\Delta\psi+V\psi,
$$

with $m>0$, real potential $V$, and sufficiently regular solution in a region where $\psi\neq0$. We write

$$
\psi=R e^{iS/\hbar},
\qquad
R>0,
\qquad
\rho=R^2.
$$

The decomposition is local. Around zeros of $\psi$, the phase can be multivalued and must be described by charts, circulation, or holonomy.

## 2. Temporal derivative

By the product rule,

$$
\partial_t\psi
=e^{iS/\hbar}
\left(
\partial_tR+\frac{i}{\hbar}R\partial_tS
\right).
$$

Multiplying by $i\hbar$,

$$
i\hbar\partial_t\psi
=e^{iS/\hbar}
\left(
i\hbar\partial_tR-R\partial_tS
\right).
$$

## 3. Gradient and Laplacian

The gradient is

$$
\nabla\psi
=e^{iS/\hbar}
\left(
\nabla R+\frac{i}{\hbar}R\nabla S
\right).
$$

Applying the divergence again,

$$
\Delta\psi
=e^{iS/\hbar}
\left[
\Delta R
+\frac{2i}{\hbar}\nabla R\cdot\nabla S
+\frac{i}{\hbar}R\Delta S
-\frac{1}{\hbar^2}R|\nabla S|^2
\right].
$$

## 4. Substitution in the equation

Cancelling the non-zero factor $e^{iS/\hbar}$, we obtain

$$
i\hbar\partial_tR-R\partial_tS
=
-\frac{\hbar^2}{2m}\Delta R
-\frac{i\hbar}{m}\nabla R\cdot\nabla S
-\frac{i\hbar}{2m}R\Delta S
+\frac{R}{2m}|\nabla S|^2
+VR.
$$

Since $R$, $S$, and $V$ are real, the real and imaginary parts must coincide separately.

## 5. Imaginary part: continuity

The imaginary part yields

$$
\hbar\partial_tR
=
-\frac{\hbar}{m}\nabla R\cdot\nabla S
-\frac{\hbar}{2m}R\Delta S.
$$

Multiplying by $2R/\hbar$,

$$
2R\partial_tR
=
-\frac{2R}{m}\nabla R\cdot\nabla S
-\frac{R^2}{m}\Delta S.
$$

Using

$$
\partial_t\rho=2R\partial_tR
$$

and

$$
\nabla\cdot(\rho\nabla S)
=2R\nabla R\cdot\nabla S+R^2\Delta S,
$$

it follows that

$$
\partial_t\rho
+\nabla\cdot\left(\rho\frac{\nabla S}{m}\right)=0.
$$

Defining

$$
v=\frac{\nabla S}{m},
$$

we obtain the continuity equation

$$
\boxed{
\partial_t\rho+\nabla\cdot(\rho v)=0.
}
$$

## 6. Real part: quantum Hamilton--Jacobi

The real part yields

$$
-R\partial_tS
=
-\frac{\hbar^2}{2m}\Delta R
+\frac{R}{2m}|\nabla S|^2
+VR.
$$

Dividing by $R>0$ and bringing all terms to the same side,

$$
\partial_tS
+\frac{|\nabla S|^2}{2m}
+V
-\frac{\hbar^2}{2m}\frac{\Delta R}{R}
=0.
$$

Since $R=\sqrt\rho$, we define

$$
Q[\rho]
=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho},
$$

and therefore

$$
\boxed{
\partial_tS+\frac{|\nabla S|^2}{2m}+V+Q[\rho]=0.
}
$$

## 7. The role of the conjugate

The equation for $\bar\psi$ is the conjugate of the equation for $\psi$. Subtracting the two equations eliminates the real terms and produces current conservation; adding them, after polar decomposition, produces the dynamic phase equation. Thus, the conjugate is not an algebraic decoration: it allows the construction of the positive bilinear form $\rho=\bar\psi\psi$ and the conserved current.

In the isolated Hamilton--Jacobi formulation, $S$ does not contain by itself the normalization information. Therefore, the hydrodynamic representation has two equations: one for the phase and another for the density.

## 8. Limitations

This note demonstrates a local equivalence between the Schrödinger equation and the quantum continuity--Hamilton--Jacobi pair. It does not demonstrate that $\rho$ is ontologically a classical fluid, nor does it derive the Schrödinger equation from the official action of GDQ.

[[index|← Fundamental Derivations]]

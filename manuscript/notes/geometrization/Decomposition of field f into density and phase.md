---
title: "Decomposition of field f into density and phase"
type: derivation
status: exact-identity
---

# Decomposition of field $f$ into density and phase

If

$$
f=-\frac{S_I}{\hbar}+i\frac{S_R}{\hbar},
\qquad
\bar f=-\frac{S_I}{\hbar}-i\frac{S_R}{\hbar},
$$

then

$$
S_I=-\frac{\hbar}{2}(f+\bar f),
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

By the constitutional definition,

$$
\rho=e^{-(f+\bar f)/2}=e^{S_I/\hbar},
$$

and

$$
\Psi
=\sqrt\rho\,e^{iS_R/\hbar}
=e^{S_I/(2\hbar)}e^{iS_R/\hbar}.
$$

## Gradient term

Expanding $\partial_\mu f\,\partial_{\bar\nu}\bar f$ and taking the Hermitian real part,

$$
\operatorname{Re}\left(
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
=
\frac1{\hbar^2}g^{\mu\bar\nu}
\left(
\partial_\mu S_I\partial_{\bar\nu}S_I
+\partial_\mu S_R\partial_{\bar\nu}S_R
\right).
$$

The cross terms are imaginary before symmetrization. The identity shows how density and phase contribute to the same term without identifying them.

## Local $S_I$ is not the global functional $\mathcal W$

The field $S_I$ is local:

$$
S_I=S_I(x,\tau).
$$

Perelman's functional, when used as a geometric reference, is global:

$$
\mathcal W=\mathcal W[g,F,\tau].
$$

Therefore, the expression

$$
S_I=\hbar\mathcal W
$$

should not be used as a pointwise identity. The correct local relation is

$$
\boxed{
S_I=\hbar\ln\rho=-\hbar\,\operatorname{Re}f.
}
$$

If it is necessary to connect a global quantity to a local quantity, one must introduce an integrand density or a functional derivative, for example:

$$
\mathcal W=\int_M\mathfrak w\,dV_g
$$

or

$$
\Pi_I(x)=\frac{\delta\mathcal W}{\delta S_I(x)}.
$$

Even in these cases, $\mathfrak w$ or $\Pi_I$ are not the entire global functional $\mathcal W$.

---
title: "Monotonicity does not imply stability without Hessian"
---

# Monotonicity does not imply stability without Hessian

This note establishes a necessary distinction in GDQ: monotonic Perelman--Bismut functionals control the geometric flow, but are not sufficient to declare a particle stable. Stability of a material configuration requires the spectrum of the second variation in the physical sector.

## 1. Auxiliary functionals

In the torsional/Bismut sector, the geometric energy functional at fixed scale is

$$
\mathcal F_T(g,H,\phi)
=
\int_M
\left(
R
-\frac1{12}|H|^2
+|\nabla\phi|^2
\right)
e^{-\phi}dV_g.
$$

The variable-scale functional is

$$
\mathcal W_T(g,H,\phi,\sigma)
=
\int_M
\left[
\sigma
\left(
R
-\frac1{12}|H|^2
+|\nabla\phi|^2
\right)
+\phi-d
\right]
(4\pi\sigma)^{-d/2}e^{-\phi}dV_g.
$$

These functionals are auxiliaries for geometric stability. They do not replace the official action of GDQ.

## 2. Monotonicity hypotheses

The monotonicity identity requires:

1. positive Riemannian/Hermitian bulk;
2. sufficient regularity of the solution;
3. real and antisymmetric $H$;
4. torsional Bianchi condition, for example $dH=0$ in the simple sector;
5. normalized measure;
6. zero or compensated boundary terms;
7. adequate gauge;
8. preserved sector topology.

The measure used is

$$
d\mu
=
(4\pi\sigma)^{-d/2}e^{-\phi}dV_g,
$$

or, in the complex action,

$$
\rho=e^{-(f+\bar f)/2}.
$$

## 3. Derivative as a sum of squares

In the convention where the functional increases with $\tau$:

$$
\frac{d\mathcal F_T}{d\tau}
=
2\int_M
\left|
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right|^2
e^{-\phi}dV_g
+
\frac16
\int_M
\left|
d_\phi^\dagger H
\right|^2
e^{-\phi}dV_g
\ge0.
$$

For $\mathcal W_T$:

$$
\frac{d\mathcal W_T}{d\tau}
=
2\sigma
\int_M
\left|
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
-\frac1{2\sigma}g_{ij}
\right|^2
d\mu
+
\frac{\sigma}{6}
\int_M
\left|
d_\phi^\dagger H
\right|^2
d\mu
\ge0.
$$

If the flow orientation is reversed, the same statements appear with the opposite sign. The invariant content is: the derivative is a sum of squares and vanishes at solitons.

## 4. What monotonicity proves

It proves that the functional acts as a Lyapunov function for the flow in the sector where the hypotheses hold.

It also characterizes critical points. For $\mathcal W_T$, equality occurs when

$$
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij},
$$

and

$$
d_\phi^\dagger H=0.
$$

This identifies Ricci--Bismut/Perelman soliton candidates.

## 5. What monotonicity does not prove

Monotonicity alone does not determine whether the critical point is a minimum, maximum, or saddle in the physical perturbation space.

For this, one must calculate the second variation:

$$
\delta^2\mathcal I_T[U,U]
=
\langle U,\mathcal J_{\mathfrak S}U\rangle_{\rho_\ast},
$$

where

$$
U=(h,\beta,\eta)
$$

represents metric, torsion, and dilaton/real phase perturbations, and

$$
\mathcal J_{\mathfrak S}
=
D^2\mathcal I_T|_{\mathfrak S}.
$$

Schematically:

$$
\mathcal J_{\mathfrak S}
=
\begin{pmatrix}
\Delta_L^\phi+\mathcal R_{HH}+\mathcal R_{\phi\phi}
&
\mathcal C_{gH}
&
\mathcal C_{g\phi}
\\
\mathcal C_{Hg}
&
\Delta_{H,\phi}+\mathcal M_H
&
\mathcal C_{H\phi}
\\
\mathcal C_{\phi g}
&
\mathcal C_{\phi H}
&
-\Delta_\phi+\mathcal V_\phi
\end{pmatrix}.
$$

Here $\Delta_L^\phi$ is the weighted Lichnerowicz, $\Delta_{H,\phi}$ is the weighted Hodge, and the blocks $\mathcal C$ record lower-order couplings.

## 6. Physical space

The spectrum must be evaluated after removing modes that do not represent physical instability:

$$
\mathcal H_{\rm phys}
=
\left(
\ker_{\rm diff}
\oplus
\ker_{\rm gauge}
\oplus
\ker_{\rm trans}
\oplus
\ker_{\rm rot}
\oplus
\ker_{\rm scale}
\oplus
\ker_{\rm moduli}
\right)^\perp.
$$

In the sign where $\mathcal I_T$ is the minimized free energy, the linear stability condition is

$$
\operatorname{spec}
\left(
\mathcal J_{\mathfrak S}\big|_{\mathcal H_{\rm phys}}
\right)
\subseteq[0,\infty).
$$

A physical negative eigenvalue means instability. An unexplained zero eigenvalue means a marginal mode or uncontrolled modulus.

## 7. Gaussian case

For the neutral Gaussian soliton:

$$
g=\delta,
\qquad
H=0,
\qquad
\phi=\frac{|x|^2}{4\sigma},
$$

the reduced scalar operator is of Ornstein--Uhlenbeck type:

$$
\mathcal L_{\rm OU}
=
-\Delta
+\frac{x}{2\sigma}\cdot\nabla.
$$

Its spectrum in $L^2(\rho_NdV)$ is

$$
\lambda_k=\frac{k}{2\sigma}.
$$

After removing the constant mode and the symmetry/moduli modes of the sector, the reduced gap is positive.

## 8. Final criterion

The correct implication is:

$$
\text{monotonicity}
+
\text{real critical point}
+
\text{compatible boundaries}
+
\text{preserved topology}
+
\text{physical Hessian without negative eigenvalues}
\Rightarrow
\text{local/orbital stability}.
$$

Without the last term, there is no proof of particle stability.

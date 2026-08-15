---
title: "First variation of the GDQ action: complete structure"
---

# First variation of the GDQ action: complete structure

This note gathers the universal algebra used in Chapters 4 and 5. It does not replace the pedagogical derivations of the main text.

Define

$$
C=\frac{\hbar}{\Lambda_C^2},
\qquad
\mathcal L_0
=\tau\left(
\mathcal R+g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n.
$$

Then

$$
S=\operatorname{Re}
\int_\gamma\int_M
C\mathcal U\mathcal L_0\,dV_g\frac{d\tau}{\tau}.
$$

## Product rule

$$
\delta S
=\operatorname{Re}\int_\gamma\int_M
C\mathcal U
\left[
\delta\mathcal L_0
+\mathcal L_0\frac{\delta\mathcal U}{\mathcal U}
+\mathcal L_0\frac{\delta dV_g}{dV_g}
\right]
dV_g\frac{d\tau}{\tau}.
$$

For variations of $f$ and $\bar f$ with fixed $z_\tau$,

$$
\frac{\delta\mathcal U}{\mathcal U}
=-\frac12(\delta f+\delta\bar f).
$$

If $g^{AB}$ is the metric variable,

$$
\frac{\delta dV_g}{dV_g}
=-\frac12g_{AB}\delta g^{AB}.
$$

If, instead, we use $g_{AB}$, the sign is positive:

$$
\frac{\delta dV_g}{dV_g}
=\frac12g^{AB}\delta g_{AB}.
$$

The two conventions must not be mixed.

## Complex gradient

$$
\begin{aligned}
\delta\left(
g^{\mu\bar\nu}\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
={}&\delta g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
\\
&+g^{\mu\bar\nu}
\partial_\mu\delta f\partial_{\bar\nu}\bar f
\\
&+g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\delta\bar f.
\end{aligned}
$$

The last two terms are integrated by parts with the weight $\mathcal U$. They produce the Euler--Lagrange operators and the boundary concomitant.

## Weighted curvature

In the $\delta g^{AB}$ convention,

$$
\begin{aligned}
\delta\int_M\mathcal U\mathcal R\,dV_g
={}&\int_M
\left[
\mathcal U\left(
\mathcal R_{AB}-\frac12\mathcal Rg_{AB}
\right)
\\
&+g_{AB}\Delta_g\mathcal U
-\nabla_A\nabla_B\mathcal U
\right]
\delta g^{AB}\,dV_g
+B_{\mathcal R}.
\end{aligned}
$$

## Normalization

The constraint is

$$
N[\mathcal U,g]
=\int_M\mathcal U\,dV_g=1.
$$

We vary

$$
S_{\rm restricted}
=S-C\int_\gamma\lambda(\tau)(N-1)\frac{d\tau}{\tau}.
$$

For $q=\ln\rho$,

$$
\delta_qN
=\int_M\mathcal U\,\delta q\,dV_g.
$$

For the inverse metric,

$$
\delta_gN
=-\frac12\int_M
\mathcal U g_{AB}\delta g^{AB}\,dV_g.
$$

Thus, the same $\lambda(\tau)$ appears in the normalized density and metric equations.

## Final structure

After integrations by parts,

$$
\delta S_{\rm restricted}
=\int_\gamma\int_M
\left(
\mathcal E_g^{AB}\delta g_{AB}
+\mathcal E_f\delta f
+\mathcal E_{\bar f}\delta\bar f
\right)
+\int_\gamma\int_{\partial M}\Theta.
$$

The bulk coefficients provide the equations. $\Theta$ provides the interface momenta. The explicit formulas in $(\rho,S_R)$ are in [[../../05_equations_conservation/index|Chapter 5]].

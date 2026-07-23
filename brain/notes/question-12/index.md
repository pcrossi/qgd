---
title: Question 12 - Metric variation and flow
status: closed
source: questoes/q12/questao_12.md
updated: 2026-07-16
---

# Question 12 - Metric variation and flow

Q12 asks whether the official action produces the GDQ metric equation/metric
flow.

The metric equation is obtained by varying the official action with respect to
$g^{\mu\bar\nu}$ while holding $f,\bar f$ fixed in that variation.

## Variational equation

Define

$$
X=g^{\alpha\bar\beta}
\partial_\alpha f
\partial_{\bar\beta}\bar f,
\qquad
\Phi=\frac{f+\bar f}{2}.
$$

With $\delta_g\mathcal U=0$, the metric Euler tensor is

$$
\mathcal E_{\mu\bar\nu}
=
\tau
\left[
\mathcal U\,G_{\mu\bar\nu}
+
\left(
g_{\mu\bar\nu}\Delta
-\nabla_\mu\nabla_{\bar\nu}
\right)\mathcal U
\right]
+
\tau\mathcal U
\left[
\partial_\mu f\partial_{\bar\nu}\bar f
-\frac12g_{\mu\bar\nu}X
\right]
-\frac12
\mathcal U
g_{\mu\bar\nu}
(\Phi-n)
+\mathcal E_{\mu\bar\nu}^{H}.
$$

The equation is

$$
\mathcal E_{\mu\bar\nu}=0.
$$

## Type of equations

- The stationary bulk equation is elliptic after diffeomorphism gauge fixing.
- The associated $\tau$-flow is Ricci--Perelman/Ricci--Bismut type and
  parabolic after DeTurck gauge fixing.
- Physical causal evolution is not this flow; it is hyperbolic only in the
  effective Lorentzian layer $(N,h)$.

## Torsion

Torsion enters through the Bismut connection and $H^2$:

$$
\nabla^B=\nabla^{LC}+\frac12H,
\qquad
\mathcal R\to\mathcal R_B.
$$

Structurally,

$$
\mathcal R_B
=
\mathcal R_{LC}
-\frac{1}{12}H_{ABC}H^{ABC}
+\text{divergence},
$$

with coefficient depending on the chosen normalization for $H$.

## Conservation

Diffeomorphism invariance gives the Noether/Bianchi identity. On shell,

$$
\nabla^AT_{AB}^{\rm eff}=0
$$

or, in the torsional sector,

$$
\nabla^{B\,A}T_{AB}^{\rm eff}=0.
$$

## Status

Q12 is closed as a variational derivation of the metric equation. The flow in
$\tau$ is geometric/diffusive and not physical chronological evolution.


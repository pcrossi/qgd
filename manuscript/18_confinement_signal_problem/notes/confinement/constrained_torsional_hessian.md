---
title: "Constrained torsional Hessian of the throat"
---

# Constrained torsional Hessian of the throat

This note shows how the conservation of torsional charge produces stiffness. The central point is that pulling the stoma does not allow volume and torsion module to vary independently.

## 1. Conservation of Charge

Let $\Sigma_s$ be a three-dimensional cycle enclosing the throat. Suppose:

$$
dH_s=0,
\qquad
Q_T:=\int_{\Sigma_s}H_s={\rm constant}.
$$

In the fixed class:

$$
H_s
=
Q_T\eta_s+d\beta_s,
\qquad
\int_{\Sigma_s}\eta_s=1.
$$

The representative of least norm is the harmonic:

$$
H_s=Q_T\eta_s.
$$

Then:

$$
\mathcal E_T(s)
=
\frac{\kappa_T}{2}Q_T^2
\int_{\Sigma_s}
|\eta_s|_{g_s}^2\,d\mu_{g_s}.
$$

## 2. Homogeneous Case

If:

$$
\eta_s
=
\frac{{\rm vol}_{\Sigma_s}}{V(s)},
\qquad
V(s)={\rm Vol}(\Sigma_s),
$$

then:

$$
H_s
=
\frac{Q_T}{V(s)}
{\rm vol}_{\Sigma_s},
$$

and:

$$
\mathcal E_T(s)
=
\frac{\kappa_TQ_T^2}{2V(s)}.
$$

Thus, a deformation that alters $V$ necessarily alters $|H|$.

## 3. Homogeneous Radial Functional

In the homogeneous $S^3$ sector of the throat:

$$
\mathcal W_Q(R)
=
\tau
\left(
\frac6{R^2}
-
\frac{Q_T^2}{2\pi^2R^6}
\right)
+3\log R.
$$

The first variation is:

$$
\mathcal W_Q'(R)
=
\frac{3}{\pi^2R^7}
\left[
Q_T^2\tau
+\pi^2R^6
-4\pi^2\tau R^4
\right].
$$

Therefore, the saddle satisfies:

$$
R^6-4\tau R^4+\frac{\tau Q_T^2}{\pi^2}=0.
$$

## 4. Second Variation

Before imposing the saddle:

$$
\mathcal W_Q''(R)
=
-\frac{3}{\pi^2R^8}
\left[
7Q_T^2\tau
+\pi^2R^6
-12\pi^2\tau R^4
\right].
$$

Eliminating $Q_T$ by the stationary equation:

$$
K_R
:=
\left.
\mathcal W_Q''(R)
\right|_{\rm saddle}
=
\frac{6(3R^2-8\tau)}{R^4}.
$$

Therefore:

$$
K_R>0
\quad
\Longleftrightarrow
\quad
R^2>\frac83\tau.
$$

## 5. Reduced Evaluation

With:

$$
R=1.03707435228632,
\qquad
\tau=0.274900522513626,
\qquad
Q_T=1,
$$

we obtain:

$$
\frac{R^2}{\tau}
=
3.91240875912406
>
\frac83,
$$

and:

$$
K_R
=
5.32888850629080>0.
$$

Thus, torsional conservation stabilizes the homogeneous radial mode.

## 6. Static Response

For a classical source $J_R$:

$$
\delta^2\mathcal W_J
=
\frac12K_R(\delta R)^2
-J_R\delta R.
$$

Therefore:

$$
\delta R
=
K_R^{-1}J_R,
\qquad
K_R^{-1}
=
0.187656393790\ldots.
$$

Since $V_{S^3}\propto R^3$ and $Q_T$ is conserved:

$$
\frac{\delta |H|}{|H|}
=
-3\frac{\delta R}{R}.
$$

## 7. Limit

This is a sectorial theorem for the constrained homogeneous mode. Total coercivity still requires controlling anisotropic modes, curvature/dilaton blocks, and causal mobility.

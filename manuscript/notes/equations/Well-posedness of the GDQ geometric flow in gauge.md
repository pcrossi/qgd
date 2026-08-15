---
title: "Well-posedness of the GDQ geometric flow in gauge"
---

# Well-posedness of the GDQ geometric flow in gauge

This note records the technical result used in Chapter 5: the geometric flow of GDQ in $\tau$ is locally well-posed after fixing the gauge degeneracies. The statement does not identify $\tau$ with physical time $t$ and does not alter the official action.

## 1. The problem

The problem is to study the auxiliary geometric relaxation evolution:

$$
\partial_\tau U=\mathcal P(U),
$$

with

$$
U=(g,H,\phi,\chi),
\qquad
f=\phi+i\chi.
$$

Here, $g$ is the Hermitian/Riemannian bulk metric, $H$ is the Bismut torsion when the Hermitian class considered includes it, $\phi=\operatorname{Re}f$, and $\chi=\operatorname{Im}f$.

The density remains:

$$
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
$$

The stationary system associated with the official action is elliptic after gauge fixing. The flow in $\tau$ is parabolic after gauge fixing. The physical evolution reconstructed in $t$ is another problem.

## 2. Schematic form of the flow

In the torsional sector compatible with the Bismut connection, the geometric part can be written, in real notation, as:

$$
\partial_\tau g_{ij}
=
-2
\left(
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right)
+\text{boundary terms or normalization}.
$$

For torsion, the principal part is Laplace--Hodge:

$$
\partial_\tau H
=
\Delta_{d,g}H
+\mathcal L_{\nabla\phi}H
+\text{lower-order terms}.
$$

For scalars:

$$
\partial_\tau\phi
=
\Delta_g\phi+\text{lower-order terms},
\qquad
\partial_\tau\chi
=
\Delta_g\chi+\text{lower-order terms},
$$

after choosing the parabolic sign convention.

The quadratic terms $H_{ik\ell}H_j{}^{k\ell}$, $|H|^2$, $|\nabla\phi|^2$, and the transport terms are of lower order for the principal classification.

## 3. Why gauge fixing is necessary

Ricci's equation is not strongly parabolic before gauge fixing because the action is invariant under diffeomorphisms. This degeneracy is geometric, not a physical pathology.

We choose a fixed reference metric $\bar g$ and define DeTurck's vector:

$$
W^k
=
g^{pq}
\left(
\Gamma^k_{pq}(g)-\Gamma^k_{pq}(\bar g)
\right).
$$

The metric flow in gauge is:

$$
\partial_\tau g_{ij}
=
-2
\left(
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right)
+\mathcal L_Wg_{ij}.
$$

DeTurck's cancellation swaps the degenerate principal part for:

$$
\partial_\tau g_{ij}
=
g^{ab}\partial_a\partial_bg_{ij}
+\text{lower-order terms}.
$$

For $H$, Hodge gauge is used. If $H=dA$ locally, we impose:

$$
d_g^\dagger A=0.
$$

Then the torsional principal part is:

$$
\partial_\tau H
=
g^{ab}\nabla_a\nabla_bH
+\text{lower-order terms}.
$$

## 4. Principal symbol

In the fixed gauge, the system has the quasi-linear form:

$$
\partial_\tau U
=
\mathcal A^{ab}(U)\partial_a\partial_bU
+\mathcal B(U,\partial U),
$$

with principal symbol:

$$
\sigma_{\rm pr}(\xi)
=
|\xi|_g^2 I.
$$

Since the bulk is Riemannian in the flow problem,

$$
|\xi|_g^2=g^{ab}\xi_a\xi_b>0
\qquad
\text{for }\xi\ne0.
$$

Therefore, the system in gauge is strongly parabolic as long as $g$ remains uniformly positive.

## 5. Functional spaces

A formulation in parabolic Hölder uses data:

$$
g_0,H_0,\phi_0,\chi_0\in C^{k,\alpha},
\qquad
k\ge2,
\qquad
0<\alpha<1,
$$

with

$$
g_0\ge\lambda\bar g
\qquad
\text{for some }\lambda>0,
$$

and compatibilities:

$$
dH_0=0,
\qquad
\int_Me^{-\phi_0}dV_{g_0}=1,
\qquad
\rho_0=e^{-\phi_0}>0.
$$

Then the solution in gauge locally belongs to:

$$
U\in C^{1+\alpha/2,\,2+\alpha}([0,T]\times M).
$$

In Sobolev, for $d=\dim_{\mathbb R}M=8$, one can take:

$$
U_0\in H^s,
\qquad
s>\frac d2+2=6,
$$

for example, $s\ge7$.

## 6. Local theorem

Under the assumptions above, there exists $T>0$ and a unique solution in gauge:

$$
U(\tau)=(g(\tau),H(\tau),\phi(\tau),\chi(\tau)),
\qquad
0\le\tau\le T.
$$

Furthermore:

1. if $U_0$ is smooth, then $U(\tau)$ is smooth for $\tau>0$;
2. the map $U_0\mapsto U(\tau)$ depends continuously on the data;
3. in the geometric system without gauge, uniqueness is up to diffeomorphisms.

To undo the gauge, one solves:

$$
\frac{d}{d\tau}\Phi_\tau
=
-W(g(\tau))\circ\Phi_\tau,
\qquad
\Phi_0=\operatorname{id},
$$

and transports:

$$
\tilde g= \Phi_\tau^*g,
\qquad
\tilde H=\Phi_\tau^*H,
\qquad
\tilde f=\Phi_\tau^*f.
$$

## 7. Continuation criterion

The solution can be continued beyond $T$ as long as the geometry remains uniformly controlled. A sufficient criterion is:

$$
0<\lambda\bar g\le g(\tau)\le\Lambda\bar g<\infty,
$$

and

$$
\sup_{[0,T)\times M}
\left(
|{\rm Rm}(g)|
+|H|^2
+|\nabla H|^2
+|\nabla\phi|^2
+|\nabla^2\phi|
+|\nabla\chi|^2
+|\nabla^2\chi|
\right)
<\infty.
$$

It also maintains:

$$
\rho=e^{-\phi}>0
$$

and the boundary/gauge conditions of the sector.

Therefore, finite-time failure means loss of one of these conditions: metric degeneration, curvature explosion, torsional explosion, loss of regularity of $f$, appearance of density zero, or boundary incompatibility.

## 8. Relation with monotonicity

The Perelman--Bismut monotonicity, when valid in the sector, provides control of stability and attractors. It does not replace local well-posedness.

Thus, the correct chain is:

$$
\text{gauge}
\to
\text{strong parabolic symbol}
\to
\text{existence, uniqueness and continuous dependence}
\to
\text{continuation criterion}.
$$

Only after that enter Lyapunov functionals, monotonicity, and asymptotic analysis.

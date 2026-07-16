---
title: Chapter 07 detailed map
status: active
source: manuscrito/07_classical_limit/
---

# Chapter 07 detailed map

## 07.1 — Meaning of the classical limit

The classical limit requires:

1. surviving variables;
2. a small dimensionless parameter;
3. a limiting equation;
4. an error estimate;
5. failure regions.

GDQ already supplies

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

The chapter separates semiclassical limit, macroscopic averaging and torsion
depolarisation. The proof primarily uses the first: small Bohm correction.

## 07.2 — Starting Hamilton--Jacobi--Bohm system

The official Cauchy space is larger:

$$
(\rho,p_\rho,S_R,\Pi_{S_R}).
$$

The chapter works in the Madelung polarisation

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\,\rho.
$$

In a local nonrelativistic chart the effective reduced action is

$$
I_{\rm M}
=\int dt\int_{\Sigma_t}
\left[
\rho
\left(
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}+V
\right)
+\frac{\hbar^2}{8m}\frac{|\nabla\rho|^2}{\rho}
\right]d\Sigma.
$$

Varying $S_R$ gives continuity; varying $\rho$ gives
Hamilton--Jacobi--Bohm with

$$
Q_B=-\frac{\hbar^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

## 07.3 — Control parameter

For $R=\sqrt\rho$ and $p=|\nabla S_R|$, define $L_\rho$ by

$$
\left|\frac{\Delta R}{R}\right|
\le\frac{C_R}{L_\rho^2}.
$$

Then

$$
\varepsilon_{\rm cl}
=\frac{\hbar}{pL_\rho}
=\frac{\lambda_{\rm dB}^{\rm red}}{L_\rho},
$$

and

$$
\frac{|Q_B|}{T_{\rm cl}}
\le C_R\varepsilon_{\rm cl}^2.
$$

The force correction also needs third-derivative control:

$$
\frac{|\mathbf F_B|}{|\mathbf F_{\rm cl}|}
=O\left(\varepsilon_{\rm cl}^2\frac{L_V}{L_\rho}\right).
$$

## 07.4 — Hamilton--Jacobi limit

For families with $\rho_\varepsilon\ge\rho_*>0$, uniform amplitude regularity,
phase convergence and $\varepsilon_{\rm cl}\to0$, the Bohm term vanishes in
the adopted energy scale. The limit satisfies

$$
\partial_tS_0+\frac{|\nabla S_0|^2}{2m}+V=0.
$$

The density remains and is transported by the limiting continuity equation.

## 07.5 — Characteristics and Newton

From

$$
\partial_tS_0+H(x,\nabla S_0,t)=0,
$$

the characteristics satisfy Hamilton equations:

$$
\dot x^i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial x^i}.
$$

For $H=|p|^2/(2m)+V$ this gives

$$
m\ddot x=-\nabla V.
$$

Keeping $Q_B$ gives the correction force $-\nabla Q_B$.

## 07.6 — Liouville

Before caustics, the phase defines $p=\nabla S_0$. The monocinetic phase-space
measure is

$$
F(x,p,t)=\rho_0(x,t)\delta(p-\nabla S_0(x,t)).
$$

Using continuity and Hamilton equations gives Liouville in weak form:

$$
\partial_tF
+\frac{\partial H}{\partial p}\cdot\nabla_xF
-\frac{\partial H}{\partial x}\cdot\nabla_pF=0.
$$

After caustics, one needs multiple branches or a general phase-space measure.

## 07.7 — WKB and stationary phase

With

$$
\Psi=R\,e^{iS_R/\hbar},
$$

the Schrödinger form splits into Hamilton--Jacobi--Bohm and continuity. This
checks the Madelung representation but does not replace the derivation from
the official GDQ action.

The WKB leading order gives Hamilton--Jacobi; the next order gives transport
of amplitude. Stationary phase selects extremal classical paths in oscillatory
integrals. Maslov phases handle caustics but must not be conflated with proof
of spin without additional construction.

## 07.8 — Cotangent global potential to Kepler

On $S^3$ of radius $R_E$, the radial harmonic equation gives

$$
V_E(r)=V_0-\frac{\kappa}{R_E}\cot\left(\frac r{R_E}\right).
$$

This line must be read as the product

$$
V_E(r)=V_0-\frac{\kappa}{R_E}\cot\left(\frac r{R_E}\right),
$$

with the conventional overall sign fixed by the source. Conceptually, the
Kepler limit is the expansion of the cotangent Green kernel:

$$
\frac1{R_E}\cot\left(\frac r{R_E}\right)
=\frac1r-\frac{r}{3R_E^2}+O\left(\frac{r^3}{R_E^4}\right).
$$

Thus the local $1/r$ potential is the local limit of the global cotangent
potential. The coupling $\kappa$ still comes from the sectoral Hessian
normalisation.

## 07.9 — Noether constants

Classical conservation laws survive if the reduction and boundary conditions
preserve the corresponding symmetries:

- time homogeneity gives energy conservation;
- spatial homogeneity gives momentum conservation;
- isotropy gives angular momentum conservation;
- phase shift gives transported charge/probability in the Madelung sector.

Each physical charge identification requires its own sectoral map and
normalisation.

## 07.10 — Torsion and scope

The scalar correspondence is established in the regular Madelung sector. Torsion
does not have to vanish in all macroscopic regimes. The Levi--Civita limit
requires depolarisation/isotropisation:

$$
\langle H\rangle_{\rm macro}\simeq0.
$$

If the experiment is sensitive to spin, vorticity or polarisation, the
torsional sector must remain.

## 07.11 — Maxwell correspondence

Given the already constructed primitive $U(1)_Q$ direction and effective
connection $A$, define

$$
F=dA.
$$

Then $dF=0$ gives the homogeneous Maxwell equations. The quadratic restriction
of the physical Hessian has the form

$$
I_Q[A]
=-\frac{Z_Q}{4}
\int F_{ab}F^{ab}\sqrt{-g}\,d^4x
+\int A_aJ_Q^a\sqrt{-g}\,d^4x.
$$

Varying gives

$$
\nabla_aF^{ab}=j^b,
$$

up to the current sign convention. $Z_Q$, $\varepsilon_0$, $\mu_0$ and
$\alpha$ are normalisation questions, not part of the formal Maxwell shape.

## 07.12 — Einstein/Newton correspondence

The macroscopic metric correspondence uses torsion averaging, the weighted
metric equation from Chapter 5 and a hydrodynamic closure of the stress
contained in $f$.

The exact identity

$$
\nabla_\mu\nabla_\nu f_R
=\nabla_\mu f_R\nabla_\nu f_R
-\frac1\rho\nabla_\mu\nabla_\nu\rho
$$

connects the legacy Hessian intuition to the official variational equation.

The trace-reversed form is

$$
R_{\mu\nu}
=\kappa_G
\left(T_{\mu\nu}-\frac12g_{\mu\nu}T\right)
+\Lambda g_{\mu\nu}.
$$

Algebraically this becomes Einstein's equation. Dimensional analysis gives
$\kappa_G=C_GG/c^4$, and comparison with Poisson fixes

$$
\kappa_G=\frac{8\pi G}{c^4}.
$$

The value of $G$ and torsion residuals remain sectoral/global questions.

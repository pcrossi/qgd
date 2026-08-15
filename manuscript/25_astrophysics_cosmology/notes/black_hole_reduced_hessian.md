---
title: "Note — Reduced Hessian of the regular black hole"
---

# Note — Reduced Hessian of the regular black hole

This note records the reduced spectral blocks used to test the stability of the GDQ black hole as a soliton with horizon. The final covariant operator is:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm BH}^{\rm phys}
\operatorname{Hess}_{\Phi_{\rm BH,*}}\mathcal S_{\rm GDQ}
P_{\rm BH}^{\rm phys}.
$$

The reduction below is not the complete 8D matrix; it is the evaluation of the blocks that can be computed from the radial saddle and the static exterior.

## 1. Torsional origin of $\lambda_T$

In the Bismut connection:

$$
\mathcal R^B
=
\mathcal R^{LC}
-
\frac{1}{12}|H|^2.
$$

In the isotropic core:

$$
H_{abc}
=
q_T\rho\,\varepsilon_{abc}.
$$

Then:

$$
|H|^2
=
6q_T^2\rho^2.
$$

The reduced torsional term is:

$$
E_H
=
\frac{1}{12}\int |H|^2\,dV
=
\frac{q_T^2}{2}\int\rho^2\,dV
=
\frac{q_T^2}{2}\int u^4\,dV.
$$

Comparing with:

$$
U_T
=
\frac{\lambda_T}{2}\int u^4\,dV,
$$

it follows:

$$
\lambda_T=q_T^2.
$$

In the minimal isotropic normalization of the three orthogonal Cartan--Bismut circulation channels:

$$
q_T^2=1+1+1=3.
$$

Therefore:

$$
\lambda_T=3.
$$

## 2. Virial

For:

$$
E[u]=K+U_T+W,
$$

with:

$$
K=\frac{1}{2}\int|\nabla u|^2\,dV,
\qquad
U_T=\frac{\lambda_T}{2}\int u^4\,dV,
\qquad
W=\frac{1}{2}\int\phi u^2\,dV,
$$

the rescaling preserving mass:

$$
u_a(r)=a^{3/2}u(ar)
$$

implies, without boundary:

$$
2K+3U_T+W=0.
$$

For $\lambda_T=3$, the evaluation reduced to:

$$
K=3.1675522712965487\times10^{-1},
$$

$$
U_T=9.808336775055311\times10^{-2},
$$

$$
W=-9.274781821673822\times10^{-1},
$$

with:

$$
2K+3U_T+W
=
2.8237534358688254\times10^{-4}.
$$

The relative residue was:

$$
1.5220431610642136\times10^{-4}.
$$

In the collective direction:

$$
\frac{d^2E}{da^2}\bigg|_{a=1}
=
1.193971365853>0.
$$

## 3. Amplitude radial block with Schur

The second variation before eliminating $\phi$ is:

$$
\left[
-\frac{1}{2}\Delta
+
\phi-\mu
+
3\lambda_Tu^2
\right]\delta u
+
u\,\delta\phi
=
0.
$$

The potential perturbation satisfies:

$$
\Delta\delta\phi
=
2u\,\delta u.
$$

Eliminating $\delta\phi$ by Schur complement:

$$
K_{uu}^{\rm Schur}
=
-\frac{1}{2}\Delta
+
\phi-\mu
+
3\lambda_Tu^2
+
u\,\Delta^{-1}(2u\,\cdot).
$$

The normalization mode:

$$
y_N(r)=ru(r)
$$

is removed by:

$$
P_N
=
1
-
\frac{|y_N\rangle\langle y_N|}
{\langle y_N,y_N\rangle}.
$$

The physical radial block is:

$$
K_{uu,0}^{\rm phys}
=
P_NK_{uu}^{\rm Schur}P_N.
$$

Before the projection:

$$
\lambda_{\rm raw,1}
=
-1.927437459951\times10^{-1}.
$$

After the projection:

$$
\lambda_{\rm phys,1}
=
-5.982003087324\times10^{-13}
\simeq0,
$$

and:

$$
\lambda_{\rm phys,2}
=
3.651456961676\times10^{-2}>0.
$$

The mesh convergence was:

| $N$ | $\lambda_{\rm phys,2}$ |
|---:|---:|
| $300$ | $3.650859450588\times10^{-2}$ |
| $450$ | $3.651280931120\times10^{-2}$ |
| $650$ | $3.651456961676\times10^{-2}$ |
| $850$ | $3.651524343579\times10^{-2}$ |

## 4. Scalar harmonics of amplitude

For:

$$
\delta u(r,\Omega)
=
\frac{y_l(r)}{r}Y_{l m}(\Omega),
$$

the local operator receives:

$$
\frac{l(l+1)}{2r^2}.
$$

The radial Schur Green uses:

$$
\left(
\frac{d^2}{dr^2}
-
\frac{l(l+1)}{r^2}
\right)
\delta\psi_l
=
2uy_l.
$$

For $0\le l\le 8$, there was no negative physical eigenvalue. The smallest mode was:

$$
\lambda_{l=1}
=
1.909625790263\times10^{-3}>0.
$$

## 5. Phase/circulation sector

The quadratic form is:

$$
Q_θ[\delta\theta]
=
\frac{1}{2}\int\rho|\nabla\delta\theta|^2\,dV.
$$

Therefore:

$$
K_\theta
=
-\nabla\cdot(\rho\nabla).
$$

The zero at $l=0$ is:

$$
8.536256780627\times10^{-13}
\simeq0,
$$

and represents the global phase protected by Noether. The smallest non-zero physical mode was:

$$
\lambda_{l=1}
=
6.572554660398\times10^{-2}>0.
$$

## 6. Torsional and axial metric sector

Without an artificial infrared floor, the reduced torsional block is:

$$
K_{HH,l}^{red}
=
-\frac{d^2}{dr^2}
+
\frac{l(l+1)}{r^2}
+
2\lambda_T\rho(r).
$$

The smallest gap found was:

$$
\lambda_{\min}(K_{HH}^{red})
=
1.475541776890\times10^{-1}>0.
$$

In the static exterior patch, the reduced axial metric sector is:

$$
K_{gg,l}^{red}
=
-\frac{d^2}{dr^2}
+
V_{gg,l}(r),
$$

with:

$$
V_{gg,l}
=
A
\left[
\frac{l(l+1)}{r^2}
-
\frac{6m(r)}{r^3}
+
4\pi(\epsilon-p_r)
\right].
$$

The smallest gap found was:

$$
\lambda_{\min}(K_{gg}^{red})
=
1.493545907614\times10^{-1}>0.
$$

## 7. Cross-couplings by Schur

The metric--dilatonic coupling comes from the variation of the weighted measure:

$$
\mathcal U=e^{-f_R}(4\pi z_\tau)^{-n}.
$$

In the reduced exterior patch:

$$
J_{gf}^{red}
\sim
\sqrt A\,|\partial_r f_R|\sqrt\rho.
$$

The metric--torsional coupling comes from the variation of:

$$
\sqrt g\,|H|^2.
$$

In the reduced sector:

$$
J_{gH}^{red}
\sim
\sqrt{\lambda_T}\rho.
$$

The norms were:

$$
\|K_{gf}^{red}\|
=
6.166879064740\times10^{-4},
$$

$$
\|K_{gH}^{red}\|
=
8.076881453156\times10^{-6}.
$$

The Schur ratios were:

$$
\chi_{gf}
=
1.333410946325\times10^{-3},
$$

$$
\chi_{gH}
=
2.960174621482\times10^{-9}.
$$

Since both are much smaller than $1$, the reduced cross-couplings do not close the gap of the tested diagonal blocks.

## 8. Horizon and Page toy

The reduced surface gravity is:

$$
\kappa_H
=
\frac{1}{2}e^{\Phi(r_H)}|A'(r_H)|.
$$

The temperature is:

$$
T_H
=
\frac{\kappa_H}{2\pi}.
$$

For the two horizons:

$$
T_1=2.332099662324\times10^{-2},
\qquad
T_2=4.844788989724\times10^{-3}.
$$

The Page curve preserved in this layer is only a toy unitary one:

$$
S_{\rm toy}(0)=0,
\qquad
\max S_{\rm toy}=2.696953704284\times10^{-5},
\qquad
S_{\rm toy}(1)=0.
$$

The physical Page curve requires real spectral channels of $K_{\rm BH}^{\rm phys}$ in regular coordinates crossing horizons.

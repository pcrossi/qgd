---
title: "Hessian, projectors and interface response"
---

# Hessian, projectors and interface response

## 1. Statement

This note records the construction that must be used whenever the chapter refers to a real apparatus. The ideal holonomy effect is topological. The correction for a real apparatus is variational.

The correct chain in GDQ is:

$$
J_{\rm app}^{\rm classical}
\to
\Phi_\ast
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{observable}.
$$

Here $\Phi=(g,J,H,f)$ denotes the relevant geometric fields: Hermitian metric, complex structure, Bismut torsion and complex potential/dilaton.

## 2. Background with classical source

The apparatus enters as classical boundary data or an external source. For the solenoid, this source represents the macroscopic current, material, shielding and geometry of the tube.

The official action is not altered. The stationary condition with source is solved:

$$
\left.
\frac{\delta}{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm app}
\right)
\right|_{\Phi_\ast}
=
0.
$$

The source $\mathcal S_{\rm app}$ is not a new fundamental term. It specifies the apparatus defining the experiment, as a physical boundary condition.

## 3. Official Hessian

On the background $\Phi_\ast$, the Hessian is:

$$
K_{\rm GDQ}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi}
\right|_{\Phi_\ast}.
$$

In local coordinates, a fluctuation is written:

$$
\delta\Phi
=
(\delta g,\delta J,\delta H,\delta f).
$$

The second variation has the form:

$$
\delta^2\mathcal S_{\rm GDQ}
=
\langle
\delta\Phi,
K_{\rm GDQ}\delta\Phi
\rangle.
$$

The inner product contains the weighted measure of GDQ:

$$
d\mu_\ast
=
\mathcal U_\ast\sqrt{\det g_\ast}\,d^{2n}z\,\frac{d\tau}{\tau}.
$$

## 4. Removal of non-physical modes

Not all fluctuations of $\Phi$ are physical. There are directions representing changes of chart, gauge, reparametrization or violation of the charge and flux constraints.

We define the physical subspace by:

$$
\mathcal V_{\rm phys}
=
\ker C_Q
\cap
\ker C_F
\cap
\mathcal G^\perp.
$$

Here $C_Q$ is the charge constraint, $C_F$ is the flux constraint and $\mathcal G$ is the subspace tangent to the gauge orbits.

The weighted orthogonal projector is:

$$
P_{\rm phys}:
\mathcal V
\to
\mathcal V_{\rm phys}.
$$

The physical Hessian is:

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}
P_{\rm phys}.
$$

This is the quantity that can be diagonalized or reduced to the boundary.

## 5. Boundary-interior separation

We divide the physical fluctuations into boundary variables $Y$ and internal variables $I$:

$$
\delta\Phi_{\rm phys}
=
(\delta\Phi_Y,\delta\Phi_I).
$$

Then:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}.
$$

For a perturbation imposed on the boundary by the apparatus, the interior relaxes through the linear equation:

$$
K_{II}\delta\Phi_I
=
-
K_{IY}\delta\Phi_Y.
$$

When $K_{II}$ has a positive gap in the physical sector, the solution is:

$$
\delta\Phi_I
=
-
K_{II}^{-1}K_{IY}\delta\Phi_Y.
$$

Substituting into the quadratic form, we obtain:

$$
\mathsf R_{\rm app}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

This is the DtN/Schur matrix: it transforms boundary deformation into an effective normal response.

## 6. Application to real Aharonov--Bohm

In ideal AB:

$$
A_{\rm eff}
=
A_{\rm harm}.
$$

In the real solenoid:

$$
A_{\rm eff}
=
A_{\rm harm}
+
\delta A_{\rm surf}.
$$

The correction $\delta A_{\rm surf}$ is determined by $\mathsf R_{\rm sol}$ and the classical source of the apparatus. The phase is:

$$
\Delta\varphi
=
\frac{q}{\hbar c}
\oint_\gamma A_{\rm eff}.
$$

Thus:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}
+
\frac{q}{\hbar c}
\oint_\gamma\delta A_{\rm surf}.
$$

The first term is topological. The second term is metrological.

## 7. Strong closure condition

For a metrological prediction of a concrete solenoid, it is still necessary to provide:

1. apparatus geometry;
2. macroscopic current;
3. material and shielding;
4. domain and boundary;
5. background $\Phi_\ast$;
6. projector $P_{\rm phys}$;
7. spectrum of $K_{II}$;
8. calculation of $\mathsf R_{\rm sol}$;
9. integral of $\delta A_{\rm surf}$ along the experimental path.

Without these data, the chapter closes the ideal effect and the form of the correction, but not a specific real apparatus.

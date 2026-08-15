---
title: "Note — Integrated cosmological solver"
---

# Note — Integrated cosmological solver

This note defines the contract of the integrated cosmological solver. It does not introduce a new action and does not replace the official action with Einstein--Hilbert. The objective is to project the official action to a common cosmological background and require that all observables be calculated with the same data.

## 1. Cosmological saddle

$$
\Phi_*^{\rm cos}
=
(g,J,H,f,\mathcal U)_{\rm cos}.
$$

The input collection is:

$$
\mathcal P_{\rm cos}
=
\left(
\Phi_*^{\rm cos},
R_H,
\eta_b,
T_0,
\mathcal P_{\rm prim},
\mathcal B_{\rm contorno}
\right).
$$

Once frozen, this collection cannot be readjusted to explain each observable separately.

## 2. Common physical Hessian

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm cos}^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm cos}^{\rm phys}.
$$

The physical projector removes pure diffeomorphisms, measure normalization modes, boundary modes that only redefine the boundary, and unobservable internal gauge.

The common perturbations satisfy:

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}
=
J_{\rm bar}
+
J_\gamma
+
J_\nu
+
J_H.
$$

## 3. Homogeneous background

The background comes from the weighted metric equation:

$$
\operatorname{Eul}_g(\mathcal S_{\rm GDQ})=0
\quad
\Longrightarrow
\quad
\mathcal E_{\rm cos}[a,H,\rho_i,\Theta_H]=0.
$$

It defines:

$$
H(z)=\frac{\dot a}{a}.
$$

And the distances:

$$
D_C(z)=c\int_0^z\frac{dz'}{H(z')},
$$

$$
D_L(z)=(1+z)D_C(z),
\qquad
D_A(z)=\frac{D_C(z)}{1+z}.
$$

## 4. Observables produced by the same pair

The same background must feed:

1. homogeneous expansion;
2. scalar, vector, and tensor perturbations;
3. lensing;
4. growth;
5. BBN;
6. CMB;
7. Bismut holonomies.

For BBN:

$$
T(z)=T_0(1+z),
\qquad
H(z)=H_{\rm GDQ}(z),
$$

$$
\Gamma_{ij}^{\rm GDQ}(T)
=
\Gamma_{ij}^{\rm nuc}(T)
+
\Delta\Gamma_{ij}^{\rm Bohm-Cartan}(T,\Phi_*^{\rm cos}).
$$

For lensing:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)
\frac{2\,dl}{c^2}.
$$

For the residual geometric sector:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_{\nu}^{\ \alpha\beta}
-
\frac{1}{2}g_{\mu\nu}|H|^2.
$$

For birefringence:

$$
\Delta\Psi_{\rm GDQ}
=
\frac{1}{2}
\int_{\gamma_{\rm CMB}}
\omega_{\rm pol}^{B}.
$$

## 5. Closure criterion

The closure criterion is not to calibrate each observable separately. The background and boundary parameters must be frozen before the joint comparison.

The solver is only metrologically closed if a single $\mathcal P_{\rm cos}$ simultaneously generates $H(z)$, supernovae, BAO, CMB, BBN/lithium, lensing, growth, and birefringence.

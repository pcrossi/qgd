---
title: "Operational Checklist — Chapter 14"
---

# Operational Checklist — Chapter 14

## 1. Statement

Construct the geometric taxonomy of particles without a free table: matter as soliton/stoma, effective group as automorphism of the internal bundle, charges as global weights, and generations as additive index of three stomata.

## 2. Logical status

| Block | Status | Observation |
|---|---|---|
| Soliton/stoma | Structural | Matter as geometric defect. |
| Material soliton criterion | Structurally closed | Requires stationary equation, finite energy, charge, spin, Hessian, zero modes, asymptotics, and interaction. |
| Monotonicity and stability | Conditionally closed | Monotonicity is Lyapunov; stability requires physical Hessian without negative eigenvalues. |
| Internal bundle | Structurally closed | $E_C\oplus E_W\oplus L_Y$. |
| Effective group | Structurally closed | $\operatorname{Aut}_{\rm GDQ}(E_{\rm int})$. |
| $Z_6$ and hypercharge | Closed as Diophantine | Conditional on the internal representations. |
| Anomalies | Proven | Explicit cancellation per generation. |
| Local APS index | Proven in the Hopf--Bismut prototype | A co-oriented primitive stoma provides index $1$. |
| Lifting to representations | Proven | One local unit generates $15$ Weyl components; three generate $45$. |
| Flat global product | Excluded as origin of three | Flat Betti/Euler/Berry do not provide $N_G=3$. |
| Three stomata | Closed in the reduced horizontal model | Noether, Hopf, and isolation. |
| Hessian $C_3$ | Proven in collective modes and reduced Gaussian filling | Two positive relative modes and positive reduced gap. |
| Couplings | Closed ratios | $g_s=g$, $g'^2/g^2=3/5$, $\sin^2\theta_W=3/8$. |
| Masses/mixings | Future | Subsequent chapters. |

## 3. Deductive chain

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\text{Noether}
\to
E_{\rm int}
\to
\operatorname{Aut}_{\rm GDQ}(E_{\rm int})
\to
\mathbb Z_6
\to
\mathcal E_{\rm gen}
\to
N=3
\to
\operatorname{Ind}_{\rm total}=3.
$$

## 4. Mandatory variational construction

The chapter must keep the chain explicit:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm stoma}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\text{internal modes}
\to
\text{index/charges}.
$$

In the $C_3$ sector, the constrained Hessian is:

$$
H_{\rm eff}
=
H_{\rm rel}
-
J_{\theta r}
\left(
K_\perp^{(r,0)}
\right)^{-1}
J_{\theta r}^{\dagger}.
$$

With conservation of the flux class:

$$
J_{\theta r}=0.
$$

## 5. Scripts

| Script | Classification |
|---|---|
| `verify_gaussian_soliton.py` | Verification of the neutral Gaussian solution, energy $\mathcal W=0$ and reduced OU gap. |
| `monotonicity_vs_hessian.py` | Illustration that monotonic Lyapunov does not replace positive Hessian. |
| `hypercharges_z6.py` | Diophantine search and anomaly verification. |
| `aps_index_hopf_bismut.py` | Verification of the primitive flux, reduced eta, torsional kernel, and local APS index. |
| `index_lifting_representations.py` | Count of Weyl components per index unit and per three stomata. |
| `global_product_three_stomata.py` | Betti of $T^5\times S^3$, zero Euler, flat Berry and count by three stomata. |
| `hessian_three_centers.py` | Verification of the constrained $C_3$ Hessian. |
| `physical_hessian_c3_gap.py` | Physical projector, Schur, and reduced gap of the $C_3$ junction. |
| `couplings_norms.py` | Direct evaluation of norms and coupling ratios. |
| `junction_n_selection.py` | Reduced test of selection $N=3$ and null modes for $N>3$. |

## 6. Historical scripts of geometric taxonomy

The final/reduced scripts above replace the need to migrate all exploratory scripts of geometric taxonomy to the body of the chapter. The complete list of historical scripts remains in `the external history of construction` and is registered in [[notes/preserved_scripts_taxonomy|Scripts migrated from the geometric taxonomy]].

## 7. Points that cannot be forgotten

- Do not say that fractional charges are literal fractional Chern.
- Do not use the Standard Model as ontology.
- Do not use $N_G=3$ as input.
- Do not turn masses and mixings into part of the geometric taxonomy.
- Do not compare couplings of different scales without background.
- Do not omit the constrained Hessian of the three centers.

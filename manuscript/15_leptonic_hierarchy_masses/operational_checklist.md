---
title: "Operational Checklist — Chapter 15"
---

# Operational Checklist — Chapter 15

## 1. Statement

Derive leptonic ratios as GDQ dimensionless geometric stiffnesses, without confusing unit calibration, auxiliary spectral benchmark, or empirical formula with ontological foundation.

## 2. Logical Status

| Block | Status | Observation |
|---|---|---|
| Mass as geometric cost | Structural | Defect sustaining energy. |
| Absolute scale | Metrological | MeV requires external unit standard. |
| Rosen--Morse | Auxiliary benchmark | Does not identify generations. |
| Muon | Closed in the intrinsic reduced model | $\frac32\alpha^{-1}+\frac65+2\alpha$. |
| Tau | Closed by conditional geometric saturation | Koide as geometry, not empirical input. |
| Fourth generation | Excluded on the reduced support | No fourth orthogonal projector in $R^3$. |
| Perelman 3D/8D reduction | Closed conditional theorem | Perelman acts on the curved factor $B_3$, not on the general 8D. |
| Product 8D background | Closed | $a_W=a_f=a_H=\varepsilon=0$ and $\Delta_{\rm Schur}=0$. |
| Product 8D Hessian | Closed | $J=0$, Schur preserves ratios. |
| Warped/mixed | Conditional | Criterion $j_{\rm mix}^2/m_\perp^2<\lambda_B^{\rm gap}$. |

## 3. Constructive Chain

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ell
\to
K_{\rm phys}^{\ell}
\to
P_k
\to
R_\mu
\to
Q=\frac23
\to
R_\tau
\to
H_B-JH_\perp^{-1}J^\dagger.
$$

## 4. Final/Reduced Scripts

| Script | Classification |
|---|---|
| `intrinsic_tension_mu_tau.py` | Direct evaluation of the intrinsic GDQ path. |
| `symbolic_derivation_leptonic_hierarchy.py` | Symbolic derivation of the reduced formulas. |
| `koide_saturation.py` | Verification of geometric saturation and two branches. |
| `perelman_reduction_3d_bulk8.py` | Symbolic-numerical verification of the 3D reduction in the factored 8D bulk. |
| `stationary_8d_background.py` | Direct evaluation of the parameters $a_W,a_f,a_H,\varepsilon,\lambda_B^{\rm gap}$. |
| `hessian_8d_schur.py` | Test of product/warped-mixed reduced Schur. |
| `warped_mixed_criterion.py` | Test of the subcritical criterion for mixed backgrounds. |
| `hierarchy_8d_schur_response.py` | 8D response of the ratios under Schur complement. |
| `rosen_morse_benchmark.py` | Auxiliary benchmark, not ontology. |
| `verify_metrological_calibration.py` | Symbolic-numerical verification of the metrological calibration. |

## 5. Points that must not be forgotten

- Do not declare absolute mass without calibration.
- Do not confuse $\Lambda_C$, $\widehat\Lambda_\tau$, sector masses and metrological scale $E_0$.
- Do not use Rosen--Morse as a physical generation.
- Do not use Koide as an empirical input.
- Do not call corrections fundamental renormalization.
- Do not omit Hessian/Schur in the 8D lifting.
- Do not promote Koide's light branch without a proper Hessian.
- Do not carry fruitless attempts to the main narrative.

---
title: "Operational checklist — Chapter 12"
---

# Operational checklist — Chapter 12

## 1. Objective

Explain tunneling, double slit, detector, and delayed choice as problems of density, phase, boundary, and transport in the reduced sector of GDQ.

## 2. Logical Status

| Block | Status | Observation |
|---|---|---|
| Hartman | Conditional reduced theorem | $g_{xx}\propto\rho$ holds in the declared evanescent channel, not universally. |
| Double slit without detector | Closed in the flat Madelung sector | Recovers interference. |
| Bohm nodes | Effective reduction | Geometric pressure at zeros. |
| DtN/Schur detector | Structurally closed | Reduced linear channel. |
| Visibility | Conditionally closed | $\mathcal C=e^{-\Gamma_{\rm det}}$. |
| Delayed choice | Structurally closed | Causal boundary/transport. |
| Real apparatus | Metrological program | Requires material data and full Hessian. |

## 3. Deductive Chain

$$
J_{\rm app}^{\rm classical}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\rho,S_R
\to
\Omega,\partial\Omega
\to
\text{slits/barrier}
\to
\text{two contributions}
\to
\mathsf R_{\rm det}
\to
\Gamma_{\rm det}
\to
\rho_{\rm obs}.
$$

Technical construction named:

- [[notes/gdq_construction_transport_interference|GDQ construction of transport and interference]]

## 4. Scripts

| Script | Classification |
|---|---|
| `reduced_hartman_saturation.py` | Direct evaluation of reduced formula. |
| `reduced_double_slit.py` | Madelung/paraxial effective reduction. |
| `detector_schur_visibility.py` | Effective reduction/apparatus. |
| `delayed_choice_kernel.py` | Reduced causal transport. |
| `double_slit_detector_dtn.py` | Specific DtN detector, mesh and coherence. |
| `compare_gdq_standard_double_slit.py` | Comparison of reduced GDQ vs standard limits. |
| `electro_optic_mzi_response.py` | Temporal response of EO-MZI, $\mathsf R_{\rm app}(t)$, $\Gamma_{\rm det}$ and comparison with crosstalk. |
| `material_hessian_eo_mzi.py` | Reduced material Hessian and imperfections equivalent to $-30\,{\rm dB}$. |

## 5. Points that must not be forgotten

- Do not call $g_{xx}\propto\rho$ a general theorem outside the reduced evanescent sector.
- Do not treat the detector as an external collapse.
- Do not use advanced propagator as a physical signal to the past.
- Do not claim complete metric evolution for the double slit.
- Do not confuse raw visibility with the coherence coefficient.

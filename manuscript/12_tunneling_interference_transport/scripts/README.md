---
title: "Scripts — Chapter 12"
---

# Scripts — Chapter 12

| Script | Objective | Classification |
|---|---|---|
| `reduced_hartman_saturation.py` | Evaluate $D_{\rm proper}(L)$ and $\tau_{\rm GDQ}(L)$ in the reduced evanescent channel. | Direct evaluation of reduced formula. |
| `reduced_double_slit.py` | Generate coherent/incoherent reduced pattern. | Effective reduction. |
| `detector_schur_visibility.py` | Evaluate $\mathsf R_{\rm det}$ and visibility. | Effective reduction/apparatus. |
| `delayed_choice_kernel.py` | Integrate causal temporal response of the apparatus. | Reduced transport. |
| `double_slit_detector_dtn.py` | Evaluate double slit with specific DtN detector, mesh refinement, and coherence table. | Direct evaluation of reduced detector. |
| `compare_gdq_standard_double_slit.py` | Compare coherent limit, incoherent limit, and reduced GDQ curve by $\exp(-\Gamma_{\rm det})$. | Phenomenological/controlled comparison. |
| `electro_optic_mzi_response.py` | Calculate $\mathsf R_{\rm app}(t)$, $\Gamma_{\rm det}$, and residual coherence in EO-MZI with frozen data. | Direct evaluation of reduced model with external apparatus data. |
| `material_hessian_eo_mzi.py` | Calculate ideal MZI and imperfections equivalent to $-30\,{\rm dB}$. | Reduced material engineering model. |

The new scripts are self-contained: they do not import files from questions or auxiliary modules external to the script itself.

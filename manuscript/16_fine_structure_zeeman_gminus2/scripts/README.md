---
title: "Scripts — Chapter 16"
---

# Scripts — Chapter 16

| Script | Objective | Classification |
|---|---|---|
| `calculate_einstein_mean_alpha.py` | Evaluate $\alpha_E^{\rm mean}$ without CODATA. | Direct evaluation of derived quantity. |
| `calculate_iso_hessian_projector.py` | Evaluate $\mathcal P_{\rm iso}=9/(8\pi^4)$ as angular/torsional contraction of the mean Hessian. | Direct evaluation of derived quantity. |
| `test_schur_dtn_alpha.py` | Record the round DtN/Schur diagnostic and its difference from the Einstein mean. | Consistency test / geometric diagnostic. |
| `zeeman_linear_response.py` | Verify Zeeman channels of a weak magnetic source. | Reduced symbolic-numerical test. |
| `gminus2_leading_term.py` | Calculate $a^{(1)}=\alpha/(2\pi)$ and compare with recorded references. | Direct evaluation of the leading term. |
| `evaluate_anomaly_hessian.py` | Verify the Hessian contraction that produces $\alpha/(2\pi)$. | Consistency test of the reduced operator. |
| `test_hierarchy_does_not_replace_gminus2.py` | Confirm that the leptonic hierarchy provides background, but does not close $g-2$. | Diagnostic of non-replacement. |
| `calculate_upper_residuals_gminus2.py` | Calculate residuals after subtracting $\alpha/(2\pi)$. | External metrological comparison. |
| `construct_gminus2_hessian_blocks.py` | Construct leading block and `required` blocks. | Derived leading; diagnostic inverse `required`. |
| `evaluate_gdq_gminus2_hessian.py` | Evaluate $a_\ell$ from an NPZ with $H,c,m_\perp$. | Operator evaluator. |
| `extract_upper_channel_gminus2.py` | Extract $K_i,J_i,\mu_i$ from the transverse complement. | Diagnostic/derivation tool. |
| `audit_nonuniqueness_upper_channel_gminus2.py` | Show that `required` blocks are not unique. | Negative result. |
| `official_galerkin_gminus2_hessian.py` | Calculate reduced Galerkin Hessian from the official action. | Consistency test; not prediction. |
| `construct_leptonic_source_background_gminus2.py` | Construct minimal effective backgrounds and linear magnetic map. | Positive effective reduction. |
| `derive_physical_upper_channel_gminus2.py` | Test Hodge rule for direct upper source. | Negative result: $\mu_2=0$. |
| `derive_h1_mixture_gminus2.py` | Evaluate harmonic mixture $H_1$. | Allowed mechanism, not final metrology. |
| `calculate_upper_variations_gdq_gminus2.py` | Evaluate reduced cubic/quartic tensors. | Variational diagnostic. |
| `contract_density_channel_gminus2.py` | Contract $\Delta H_{12}=\eta_\ell T_{123}$. | Conditional evaluation. |
| `calculate_eta_via_saddle_gminus2.py` | Solve normalized angular saddle for $\eta_\ell$. | Reduced negative result. |

All scripts are self-contained, commented, and write Markdown output in the same folder.

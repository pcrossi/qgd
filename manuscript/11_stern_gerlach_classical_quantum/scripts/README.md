---
title: "Scripts — Chapter 11"
---

# Scripts — Chapter 11

| Script | Goal | Classification |
|---|---|---|
| `calculate_sg_weights.py` | Calculate Stern--Gerlach angular weights. | Operational consistency test. |
| `simulate_sg_deflection.py` | Calculate deflection in a fixed channel. | Effective reduction/apparatus. |
| `test_sg_sequences.py` | Test incompatible sequential measurements. | Symbolic test. |
| `simulate_sg_capture.py` | Integrate the conditioned martingale and compare with first passage. | Operational Born statistical test. |
| `validate_sg_born_threshold.py` | Verify $P_\varepsilon(+)\to p_0$ when $\varepsilon\to0$. | Convergence test. |
| `simulate_complete_sg_beam.py` | Combine capture, channel, and propagation to the screen. | Full effective beam reduction. |
| `simulate_sg_sequences.py` | Simulate $z\to z$ and $z\to x\to z$. | Operational incompatibility test. |
| `simulate_nonadiabatic_sg.py` | Integrate Landau--Zener and calculate drift outside the QND regime. | Dynamic boundary. |
| `solve_sg_robin_channels.py` | Solve the reduced two-channel Robin spectrum. | Method test, not physical prediction. |
| `construct_sg_stationary_background.py` | Verify the Gaussian shrinker of the normal slice $\mathbb C^2$. | Direct bulk background evaluation. |
| `verify_sg_variational_boundary.py` | Verify $K-n(F)=0$ and $r_c=\sqrt{6\tau}$. | Boundary variational test. |
| `solve_sg_gaussian_robin.py` | Test the axial spectrum on the Gaussian background with diagnostic Robin. | Reduced diagnostic. |
| `test_sg_gaussian_zh.py` | Show zero axial infimum in the outer Gaussian. | Preserved negative result. |
| `solve_sg_cylindrical_hopf_dtn.py` | Calculate the axial DtN of the Hopf cylinder. | Reduced structural calculation. |
| `compare_sg_stationary_actions.py` | Compare Gaussian/cylindrical on-shell $\mathcal W$. | Reduced comparison. |
| `verify_sg_cylindrical_radius_stability.py` | Confirm $\mathcal W''(2\sqrt\tau)>0$. | Homogeneous stability. |
| `verify_sg_hopf_atlas.py` | Verify gluing, projector, and Fubini--Study metric. | Geometric/symbolic-numerical test. |
| `verify_sg_hopf_bismut_triplet.py` | Verify that the Hopf triplet of the normal slice $\mathbb C^2$ is self-dual and orthonormal after normalization. | Geometric/symbolic-numerical test. |
| `verify_sg_noether_zeeman.py` | Verify the Noether--Zeeman multiplier identity and parallel/antiparallel selection. | Symbolic-numerical consistency test. |
| `evaluate_gdq_sg_background.py` | Evaluate $\kappa_H^{\rm SG}$ and $\Gamma_{\rm SG}$ from physical spectrum. | Prediction evaluator, without phenomenological defaults. |
| `test_sg_background_pipeline.py` | Validate the evaluator with a synthetic fixture. | Code test, not physical. |
| `test_sg_physical_zeeman.py` | Convert apparatus data into $\Delta$ and $v$. | Dimensional test with external data. |

The files `output_*.md` preserve the audited runs. Scripts marked as "method test" or "fixture" must not be cited as a metrological prediction of GDQ.

---
title: "Scripts — Chapter 17"
---

# Scripts — Chapter 17

| Script | Objective | Classification |
|---|---|---|
| `derive_baryon_deltas.py` | Derive the reduced invariant $\delta_B=\ln(2\pi^2)3\sqrt2/5$. | Direct evaluation of conditional reduced derivation. |
| `symbolic_derivation_baryon_masses.py` | Symbolically derive $M_p/M_e$, $\delta_B$, and $M_n/M_e$. | Self-contained symbolic derivation. |
| `calculate_baryon_masses.py` | Evaluate reduced proton/neutron masses. | Direct evaluation. |
| `surface_radius_convergence.py` | Verify that the regularized shell converges to the surface radius $r_p$. | Consistency test. |
| `calculate_baryon_radii_moments.py` | Evaluate the proton radius and reduced magnetic moments. | Direct evaluation. |
| `calculate_reduced_form_factors.py` | Test Sachs normalizations and neutron squared radius. | Consistency test. |
| `neutron_torsional_profile.py` | Numerically solve the leading $H_n(\xi)$ profile and $G_E^n(q^2)$. | Direct evaluation of reduced variational profile. |
| `collective_surface_modes.py` | Evaluate collective surface impedance via Schur in three modes. | Reduced test of probe response. |
| `baryon_stability_spectrum.py` | Evaluate leading rotational spectrum and structural stability. | Direct reduced evaluation. |
| `validate_free_beta.py` | Verify beta endpoint and continuous character. | Consistency test. |
| `solve_bismut_dirac_modes_beta.py` | Evaluate the electronic and neutral torsional tangential kernels. | Direct evaluation of the declared operator. |
| `verify_four_mode_overlap_beta.py` | Verify the angular basis $S,T$, Gram $2,6$, and Fierz. | Structural symbolic-numerical verification. |
| `verify_noether_freedom_beta.py` | Demonstrate that Ward–Noether preserves a transverse scale freedom. | Algebraic test of non-identifiability. |
| `verify_causal_jets_beta.py` | Verify the cubic composition of the overlap causal jets. | Structural symbolic verification. |
| `verify_quartic_flux_projection_beta.py` | Verify the flux projector and the quartic Schur complement. | Structural symbolic verification. |
| `validate_free_beta_complete.py` | Calculate endpoint, analytical/Simpson phase space, contracted norm, lifetime, half-life, reduced continuous spectrum, and comparison. | Direct evaluation, convergence test, and phenomenological comparison. |
| `electronic_scale_beta.py` | Determine $M_ec^2$ from $Q_\beta$ and $\delta_B$. | Reduced metrological determination. |
| `compare_neutron_tau.py` | Evaluate reduced $\tau_n$ and compare with reference. | Phenomenological comparison. |
| `verify_green_current_hessian.py` | Verify the Green's identity of the Hessian bilinear current. | Structural symbolic verification. |

All scripts are self-contained and write Markdown output to the same folder.

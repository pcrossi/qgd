---
title: "Operational Checklist — Chapter 17"
---

# Operational Checklist — Chapter 17

## 1. Statement

Consolidate proton, neutron, and baryonic structure as trimodal solutions of GDQ, preserving bulk mass, surface torsion, integer charge, spin, parity, radius, moments, form factors, and free beta decay.

## 2. Constructive Chain

$$
\mathcal S_{\rm GDQ}
\to
\Phi_B
\to
K_B^{\rm phys}
\to
P_{\rm topo}
\to
\mathcal I_B
\to
Q_B,J^P,r_B,\mu_B,G_{E,M},\Gamma_n.
$$

## 3. Logical Status

| Block | Status | Observation |
|---|---|---|
| trimodal soliton | structurally closed | three glued stomata |
| $6\pi^5$ volume | reduced closed | mass ratio |
| surface torsion | reduced closed | Stokes/transgression |
| charge | closed | integer residue |
| spin/parity | closed | holonomy/involution |
| radius/moments | closed under surface reduction | full Hessian for fine metrology |
| form factors | structural/reduced | scattering data is a future refinement |
| $H_n(\chi)$ | closed under leading variational profile | zero charge and low-energy slope |
| collective impedance | closed in reduced surface model | three-mode Schur; full Hessian is fine metrology |
| spectrum/stability | structurally closed | $\Delta(1232)$ is a leading test only |
| continuous beta | closed | endpoint is not a fixed antineutrino energy |
| Ward/beta overlap | structurally closed | Noether fixes selection; fourth variation fixes magnitude |
| lifetime | conditionally closed | $10^{-3}$ level |

## 4. Final/Reduced Scripts

| Script | Classification |
|---|---|
| `calculate_baryon_masses.py` | Direct evaluation of reduced mass. |
| `surface_radius_convergence.py` | Consistency test of the radius as a surface observable. |
| `calculate_baryon_radii_moments.py` | Direct evaluation of reduced radius and moments. |
| `calculate_reduced_form_factors.py` | Sachs form factor normalization test. |
| `neutron_torsional_profile.py` | Direct evaluation of the leading $H_n(\chi)$ profile and leading $G_E^n$. |
| `collective_surface_modes.py` | Reduced test of collective impedance via Schur. |
| `baryon_stability_spectrum.py` | Evaluation of the leading spectrum and structural stability. |
| `validate_free_beta.py` | Test of the beta endpoint and continuous spectrum. |
| `solve_bismut_dirac_modes_beta.py` | Evaluation of tangential outgoing modes. |
| `verify_four_mode_overlap_beta.py` | Verification of the angular basis $S,T$ and Gram $2,6$. |
| `verify_noether_freedom_beta.py` | Test showing that Noether does not fix the transverse normalization. |
| `verify_causal_jets_beta.py` | Symbolic test of third-order causal jets. |
| `verify_quartic_flux_projection_beta.py` | Test of the flux projector and quartic Schur. |
| `compare_neutron_tau.py` | Evaluation of the reduced lifetime and comparison. |

## 5. Preserved Points

- Internal modes of the three stomata are not fundamental point-like quarks.
- $T^5\times S^3$ is a spectral/effective cycle, not the official local bulk.
- The fundamental baryon charge is integer at the global boundary.
- The neutron mass difference is not a fixed antineutrino energy.
- The lifetime is conditionally closed at the reduced level, not a complete differential.

## 6. Consolidated Technical Note

The self-contained derivation of masses, torsional equilibrium, $\delta_B$, the $H_n$ profile, the symplectic current, continuous beta, and the lifetime is gathered in [[notes/baryons/proofs_lemmas_definitions|Proofs, lemmas, and definitions of the baryonic sector]].

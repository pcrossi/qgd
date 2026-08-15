---
title: "Operational Checklist — Chapter 19"
---

# Operational Checklist — Chapter 19

## 1. Statement

Consolidate the geometric electroweak breaking of GDQ without turning the theory into a fundamental Standard Model.

## 2. Constructive Chain

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
=
P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]P_{\rm phys}
\to
\Phi_{\rm EW}
\to
a_2,a_4
\to
U(1)_{\rm EM}
\to
m_W,m_Z,m_\gamma.
$$

## 3. Preserved Constraints

| Constraint | Use |
|---|---|
| interface volume | cancels quadratic area term |
| torsional flux | provides surface stiffness |
| generator $Q=T_3+Y$ | preserves massless photon |
| projector $P_{\rm phys}$ | removes gauge/null modes |
| kinetic normalization | converts $\beta_\ast$ into reduced canonical field |
| spectral transport | separates the common point $3/8$ from the operational value $2/9$ |

## 4. Final/Reduced Scripts

| Script | Description |
|---|---|
| `electroweak_hopf_mode.py` | Symbolic verification of the Hopf mode and the preserved generator. |
| `electroweak_quartic_potential.py` | Direct evaluation of $a_2$, $a_4$, and $\beta_\ast$. |
| `neutral_mass_matrix.py` | Test of $W/Z/\gamma$ eigenvalues. |
| `simulate_electroweak_wz.py` | Reduced mass diagnostics for transport scenarios. |
| `hopf_kinetic_normalization.py` | Direct evaluation of the internal norm of the Hopf mode. |
| `conditional_weinberg_transport.py` | Conditional calculation of $Z_W/Z_Y=10/21$, $Q_\ast$, and W/Z comparison. |
| `schur_em_interface.py` | Verification of the electromagnetic Schur complement. |
| `no_go_berger_collar.py` | No-go product/Berger/collar and photonic divergence in the infinite collar. |
| `audit_vk.py` | Confirmation that $v_K$ is not the electroweak scale. |
| `verify_powers_units.py` | Editorial-dimensional check of $M^2$ and quadratic units. |
| `yukawa_overlap_demo.py` | Self-contained demonstration of the overlap structure. |

## 5. Points not migrated as foundation

- Homogeneous conformal breathing as Higgs.
- Berger stabilization by homogeneous ansatz, except as a preserved no-go.
- Direct tuning of $\sin^2\theta_W$ by target; the preserved path is the conditional spectral transport.
- Exploratory scripts with no-go or reverse engineering.

These items remain as methodological history; the manuscript preserves only the final reduced chain and the conclusions that refined the path.

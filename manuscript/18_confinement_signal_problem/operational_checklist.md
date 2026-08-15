---
title: "Operational checklist — Chapter 18"
---

# Operational checklist — Chapter 18

## 1. Statement

Consolidate signal problem, confinement, effective color, Wilson loops, area law, transverse gap, and GDQ--Yang--Mills sectorial relation.

## 2. Constructive Chains

Signal problem:

$$
\rho>0
\to
S_R
\to
\operatorname{Hol}(P_{ij})=-1
\to
\mathsf S_{ab}
\to
\text{positive benchmark}.
$$

Confinement:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm tube}
\to
K_{\perp}^{\rm phys}
\equiv
P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}[\Phi_{\rm tube}]P_{\rm phys}
\to
\sigma_{\rm GDQ}
\to
V(r)
\to
\langle W(C)\rangle.
$$

Color sector:

$$
E_{\rm int}
\to
SU(3)_C
\to
A_C
\to
F_C
\to
\mathfrak H_\Theta.
$$

## 3. Logical Status

| Block | Status | Observation |
|---|---|---|
| signal as phase | structurally closed | positive measure |
| Cayley interface | benchmark closed | machine unitarity |
| general variance | open | requires asymptotic bound |
| Ricci--Bohm tube | structurally closed | positive tension |
| area law | effective closed | geometric/isomorphic sector |
| gap | conditionally closed | effective geometric operator |
| Yang--Mills | sectorial effective reduction | not fundamental action |
| $\alpha_s^{\rm eff}$ | proposal preserved | not full running |
| radius/form factor | conditionally closed | canonical radius and compressed probe separated |
| torsional Hessian | sectorially closed | stable constrained homogeneous mode |

## 4. Final/Reduced Scripts

| Script | Classification |
|---|---|
| `cayley_signal_interface.py` | Consistence test of unitary/contractive interface. |
| `positive_signal_benchmark.py` | Reduced benchmark of positive correlation. |
| `reduced_physical_signal_benchmark.py` | Reduced physical benchmark with preserved external comparison. |
| `signal_variance_autocorrelation.py` | Reduced scaling test. |
| `integrate_ricci_bohm_confinement_tube.py` | Direct evaluation of transverse tension. |
| `ricci_bohm_cap_coefficient.py` | Numerical derivation of the coefficient $C_{\rm GDQ}=\pi$. |
| `compare_tension_confinement_radii.py` | Comparison of tension by radii. |
| `radius_form_factor_tension.py` | Calculation of canonical radius, form factor, and tension. |
| `constrained_torsional_hessian.py` | Evaluation of constrained radial Hessian. |
| `operational_heaviside_yang_mills.py` | Symbolic verification of the GDQ--YM operational bridge. |
| `alpha_s_fredholm_confinement.py` | Evaluation of the Fredholm proposal. |
| `hyperon_polarization_confinement.py` | Preserved phenomenological evaluation. |

## 5. Preserved Points

- GDQ does not postulate Yang--Mills as a fundamental action.
- Quarks/color are operational language of the reduced sector.
- Signal problem is not declared algorithmically solved in general.
- Area law and gap hold in the declared geometric/isomorphic sector.
- The comparison with $\sigma_{\rm had}\simeq0.89\,{\rm GeV/fm}$ is posterior; the reference value does not enter the derivation of $C_{\rm GDQ}$, $r_p$, or $F_{\rm shape}$.
- The `required` scripts and device thermal adjustments remain historical/future.
- No final reduced script for the signal problem and confinement was omitted from this chapter; exploratory or reverse engineering scripts are kept out of the main manuscript as they are not the final adopted chain.

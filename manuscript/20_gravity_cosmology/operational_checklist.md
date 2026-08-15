---
title: "Operational checklist — Chapter 20"
---

# Operational checklist — Chapter 20

## 1. Chapter statement

The chapter answers how GDQ treats:

1. Newton's constant;
2. vacuum energy;
3. dark energy equation of state;
4. galactic critical acceleration;
5. metrological limits of perturbative cosmology.

## 2. Preserved constructions

| Construction | Location | Status |
|---|---|---|
| separation of $M_{\rm loc}=\mathbb R^4\times T^4$ and $M_E=T^5\times S^3$ | `index`, `20.1` | operational definition |
| group $\Pi_G=GM_p^2/(\hbar c)$ | `20.2`, note `newton_pi_group_proof` | exact dimensional derivation |
| response $G=c^4R_H/(2E_H)$ | `20.2` | global boundary condition |
| thermal-axial chain | `20.3`, note `newton_thermal_axial_chain` | conditional on gluing |
| Buckingham prefactor | `20.2`, note `buckingham_prefactor_audit` | strong phenomenology |
| $\rho_\Lambda$ to vacuum energy | `20.4`, `20.5`, note `rho_lambda_derivation` | conditional structural |
| $w=-1$ homogeneous | `20.6` | closed in the stationary background |
| perturbations by Hessian | `20.6`, note `cosmological_hessian_perturbations` | metrological program |
| $a_0=cH_0/(2\pi)$ | `20.7`, note `critical_acceleration` | structural |

## 3. Hessian, projectors and constraints

The complete variational construction was recorded as:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast^{\rm cos}]
P_{\rm phys}.
$$

The text makes it explicit that $P_{\rm phys}$ removes:

1. pure diffeomorphisms;
2. normalization modes;
3. boundary modes;
4. unobservable internal gauge.

The chapter does not claim to have diagonalized the complete cosmological Hessian. It keeps this as the next metrological level.

## 4. Incorporated scripts

| Script | Output | Main result |
|---|---|---|
| `scripts/calculate_newton_g.py` | `scripts/output_calculate_newton_g.md` | with $\alpha_E$: $G_{\rm GDQ}=6.656497635372\times10^{-11}$, error $-0.266730\%$; with metrological $\alpha$: error $-0.262330\%$ |
| `scripts/calculate_thermal_axial_g_chain.py` | `scripts/output_calculate_thermal_axial_g_chain.md` | verifies $\Delta u_v=1/(2\alpha)$ under gluing $R=\pi^2\sqrt\alpha R_H$ |
| `scripts/symbolic_rho_lambda_derivation.py` | `scripts/output_symbolic_rho_lambda_derivation.md` | verifies the algebraic chain, $28=\binom82$ and final dimension ${\rm kg/m^3}$ |
| `scripts/calculate_rho_lambda.py` | `scripts/output_calculate_rho_lambda.md` | $\rho_\Lambda^{\rm GDQ}=6.136532599384\times10^{-27}\,{\rm kg/m^3}$, error $+5.033622\%$ |
| `scripts/symbolic_a0_derivation.py` | `scripts/output_symbolic_a0_derivation.md` | verifies $R_H=c/H_0$, $a_H=c^2/R_H=cH_0$ and $a_0=a_H/(2\pi)$ |
| `scripts/calculate_galactic_a0.py` | `scripts/output_calculate_galactic_a0.md` | $a_0=1.042197881145\times10^{-10}\,{\rm m/s^2}$ for $H_0=67.4$ |

All are self-contained, commented, and do not use the accepted value as input for the GDQ formula. Accepted values enter only in the final comparison.

## 5. Non-incorporated historical scripts

The exploratory solvers from the `historical gravitational numerical laboratory` were preserved as history. They were not copied to the chapter because they test local ansätze and exploratory warps that the final conclusion of the reduced Newton calculation does not use as a foundation.

The chapter uses only the consolidated route:

$$
\text{global boundary}
\to
\text{final reduced formula}
\to
\text{explicit comparison}.
$$

## 6. Mandatory comparisons

| Quantity | GDQ | Reference used | Error |
|---|---:|---:|---:|
| $G$ with $\alpha_E$ | $6.656497635372\times10^{-11}$ | $6.67430\times10^{-11}$ | $-0.266730\%$ |
| $G$ with metrological $\alpha$ | $6.656791325455\times10^{-11}$ | $6.67430\times10^{-11}$ | $-0.262330\%$ |
| $\rho_\Lambda$ | $6.136532599384\times10^{-27}$ | $5.842445930612\times10^{-27}$ | $+5.033622\%$ |
| $a_0$, $H_0=67.4$ | $1.042197881145\times10^{-10}$ | $1.20\times10^{-10}$ | $-13.150177\%$ |
| $a_0$, $H_0=73$ | $1.128789989964\times10^{-10}$ | $1.20\times10^{-10}$ | $-5.934168\%$ |

## 7. Editorial result

Nothing essential was omitted for the structural level of the chapter.

What is left out is not a failed attempt to be preserved in the main text, but a metrological program:

1. solve complete $\Phi_\ast^{\rm cos}$;
2. diagonalize $K_{\rm cos}^{\rm phys}$;
3. calculate transfer functions;
4. compare with CMB, BAO, SNe, lensing, and structure growth.

---
title: "Operational Checklist — Chapter 21"
---

# Operational Checklist — Chapter 21

## 1. Statement

The chapter answers:

1. how the strong CP angle relaxes without postulating any new fundamental particle;
2. how topological periodicity generates a global potential;
3. how relaxation is proven by Lyapunov;
4. how to compare the residual CP with the neutron EDM limit;
5. why a local point magnetic monopole is not a fundamental ontology;
6. how Hopf--Cauchy provides half-monodromy.

## 2. Preserved Constructions

| Construction | Location | Status |
|---|---|---|
| $q_C=(8\pi^2)^{-1}{\rm Tr}(F_C\wedge F_C)$ | `21.1` | effective definition |
| $Q_C\in\mathbb Z$ and $\theta\sim\theta+2\pi$ | `21.1`, `21.3` | topological |
| angular mode $\vartheta_B$ | `21.2` | structural |
| $V=\chi(1-\cos\theta)$ | `21.3` | periodic global potential |
| $K_{\rm CP}^{\rm phys}=P_{\rm phys}\delta^2\mathcal S_{\rm GDQ}P_{\rm phys}$ | `21.3`, `21.9`, Hessian note | physical channel definition |
| $\chi_{\rm top}^{\rm GDQ}=\langle\eta_B,K_{\rm CP}^{\rm phys}\eta_B\rangle$ | Hessian note | conditional on strong background |
| flow $\dot\theta=-\kappa\chi\sin\theta$ | `21.4` | relaxation |
| $f_B$ as torsional rigidity | `21.5` | conditional on normalization |
| residual EDM | `21.6` | conservative comparison |
| $\nabla\cdot(\nabla\times v)=0$ | `21.7` | local identity |
| $\operatorname{Res}\Omega_S=1/2$ | `21.8` | half-monodromy |

## 3. Hessian, Projectors and Constraints

The metrological normalization of the torsional mode must come from:

$$
K_{\rm tor}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

The chapter does not claim that the complete $K_{\rm tor}^{\rm phys}$ has already been diagonalized. The value of $f_B$ is classified as a proposed geometric rigidity and conditioned on the final canonical extraction.

## 4. Incorporated Scripts

| Script | Output | Result |
|---|---|---|
| `torsional_cp_relaxation.py` | `output_torsional_cp_relaxation.md` | $f_B=6.442945228853\times10^{17}$ GeV, $m_B=8.837901608259\times10^{-12}$ eV |
| `cp_periodicity_integer_charge.py` | `output_cp_periodicity_integer_charge.md` | invariance of $\exp(i\theta Q_C)$ under $\theta\mapsto\theta+2\pi$ for $Q_C\in\mathbb Z$ |
| `hessian_cp_susceptibility.py` | `output_hessian_cp_susceptibility.md` | Hessian $+\chi$ at the CP minimum and $-\chi$ at the unstable maximum |
| `hopf_cauchy_residue.py` | `output_hopf_cauchy_residue.md` | residue $1/2$, holonomy $-1$ |
| `monopole_vorticity.py` | `output_monopole_vorticity.md` | divergence of regular vorticity equal to zero |

All scripts are self-contained, commented, and generate Markdown.

## 5. Comparisons

| Quantity | Reduced Value | Reference/comparison | Status |
|---|---:|---:|---|
| $f_B$ | $6.442945228853\times10^{17}$ GeV | high axion-like scale | conditional |
| $m_B$ if there is a pole | $8.837901608259\times10^{-12}$ eV | relationship with $\chi_{\rm top}^{1/4}=75.46$ MeV | comparison |
| limit $|d_n|$ | relaxes to zero | $1.8\times10^{-26}\,e\,{\rm cm}$ | compatible |
| maximum $\theta_{\rm residual}$ | $4.736842105263\times10^{-11}$ | inferred from EDM limit | comparison |

## 6. What was not kept

Historical attempts that treated the quadratic potential as global or fundamental axion language were not incorporated. The chapter keeps only the periodic form, Lyapunov relaxation, and the torsional interpretation.

## 7. Editorial Result

The chapter is structurally closed. The following remain as refinements:

1. canonical normalization of $f_B$ by the official Hessian;
2. topological susceptibility calculated directly in the strong background;
3. residual EDM with boundaries, noise, and finite volume;
4. quantitative cosmology of the torsional mode.

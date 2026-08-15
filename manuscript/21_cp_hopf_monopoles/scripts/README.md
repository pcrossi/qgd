---
title: "Chapter 21 Scripts"
---

# Chapter 21 Scripts

The scripts are final/reduced, self-contained, and commented. They do not preserve historical attempts.

| Script | Output | Function |
|---|---|---|
| `torsional_cp_relaxation.py` | `output_torsional_cp_relaxation.md` | Integrates the flow $\dot\theta=-\kappa\chi\sin\theta$, calculates $f_B$, $m_B$, and compares with the EDM limit. |
| `cp_periodicity_integer_charge.py` | `output_cp_periodicity_integer_charge.md` | Verifies the invariance of the topological phase under $\theta\mapsto\theta+2\pi$ when $Q_C\in\mathbb Z$. |
| `hessian_cp_susceptibility.py` | `output_hessian_cp_susceptibility.md` | Verifies that the Hessian of the periodic potential is $+\chi$ at the CP minimum and $-\chi$ at the unstable maximum. |
| `hopf_cauchy_residue.py` | `output_hopf_cauchy_residue.md` | Symbolically verifies the half-monodromy by residue $1/2$. |
| `monopole_vorticity.py` | `output_monopole_vorticity.md` | Verifies that a regular vorticity has zero divergence and separates local domain from global topology. |

Classification:

1. `torsional_cp_relaxation.py`: direct evaluation of reduced flow and phenomenological comparison;
2. `cp_periodicity_integer_charge.py`: symbolic/didactic verification of topological identity;
3. `hessian_cp_susceptibility.py`: symbolic/numerical consistency verification;
4. `hopf_cauchy_residue.py`: symbolic verification of topological identity;
5. `monopole_vorticity.py`: symbolic/didactic verification of differential identity.

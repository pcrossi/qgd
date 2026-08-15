---
title: "Chapter 20 Scripts"
---

# Chapter 20 Scripts

These scripts are self-contained and commented. They evaluate only the final reduced formulas used in the chapter.

| Script | Output | Function |
|---|---|---|
| `calculate_newton_g.py` | `output_calculate_newton_g.md` | Evaluates the reduced formula of $\Pi_G$ and compares it with the accepted $G$. |
| `calculate_thermal_axial_g_chain.py` | `output_calculate_thermal_axial_g_chain.md` | Verifies the thermal-axial saddle and the gluing condition that generates $e^{-1/(2\alpha)}$. |
| `symbolic_rho_lambda_derivation.py` | `output_symbolic_rho_lambda_derivation.md` | Records the algebraic derivation, $28$ count, and dimensional analysis of $\rho_\Lambda$. |
| `calculate_rho_lambda.py` | `output_calculate_rho_lambda.md` | Evaluates the dark energy density and compares it with the inferred value. |
| `symbolic_a0_derivation.py` | `output_symbolic_a0_derivation.md` | Records the symbolic and dimensional derivation of $a_0=cH_0/(2\pi)$. |
| `calculate_galactic_a0.py` | `output_calculate_galactic_a0.md` | Evaluates the $a_0$ scale and compares it with a typical MOND scale. |

Classification:

1. `calculate_newton_g.py`: strong phenomenological comparison, not a complete ab initio prediction;
2. `calculate_thermal_axial_g_chain.py`: symbolic-numerical evaluation of a conditional chain;
3. `symbolic_rho_lambda_derivation.py`: symbolic/dimensional verification of the structural chain;
4. `calculate_rho_lambda.py`: direct evaluation of a structural formula conditioned on a cosmological boundary;
5. `symbolic_a0_derivation.py`: symbolic/dimensional verification without experimental input;
6. `calculate_galactic_a0.py`: direct evaluation of a horizon scale and phenomenological comparison.

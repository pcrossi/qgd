---
title: "Scripts — Chapter 5"
---

# Scripts — Chapter 5

These scripts are symbolic verifications or pedagogical illustrations linked to Chapter 5. They do not replace the derivations in the text.

## Scripts

1. `verify_phase_current_1d.py`
   - Classification: current conservation illustration.
   - Shows that zero divergence preserves integrated charge and that boundary flux changes the charge.
   - Output: `output_verify_phase_current_1d.md`.

2. `verify_bohm_fisher_variation.py`
   - Classification: numerical/symbolic variation test.
   - Compares the variational derivative of the Fisher energy with the Bohm operator on a 1D grid.
   - Output: `output_verify_bohm_fisher_variation.md`.

3. `verify_noether_phase_shift.py`
   - Classification: continuous symmetry illustration.
   - Verifies that a density that depends only on $\partial S_R$ is invariant under global phase shift.
   - Output: `output_verify_noether_phase_shift.md`.

4. `verify_canonical_polarization_toy.py`
   - Classification: Routh/Cauchy–Schwarz illustration.
   - Shows that, with fixed charge and normalization, the minimizer satisfies $\Pi=(Q_S/N_\rho)\rho$.
   - Output: `output_verify_canonical_polarization_toy.md`.

5. `verify_parabolic_symbol_qgd.py`
   - Classification: symbolic-numerical verification of strong parabolicity.
   - Illustrates that, after gauge, the principal symbol has the form $\sigma_{\rm pr}(\xi)=|\xi|_g^2I$ in a positive metric.
   - Output: `output_verify_parabolic_symbol_qgd.md`.

## Usage

```bash
python3 verify_phase_current_1d.py
python3 verify_bohm_fisher_variation.py
python3 verify_noether_phase_shift.py
python3 verify_canonical_polarization_toy.py
python3 verify_parabolic_symbol_qgd.py
```

---
title: "Optional scripts — Chapter 6"
---

# Optional scripts — Chapter 6

These scripts are self-contained educational verifications for Chapter 6. They illustrate steps of the global-local bridge, but do not replace the lemmas of the text.

General classification:

- consistency check;
- numerical toy model;
- no tuning to experimental data;
- no modification of the official action.

## Scripts

| Script | Output | Function |
|---|---|---|
| `verify_pointed_limit_torus_sphere.py` | `output_verify_pointed_limit_torus_sphere.md` | Verifies the local flattening of $S^1_R$ and $S^3_R$ as $R\to\infty$. |
| `verify_weighted_measure_transport.py` | `output_verify_weighted_measure_transport.md` | Tests the transport of weighted density with the correct Jacobian. |
| `verify_localization_gap_toy.py` | `output_verify_localization_gap_toy.md` | Shows a localized bound mode preserving the gap as the domain grows. |
| `verify_riesz_resolvent_toy.py` | `output_verify_riesz_resolvent_toy.md` | Compares Riesz projectors in a finite family of operators. |
| `verify_clock_homomorphism.py` | `output_verify_clock_homomorphism.md` | Verifies $\tau_\gamma(t)=\tau_0e^{\kappa t}$ from the causal homomorphism. |

## Usage

Run from the project root:

```bash
python3 manuscript/06_global_local_bridge/scripts/verify_pointed_limit_torus_sphere.py
python3 manuscript/06_global_local_bridge/scripts/verify_weighted_measure_transport.py
python3 manuscript/06_global_local_bridge/scripts/verify_localization_gap_toy.py
python3 manuscript/06_global_local_bridge/scripts/verify_riesz_resolvent_toy.py
python3 manuscript/06_global_local_bridge/scripts/verify_clock_homomorphism.py
```

---
title: "Optional scripts — Chapter 7"
---

# Optional scripts — Chapter 7

Self-contained educational scripts to verify steps of the classical limit.

General classification:

- consistency verification;
- numerical toy model;
- no experimental tuning;
- no modification of the official action.

## Scripts

| Script | Output | Function |
|---|---|---|
| `verify_bohm_epsilon_cl.py` | `output_verify_bohm_epsilon_cl.md` | Confirms the scaling $|Q_B|/T_{\rm cl}\sim\varepsilon_{\rm cl}^2$. |
| `verify_hamilton_newton.py` | `output_verify_hamilton_newton.md` | Verifies Hamilton $\to$ Newton in a harmonic oscillator. |
| `verify_monokinetic_liouville.py` | `output_verify_monokinetic_liouville.md` | Tests norm conservation of an advected density. |
| `verify_cotangent_kepler.py` | `output_verify_cotangent_kepler.md` | Verifies the global cotangent $\to$ local Kepler limit. |
| `verify_classical_noether.py` | `output_verify_classical_noether.md` | Verifies conservation by symmetry in classical toy models. |
| `verify_macroscopic_gravity.py` | `output_verify_macroscopic_gravity.md` | Verifies trace-reversed $\to$ Einstein, the $8\pi$ factor, and geodesic vanishing of antisymmetric torsion. |

## Usage

Run from the project root:

```bash
python3 manuscript/07_classical_limit/scripts/verify_bohm_epsilon_cl.py
python3 manuscript/07_classical_limit/scripts/verify_hamilton_newton.py
python3 manuscript/07_classical_limit/scripts/verify_monokinetic_liouville.py
python3 manuscript/07_classical_limit/scripts/verify_cotangent_kepler.py
python3 manuscript/07_classical_limit/scripts/verify_classical_noether.py
python3 manuscript/07_classical_limit/scripts/verify_macroscopic_gravity.py
```

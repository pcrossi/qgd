---
title: "Scripts — Chapter 9"
---

# Scripts — Chapter 9

The scripts in this directory are reduced and pedagogical verifications. They do not replace the complete Hessian of the official action.

| Script | Goal | Classification |
|---|---|---|
| `verify_born_projectors.py` | Verify positivity, additivity, Born on projectors, basis change, composition, and marginals. | Operational consistency test. |
| `verify_entanglement_no_signalling.py` | Verify non-factorization, singlet correlation, local marginals, and ideal CHSH in the reduced sector. | Reduced operational consistency test. |
| `simulate_decoherence_sae.py` | Show coherence suppression, asymptotic gap, and ideal repeatability. | Effective reduction $S+A+E$. |
| `detector_response_schur.py` | Calculate $\text{R}_{\rm app}$ and $\Gamma_{\rm det}$ in a toy model. | Effective reduction/apparatus. |
| `ohmic_detector_born_capture.py` | Verify ohmic DtN, capture martingale, and Born frequency in a reduced detector. | Consistency test with dimensionless parameters. |

## Usage

Run from the project root:

```bash
python3 manuscript/09_measurement_born_interface/scripts/verify_born_projectors.py
python3 manuscript/09_measurement_born_interface/scripts/verify_entanglement_no_signalling.py
python3 manuscript/09_measurement_born_interface/scripts/simulate_decoherence_sae.py
python3 manuscript/09_measurement_born_interface/scripts/detector_response_schur.py
python3 manuscript/09_measurement_born_interface/scripts/ohmic_detector_born_capture.py
```

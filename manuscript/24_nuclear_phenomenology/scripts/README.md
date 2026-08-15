---
title: "Scripts — Chapter 24"
---

# Scripts — Chapter 24

The scripts in this folder are self-contained verifiers. They do not depend on historical audit files or documents external to the chapter.

## Scripts

| Script | What it verifies | Output |
|---|---|---|
| `reduced_alpha_decay.py` | reduced alpha table, residues, and RMS | `output_reduced_alpha_decay.md` |
| `alpha_pipeline_reduced_schur_riesz.py` | complete reduced alpha channel construction: Schur, Riesz, determinant mobility, rate, and RMS | `output_alpha_pipeline_reduced_schur_riesz.md` |
| `spin_torsion_shells.py` | shell closures by spin--torsion counting | `output_spin_torsion_shells.md` |
| `reduced_klein_nishina.py` | angular factor and Thomson limit | `output_reduced_klein_nishina.md` |
| `total_and_flux_klein_nishina.py` | classical radius, Thomson, angular integration, and total Klein--Nishina cross section | `output_total_and_flux_klein_nishina.md` |
| `reduced_torsional_neutrinos.py` | candidate neutral masses and comparison | `output_reduced_torsional_neutrinos.md` |
| `neutrino_oscillations_sheet_mode.py` | reduced reconstruction of $K^\nu$, sheet--mode mixing, and oscillation probabilities | `output_neutrino_oscillations_sheet_mode.md` |

## Execution

At the project root:

```bash
python3 manuscript/24_nuclear_phenomenology/scripts/reduced_alpha_decay.py
python3 manuscript/24_nuclear_phenomenology/scripts/alpha_pipeline_reduced_schur_riesz.py
python3 manuscript/24_nuclear_phenomenology/scripts/spin_torsion_shells.py
python3 manuscript/24_nuclear_phenomenology/scripts/reduced_klein_nishina.py
python3 manuscript/24_nuclear_phenomenology/scripts/total_and_flux_klein_nishina.py
python3 manuscript/24_nuclear_phenomenology/scripts/reduced_torsional_neutrinos.py
python3 manuscript/24_nuclear_phenomenology/scripts/neutrino_oscillations_sheet_mode.py
```

General classification: reduced verifications and consistency tests. They do not replace the direct metrological evaluation of the complete Hessian.

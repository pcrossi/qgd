#!/usr/bin/env python3
"""
QGD — Chapter 9 / Reduced Detector Response

Objective:
    Calculate an apparatus impedance by Schur complement and evaluate
    the coherence factor exp(-Gamma_det) in a toy model.

Theoretical source:
    manuscript/09_measurement_born_interface/notes/apparatus_as_boundary_hessian_schur.md
    manuscript/09_measurement_born_interface/notes/gdq_construction_of_measurement.md

Classification:
    Effective reduction/apparatus. Not a metrological prediction.

Output:
    manuscript/09_measurement_born_interface/scripts/output_detector_response_schur.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_detector_response_schur.md"

    k_boundary = np.array([[2.0, 0.15], [0.15, 1.5]])
    k_internal = np.array([[4.0, 0.2], [0.2, 3.0]])
    k_coupling = np.array([[0.7, 0.1], [0.05, 0.4]])

    r_app = k_boundary - k_coupling @ np.linalg.inv(k_internal) @ k_coupling.T
    delta_phi = np.array([1.0, -1.0])
    gamma = 0.5 * float(delta_phi @ r_app @ delta_phi)
    coherence = float(np.exp(-gamma))
    eigs = np.linalg.eigvalsh(r_app)

    text = f"""# Output — reduced detector response by Schur

Classification: effective reduction/apparatus.

## Impedance matrix

$$
\\text{{R}}_{{\\rm app}}
=
\\begin{{pmatrix}}
{r_app[0,0]:.12f} & {r_app[0,1]:.12f} \\\\
{r_app[1,0]:.12f} & {r_app[1,1]:.12f}
\\end{{pmatrix}}.
$$

## Verifications

| test | value |
|---|---:|
| minimum eigenvalue of R_app | {eigs.min():.12f} |
| maximum eigenvalue of R_app | {eigs.max():.12f} |
| Gamma_det | {gamma:.12f} |
| C_det = exp(-Gamma_det) | {coherence:.12f} |

Interpretation: the positive detector response reduces the coherence by
$\\mathcal C_{{\\rm det}}=e^{{-\\Gamma_{{\\rm det}}}}$. The numbers are from a toy model.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

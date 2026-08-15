#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `hyperon polarization confinement` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / hyperon polarization.

Evaluates the preserved phenomenological form:

    P = base * chi_over_delta2

with a reduced choice that reproduces the preliminary estimate P≈0.85%.
Classification: preserved phenomenology; not a proof of confinement.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_hyperon_polarization_confinement.md"

    base = 0.005
    chi_over_delta2 = 1.7
    p = base * chi_over_delta2

    text = f"""# Output — hyperon polarization

Classification: preserved phenomenology.

| quantity | value |
|---|---:|
| thermal-vortical base | {base:.12f} |
| chi_Fano/delta^2 | {chi_over_delta2:.12f} |
| P_Lambda | {p:.12f} |
| percent P_Lambda | {100.0*p:.6f}% |

Interpretation: the value preserves the reduced estimate of torsion/vorticity coupling.
It is not used as a proof of confinement.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

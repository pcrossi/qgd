#!/usr/bin/env python3
"""
GDQ — Chapter 11 / Reduced Stern--Gerlach Deflection

Goal:
    Calculate the geometric separation of the two channels in an ideal magnet model.

Theoretical source:
    manuscript/11_stern_gerlach_classical_quantum/notes/force_deflection_sg_reduced_sector.md

Classification:
    Effective reduction/apparatus. Parameters are classical data of the apparatus.

Output:
    scripts/output_simulate_sg_deflection.md
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_simulate_sg_deflection.md"

    mu_B = 9.2740100783e-24
    mass_ag = 1.790e-25
    L = 0.03
    vy = 500.0
    grad_B = 100.0

    dz = mu_B * L**2 * grad_B / (2 * mass_ag * vy**2)
    sep = 2 * dz

    text = f"""# Output — reduced Stern--Gerlach deflection

Classification: effective reduction/apparatus.

Example parameters:

| parameter | value |
|---|---:|
| magnetic moment used | {mu_B:.12e} J/T |
| effective atom mass | {mass_ag:.12e} kg |
| magnet length | {L:.12e} m |
| longitudinal velocity | {vy:.12e} m/s |
| field gradient | {grad_B:.12e} T/m |

Result:

| channel | deflection |
|---|---:|
| + | {dz:.12e} m |
| - | {-dz:.12e} m |
| separation | {sep:.12e} m |

Interpretation: the values are for an idealized apparatus. The formula validates the
fixed-channel reduction; it is not metrology of a real apparatus.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

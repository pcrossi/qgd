#!/usr/bin/env python3
"""
Goal:
    Self-contained record of the `reduced torsional neutrinos` verification associated with chapter `24_nuclear_phenomenology`.
Reduced candidate of neutral masses/inertial scales.

Scientific classification:
    reduced GDQ candidate.

The script does not use observed squared differences as input. It freezes the
scale S_nu=alpha^7 Q_beta^2 and the candidate spectrum
lambda=(0, chi_nu^2/2, 6*pi/5), then compares them with reference values
used in the manuscript to evaluate order of magnitude and relative error.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_reduced_torsional_neutrinos.md"

ALPHA = 1.0 / 137.035999177
Q_BETA_EV = 0.782333559310e6

# Reference values used only for final comparison.
DM21_REF = 7.49e-5
DM31_REF = 2.534e-3


def rel_err(value: float, ref: float) -> float:
    return (value - ref) / ref


def main() -> None:
    chi_nu = (12.0 / 25.0) * math.exp(-ALPHA / 4.0)
    s_nu = ALPHA**7 * Q_BETA_EV**2
    lambdas = [0.0, 0.5 * chi_nu**2, 6.0 * math.pi / 5.0]
    masses = [math.sqrt(s_nu * lam) for lam in lambdas]
    dm21 = s_nu * (lambdas[1] - lambdas[0])
    dm31 = s_nu * (lambdas[2] - lambdas[0])

    theta12 = math.degrees(math.atan(1.0 / math.sqrt(2.0)))
    theta23 = 45.0
    theta13 = math.degrees(math.asin(chi_nu / math.pi))
    delta_cp = math.degrees(3.84)

    lines: list[str] = []
    lines.append("# Output — reduced torsional neutrinos\n\n")
    lines.append("Classification: reduced GDQ candidate.\n\n")
    lines.append("## Inputs frozen before comparison\n\n")
    lines.append(f"- alpha: `{ALPHA:.15e}`\n")
    lines.append(f"- Q_beta: `{Q_BETA_EV:.12e} eV`\n")
    lines.append(f"- S_nu = alpha^7 Q_beta^2: `{s_nu:.12e} eV^2`\n")
    lines.append(f"- chi_nu = (12/25) exp(-alpha/4): `{chi_nu:.12e}`\n\n")

    lines.append("## Candidate eigenvalues\n\n")
    lines.append("| mode | lambda |\n")
    lines.append("|---:|---:|\n")
    for i, lam in enumerate(lambdas, start=1):
        lines.append(f"| {i} | {lam:.12e} |\n")

    lines.append("\n## Candidate masses\n\n")
    lines.append("| mode | mass (eV) |\n")
    lines.append("|---:|---:|\n")
    for i, mass in enumerate(masses, start=1):
        lines.append(f"| {i} | {mass:.12e} |\n")
    lines.append(f"| sum | {sum(masses):.12e} |\n")

    lines.append("\n## Squared differences\n\n")
    lines.append("| quantity | Reduced GDQ | reference | relative error |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| dm21 | {dm21:.12e} | {DM21_REF:.12e} | {rel_err(dm21, DM21_REF):+.6e} |\n")
    lines.append(f"| dm31 | {dm31:.12e} | {DM31_REF:.12e} | {rel_err(dm31, DM31_REF):+.6e} |\n")

    lines.append("\n## Associated raw angles\n\n")
    lines.append("| parameter | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| theta12 | {theta12:.9f} deg |\n")
    lines.append(f"| theta23 | {theta23:.9f} deg |\n")
    lines.append(f"| theta13 | {theta13:.9f} deg |\n")
    lines.append(f"| historical candidate delta_CP | {delta_cp:.9f} deg |\n")

    lines.append("\n## Interpretation\n\n")
    lines.append(
        "The upper mode is very close to the atmospheric oscillation scale; "
        "the solar mode is within a few percent. The calculation is a reduced candidate, "
        "as the eigenvalues must still be obtained from the official neutral Hessian "
        "rather than from the analytical reduced form.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

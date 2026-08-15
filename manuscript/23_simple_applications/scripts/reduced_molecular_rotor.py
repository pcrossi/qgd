#!/usr/bin/env python3
"""Chapter 23 — reduced molecular rotor.

Objective:
    Evaluate the ideal rotational spectrum and the leading centrifugal distortion
    for a reference molecule, using spectroscopic constants as external data.

Classification:
    Phenomenological comparison. B and omega_e are external inputs; absolute
    prediction would require deriving them from the Hessian of the molecular bridge.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).with_name("output_reduced_molecular_rotor.md")


def main() -> None:
    # Carbon monoxide 12C16O, approximate spectroscopic reference values
    # in cm^-1. These enter as external data, not parameters derived here.
    B_cm = 1.931_280_87
    omega_e_cm = 2169.813_58
    D_cm_gdq = 4.0 * B_cm**3 / omega_e_cm**2

    # Typical tabulated value for order of magnitude comparison.
    D_cm_ref = 6.121e-6

    lines = [
        "---",
        'title: "Output — Reduced Molecular Rotor"',
        "---",
        "",
        "# Output — Reduced Molecular Rotor",
        "",
        "- comparison molecule: CO;",
        f"- external $B$ = `{B_cm:.8f}` cm^-1;",
        f"- external $\\omega_e$ = `{omega_e_cm:.8f}` cm^-1;",
        f"- $D_{{\\rm GDQ}}=4B^3/\\omega_e^2$ = `{D_cm_gdq:.12e}` cm^-1;",
        f"- typical reference $D$ = `{D_cm_ref:.12e}` cm^-1;",
        f"- relative error = `{D_cm_gdq/D_cm_ref-1.0:+.12e}`;",
        "- classification: phenomenological comparison.",
        "",
        "| $J$ | $E_J=BJ(J+1)$ [cm^-1] | $E_J$ with distortion [cm^-1] | correction [cm^-1] |",
        "|---:|---:|---:|---:|",
    ]
    for j in range(0, 11):
        x = j * (j + 1)
        rigid = B_cm * x
        corr = D_cm_gdq * x * x
        lines.append(f"| {j} | `{rigid:.12f}` | `{rigid-corr:.12f}` | `{-corr:.12e}` |")

    lines += [
        "",
        "Interpretation: the $J(J+1)$ form comes from the $S^2$ angular domain; the",
        "constant $D$ is close to the spectroscopic order when $B$ and $\\omega_e$ are given.",
        "For a GDQ prediction, these data must come from the molecular Hessian.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
GDQ — Chapter 10 / Cauchy and Hopf residue

Goal:
    Numerically verify that the logarithmic connection of a local spinor
    section s(z)=z^(1/2) has normalized circulation 1/2 around the defect.

Construction:
    Omega_S = (1/2) dz/z. In one turn z(theta)=r exp(i theta),
    dz/z = i dtheta. Thus:

        (1/(2 pi i)) int Omega_S = 1/2.

    The script numerically integrates this expression for different radii. The
    result must not depend on r, as long as the loop does not cross the core.

Classification:
    Symbolic-numerical test of a topological identity. Not a metrological
    prediction.

Output:
    scripts/output_verify_residue_hopf_cauchy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def residue_integral(radius: float, n: int = 200_000) -> complex:
    """Integrates Omega=(1/2) dz/z on the circle |z|=radius."""
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dtheta = 2.0 * np.pi / n
    z = radius * np.exp(1j * theta)
    dz = 1j * z * dtheta
    omega = 0.5 * dz / z
    integral = np.sum(omega)
    return integral / (2.0 * np.pi * 1j)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_residue_hopf_cauchy.md"

    radii = [0.05, 0.1, 0.3, 0.7, 1.0]
    rows = []
    for r in radii:
        val = residue_integral(r)
        rows.append((r, val.real, val.imag, abs(val - 0.5)))

    table = "\n".join(
        f"| {r:.3f} | {re:.12f} | {im:.12e} | {err:.12e} |"
        for r, re, im, err in rows
    )

    text = f"""# Output — verify Hopf/Cauchy residue

Classification: symbolic-numerical test of topological identity.

Integral tested:

$$
\\frac{{1}}{{2\\pi i}}\\oint_{{|z|=r}} \\frac12\\frac{{dz}}{{z}}.
$$

| radius r | Re(integral) | Im(integral) | error to 1/2 |
|---:|---:|---:|---:|
{table}

Interpretation: the normalized circulation is $1/2$ and is independent of the loop radius.
This represents the Hopf spinor half-monodromy around the stoma.
"""
    out.write_text(text, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

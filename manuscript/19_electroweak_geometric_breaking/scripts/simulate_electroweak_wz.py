#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `simulate electroweak wz` verification associated with chapter `19_electroweak_geometric_breaking`.

GDQ — Chapter 19 / W-Z diagnostic.

Calculates effective masses:

    mW = g v / 2
    mZ = v sqrt(g^2+g'^2) / 2

for electroweak transport scenarios discussed in spectral transport.

Classification: reduced diagnostic. Does not use mW or mZ as input.
"""

from __future__ import annotations

from pathlib import Path
import math


def masses(v: float, alpha_inv: float, sin2: float) -> tuple[float, float, float, float]:
    alpha = 1.0 / alpha_inv
    e = math.sqrt(4.0 * math.pi * alpha)
    s = math.sqrt(sin2)
    c = math.sqrt(1.0 - sin2)
    g = e / s
    gp = e / c
    m_w = 0.5 * g * v
    m_z = 0.5 * math.sqrt(g * g + gp * gp) * v
    return g, gp, m_w, m_z


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_simulate_electroweak_wz.md"

    v = 246.111195996
    # Reference values used in previous project diagnostics.
    # They are used only after calculation for comparison; they do not enter
    # the construction of g, g', mW, or mZ.
    m_w_ref = 80.379
    m_z_ref = 91.1876
    ratio_ref = m_w_ref / m_z_ref

    cases = [
        ("geometric point", 137.035999, 3.0 / 8.0),
        ("transport 2/9", 137.035999, 2.0 / 9.0),
        ("EW resolution", 128.0, 3.0 / 8.0),
        ("EW resolution with 2/9", 128.0, 2.0 / 9.0),
    ]

    lines = [
        "# Output — electroweak W/Z diagnostic",
        "",
        "Classification: reduced diagnostic; not a fit to $m_W$ or $m_Z$.",
        "",
        "Scale used: $v={:.12f}\\,\\mathrm{{GeV}}$.".format(v),
        "",
        "| case | alpha_inv | sin2_theta | g | g_prime | m_W GeV | W error | m_Z GeV | Z error | ratio error |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, alpha_inv, sin2 in cases:
        g, gp, mw, mz = masses(v, alpha_inv, sin2)
        ratio = mw / mz
        err_w = (mw - m_w_ref) / m_w_ref
        err_z = (mz - m_z_ref) / m_z_ref
        err_ratio = (ratio - ratio_ref) / ratio_ref
        lines.append(
            f"| {name} | {alpha_inv:.6f} | {sin2:.12f} | {g:.6f} | {gp:.6f} | {mw:.4f} | {err_w:.4%} | {mz:.4f} | {err_z:.4%} | {err_ratio:.4%} |"
        )
    lines += [
        "",
        "References used only for comparison: $m_W={:.6f}\\,\\mathrm{{GeV}}$,".format(m_w_ref),
        "$m_Z={:.6f}\\,\\mathrm{{GeV}}$, and $m_W/m_Z={:.9f}$.".format(m_z_ref, ratio_ref),
        "",
        "Interpretation: $3/8$ is the common geometric point; $2/9$ represents the conditional",
        "global transport path discussed in spectral transport. The comparison shows where",
        "the structural path already approximates the accepted values and where it still requires",
        "global transport/boundary Hessian.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

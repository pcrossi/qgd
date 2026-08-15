#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Reduced Hartman effect

Objective
---------
Numerically verify the reduced formula of proper length saturation in the evanescent channel:

    D_proper(L) = sqrt(g0)/kappa * (1-exp(-kappa*L))

and the effective proper time:

    tau_GDQ(L) = D_proper(L)/v0.

Classification
--------------
Direct evaluation of reduced formula. No experimental target is used.
It is not an evolution of the complete GDQ metric.

Output
-----
output_reduced_hartman_saturation.md
"""

from __future__ import annotations

import math
from pathlib import Path


def d_prop(length: float, kappa: float, g0: float) -> float:
    """Reduced proper distance inside the barrier."""

    return math.sqrt(g0) / kappa * (1.0 - math.exp(-kappa * length))


def tau_gdq(length: float, kappa: float, g0: float, v0: float) -> float:
    """Effective proper time for local physical velocity v0."""

    return d_prop(length, kappa, g0) / v0


def main() -> None:
    out = Path(__file__).with_name("output_reduced_hartman_saturation.md")

    kappa = 1.0
    g0 = 1.0
    v0 = 1.0
    lengths = [0.1, 0.5, 1.0, 2.0, 4.0, 8.0]
    limit = math.sqrt(g0) / kappa
    tau_limit = limit / v0

    lines = [
        "# Output — reduced Hartman in Chapter 12",
        "",
        "Classification: direct evaluation of reduced formula.",
        "",
        "Reduced parameters:",
        "",
        f"- `kappa = {kappa}`",
        f"- `g0 = {g0}`",
        f"- `v0 = {v0}`",
        f"- `D_proper(infinity) = {limit:.12f}`",
        f"- `tau_GDQ(infinity) = {tau_limit:.12f}`",
        "",
        "| length | D_proper(L) | tau_GDQ(L) | fraction of the limit |",
        "|---:|---:|---:|---:|",
    ]

    for length in lengths:
        d = d_prop(length, kappa, g0)
        tau = tau_gdq(length, kappa, g0, v0)
        lines.append(
            f"| {length:.1f} | {d:.12f} | {tau:.12f} | {d/limit:.12f} |"
        )

    lines += [
        "",
        "Interpretation: the proper distance and the effective proper time saturate. The ratio",
        "`L/tau_GDQ(L)` is neither local velocity nor front velocity.",
        "",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

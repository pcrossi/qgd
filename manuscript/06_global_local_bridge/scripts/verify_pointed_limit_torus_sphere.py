#!/usr/bin/env python3
"""
Objective:
    Self-contained verification record of `verify_pointed_limit_torus_sphere` associated with chapter `06_global_local_bridge`.

Educational verification of the pointed limit in Chapter 6.

Model:
- circle of radius R: ds^2 = dx^2 exactly in local arc coordinates;
- sphere S^3_R in radial normal coordinate r:
  ds^2 = dr^2 + R^2 sin(r/R)^2 dOmega_2^2.

In flat space R^3, the angular coefficient is r^2.
The local relative error is:

    E_R(r) = |R^2 sin(r/R)^2 - r^2| / r^2.

For a fixed window 0 < r <= L, E_R = O((L/R)^2).
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_pointed_limit_torus_sphere.md")


def sphere_error(R: float, L: float, samples: int = 1000) -> float:
    max_error = 0.0
    for k in range(1, samples + 1):
        r = L * k / samples
        angular = R * R * math.sin(r / R) ** 2
        flat = r * r
        max_error = max(max_error, abs(angular - flat) / flat)
    return max_error


def main() -> None:
    L = 1.0
    radii = [5, 10, 20, 50, 100, 200]
    rows = []
    for R in radii:
        err = sphere_error(R, L)
        scaled = err * R * R / (L * L)
        rows.append((R, err, scaled))

    lines = [
        "---",
        'title: "Output — pointed limit torus/sphere"',
        "---",
        "",
        "# Output — pointed limit torus/sphere",
        "",
        "Classification: consistency verification / geometric toy model.",
        "",
        "Fixed local window: $0<r\\le 1$.",
        "",
        "| $R$ | maximum angular error in $S^3_R$ | rescaled error $E_R R^2$ |",
        "|---:|---:|---:|",
    ]
    for R, err, scaled in rows:
        lines.append(f"| {R} | {err:.12e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusion: the local error decays as $O(R^{-2})$, compatible with the",
        "pointed convergence used in Chapter 6.",
        "",
        "Note: the large circle $S^1_R$ in local arc coordinates already has a",
        "local flat metric; the global non-triviality vanishes only in the",
        "pointed limit, not by global identification.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verifies the homogeneous Hessian of the radius of the GDQ cylindrical shrinker."""

from __future__ import annotations

import argparse
import math
from pathlib import Path


def w_homogeneous(radius: float, tau: float) -> float:
    return (
        6.0 * tau / radius**2
        + 3.0 * math.log(radius / (2.0 * math.sqrt(tau)))
        + 0.5 * math.log(math.pi)
        - 3.0
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "output_verify_sg_cylindrical_radius_stability.md"
        ),
    )
    args = parser.parse_args()
    tau = args.tau
    radius = 2.0 * math.sqrt(tau)
    derivative = -12.0 * tau / radius**3 + 3.0 / radius
    hessian = 36.0 * tau / radius**4 - 3.0 / radius**2
    step = 1e-4 * radius
    finite_hessian = (
        w_homogeneous(radius + step, tau)
        - 2.0 * w_homogeneous(radius, tau)
        + w_homogeneous(radius - step, tau)
    ) / step**2
    lines = [
        "# Output — homogeneous stability of the cylindrical radius",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| $a_*$ | {radius:.12e} |",
        f"| $W(a_*)$ | {w_homogeneous(radius, tau):.12e} |",
        f"| $W'(a_*)$ | {derivative:.12e} |",
        f"| analytical $W''$ | {hessian:.12e} |",
        f"| finite difference $W''$ | {finite_hessian:.12e} |",
        "",
        f"- stable homogeneous mode: `{hessian > 0}`",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

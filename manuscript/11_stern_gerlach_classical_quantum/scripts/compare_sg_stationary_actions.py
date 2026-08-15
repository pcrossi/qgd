#!/usr/bin/env python3
"""Compares on-shell W of the outer Gaussian and cylindrical branches."""

from __future__ import annotations

import argparse
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_compare_sg_stationary_actions.md"),
    )
    args = parser.parse_args()
    x_c = 1.5
    q2 = math.exp(-x_c) * (1.0 + x_c)
    f0_gaussian = math.log(q2)
    mean_x = (x_c**2 + 2.0 * x_c + 2.0) / (x_c + 1.0)
    bulk_gaussian = 2.0 * mean_x + f0_gaussian - 4.0
    boundary_gaussian = -3.0 * x_c / (1.0 + x_c)
    total_gaussian = bulk_gaussian + boundary_gaussian
    total_cylinder = 0.5 * math.log(math.pi) - 1.5
    difference = total_cylinder - total_gaussian
    lines = [
        "# Output — comparison of stationary actions",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| $W_G$ bulk | {bulk_gaussian:.12e} |",
        f"| $W_G$ boundary | {boundary_gaussian:.12e} |",
        f"| $W_G$ total | {total_gaussian:.12e} |",
        f"| $W_{{\\rm cylinder}}$ | {total_cylinder:.12e} |",
        f"| $W_{{\\rm cylinder}}-W_G$ | {difference:.12e} |",
        "",
        f"- cylinder has lower $W$: `{difference < 0}`",
        "",
        "Classification: reduced comparison of stationary branches; it is not final metrology",
        "of a real apparatus.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

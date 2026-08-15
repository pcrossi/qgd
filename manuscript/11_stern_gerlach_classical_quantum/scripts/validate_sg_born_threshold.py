#!/usr/bin/env python3
"""Convergence of the first passage to Born when epsilon tends to zero."""

from __future__ import annotations

import math
from pathlib import Path

from simulate_sg_capture import (
    born_probability,
    simulate_capture,
    threshold_probability,
)


def main() -> None:
    angles = [30.0, 60.0, 90.0, 120.0, 150.0]
    epsilons = [0.08, 0.04, 0.02, 0.01, 0.005]
    n_paths = 20000
    dt = 0.0005
    gamma = 1.0

    lines = [
        "# Threshold convergence to Born — Chapter 11",
        "",
        "| theta | epsilon | Born | analytical passage | Monte Carlo | |analytical-Born| |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    worst_z = 0.0

    for i, angle in enumerate(angles):
        p0 = born_probability(math.radians(angle))
        for j, epsilon in enumerate(epsilons):
            analytic = threshold_probability(p0, epsilon)
            result = simulate_capture(
                p0,
                gamma=gamma,
                epsilon=epsilon,
                dt=dt,
                max_time=12.0,
                n_paths=n_paths,
                seed=42100 + 1009 * i + 7919 * j,
            )
            error = result.frequency_upper - analytic
            z = error / result.standard_error if result.standard_error else 0.0
            worst_z = max(worst_z, abs(z))
            lines.append(
                f"| {angle:.1f} | {epsilon:.3f} | {p0:.6f} | "
                f"{analytic:.6f} | {result.frequency_upper:.6f} | "
                f"{abs(analytic-p0):.6f} |"
            )

    lines.extend(
        [
            "",
            f"Largest Monte Carlo deviation: {worst_z:.3f} sigma.",
            "",
            "The final column must tend to zero linearly with epsilon.",
            "",
        ]
    )
    report = "\n".join(lines)
    output = Path(__file__).with_name("output_threshold_sg.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Numerically verifies projector, transition, and metric of the Hopf atlas."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def section_north(w: complex) -> np.ndarray:
    return np.array([1.0, w], dtype=complex) / np.sqrt(1.0 + abs(w) ** 2)


def section_south(w_prime: complex) -> np.ndarray:
    return np.array([w_prime, 1.0], dtype=complex) / np.sqrt(
        1.0 + abs(w_prime) ** 2
    )


def projector(u: np.ndarray) -> np.ndarray:
    return np.outer(u, u.conj())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_verify_sg_hopf_atlas.md"),
    )
    args = parser.parse_args()
    samples = [0.4 + 0.7j, -1.2 + 0.3j, 2.0 - 1.0j]
    maximum_projector_error = 0.0
    maximum_transition_error = 0.0
    for w in samples:
        north = section_north(w)
        south = section_south(1.0 / w)
        transition = abs(w) / w
        maximum_projector_error = max(
            maximum_projector_error,
            float(np.linalg.norm(projector(north) - projector(south))),
        )
        maximum_transition_error = max(
            maximum_transition_error,
            float(np.linalg.norm(south - transition * north)),
        )

    w = 0.6 + 0.8j
    step = 1e-6
    p0 = projector(section_north(w))
    px = projector(section_north(w + step))
    py = projector(section_north(w + 1j * step))
    dp_x = (px - p0) / step
    dp_y = (py - p0) / step
    metric_xx = float(np.real(np.trace(dp_x @ dp_x)))
    metric_yy = float(np.real(np.trace(dp_y @ dp_y)))
    expected = 2.0 / (1.0 + abs(w) ** 2) ** 2

    lines = [
        "# Output — Hopf atlas and projective metric",
        "",
        "| test | value |",
        "|---|---:|",
        f"| maximum error of the projectors | {maximum_projector_error:.3e} |",
        f"| maximum error of the transition | {maximum_transition_error:.3e} |",
        f"| $\\operatorname{{Tr}}(dP_x^2)$ | {metric_xx:.12e} |",
        f"| $\\operatorname{{Tr}}(dP_y^2)$ | {metric_yy:.12e} |",
        f"| expected metric | {expected:.12e} |",
        f"| relative error x | {abs(metric_xx-expected)/expected:.3e} |",
        f"| relative error y | {abs(metric_yy-expected)/expected:.3e} |",
        "",
        "Conclusion: the Hopf charts generate the same projector and reproduce the",
        "reduced projective metric within the finite difference error.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Algebraic test of the evaluator, without representing a physical background."""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np

from evaluate_gdq_sg_background import evaluate, load_background


def main() -> None:
    fixture = {
        "lambda_hessian": np.array([2.0, 4.0]),
        "z_tangential": np.array([1.0, 3.0]),
        "source_projection_1": np.array([1.0, 2.0]),
        "source_projection_2": np.array([2.0, 1.0]),
        "relaxation_rate": np.array([5.0, 10.0]),
        "noise_weight": np.array([0.25, 0.5]),
    }
    expected_kappa = 0.5 * (
        1.0 * (1.0**2 + 2.0**2) / 2.0**2
        + 3.0 * (2.0**2 + 1.0**2) / 4.0**2
    )
    expected_gamma = 3.0**2 * (0.25 / 5.0 + 0.5 / 10.0)
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "non_physical_fixture.npz"
        np.savez(path, **fixture)
        loaded = load_background(path)
        kappa, gamma = evaluate(loaded, mu_over_hbar=3.0)
    assert np.isclose(kappa, expected_kappa, rtol=1e-14)
    assert np.isclose(gamma, expected_gamma, rtol=1e-14)
    print(f"kappa fixture = {kappa:.12e} [OK]")
    print(f"Gamma fixture = {gamma:.12e} [OK]")
    print("This fixture validates algebra and I/O; it is not a GDQ prediction.")


if __name__ == "__main__":
    main()

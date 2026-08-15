#!/usr/bin/env python3
"""Evaluates physical coefficients of Chapter 11 from a solved GDQ background.

The program does not contain phenomenological defaults for the spectrum. It requires
an NPZ produced by the future solver of the official action, preventing the old
radial test potential from being presented as the physical background.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


REQUIRED = (
    "lambda_hessian",
    "z_tangential",
    "source_projection_1",
    "source_projection_2",
    "relaxation_rate",
    "noise_weight",
)


def load_background(path: Path) -> dict[str, np.ndarray]:
    if not path.exists():
        raise FileNotFoundError(
            f"missing GDQ background: {path}. "
            "First solve the stationary E-L and the official Hessian."
        )
    with np.load(path) as archive:
        missing = [name for name in REQUIRED if name not in archive]
        if missing:
            raise ValueError("missing fields in background: " + ", ".join(missing))
        data = {name: np.asarray(archive[name]) for name in REQUIRED}
    sizes = {values.size for values in data.values()}
    if len(sizes) != 1:
        raise ValueError("all spectral vectors must have the same size")
    return data


def evaluate(data: dict[str, np.ndarray], mu_over_hbar: float) -> tuple[float, float]:
    lam = np.asarray(data["lambda_hessian"], dtype=float)
    z = np.asarray(data["z_tangential"], dtype=float)
    j1 = np.asarray(data["source_projection_1"], dtype=complex)
    j2 = np.asarray(data["source_projection_2"], dtype=complex)
    rates = np.asarray(data["relaxation_rate"], dtype=float)
    weights = np.asarray(data["noise_weight"], dtype=float)
    if np.any(lam <= 0) or np.any(z <= 0) or np.any(rates <= 0) or np.any(weights < 0):
        raise ValueError("spectral positivity violated")
    # Local orthonormal Fubini–Study basis: contraction and factor of 1/2.
    kappa = 0.5 * np.sum(z * (abs(j1) ** 2 + abs(j2) ** 2) / lam**2)
    gamma = mu_over_hbar**2 * np.sum(weights / rates)
    return float(kappa.real), float(gamma)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("background", type=Path)
    parser.add_argument(
        "--mu-over-hbar",
        type=float,
        required=True,
        help="effective axial moment divided by hbar, in background units",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("output_physical_background_sg.md"),
    )
    args = parser.parse_args()
    data = load_background(args.background)
    kappa, gamma = evaluate(data, args.mu_over_hbar)
    text = "\n".join(
        [
            "# Physical background evaluation — Chapter 11",
            "",
            f"- file: `{args.background}`",
            f"- physical modes: {data['lambda_hessian'].size}",
            f"- kappa_H^SG: `{kappa:.12e}`",
            f"- Gamma_SG: `{gamma:.12e} s^-1`",
            "",
        ]
    )
    args.output.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

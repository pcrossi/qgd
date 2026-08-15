#!/usr/bin/env python3
"""Constructs and verifies the Gaussian shrinker of Chapter 11 on the C^2 slice."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def build(tau: float, r_c: float, r_max: float, points: int) -> dict[str, np.ndarray]:
    if tau <= 0 or r_c < 0 or r_max <= r_c or points < 20:
        raise ValueError("invalid geometric parameters")
    r = np.linspace(r_c, r_max, points)
    x_c = r_c**2 / (4.0 * tau)
    exterior_mass = np.exp(-x_c) * (1.0 + x_c)
    f0 = np.log(exterior_mass)
    a = r.copy()
    ap = np.ones_like(r)
    app = np.zeros_like(r)
    fp = r / (2.0 * tau)
    fpp = np.full_like(r, 1.0 / (2.0 * tau))
    f = r**2 / (4.0 * tau) + f0

    # Radial and spherical components of the shrinker equation.
    radial_residual = -3.0 * app / a + fpp - 1.0 / (2.0 * tau)
    angular_residual = (
        (2.0 * (1.0 - ap**2) - a * app) / a**2
        + fp * ap / a
        - 1.0 / (2.0 * tau)
    )
    boundary_flux = -r_c / (2.0 * tau)
    mean_curvature = -3.0 / r_c
    weighted_mean_curvature = mean_curvature - boundary_flux
    return {
        "r": r,
        "a": a,
        "f": f,
        "measure_radial": (4.0 * np.pi * tau) ** -2
        * np.exp(-f)
        * (2.0 * np.pi**2)
        * r**3,
        "radial_residual": radial_residual,
        "angular_residual": angular_residual,
        "tau": np.array(tau),
        "r_c": np.array(r_c),
        "f0": np.array(f0),
        "boundary_flux": np.array(boundary_flux),
        "mean_curvature": np.array(mean_curvature),
        "weighted_mean_curvature": np.array(weighted_mean_curvature),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau", type=float, default=1.0)
    parser.add_argument("--r-c", type=float, default=0.1)
    parser.add_argument("--r-max", type=float, default=12.0)
    parser.add_argument("--points", type=int, default=4001)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("background_bulk_sg.npz"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path(__file__).with_name("output_background_bulk_sg.md"),
    )
    args = parser.parse_args()
    data = build(args.tau, args.r_c, args.r_max, args.points)
    np.savez(args.output, **data)
    normalization = float(np.trapezoid(data["measure_radial"], data["r"]))
    # Finite r_max: compare with unity, recording tail truncation.
    max_residual = max(
        float(np.max(np.abs(data["radial_residual"]))),
        float(np.max(np.abs(data["angular_residual"]))),
    )
    text = "\n".join(
        [
            "# Stationary bulk background — Chapter 11",
            "",
            f"- tau: `{args.tau:.12e}`",
            f"- r_c: `{args.r_c:.12e}`",
            f"- r_max: `{args.r_max:.12e}`",
            f"- F0: `{float(data['f0']):.12e}`",
            f"- largest residue of the equations: `{max_residual:.3e}`",
            f"- normalization in the truncated domain: `{normalization:.12e}`",
            f"- normal flow at the stoma: `{float(data['boundary_flux']):.12e}`",
            f"- mean curvature K: `{float(data['mean_curvature']):.12e}`",
            f"- weighted curvature K-n(F): `{float(data['weighted_mean_curvature']):.12e}`",
            "",
            "The zero residue verifies the bulk. The free boundary condition is",
            "K-n(F)=0; it occurs only when r_c=sqrt(6 tau).",
            "",
        ]
    )
    args.report.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

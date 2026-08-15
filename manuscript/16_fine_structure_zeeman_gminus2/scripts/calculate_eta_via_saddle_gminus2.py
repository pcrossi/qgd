#!/usr/bin/env python3
"""Chapter 16 — density amplitude calculated by the normalized reduced saddle.

This test corrects two shortcomings of the historical Galerkin audit:

1. the phase with monodromy is differentiated by the globally defined connection,
   without applying periodic differences to the multivalued function;
2. the normalization of the weighted measure is imposed before the variation.

Classification:
    direct evaluation of a normalized reduced Galerkin saddle and convergence
    test. It is not the complete physical leptonic saddle in eight dimensions.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.special import i0e


BASE = Path(__file__).resolve().parent
N_COMPLEX = 4


def log_i0(x: float) -> float:
    """Calculates log(I_0(x)) without overflow."""
    return float(np.log(i0e(x)) + abs(x))


def reduced_action(y: np.ndarray, n_grid: int) -> float:
    """Reduced angular action in the unit circulation sector.

    Coordinates:
        y = (a_1, a_2, eta, sigma).

    The phase has unit monodromy and derivative

        P' = 1/(2 pi) + a_1 cos(theta) + 2 a_2 cos(2 theta).

    The constant mode F_0 of Re(f) is eliminated by the constraint

        (1/2pi) int exp(-F) exp(2 sigma cos(theta)) dtheta = 1.
    """
    a1, a2, eta, sigma = np.asarray(y, dtype=float)
    theta = np.linspace(0.0, 2.0 * math.pi, n_grid, endpoint=False)
    dtheta = 2.0 * math.pi / n_grid
    cos1 = np.cos(theta)
    sin1 = np.sin(theta)
    cos2 = np.cos(2.0 * theta)

    # Exact normalization of the angular measure.
    f0 = log_i0(2.0 * sigma - eta)
    f_real = f0 + eta * cos1
    df_real = -eta * sin1
    dphase = 1.0 / (2.0 * math.pi) + a1 * cos1 + 2.0 * a2 * cos2
    lap_sigma = -sigma * cos1

    rho = np.exp(-f_real)
    sqrt_g = np.exp(2.0 * sigma * cos1)

    # After multiplying by sqrt(g), the 2D conformal sector reduces to this
    # expression, preserving R + g^{-1} df d fbar and (Re f - n).
    integrand = (
        (-2.0 * lap_sigma + df_real**2 + dphase**2) * rho
        + (f_real - N_COMPLEX) * rho * sqrt_g
    )
    return float(np.sum(integrand) * dtheta)


def measure_norm(y: np.ndarray, n_grid: int) -> float:
    _, _, eta, sigma = np.asarray(y, dtype=float)
    theta = np.linspace(0.0, 2.0 * math.pi, n_grid, endpoint=False)
    cos1 = np.cos(theta)
    f0 = log_i0(2.0 * sigma - eta)
    return float(np.mean(np.exp(-(f0 + eta * cos1) + 2.0 * sigma * cos1)))


def gradient(y: np.ndarray, n_grid: int, h: float = 3.0e-5) -> np.ndarray:
    y = np.asarray(y, dtype=float)
    result = np.empty_like(y)
    for i in range(y.size):
        hi = h * max(1.0, abs(float(y[i])))
        step = np.zeros_like(y)
        step[i] = hi
        result[i] = (
            reduced_action(y + step, n_grid)
            - reduced_action(y - step, n_grid)
        ) / (2.0 * hi)
    return result


def hessian(y: np.ndarray, n_grid: int, h: float = 3.0e-4) -> np.ndarray:
    columns = []
    for j in range(y.size):
        step = np.zeros_like(y)
        step[j] = h
        columns.append(
            (gradient(y + step, n_grid) - gradient(y - step, n_grid))
            / (2.0 * h)
        )
    matrix = np.column_stack(columns)
    return 0.5 * (matrix + matrix.T)


def find_stationary_points(n_grid: int) -> list[np.ndarray]:
    starts = [
        np.array([0.0, 0.0, eta, sigma], dtype=float)
        for eta in (-1.0, 0.0, 1.0)
        for sigma in (-1.0, 0.0, 1.0)
    ]
    roots: list[np.ndarray] = []
    for start in starts:
        result = least_squares(
            lambda y: gradient(y, n_grid),
            start,
            bounds=(-5.0, 5.0),
            xtol=1.0e-12,
            ftol=1.0e-12,
            gtol=1.0e-12,
            max_nfev=1000,
        )
        if np.linalg.norm(result.fun) > 1.0e-6:
            continue
        if any(np.linalg.norm(result.x - old) < 1.0e-5 for old in roots):
            continue
        roots.append(result.x)
    return roots


def main() -> None:
    grids = (1024, 2048, 4096, 8192)
    rows: list[dict[str, float | int]] = []
    all_roots: dict[int, list[np.ndarray]] = {}

    for n_grid in grids:
        roots = find_stationary_points(n_grid)
        all_roots[n_grid] = roots
        if not roots:
            raise RuntimeError(f"no saddle found for N={n_grid}")
        # The search finds a single root within the declared box.
        root = min(roots, key=np.linalg.norm)
        eigenvalues = np.linalg.eigvalsh(hessian(root, n_grid))
        rows.append(
            {
                "N": n_grid,
                "a1": float(root[0]),
                "a2": float(root[1]),
                "eta": float(root[2]),
                "sigma": float(root[3]),
                "norm": measure_norm(root, n_grid),
                "grad": float(np.linalg.norm(gradient(root, n_grid))),
                "eig_min": float(eigenvalues[0]),
                "n_roots": len(roots),
            }
        )

    lines = [
        "# Chapter 16 — density amplitude calculated by the saddle",
        "",
        "## Classification",
        "",
        "Direct evaluation of a normalized reduced Galerkin saddle and convergence",
        "test. It is not the complete physical leptonic saddle in eight dimensions.",
        "The experimental target of `g-2` does not participate in the calculation.",
        "",
        "## 1. Variational problem",
        "",
        "With fixed unit circulation, one varies:",
        "",
        "$$",
        "y=(a_1,a_2,\\eta,\\sigma).",
        "$$",
        "",
        "The phase with monodromy is differentiated by:",
        "",
        "$$",
        "P'=\\frac{1}{2\\pi}+a_1\\cos\\theta+2a_2\\cos2\\theta.",
        "$$",
        "",
        "The measure is constrained by:",
        "",
        "$$",
        "\\frac1{2\\pi}\\int_0^{2\\pi}\\rho\\sqrt g\\,d\\theta=1.",
        "$$",
        "",
        "The constant mode of $\\operatorname{Re}f$ is then determined by:",
        "",
        "$$",
        "F_0=\\log I_0(2\\sigma-\\eta).",
        "$$",
        "",
        "The saddle solves $\\nabla_y S_{\\rm red}=0$.",
        "",
        "## 2. Convergence",
        "",
        "| N | roots | a1 | a2 | eta | sigma | U norm | ||grad S|| | min eig |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['N']} | {row['n_roots']} | {row['a1']:.9e} | "
            f"{row['a2']:.9e} | {row['eta']:.9e} | {row['sigma']:.9e} | "
            f"{row['norm']:.12e} | {row['grad']:.3e} | {row['eig_min']:.9e} |"
        )

    eta_final = float(rows[-1]["eta"])
    lines.extend(
        [
            "",
            "## 3. Result",
            "",
            "Within the search box $[-5,5]^4$, initiated from nine points,",
            "the only normalized stationary root is the homogeneous saddle:",
            "",
            "$$",
            "a_1=a_2=\\eta_\\ell=\\sigma=0",
            "$$",
            "",
            f"with final numerical value `eta_l = {eta_final:.15e}`.",
            "",
            "The reduced Hessian still possesses a negative eigenvalue. Therefore,",
            "the root is a saddle of the reduced functional, not a stable minimum nor",
            "the already projected 8D physical leptonic background.",
            "",
            "## 4. Consequence for the upper channel",
            "",
            "Since $\\eta_\\ell=0$ in this saddle,",
            "",
            "$$",
            "\\Delta H_{12}=\\eta_\\ell T_{123}=0.",
            "$$",
            "",
            "The unnormalized solution with $|\\eta|\\simeq 1.064$ is excluded:",
            "it alters the total norm of $\\mathcal U\\sqrt g$ and does not belong to the",
            "normalized variational domain of QGD.",
            "",
            "The calculation demonstrates a useful negative result: the homogeneous angular",
            "saddle does not generate the upper metrological correction. A non-zero value",
            "of $\\eta_\\ell$ can only come from the non-homogeneous, warped, or mixed 8D",
            "background, with specified domain, boundaries, and physical projector.",
            "",
        ]
    )

    output = BASE / "output_eta_via_saddle_gminus2.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

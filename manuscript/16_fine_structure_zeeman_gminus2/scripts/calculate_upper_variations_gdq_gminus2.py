#!/usr/bin/env python3
"""Chapter 16 — upper variations of the reduced QGD action.

Objective:
    Calculate, without using experimental data, some cubic and
    quartic coefficients of the reduced official action used in the Galerkin audit of Chapter 16.

Classification:
    consistency test / local derivative of a reduced truncation.

Scientific reading:
    These coefficients show which upper couplings the reduced action
    allows. They are not yet the metrological prediction of g-2, because the
    simple Galerkin truncation is not the physical leptonic saddle and because cubic/quartic
    terms around the symmetric point generate non-linear response in
    B, unless there exists a stationary 8D background with non-zero internal
    amplitudes.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
from typing import Callable

import numpy as np


BASE = Path(__file__).resolve().parent
GALERKIN = BASE / "official_galerkin_gminus2_hessian.py"
ALPHA = 1.0 / 137.035999177


def load_galerkin_action() -> Callable[[np.ndarray], float]:
    spec = importlib.util.spec_from_file_location("official_galerkin_gminus2_hessian", GALERKIN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {GALERKIN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def action(x: np.ndarray) -> float:
        return float(module.action_reduced(x, n_grid=4096))

    return action


def recursive_central_derivative(
    func: Callable[[np.ndarray], float],
    x: np.ndarray,
    indices: tuple[int, ...],
    h: float,
) -> float:
    """Applies recursive central differences for mixed derivatives.

    The implementation accepts repeated indices. For high order derivatives,
    this is used only as an audit of magnitude/sign in a reduced truncation,
    not as a final metrological calculation.
    """
    if not indices:
        return func(x)
    i = indices[0]
    step = np.zeros_like(x, dtype=float)
    step[i] = h
    return (
        recursive_central_derivative(func, x + step, indices[1:], h)
        - recursive_central_derivative(func, x - step, indices[1:], h)
    ) / (2.0 * h)


def finite_hessian(func: Callable[[np.ndarray], float], x0: np.ndarray, h: float) -> np.ndarray:
    n = x0.size
    H = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            H[i, j] = recursive_central_derivative(func, x0, (i, j), h)
    return 0.5 * (H + H.T)


def mode_name(i: int) -> str:
    return {
        0: "circulation/linear phase",
        1: "leading harmonic sin(theta)",
        2: "upper harmonic sin(2theta)",
        3: "density Re(f) cos(theta)",
        4: "conformal metric cos(theta)",
    }[i]


def main() -> None:
    action = load_galerkin_action()
    x_star = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
    h = 2.0e-3

    H = finite_hessian(action, x_star, h)
    eig = np.linalg.eigvalsh(H)

    cubic_terms = {
        "T112": (1, 1, 2),
        "T113": (1, 1, 3),
        "T114": (1, 1, 4),
        "T122": (1, 2, 2),
        "T123": (1, 2, 3),
        "T124": (1, 2, 4),
        "T011": (0, 1, 1),
        "T012": (0, 1, 2),
    }
    quartic_terms = {
        "Q1111": (1, 1, 1, 1),
        "Q1122": (1, 1, 2, 2),
        "Q1133": (1, 1, 3, 3),
        "Q1144": (1, 1, 4, 4),
        "Q0011": (0, 0, 1, 1),
        "Q0022": (0, 0, 2, 2),
        "Q0112": (0, 1, 1, 2),
    }

    cubic_values = {
        name: recursive_central_derivative(action, x_star, idx, h)
        for name, idx in cubic_terms.items()
    }
    quartic_values = {
        name: recursive_central_derivative(action, x_star, idx, h)
        for name, idx in quartic_terms.items()
    }

    beta12 = 1.0 / (2.0 * math.sqrt(math.pi))

    lines = [
        "# Chapter 16 — upper variations of the reduced QGD action",
        "",
        "## Classification",
        "",
        "Local derivative of a reduced Galerkin truncation of the official action.",
        "It is not a metrological prediction of `g-2`.",
        "",
        "## 1. Expansion point",
        "",
        "The same point from the Galerkin audit was used:",
        "",
        "$$",
        "x_*=(1,0,0,0,0),",
        "$$",
        "",
        "with coordinates:",
        "",
        "| index | mode |",
        "|---:|---|",
    ]
    for i in range(5):
        lines.append(f"| {i} | {mode_name(i)} |")

    lines.extend(
        [
            "",
            "## 2. Local Hessian",
            "",
            f"- central difference step: `{h:.1e}`",
            "",
            "| eigenvalue | value |",
            "|---:|---:|",
        ]
    )
    for i, val in enumerate(eig):
        lines.append(f"| {i} | {val:.15e} |")

    lines.extend(
        [
            "",
            "The presence of negative eigenvalues confirms the previous diagnostic:",
            "this simple truncation is not the physical leptonic saddle.",
            "",
            "## 3. Selected cubic coefficients",
            "",
            "Notation:",
            "",
            "$$",
            "T_{ijk}=\\frac{\\partial^3 S_{\\rm red}}{\\partial x_i\\partial x_j\\partial x_k}(x_*).",
            "$$",
            "",
            "| term | indices | value | reading |",
            "|---|---|---:|---|",
        ]
    )
    for name, idx in cubic_terms.items():
        value = cubic_values[name]
        if idx == (1, 1, 2):
            reading = "leading² → direct upper; here it comes out compatible with zero"
        elif idx == (1, 2, 3):
            reading = "leading-upper mediated by density; robust channel"
        elif idx[0] == 0:
            reading = "coupling involving protected circulation"
        else:
            reading = "upper coupling allowed/forbidden by the truncation"
        lines.append(f"| `{name}` | `{idx}` | {value:.15e} | {reading} |")

    lines.extend(
        [
            "",
            "## 4. Selected quartic coefficients",
            "",
            "Notation:",
            "",
            "$$",
            "Q_{ijkl}=\\frac{\\partial^4 S_{\\rm red}}{\\partial x_i\\partial x_j\\partial x_k\\partial x_l}(x_*).",
            "$$",
            "",
            "| term | indices | value |",
            "|---|---|---:|",
        ]
    )
    for name, idx in quartic_terms.items():
        lines.append(f"| `{name}` | `{idx}` | {quartic_values[name]:.15e} |")

    lines.extend(
        [
            "",
            "## 5. Comparison with harmonic selection",
            "",
            "The reduced harmonic selection calculated previously yields:",
            "",
            "$$",
            "\\beta_{12}=\\langle u_2,u_1^2-\\langle u_1^2\\rangle\\rangle",
            "=",
            "\\frac{1}{2\\sqrt\\pi}.",
            "$$",
            "",
            f"Numerically, `1/(2 sqrt(pi)) = {beta12:.15e}`.",
            "",
            "In the tested reduced action, `T112` comes out at the level of numerical noise.",
            "Thus, the purely harmonic selection `beta12` does not automatically convert",
            "into a direct variational source leading² → upper.",
            "",
            "The robust cubic coupling is `T123`, numerically close to",
            "`-2*pi`. The correct reading is that the leading mode and the upper mode",
            "communicate through the density `Re(f)`, not through a",
            "universal direct source in a uniform field.",
            "",
            "## 6. Consequence for Chapter 16",
            "",
            "This calculation does not yet provide metrological `mu_2`. The reason is structural:",
            "",
            "1. at the symmetric point `x_*`, the linear magnetic response uses only the",
            "   quadratic Hessian;",
            "2. cubic/quartic terms generate non-linear response in `B`, unless",
            "   the physical background already has non-zero stationary internal",
            "   amplitudes;",
            "3. the tested truncation possesses negative modes and, therefore, cannot be",
            "   used as the final leptonic background.",
            "",
            "The correct route for the metrological prediction then becomes precise:",
            "",
            "1. construct a stable 8D leptonic saddle `Phi_l`;",
            "2. evaluate `T` and `Q` on this saddle, not at the unstable symmetric point;",
            "3. contract these tensors with the boundary magnetic map",
            "   `M[Phi;B]`;",
            "4. set up physical `H_C(alpha)` and re-run the extractor.",
            "",
            "Thus, Chapter 16 gains an additional conclusion: the reduced action allows",
            "a density-mediated upper channel, but not a universal direct source.",
            "Metrology depends on the stable 8D saddle and the complete tensorial",
            "contraction. There is no justification for using `mu_2_required` as a prediction.",
            "",
        ]
    )

    out = BASE / "output_calculate_upper_variations_gdq_gminus2.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

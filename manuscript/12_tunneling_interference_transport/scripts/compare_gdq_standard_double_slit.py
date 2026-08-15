#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Reduced comparison with the operational standard

Objective
---------
Compare three curves in the Madelung sector on a fixed background:

1. usual coherent limit: two Gaussians with full cross-term;
2. usual incoherent limit: I1+I2 mixture;
3. reduced GDQ: cross-term damped by exp(-Gamma_det), with Gamma_det
   derived from the DtN/Schur impedance of the detector.

Classification
--------------
Phenomenological/controlled comparison. It is not a complete evolution of the GDQ metric.

Outputs
-------
- comparacao_gdq_padrao_dupla_fenda.png
- comparison_gdq_standard_double_slit.md
"""

from __future__ import annotations

import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-gdq")

import matplotlib.pyplot as plt
import numpy as np


def coth(x: float) -> float:
    return math.cosh(x) / math.sinh(x)


def dtn_massive_interval(lambda_det: float, length: float) -> float:
    return lambda_det * coth(lambda_det * length)


def detector_gamma(
    zeta_det: float,
    lambda_det: float,
    length: float,
    c_path: float = 1.0,
) -> float:
    return 0.5 * zeta_det**2 * c_path * dtn_massive_interval(lambda_det, length)


def two_path_fields(
    x: np.ndarray,
    y: float,
    *,
    mass: float,
    velocity: float,
    hbar: float,
    slit_distance: float,
    sigma0: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    y_rayleigh = 2.0 * mass * velocity * sigma0**2 / hbar
    sigma_t = sigma0 * np.sqrt(1.0 + (y / y_rayleigh) ** 2)
    i1 = (
        1.0
        / np.sqrt(2.0 * np.pi * sigma_t**2)
        * np.exp(-((x + slit_distance / 2.0) ** 2) / (2.0 * sigma_t**2))
    )
    i2 = (
        1.0
        / np.sqrt(2.0 * np.pi * sigma_t**2)
        * np.exp(-((x - slit_distance / 2.0) ** 2) / (2.0 * sigma_t**2))
    )
    phase = y * slit_distance * x / (2.0 * sigma_t**2 * y_rayleigh)
    return i1, i2, phase


def two_path_density(
    i1: np.ndarray,
    i2: np.ndarray,
    phase: np.ndarray,
    gamma: float,
) -> np.ndarray:
    return i1 + i2 + 2.0 * math.exp(-gamma) * np.sqrt(i1 * i2) * np.cos(phase)


def normalize(rho: np.ndarray) -> np.ndarray:
    peak = float(np.max(rho))
    return rho / peak if peak > 0.0 else rho


def main() -> None:
    out_dir = Path(__file__).resolve().parent

    params = dict(mass=1.0, velocity=10.0, hbar=1.0, slit_distance=1.5, sigma0=0.25)
    y_rayleigh = 2.0 * params["mass"] * params["velocity"] * params["sigma0"] ** 2 / params["hbar"]
    y_screen = 15.0 * y_rayleigh
    x = np.linspace(-6.0, 6.0, 8000)

    lambda_det = 1.1
    length = 1.0
    c_path = 1.0
    zetas = [0.5, 1.25, 2.5]

    i1, i2, phase = two_path_fields(x, y_screen, **params)
    rho_coherent = two_path_density(i1, i2, phase, gamma=0.0)
    rho_incoherent = i1 + i2
    r_det = dtn_massive_interval(lambda_det, length)

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8), constrained_layout=True)

    ax = axes[0]
    ax.plot(x, normalize(rho_coherent), color="black", lw=1.8, label="Standard coherent")
    ax.plot(x, normalize(rho_incoherent), color="tab:gray", lw=2.0, ls="--", label="Standard incoherent")
    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rho_gdq = two_path_density(i1, i2, phase, gamma)
        ax.plot(
            x,
            normalize(rho_gdq),
            lw=1.4,
            label=rf"GDQ DtN: $\zeta={zeta}$, $e^{{-\Gamma}}={math.exp(-gamma):.3f}$",
        )
    ax.set_title("Density on Screen")
    ax.set_xlabel("transverse position $x$")
    ax.set_ylabel("normalized intensity")
    ax.set_xlim(-5.0, 5.0)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    ax = axes[1]
    zeta_grid = np.linspace(0.0, 3.0, 400)
    gamma_grid = np.array([detector_gamma(float(z), lambda_det, length, c_path) for z in zeta_grid])
    ax.plot(zeta_grid, np.exp(-gamma_grid), color="tab:blue", lw=2.0, label="GDQ $e^{-\\Gamma_{\\rm det}}$")
    ax.axhline(1.0, color="black", lw=1.2, label="coherent")
    ax.axhline(0.0, color="tab:gray", lw=1.2, ls="--", label="perfect which-path")
    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        ax.scatter([zeta], [math.exp(-gamma)], s=35)
    ax.set_title("Interference Term Coefficient")
    ax.set_xlabel("detector--flow coupling $\\zeta_{\\rm det}$")
    ax.set_ylabel("coherence")
    ax.set_ylim(-0.03, 1.05)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    fig.suptitle(
        rf"Reduced comparison — $\lambda_{{det}}={lambda_det}$, "
        rf"$L={length}$, $R_{{det}}={r_det:.6f}$",
        fontsize=12,
    )

    out_png = out_dir / "comparacao_gdq_padrao_dupla_fenda.png"
    out_md = out_dir / "comparison_gdq_standard_double_slit.md"
    fig.savefig(out_png, dpi=180)
    plt.close(fig)

    rows = []
    for zeta in [0.0, *zetas]:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rows.append((zeta, gamma, math.exp(-gamma)))

    lines: list[str] = []
    lines.append("# Output — reduced GDQ vs standard comparison\n\n")
    lines.append("Classification: phenomenological/controlled comparison in the Madelung sector on a fixed background.\n\n")
    lines.append("## What was compared\n\n")
    lines.append("1. standard coherent: two Gaussians with full cross-term;\n")
    lines.append("2. standard incoherent: `I1+I2` mixture;\n")
    lines.append("3. reduced GDQ: cross-term multiplied by `exp(-Gamma_det)`.\n\n")
    lines.append("## Parameters\n\n")
    lines.append(f"- `lambda_det = {lambda_det}`\n")
    lines.append(f"- `L = {length}`\n")
    lines.append(f"- `R_det = {r_det:.12f}`\n")
    lines.append(f"- `C_path = {c_path}`\n\n")
    lines.append("## Table\n\n")
    lines.append("| zeta_det | Gamma_det | exp(-Gamma_det) |\n")
    lines.append("|---:|---:|---:|\n")
    for zeta, gamma, coherence in rows:
        lines.append(f"| {zeta:.6g} | {gamma:.9f} | {coherence:.9f} |\n")
    lines.append("\n## Figure\n\n")
    lines.append("![Reduced GDQ vs standard comparison](comparacao_gdq_padrao_dupla_fenda.png)\n\n")
    lines.append("## Interpretation\n\n")
    lines.append("The reduced GDQ coincides with the coherent standard when `zeta_det=0` and tends to the incoherent standard when `Gamma_det` grows. The distinctive feature is not the existence of fringes, but the geometric law of coherence loss via DtN/Schur impedance:\n\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{\\rm det}=\\frac12\\zeta_{\\rm det}^2C_{\\rm path}\\lambda_{\\rm det}\\coth(\\lambda_{\\rm det}L).\n")
    lines.append("$$\n")

    out_md.write_text("".join(lines), encoding="utf-8")
    print(out_png)
    print(out_md)


if __name__ == "__main__":
    main()

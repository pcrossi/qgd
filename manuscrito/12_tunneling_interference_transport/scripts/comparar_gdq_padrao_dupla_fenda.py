#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Comparação reduzida com o padrão operacional

Objetivo
--------
Comparar três curvas no setor Madelung de fundo fixo:

1. limite coerente usual: duas gaussianas com termo cruzado completo;
2. limite incoerente usual: mistura I1+I2;
3. GDQ reduzida: termo cruzado amortecido por exp(-Gamma_det), com Gamma_det
   derivado da impedância DtN/Schur do detector.

Classificação
-------------
Comparação fenomenológica/controlada. Não é evolução completa da métrica GDQ.

Saídas
------
- comparacao_gdq_padrao_dupla_fenda.png
- comparacao_gdq_padrao_dupla_fenda.md
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
    ax.plot(x, normalize(rho_coherent), color="black", lw=1.8, label="Padrão coerente")
    ax.plot(x, normalize(rho_incoherent), color="tab:gray", lw=2.0, ls="--", label="Padrão incoerente")
    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rho_gdq = two_path_density(i1, i2, phase, gamma)
        ax.plot(
            x,
            normalize(rho_gdq),
            lw=1.4,
            label=rf"GDQ DtN: $\zeta={zeta}$, $e^{{-\Gamma}}={math.exp(-gamma):.3f}$",
        )
    ax.set_title("Densidade no anteparo")
    ax.set_xlabel("posição transversal $x$")
    ax.set_ylabel("intensidade normalizada")
    ax.set_xlim(-5.0, 5.0)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    ax = axes[1]
    zeta_grid = np.linspace(0.0, 3.0, 400)
    gamma_grid = np.array([detector_gamma(float(z), lambda_det, length, c_path) for z in zeta_grid])
    ax.plot(zeta_grid, np.exp(-gamma_grid), color="tab:blue", lw=2.0, label="GDQ $e^{-\\Gamma_{\\rm det}}$")
    ax.axhline(1.0, color="black", lw=1.2, label="coerente")
    ax.axhline(0.0, color="tab:gray", lw=1.2, ls="--", label="which-path perfeito")
    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        ax.scatter([zeta], [math.exp(-gamma)], s=35)
    ax.set_title("Coeficiente do termo de interferência")
    ax.set_xlabel("acoplamento detector--fluxo $\\zeta_{\\rm det}$")
    ax.set_ylabel("coerência")
    ax.set_ylim(-0.03, 1.05)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    fig.suptitle(
        rf"Comparação reduzida — $\lambda_{{det}}={lambda_det}$, "
        rf"$L={length}$, $R_{{det}}={r_det:.6f}$",
        fontsize=12,
    )

    out_png = out_dir / "comparacao_gdq_padrao_dupla_fenda.png"
    out_md = out_dir / "comparacao_gdq_padrao_dupla_fenda.md"
    fig.savefig(out_png, dpi=180)
    plt.close(fig)

    rows = []
    for zeta in [0.0, *zetas]:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rows.append((zeta, gamma, math.exp(-gamma)))

    lines: list[str] = []
    lines.append("# Saída — comparação GDQ reduzida vs padrão\n\n")
    lines.append("Classificação: comparação fenomenológica/controlada no setor Madelung em fundo fixo.\n\n")
    lines.append("## O que foi comparado\n\n")
    lines.append("1. padrão coerente: duas gaussianas com termo cruzado completo;\n")
    lines.append("2. padrão incoerente: mistura `I1+I2`;\n")
    lines.append("3. GDQ reduzida: termo cruzado multiplicado por `exp(-Gamma_det)`.\n\n")
    lines.append("## Parâmetros\n\n")
    lines.append(f"- `lambda_det = {lambda_det}`\n")
    lines.append(f"- `L = {length}`\n")
    lines.append(f"- `R_det = {r_det:.12f}`\n")
    lines.append(f"- `C_path = {c_path}`\n\n")
    lines.append("## Tabela\n\n")
    lines.append("| zeta_det | Gamma_det | exp(-Gamma_det) |\n")
    lines.append("|---:|---:|---:|\n")
    for zeta, gamma, coherence in rows:
        lines.append(f"| {zeta:.6g} | {gamma:.9f} | {coherence:.9f} |\n")
    lines.append("\n## Figura\n\n")
    lines.append("![Comparação GDQ reduzida vs padrão](comparacao_gdq_padrao_dupla_fenda.png)\n\n")
    lines.append("## Leitura\n\n")
    lines.append("A GDQ reduzida coincide com o padrão coerente quando `zeta_det=0` e tende ao padrão incoerente quando `Gamma_det` cresce. O diferencial não é a existência das franjas, mas a lei geométrica de perda de coerência por impedância DtN/Schur:\n\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{\\rm det}=\\frac12\\zeta_{\\rm det}^2C_{\\rm path}\\lambda_{\\rm det}\\coth(\\lambda_{\\rm det}L).\n")
    lines.append("$$\n")

    out_md.write_text("".join(lines), encoding="utf-8")
    print(out_png)
    print(out_md)


if __name__ == "__main__":
    main()

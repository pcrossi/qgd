#!/usr/bin/env python3
"""Q44 — comparação gráfica entre GDQ reduzida e teoria padrão.

Classificação:

- teoria padrão coerente: superposição de duas gaussianas sem detector;
- teoria padrão incoerente: mistura `I1 + I2`, equivalente a which-path
  perfeito;
- GDQ reduzida: mesmo setor Madelung, mas com termo cruzado amortecido por
  `exp(-Gamma_det)`, onde `Gamma_det` vem da impedância DtN/Schur do detector.

Este script não é uma simulação da métrica GDQ completa.
"""

from __future__ import annotations

import math
import os
from pathlib import Path
import sys

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-gdq")

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from metodologia.numerico.gdq_reduced import (  # noqa: E402
    coherence_from_gamma,
    detector_gamma,
    dtn_massive_interval,
    two_path_density,
)


def fields(x: np.ndarray, y: float, *, m: float, v0: float, hbar: float, d: float, sigma0: float):
    y_r = 2.0 * m * v0 * sigma0**2 / hbar
    sigma_t = sigma0 * np.sqrt(1.0 + (y / y_r) ** 2)
    i1 = (1.0 / np.sqrt(2.0 * np.pi * sigma_t**2)) * np.exp(-((x + d / 2.0) ** 2) / (2.0 * sigma_t**2))
    i2 = (1.0 / np.sqrt(2.0 * np.pi * sigma_t**2)) * np.exp(-((x - d / 2.0) ** 2) / (2.0 * sigma_t**2))
    phase = y * d * x / (2.0 * sigma_t**2 * y_r)
    return i1, i2, phase, sigma_t, y_r


def normalize(rho: np.ndarray) -> np.ndarray:
    peak = float(np.max(rho))
    if peak <= 0:
        return rho
    return rho / peak


def main() -> None:
    params = dict(m=1.0, v0=10.0, hbar=1.0, d=1.5, sigma0=0.25)
    y_r = 2.0 * params["m"] * params["v0"] * params["sigma0"] ** 2 / params["hbar"]
    y = 15.0 * y_r
    x = np.linspace(-6.0, 6.0, 8000)

    lambda_det = 1.1
    length = 1.0
    c_path = 1.0
    zetas = [0.5, 1.25, 2.5]

    i1, i2, phase, sigma_t, _ = fields(x, y, **params)

    rho_standard_coherent = two_path_density(i1, i2, phase, gamma=0.0)
    rho_standard_incoherent = i1 + i2

    r_det = dtn_massive_interval(lambda_det, length)

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8), constrained_layout=True)

    ax = axes[0]
    ax.plot(x, normalize(rho_standard_coherent), color="black", lw=1.8, label="Padrão: coerente")
    ax.plot(x, normalize(rho_standard_incoherent), color="tab:gray", lw=2.0, ls="--", label="Padrão: incoerente")

    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rho_gdq = two_path_density(i1, i2, phase, gamma=gamma)
        ax.plot(
            x,
            normalize(rho_gdq),
            lw=1.4,
            label=rf"GDQ DtN: $\zeta={zeta}$, $e^{{-\Gamma}}={coherence_from_gamma(gamma):.3f}$",
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
    coherence_grid = np.exp(-gamma_grid)
    ax.plot(zeta_grid, coherence_grid, color="tab:blue", lw=2.0, label="GDQ: $e^{-\\Gamma_{\\rm det}}$")
    ax.axhline(1.0, color="black", lw=1.4, label="Padrão coerente")
    ax.axhline(0.0, color="tab:gray", lw=1.4, ls="--", label="Padrão which-path perfeito")
    for zeta in zetas:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        ax.scatter([zeta], [coherence_from_gamma(gamma)], s=35)
    ax.set_title("Coeficiente do termo de interferência")
    ax.set_xlabel("acoplamento detector--fluxo $\\zeta_{\\rm det}$")
    ax.set_ylabel("coerência")
    ax.set_ylim(-0.03, 1.05)
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)

    fig.suptitle(
        rf"Q44: comparação reduzida — $\lambda_{{det}}={lambda_det}$, $L={length}$, "
        rf"$R_{{det}}={r_det:.6f}$",
        fontsize=12,
    )

    out_png = OUT / "comparacao_gdq_padrao_q44.png"
    out_md = OUT / "comparacao_gdq_padrao_q44.md"
    fig.savefig(out_png, dpi=180)
    plt.close(fig)

    rows = []
    for zeta in [0.0, *zetas]:
        gamma = detector_gamma(zeta, lambda_det, length, c_path)
        rows.append((zeta, gamma, coherence_from_gamma(gamma)))

    lines = []
    lines.append("# Q44 — comparação gráfica GDQ reduzida vs teoria padrão\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Comparação fenomenológica/controlada no setor Madelung em fundo fixo. Não é evolução métrica completa da GDQ.\n\n")
    lines.append("## O que foi comparado\n\n")
    lines.append("1. Teoria padrão coerente: duas gaussianas superpostas, sem detector de caminho.\n")
    lines.append("2. Teoria padrão incoerente: mistura `I1 + I2`, equivalente a detector de caminho perfeito.\n")
    lines.append("3. GDQ reduzida: termo cruzado multiplicado por `exp(-Gamma_det)`, com `Gamma_det` derivado por DtN/Schur.\n\n")
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
    lines.append(f"![Comparação GDQ vs padrão](comparacao_gdq_padrao_q44.png)\n\n")
    lines.append("## Leitura\n\n")
    lines.append("A teoria padrão sem detector corresponde ao limite coerente. A teoria padrão com which-path perfeito corresponde ao limite incoerente. A GDQ reduzida fornece uma lei intermediária para a perda do termo cruzado, determinada pela impedância de contorno do detector:\n\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{\\rm det}=\\frac12\\zeta_{\\rm det}^2 C_{\\rm path}\\lambda_{\\rm det}\\coth(\\lambda_{\\rm det}L).\n")
    lines.append("$$\n")
    lines.append("\nO ponto distintivo não é a existência de franjas, mas a parametrização geométrica da perda de visibilidade por DtN/Schur.\n")

    out_md.write_text("".join(lines), encoding="utf-8")
    print(out_png)
    print(out_md)


if __name__ == "__main__":
    main()

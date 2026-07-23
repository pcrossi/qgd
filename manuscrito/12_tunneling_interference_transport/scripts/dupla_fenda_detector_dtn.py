#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Dupla fenda com detector DtN

Objetivo
--------
Avaliar a dupla fenda no setor reduzido de Madelung em fundo fixo,
incluindo um detector linear por impedância Dirichlet-to-Neumann.

Classificação
-------------
Avaliação direta de um detector reduzido derivado por DtN/Schur no setor
Madelung. Não é evolução completa da métrica GDQ.

Equações avaliadas
------------------
R_det = lambda_det*coth(lambda_det*L)

Gamma_det = 1/2*zeta_det^2*C_path*R_det

rho_det = I1 + I2 + 2*exp(-Gamma_det)*sqrt(I1*I2)*cos(Delta_phi)

Saídas
------
- saida_dupla_fenda_detector_dtn.md
- saida_dupla_fenda_detector_dtn.csv
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


def coth(x: float) -> float:
    """Cotangente hiperbólica estável para x positivo."""

    return math.cosh(x) / math.sinh(x)


def dtn_massive_interval(lambda_det: float, length: float) -> float:
    """Impedância DtN do canal K=-d_s^2+lambda_det^2 em [0,L]."""

    return lambda_det * coth(lambda_det * length)


def detector_gamma(
    zeta_det: float,
    lambda_det: float,
    length: float,
    c_path: float = 1.0,
) -> float:
    """Custo quadrático de distinção de caminhos."""

    r_det = dtn_massive_interval(lambda_det, length)
    return 0.5 * zeta_det**2 * c_path * r_det


def coherence_from_gamma(gamma: float) -> float:
    """Coeficiente de coerência do termo cruzado."""

    return math.exp(-gamma)


def two_path_fields(
    x: np.ndarray,
    y: float,
    *,
    mass: float,
    velocity: float,
    hbar: float,
    slit_distance: float,
    sigma0: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    """Intensidades reduzidas de duas fontes gaussianas paraxiais."""

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
    return i1, i2, phase, float(sigma_t), float(y_rayleigh)


def two_path_density(
    i1: np.ndarray,
    i2: np.ndarray,
    phase: np.ndarray,
    gamma: float,
) -> np.ndarray:
    """Densidade com termo cruzado amortecido por exp(-Gamma)."""

    return i1 + i2 + 2.0 * math.exp(-gamma) * np.sqrt(i1 * i2) * np.cos(phase)


def central_visibility(x: np.ndarray, rho: np.ndarray, phase: np.ndarray) -> float:
    """Visibilidade bruta em uma janela central de uma oscilação."""

    mask = np.abs(phase) <= math.pi
    if mask.sum() < 10:
        mask = np.abs(x) <= np.percentile(np.abs(x), 10)
    local = rho[mask]
    i_max = float(np.max(local))
    i_min = float(np.min(local))
    return (i_max - i_min) / (i_max + i_min)


def run_case(n: int, zeta_det: float, lambda_det: float, length: float) -> dict[str, float]:
    """Executa um caso de malha e acoplamento detector--fluxo."""

    params = dict(
        mass=1.0,
        velocity=10.0,
        hbar=1.0,
        slit_distance=1.5,
        sigma0=0.25,
    )
    y_rayleigh = 2.0 * params["mass"] * params["velocity"] * params["sigma0"] ** 2 / params["hbar"]
    y_screen = 15.0 * y_rayleigh
    x = np.linspace(-6.0, 6.0, n)
    i1, i2, phase, sigma_t, _ = two_path_fields(x, y_screen, **params)
    gamma = detector_gamma(zeta_det, lambda_det, length)
    rho = two_path_density(i1, i2, phase, gamma)

    return {
        "n": float(n),
        "zeta_det": zeta_det,
        "lambda_det": lambda_det,
        "length": length,
        "r_det": dtn_massive_interval(lambda_det, length),
        "gamma": gamma,
        "coherence": coherence_from_gamma(gamma),
        "visibility": central_visibility(x, rho, phase),
        "rho_norm": float(np.trapezoid(rho, x)),
        "sigma_t": sigma_t,
        "y_screen": float(y_screen),
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    lambda_det = 1.1
    length = 1.0
    zetas = [0.0, 0.5, 1.25, 2.5]
    meshes = [1000, 2000, 4000, 8000]

    rows = [
        run_case(n, zeta, lambda_det, length)
        for zeta in zetas
        for n in meshes
    ]
    final_rows = [row for row in rows if int(row["n"]) == meshes[-1]]

    lines: list[str] = []
    lines.append("# Saída — dupla fenda com detector DtN\n\n")
    lines.append("Classificação: avaliação direta de detector reduzido por DtN/Schur no setor Madelung em fundo fixo.\n\n")
    lines.append("## Parâmetros fixos\n\n")
    lines.append(f"- `lambda_det = {lambda_det:.12g}`\n")
    lines.append(f"- `L = {length:.12g}`\n")
    lines.append(f"- `R_det = lambda_det*coth(lambda_det*L) = {dtn_massive_interval(lambda_det, length):.12g}`\n")
    lines.append("- `C_path = 1` marcador primitivo normalizado\n\n")
    lines.append("## Resultados principais em N=8000\n\n")
    lines.append("| zeta_det | Gamma_det | exp(-Gamma_det) | visibilidade bruta central | norma trapezoidal |\n")
    lines.append("|---:|---:|---:|---:|---:|\n")
    for row in final_rows:
        lines.append(
            f"| {row['zeta_det']:.6g} | {row['gamma']:.9f} | "
            f"{row['coherence']:.9f} | {row['visibility']:.9f} | "
            f"{row['rho_norm']:.9f} |\n"
        )

    lines.append("\n## Convergência de malha\n\n")
    lines.append("| zeta_det | N | Gamma_det | exp(-Gamma_det) | visibilidade bruta central |\n")
    lines.append("|---:|---:|---:|---:|---:|\n")
    for row in rows:
        lines.append(
            f"| {row['zeta_det']:.6g} | {int(row['n'])} | {row['gamma']:.9f} | "
            f"{row['coherence']:.9f} | {row['visibility']:.9f} |\n"
        )

    lines.append("\n## Fórmula avaliada\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm det}=I_1+I_2+2e^{-\\Gamma_{\\rm det}}\\sqrt{I_1I_2}\\cos\\Delta\\phi.\n")
    lines.append("$$\n\n")
    lines.append("com\n\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{\\rm det}=\\frac12\\zeta_{\\rm det}^2C_{\\rm path}\\lambda_{\\rm det}\\coth(\\lambda_{\\rm det}L).\n")
    lines.append("$$\n\n")
    lines.append("## Leitura\n\n")
    lines.append("- `zeta_det=0` recupera interferência coerente.\n")
    lines.append("- `zeta_det` crescente reduz monotonamente o coeficiente do termo cruzado.\n")
    lines.append("- `Gamma_det>>1` leva ao limite incoerente `I1+I2`.\n")
    lines.append("- A visibilidade bruta não precisa ir exatamente a zero, pois ainda mede o envelope incoerente.\n")

    (out_dir / "saida_dupla_fenda_detector_dtn.md").write_text("".join(lines), encoding="utf-8")

    table = np.array(
        [
            [
                row["zeta_det"],
                row["n"],
                row["r_det"],
                row["gamma"],
                row["coherence"],
                row["visibility"],
                row["rho_norm"],
            ]
            for row in rows
        ],
        dtype=float,
    )
    np.savetxt(
        out_dir / "saida_dupla_fenda_detector_dtn.csv",
        table,
        delimiter=",",
        header="zeta_det,N,R_det,Gamma_det,exp_minus_Gamma,visibility,rho_norm",
        comments="",
    )
    print(out_dir / "saida_dupla_fenda_detector_dtn.md")


if __name__ == "__main__":
    main()

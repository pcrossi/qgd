#!/usr/bin/env python3
"""Q44 — dupla fenda com detector DtN reduzido.

Este script não evolui a métrica GDQ completa. Ele avalia a solução reduzida de
Madelung em fundo fixo e insere o detector por uma impedância DtN derivada do
operador K_det = -d_s^2 + lambda_det^2.
"""

from __future__ import annotations

import math
from pathlib import Path
import sys

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


def central_visibility(x: np.ndarray, rho: np.ndarray, phase: np.ndarray) -> float:
    # Use the first central oscillation window. This avoids envelope tails
    # dominating the max/min estimate.
    phase_abs = np.abs(phase)
    mask = phase_abs <= math.pi
    if mask.sum() < 10:
        mask = np.abs(x) <= np.percentile(np.abs(x), 10)
    local = rho[mask]
    imax = float(np.max(local))
    imin = float(np.min(local))
    return (imax - imin) / (imax + imin)


def run_case(n: int, zeta: float, lambda_det: float, length: float):
    params = dict(m=1.0, v0=10.0, hbar=1.0, d=1.5, sigma0=0.25)
    y_r = 2.0 * params["m"] * params["v0"] * params["sigma0"] ** 2 / params["hbar"]
    y = 15.0 * y_r
    x = np.linspace(-6.0, 6.0, n)
    i1, i2, phase, sigma_t, _ = fields(x, y, **params)
    gamma = detector_gamma(zeta, lambda_det, length)
    rho = two_path_density(i1, i2, phase, gamma)
    vis = central_visibility(x, rho, phase)
    return {
        "n": n,
        "zeta": zeta,
        "lambda_det": lambda_det,
        "length": length,
        "r_det": dtn_massive_interval(lambda_det, length),
        "gamma": gamma,
        "coherence": coherence_from_gamma(gamma),
        "visibility": vis,
        "rho_norm": float(np.trapezoid(rho, x)),
        "sigma_t": float(sigma_t),
        "y": float(y),
    }


def main() -> None:
    lambda_det = 1.1
    length = 1.0
    zetas = [0.0, 0.5, 1.25, 2.5]
    ns = [1000, 2000, 4000, 8000]

    rows = []
    for zeta in zetas:
        for n in ns:
            rows.append(run_case(n, zeta, lambda_det, length))

    final_rows = [r for r in rows if r["n"] == ns[-1]]
    lines = []
    lines.append("# Q44 — saída do solver reduzido com detector DtN\n")
    lines.append("## Classificação\n")
    lines.append("Avaliação direta de um detector reduzido derivado por DtN/Schur no setor Madelung em fundo fixo. Não é evolução da métrica completa.\n")
    lines.append("## Parâmetros fixos do detector reduzido\n")
    lines.append(f"- `lambda_det = {lambda_det:.12g}`\n")
    lines.append(f"- `L = {length:.12g}`\n")
    lines.append(f"- `R_det = lambda*coth(lambda*L) = {dtn_massive_interval(lambda_det, length):.12g}`\n")
    lines.append("- `C_path = 1` marcador primitivo normalizado\n")
    lines.append("## Resultados principais em N=8000\n")
    lines.append("| zeta_det | Gamma_det | Contraste de franja `exp(-Gamma)` | Visibilidade bruta central | Norma trapezoidal |\n")
    lines.append("|---:|---:|---:|---:|---:|\n")
    for r in final_rows:
        lines.append(
            f"| {r['zeta']:.6g} | {r['gamma']:.9f} | {r['coherence']:.9f} | "
            f"{r['visibility']:.9f} | {r['rho_norm']:.9f} |\n"
        )
    lines.append("\n## Convergência de malha\n")
    lines.append("| zeta_det | N | Gamma_det | Contraste de franja | Visibilidade bruta central |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for r in rows:
        lines.append(f"| {r['zeta']:.6g} | {r['n']} | {r['gamma']:.9f} | {r['coherence']:.9f} | {r['visibility']:.9f} |\n")
    lines.append("\n## Validação de limites\n")
    lines.append("- `zeta_det = 0`: `Gamma_det = 0`, logo o padrão coerente é recuperado.\n")
    lines.append("- `zeta_det` crescente: o termo cruzado é multiplicado por `exp(-Gamma_det)` e a visibilidade cai monotonamente.\n")
    lines.append("- `Gamma_det >> 1`: o contraste de franja `exp(-Gamma_det)` tende a zero e a densidade tende a `I1 + I2`, isto é, mistura sem interferência.\n")
    lines.append("- A visibilidade bruta central não precisa tender exatamente a zero porque ainda inclui variação do envelope incoerente; o observável de coerência é o coeficiente do termo cruzado.\n")
    lines.append("\n## Fórmula avaliada\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm det}=I_1+I_2+2e^{-\\Gamma_{\\rm det}}\\sqrt{I_1I_2}\\cos\\Delta\\phi.\n")
    lines.append("$$\n")
    lines.append("com\n")
    lines.append("$$\n")
    lines.append("\\Gamma_{\\rm det}=\\frac12\\zeta_{\\rm det}^2\\lambda_{\\rm det}\\coth(\\lambda_{\\rm det}L).\n")
    lines.append("$$\n")

    out_md = OUT / "saida_solver_detector_q44.md"
    out_md.write_text("".join(lines), encoding="utf-8")

    # Save a compact CSV-like table for reproducibility.
    table = np.array(
        [
            [r["zeta"], r["n"], r["r_det"], r["gamma"], r["coherence"], r["visibility"], r["rho_norm"]]
            for r in rows
        ],
        dtype=float,
    )
    np.savetxt(
        OUT / "saida_solver_detector_q44.csv",
        table,
        delimiter=",",
        header="zeta,N,R_det,Gamma,exp_minus_Gamma,visibility,rho_norm",
        comments="",
    )
    print(out_md)


if __name__ == "__main__":
    main()

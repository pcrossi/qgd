#!/usr/bin/env python3
"""Q51 — teste de proxy de camada para o projetor alfa.

Classificação:
    - teste diagnóstico;
    - não previsão;
    - não usa como fechamento.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "saida_teste_shell_proxy_q51.md"
MAGIC = np.array([2, 8, 20, 28, 50, 82, 126], dtype=float)

# name, daughter A, daughter Z, p_req
DATA = [
    ("U-238", 234, 90, 0.000000),
    ("U-234", 230, 90, 0.938269),
    ("U-232", 228, 90, 0.630933),
    ("Th-232", 228, 88, 0.000000),
    ("Ra-226", 222, 86, 0.812735),
    ("Po-212", 208, 82, 0.507847),
]


def dist_magic(x: float) -> float:
    return float(np.min(np.abs(MAGIC - x)))


def fit_one_param(D: np.ndarray, p: np.ndarray, form: str):
    best_rms = float("inf")
    best_c = None
    best_pred = None
    for c in np.logspace(-2, 5, 5000):
        if form == "D/(D+c)":
            pred = D / (D + c)
        elif form == "c/(D+c)":
            pred = c / (D + c)
        elif form == "lorentz_open":
            pred = 1.0 / (1.0 + (D / c) ** 2)
        elif form == "lorentz_closed":
            pred = (D / c) ** 2 / (1.0 + (D / c) ** 2)
        else:
            raise ValueError(form)
        rms = float(np.sqrt(np.mean((pred - p) ** 2)))
        if rms < best_rms:
            best_rms = rms
            best_c = c
            best_pred = pred
    return best_rms, best_c, best_pred


def main() -> None:
    rows = []
    for name, A, Z, p in DATA:
        N = A - Z
        dZ = dist_magic(Z)
        dN = dist_magic(N)
        D = dZ * dZ + dN * dN
        rows.append((name, A, Z, N, dZ, dN, D, p))

    D = np.array([r[6] for r in rows], dtype=float)
    p = np.array([r[7] for r in rows], dtype=float)

    models = ["D/(D+c)", "c/(D+c)", "lorentz_open", "lorentz_closed"]
    fits = {m: fit_one_param(D, p, m) for m in models}

    lines = []
    lines.append("# Saída — teste de proxy de camada Q51\n\n")
    lines.append("Classificação: teste diagnóstico, não previsão.\n\n")
    lines.append("Distância a números mágicos do núcleo filho:\n\n")
    lines.append("$$\n")
    lines.append("D_{\\rm shell}=d_Z^2+d_N^2.\n")
    lines.append("$$\n\n")
    lines.append("| Núcleo | A_f | Z_f | N_f | dZ | dN | D_shell | p_req |\n")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n")
    for r in rows:
        lines.append(
            f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]:.0f} | "
            f"{r[5]:.0f} | {r[6]:.0f} | {r[7]:.6f} |\n"
        )

    lines.append("\n")
    lines.append("| Proxy ajustado | RMS em p_req | c ótimo |\n")
    lines.append("| --- | ---: | ---: |\n")
    for m, (rms, c, _pred) in fits.items():
        lines.append(f"| {m} | {rms:.6f} | {c:.6f} |\n")

    lines.append("\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "A distância a números mágicos do núcleo filho não explica sozinha o "
        "peso de projeção. Em particular, U-238 e Th-232 têm distâncias de "
        "camada grandes mas p_req próximo de zero, enquanto Po-212 tem filha "
        "duplamente mágica e p_req intermediário.\n\n"
    )
    lines.append(
        "Conclusão: o projetor não pode ser reduzido a uma função escalar de "
        "números mágicos. É necessário o espectro real de "
        "K_partial^phys e o overlap com o subespaço do filho.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()


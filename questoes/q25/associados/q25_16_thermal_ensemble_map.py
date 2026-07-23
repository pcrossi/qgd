#!/usr/bin/env python3
"""Q25.16 — mapa térmico do ensemble GDQ reduzido.

Classificação: calibração/inversão fenomenológica do mapa de temperatura.

Este script não altera a ação oficial. Ele varre beta_eff no ensemble reduzido
GDQ e pergunta qual beta_eff reproduz cada ponto digitizado de C_s(1) da Fig. 2D.
"""

from __future__ import annotations

import csv
from pathlib import Path
import numpy as np
from q25_physical_common import DATA, RESULTS, PhysicalConfig, ensure_dirs, metropolis_correlations


OUT = RESULTS / "saida_q25_16_thermal_ensemble_map.md"
CSV_OUT = DATA / "q25_thermal_map_gdq_reduced.csv"


def read_digitized() -> list[dict[str, float]]:
    path = DATA / "q25_referencias_experimentais.csv"
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["paper_id"] == "parsons_2016_fig2d_digitized" and row["observable"] == "C_s_r1":
                rows.append(
                    {
                        "T_over_t": float(row["T_over_t"]),
                        "C_exp": float(row["value"]),
                        "err": float(row["error"]),
                    }
                )
    return sorted(rows, key=lambda r: r["T_over_t"])


def build_curve(beta_grid: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    c1 = []
    for idx, beta in enumerate(beta_grid):
        mc = metropolis_correlations(
            PhysicalConfig(beta_eff=float(beta), seed=2600 + idx),
            steps=28_000,
            burn=4_000,
        )
        c1.append(float(mc["C_s_r1"]))
    return beta_grid, np.array(c1)


def invert_beta(target: float, beta: np.ndarray, c1: np.ndarray) -> float | None:
    # c1 fica mais negativo com beta crescente no intervalo físico.
    order = np.argsort(c1)
    c_sorted = c1[order]
    b_sorted = beta[order]
    if target < c_sorted[0] or target > c_sorted[-1]:
        return None
    return float(np.interp(target, c_sorted, b_sorted))


def main() -> None:
    ensure_dirs()
    data = read_digitized()
    # Varredura Monte Carlo reprodutível. A enumeração exata permanece usada no
    # benchmark principal; aqui precisamos só de uma curva térmica operacional.
    beta_grid = np.linspace(0.001, 1.35, 24)
    beta, c1 = build_curve(beta_grid)

    mapped = []
    for row in data:
        b = invert_beta(row["C_exp"], beta, c1)
        if b is None:
            mapped.append({**row, "beta_eff": None, "T_eff": None, "C_gdq": None, "residual": None})
        else:
            c = float(np.interp(b, beta, c1))
            mapped.append({**row, "beta_eff": b, "T_eff": 1.0 / b if b > 0 else None, "C_gdq": c, "residual": c - row["C_exp"]})

    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["T_over_t", "C_exp", "err", "beta_eff", "T_eff", "C_gdq", "residual"])
        writer.writeheader()
        writer.writerows(mapped)

    table = "| kBT/t exp | C_s(1) exp | beta_eff GDQ | T_eff GDQ | C_s(1) GDQ | residual |\n"
    table += "|---:|---:|---:|---:|---:|---:|\n"
    for r in mapped:
        def fmt(x):
            return "fora da faixa" if x is None else f"{x:.8e}"
        table += (
            f"| {r['T_over_t']:.3f} | {r['C_exp']:.8e} | {fmt(r['beta_eff'])} | "
            f"{fmt(r['T_eff'])} | {fmt(r['C_gdq'])} | {fmt(r['residual'])} |\n"
        )

    # Ajuste empírico simples beta_eff ~ a/(T/t + b) nos pontos invertidos.
    valid = [r for r in mapped if r["beta_eff"] is not None and r["T_over_t"] > 0]
    fit_msg = ""
    if len(valid) >= 3:
        T = np.array([r["T_over_t"] for r in valid])
        B = np.array([r["beta_eff"] for r in valid])
        # Varredura em b para linearizar B = a/(T+b).
        best = None
        for b0 in np.linspace(0.0, 2.0, 1001):
            x = 1.0 / (T + b0)
            a = float(np.dot(x, B) / np.dot(x, x))
            pred = a * x
            mse = float(np.mean((pred - B) ** 2))
            if best is None or mse < best[0]:
                best = (mse, a, b0)
        assert best is not None
        mse, a, b0 = best
        fit_msg = (
            f"\nAjuste fenomenológico do mapa térmico reduzido:\n\n"
            f"$$\n\\beta_{{\\rm eff}} \\simeq \\frac{{{a:.6f}}}{{k_BT/t+{b0:.6f}}}\n$$\n\n"
            f"MSE em beta: `{mse:.8e}`.\n"
        )

    OUT.write_text(
        "# Q25.16 — Mapa térmico do ensemble GDQ reduzido\n\n"
        "Classificação: calibração/inversão fenomenológica do mapa térmico.\n\n"
        "O script varre por Monte Carlo reprodutível o ensemble positivo reduzido "
        "da GDQ e inverte a curva `C_s(1)(beta_eff)` para os pontos digitizados "
        "da Fig. 2D de Parsons.\n\n"
        + table
        + fit_msg
        + "\nInterpretação: a curva experimental pode ser representada por uma "
        "família de ensembles GDQ reduzidos com `beta_eff` variável. Isto resolve "
        "a comparação operacional da curva no modelo reduzido, mas a derivação "
        "do mapa térmico a partir da Hessiana completa do aparelho continua "
        "pendente.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

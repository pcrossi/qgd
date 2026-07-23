#!/usr/bin/env python3
"""Q25.17 — candidatos GDQ para o mapa térmico a partir da Hessiana.

Classificação: teste de consistência / resultado negativo útil.

Compara mapas beta_eff(T) construídos só com invariantes da Hessiana reduzida
contra o mapa fenomenológico invertido em Q25.16.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
import numpy as np
from q25_physical_common import DATA, RESULTS, PhysicalConfig, ensure_dirs, gdq_reduced_hessian, hessian_spectrum


IN = DATA / "q25_thermal_map_gdq_reduced.csv"
OUT = RESULTS / "saida_q25_17_hessian_thermal_map_candidates.md"


def read_map() -> tuple[np.ndarray, np.ndarray]:
    T = []
    B = []
    with IN.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["beta_eff"] and row["T_over_t"]:
                T.append(float(row["T_over_t"]))
                B.append(float(row["beta_eff"]))
    return np.array(T), np.array(B)


def candidates(T: np.ndarray) -> dict[str, np.ndarray]:
    cfg = PhysicalConfig()
    h = gdq_reduced_hessian(cfg)
    eig = hessian_spectrum(cfg)
    lam_min = float(eig.min())
    lam_max = float(eig.max())
    lam_mean = float(np.trace(h) / cfg.n_sites)
    off = abs(float(h[0, 1])) if h.shape[0] > 1 else cfg.kappa_H
    kappa = cfg.kappa_H
    gap = cfg.mass_gap

    cand = {}
    # Todos abaixo usam apenas invariantes internos do benchmark reduzido.
    cand["gap_over_T_plus_gap"] = gap / (T + gap)
    cand["sqrt_gap_kappa_over_T_plus_gap"] = math.sqrt(gap * kappa) / (T + gap)
    cand["kappa_over_T_plus_mean"] = kappa / (T + lam_mean)
    cand["offdiag_over_T_plus_gap"] = off / (T + gap)
    cand["spectral_ratio"] = (lam_min / lam_max) / (T + lam_min / lam_max)
    return cand


def main() -> None:
    ensure_dirs()
    T, B = read_map()
    cand = candidates(T)
    rows = []
    for name, pred in cand.items():
        rmse = float(np.sqrt(np.mean((pred - B) ** 2)))
        rel = float(np.sqrt(np.mean(((pred - B) / np.maximum(B, 1e-12)) ** 2)))
        rows.append((name, rmse, rel))
    rows.sort(key=lambda x: x[1])

    table = "| candidato | RMSE beta | erro relativo RMS |\n|---|---:|---:|\n"
    for name, rmse, rel in rows:
        table += f"| `{name}` | {rmse:.8e} | {rel:.8e} |\n"

    best_name = rows[0][0]
    best = cand[best_name]
    comp = "| kBT/t | beta invertido | beta candidato |\n|---:|---:|---:|\n"
    for t, b, p in zip(T, B, best):
        comp += f"| {t:.3f} | {b:.8e} | {p:.8e} |\n"

    OUT.write_text(
        "# Q25.17 — Candidatos Hessianos para o mapa térmico\n\n"
        "Classificação: teste de consistência; resultado negativo útil.\n\n"
        "Foram testados mapas construídos apenas com invariantes da Hessiana "
        "reduzida, sem usar os valores experimentais para ajustar coeficientes.\n\n"
        + table
        + "\nMelhor candidato sem alvo:\n\n"
        + comp
        + "\nVeredito: os candidatos estruturais capturam a forma decrescente "
        "esperada, mas não reproduzem quantitativamente o mapa invertido. Logo, "
        "o fator térmico do aparelho não é determinado apenas pelos invariantes "
        "escalares da Hessiana reduzida. É necessário incluir o bloco térmico/"
        "aparelho completo, mobilidade causal ou condições de contorno "
        "termodinâmicas.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

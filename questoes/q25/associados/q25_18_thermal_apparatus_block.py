#!/usr/bin/env python3
"""Q25.18 — bloco térmico/aparelho reduzido.

Classificação: modelo efetivo de aparelho + comparação.

Constrói o mapa térmico como admitância de contorno:

    beta_eff(Theta) = mu_A / (Theta + Theta_A)

onde Theta = k_B T/t é dado experimental do aparelho. Aqui mu_A e Theta_A
podem ser:

1. candidatos derivados de invariantes da Hessiana reduzida;
2. ajuste efetivo de aparelho, explicitamente classificado como contorno.

O script separa as duas coisas.
"""

from __future__ import annotations

import csv
import math
import numpy as np
from q25_physical_common import DATA, RESULTS, PhysicalConfig, ensure_dirs, gdq_reduced_hessian, hessian_spectrum


IN = DATA / "q25_thermal_map_gdq_reduced.csv"
OUT = RESULTS / "saida_q25_18_thermal_apparatus_block.md"


def read_target():
    T = []
    B = []
    with IN.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            T.append(float(row["T_over_t"]))
            B.append(float(row["beta_eff"]))
    return np.array(T), np.array(B)


def rmse_rel(pred, target):
    rmse = float(np.sqrt(np.mean((pred - target) ** 2)))
    rel = float(np.sqrt(np.mean(((pred - target) / np.maximum(target, 1e-12)) ** 2)))
    return rmse, rel


def model(T, mu, theta):
    return mu / (T + theta)


def fit_apparatus(T, B):
    best = None
    for theta in np.linspace(1e-4, 1.0, 2001):
        x = 1.0 / (T + theta)
        mu = float(np.dot(x, B) / np.dot(x, x))
        pred = mu * x
        rmse, rel = rmse_rel(pred, B)
        if best is None or rmse < best[0]:
            best = (rmse, rel, mu, theta, pred)
    assert best is not None
    return best


def main() -> None:
    ensure_dirs()
    T, B = read_target()
    cfg = PhysicalConfig()
    h = gdq_reduced_hessian(cfg)
    eig = hessian_spectrum(cfg)
    gap = cfg.mass_gap
    kappa = cfg.kappa_H
    lam_min = float(eig.min())
    lam_mean = float(np.trace(h) / cfg.n_sites)

    candidates = {
        "gap_gap": (gap, gap),
        "sqrt_gap_kappa_gap": (math.sqrt(gap * kappa), gap),
        "kappa_gap": (kappa, gap),
        "lam_min_gap": (lam_min, gap),
        "gap_sqrt_gap_kappa": (gap, math.sqrt(gap * kappa)),
        "mean_gap": (lam_mean, gap),
    }

    rows = []
    for name, (mu, theta) in candidates.items():
        pred = model(T, mu, theta)
        rmse, rel = rmse_rel(pred, B)
        rows.append((name, mu, theta, rmse, rel))
    rows.sort(key=lambda x: x[3])

    fit_rmse, fit_rel, fit_mu, fit_theta, fit_pred = fit_apparatus(T, B)

    table = "| mapa | mu_A | Theta_A | RMSE beta | erro relativo RMS |\n|---|---:|---:|---:|---:|\n"
    for name, mu, theta, rmse, rel in rows:
        table += f"| `{name}` | {mu:.8e} | {theta:.8e} | {rmse:.8e} | {rel:.8e} |\n"
    table += f"| `aparelho_efetivo_ajustado` | {fit_mu:.8e} | {fit_theta:.8e} | {fit_rmse:.8e} | {fit_rel:.8e} |\n"

    comp = "| kBT/t | beta invertido | beta aparelho ajustado |\n|---:|---:|---:|\n"
    for t, b, p in zip(T, B, fit_pred):
        comp += f"| {t:.3f} | {b:.8e} | {p:.8e} |\n"

    OUT.write_text(
        "# Q25.18 — Bloco térmico/aparelho reduzido\n\n"
        "Classificação: modelo efetivo de aparelho; comparação com mapa invertido.\n\n"
        "O mapa testado é uma admitância térmica de contorno:\n\n"
        "$$\n\\beta_{\\rm eff}(\\Theta)=\\frac{\\mu_A}{\\Theta+\\Theta_A},\\qquad \\Theta=k_BT/t.\n$$\n\n"
        "Primeiro foram testados candidatos sem alvo, usando apenas invariantes da "
        "Hessiana reduzida. Em seguida foi calculado o par efetivo de aparelho "
        "`(mu_A, Theta_A)` que melhor representa a curva invertida.\n\n"
        + table
        + "\nComparação do aparelho efetivo ajustado:\n\n"
        + comp
        + "\nVeredito: o formato de admitância térmica de contorno é compatível com "
        "a inversão fenomenológica. Porém o par `(mu_A, Theta_A)` ainda é dado de "
        "aparelho/contorno ajustado, não derivado. Para fechar a Q25 em sentido "
        "forte, esses dois números precisam sair da Hessiana completa do aparelho "
        "e da mobilidade causal, não da curva de Parsons.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

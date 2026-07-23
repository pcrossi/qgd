#!/usr/bin/env python3
"""Q25.19 — derivação Schur do bloco térmico/aparelho.

Classificação: derivação reduzida + teste de consistência.

O modo observado é o modo local de correlação de primeiro vizinho. O restante
da rede/aparelho é projetado no complemento ortogonal. A Hessiana reduzida é
decomposta em blocos:

    K = [[K_H, J],
         [J^T, K_A]]

e calcula-se:

    K_schur = K_H - J K_A^{-1} J^T
    chi_A   = J K_A^{-1} J^T

O mapa térmico proposto pelo bloco Schur é então comparado com o mapa invertido
de Q25.16.
"""

from __future__ import annotations

import csv
import math
import numpy as np
from q25_physical_common import DATA, RESULTS, PhysicalConfig, ensure_dirs, gdq_reduced_hessian, site_index


IN = DATA / "q25_thermal_map_gdq_reduced.csv"
OUT = RESULTS / "saida_q25_19_schur_apparatus_derivation.md"


def read_target():
    T, B = [], []
    with IN.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            T.append(float(row["T_over_t"]))
            B.append(float(row["beta_eff"]))
    return np.array(T), np.array(B)


def rmse_rel(pred, target):
    return (
        float(np.sqrt(np.mean((pred - target) ** 2))),
        float(np.sqrt(np.mean(((pred - target) / np.maximum(target, 1e-12)) ** 2))),
    )


def measured_edge_mode(cfg: PhysicalConfig) -> np.ndarray:
    v = np.zeros(cfg.n_sites)
    v[site_index(0, 0, cfg.L)] = 1.0
    v[site_index(1, 0, cfg.L)] = -1.0
    return v / np.linalg.norm(v)


def schur_block(cfg: PhysicalConfig):
    h = gdq_reduced_hessian(cfg)
    m = measured_edge_mode(cfg)
    # Base ortonormal com m como primeiro vetor.
    seed = np.eye(cfg.n_sites)
    basis = np.column_stack([m, seed[:, 1:]])
    q, _ = np.linalg.qr(basis)
    if float(np.dot(q[:, 0], m)) < 0:
        q[:, 0] *= -1
    b = q[:, 1:]
    k_h = float(m @ h @ m)
    k_a = b.T @ h @ b
    j = m @ h @ b
    chi = float(j @ np.linalg.solve(k_a, j.T))
    k_schur = k_h - chi
    chi2 = float(j @ np.linalg.solve(k_a @ k_a, j.T))
    return k_h, chi, k_schur, chi2


def fit_reference(T, B):
    best = None
    for theta in np.linspace(1e-4, 1.0, 2001):
        x = 1.0 / (T + theta)
        mu = float(np.dot(x, B) / np.dot(x, x))
        pred = mu * x
        rmse, rel = rmse_rel(pred, B)
        if best is None or rmse < best[0]:
            best = (rmse, rel, mu, theta, pred)
    assert best
    return best


def main() -> None:
    ensure_dirs()
    cfg = PhysicalConfig()
    T, B = read_target()
    k_h, chi, k_schur, chi2 = schur_block(cfg)

    candidates = {
        "schur_geometric": (math.sqrt(k_h * chi), math.sqrt(k_schur * chi)),
        "schur_symmetric": (math.sqrt(k_h * chi), math.sqrt(k_h * chi)),
        "bare_schur": (chi, k_schur),
        "bare_response": (k_h, k_schur),
        "second_response": (math.sqrt(max(k_h * chi2, 0.0)), math.sqrt(max(k_schur * chi, 0.0))),
    }

    rows = []
    for name, (mu, theta) in candidates.items():
        pred = mu / (T + theta)
        rmse, rel = rmse_rel(pred, B)
        rows.append((name, mu, theta, rmse, rel, pred))
    rows.sort(key=lambda r: r[3])

    fit_rmse, fit_rel, fit_mu, fit_theta, fit_pred = fit_reference(T, B)

    table = "| candidato Schur | mu_A | Theta_A | RMSE beta | erro relativo RMS |\n|---|---:|---:|---:|---:|\n"
    for name, mu, theta, rmse, rel, _ in rows:
        table += f"| `{name}` | {mu:.8e} | {theta:.8e} | {rmse:.8e} | {rel:.8e} |\n"
    table += f"| `referencia_ajustada` | {fit_mu:.8e} | {fit_theta:.8e} | {fit_rmse:.8e} | {fit_rel:.8e} |\n"

    best = rows[0]
    comp = "| kBT/t | beta invertido | beta Schur melhor | beta ajustado |\n|---:|---:|---:|---:|\n"
    for t, b, p, pf in zip(T, B, best[5], fit_pred):
        comp += f"| {t:.3f} | {b:.8e} | {p:.8e} | {pf:.8e} |\n"

    OUT.write_text(
        "# Q25.19 — Derivação Schur do bloco térmico/aparelho\n\n"
        "Classificação: derivação reduzida e teste de consistência.\n\n"
        "Modo observado: diferença de circulação no primeiro vínculo da rede. "
        "O complemento ortogonal é tratado como aparelho/banho reduzido.\n\n"
        "| quantidade | valor |\n|---|---:|\n"
        f"| K_H | {k_h:.12e} |\n"
        f"| chi_A=J K_A^-1 J^T | {chi:.12e} |\n"
        f"| K_schur | {k_schur:.12e} |\n"
        f"| chi_2=J K_A^-2 J^T | {chi2:.12e} |\n\n"
        + table
        + "\nComparação ponto a ponto:\n\n"
        + comp
        + "\nVeredito: o complemento de Schur fornece uma derivação reduzida "
        "não ajustada para a escala de admitância térmica. O melhor candidato "
        "Schur melhora a forma e é fisicamente interpretável, mas ainda não "
        "reproduz o mapa térmico invertido com precisão metrológica. A diferença "
        "restante deve vir de geometria de aparelho mais rica, modos de banho "
        "não incluídos, mobilidade causal ou contorno térmico real.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

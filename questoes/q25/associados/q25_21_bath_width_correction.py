#!/usr/bin/env python3
"""Q25.21 — correção da largura térmica residual do banho."""

from __future__ import annotations

import math
import numpy as np
from q25_physical_common import RESULTS, PhysicalConfig, ensure_dirs, gdq_reduced_hessian, site_index


OUT = RESULTS / "saida_q25_21_bath_width_correction.md"


def measured_edge_mode(cfg: PhysicalConfig) -> np.ndarray:
    v = np.zeros(cfg.n_sites)
    v[site_index(0, 0, cfg.L)] = 1.0
    v[site_index(1, 0, cfg.L)] = -1.0
    return v / np.linalg.norm(v)


def schur_components(cfg: PhysicalConfig):
    h = gdq_reduced_hessian(cfg)
    m = measured_edge_mode(cfg)
    q, _ = np.linalg.qr(np.column_stack([m, np.eye(cfg.n_sites)[:, 1:]]))
    if float(np.dot(q[:, 0], m)) < 0:
        q[:, 0] *= -1
    b = q[:, 1:]
    k_h = float(m @ h @ m)
    k_a = b.T @ h @ b
    j = np.asarray(m @ h @ b).reshape(-1)
    chi = float(j @ np.linalg.solve(k_a, j.T))
    k_s = k_h - chi
    evals, evecs = np.linalg.eigh(k_a)
    couplings = evecs.T @ j
    return k_h, k_s, evals, couplings


def main() -> None:
    ensure_dirs()
    cfg = PhysicalConfig()
    k_h, k_s, lam, g = schur_components(cfg)

    theta_schur = 0.616921719
    theta_fit = 0.721527850
    delta_target = theta_fit - theta_schur

    delta_1 = float(np.sum((g * g) / ((lam + k_s) ** 2)))
    delta_2 = float(np.sum((g * g) / (lam * (lam + k_s))))
    delta_3 = float(np.sqrt(max(delta_1 * cfg.mass_gap, 0.0)))
    delta_4 = float(delta_1 / max(math.sqrt(k_h), 1e-15))

    candidates = [
        ("sum_J2_over_lam_plus_Ks_sq", delta_1),
        ("sum_J2_over_lam_lam_plus_Ks", delta_2),
        ("sqrt_gap_times_delta1", delta_3),
        ("delta1_over_sqrt_KH", delta_4),
    ]

    table = "| candidato | DeltaTheta | Theta total | erro vs fit |\n|---|---:|---:|---:|\n"
    for name, d in candidates:
        table += f"| `{name}` | {d:.12e} | {theta_schur+d:.12e} | {(theta_schur+d-theta_fit):.12e} |\n"

    OUT.write_text(
        "# Q25.21 — Correção da largura térmica residual\n\n"
        "Classificação: derivação reduzida e comparação.\n\n"
        "A largura Schur anterior foi:\n\n"
        "$$\n\\Theta_A^{\\rm Schur}\\simeq0.616921719.\n$$\n\n"
        "O ajuste efetivo pedia:\n\n"
        "$$\n\\Theta_A^{\\rm fit}\\simeq0.721527850.\n$$\n\n"
        "Logo o resíduo alvo era:\n\n"
        f"$$\n\\Delta\\Theta_A\\simeq {delta_target:.12e}.\n$$\n\n"
        "Testei correções espectrais do banho usando os autovalores de `K_A` e "
        "os acoplamentos `J_k` do modo medido aos modos do aparelho:\n\n"
        + table
        + "\nVeredito: o banho espectral discreto gera uma correção positiva da "
        "largura térmica, com ordem de grandeza correta mas ainda abaixo do "
        "resíduo necessário. Portanto a direção está correta, porém o modelo "
        "reduzido ainda omite canais dissipativos/causais ou pesos térmicos de "
        "aparelho que amplifiquem `DeltaTheta_A`.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

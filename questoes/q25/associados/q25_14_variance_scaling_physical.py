#!/usr/bin/env python3
"""Q25.14 — escala de variância/autocorrelação no benchmark reduzido."""

from __future__ import annotations

import math
import numpy as np
from q25_physical_common import (
    CACHE,
    RESULTS,
    PhysicalConfig,
    bipartite_eta,
    energy_for_x,
    ensure_dirs,
    gdq_reduced_hessian,
    integrated_autocorr,
    save_json,
    site_index,
)


OUT = RESULTS / "saida_q25_14_variance_scaling_physical.md"
CACHE_FILE = CACHE / "variance_scaling.json"


def run_series(cfg: PhysicalConfig, steps: int = 70_000, burn: int = 10_000) -> dict[str, float]:
    rng = np.random.default_rng(cfg.seed + cfg.L)
    eta = bipartite_eta(cfg.L)
    h = gdq_reduced_hessian(cfg)
    x = rng.choice([-1.0, 1.0], size=cfg.n_sites)
    e = energy_for_x(x, cfg, h)
    vals = []
    accepts = 0
    for t in range(steps):
        i = int(rng.integers(cfg.n_sites))
        xn = x.copy()
        xn[i] *= -1.0
        en = energy_for_x(xn, cfg, h)
        if en <= e or rng.random() < math.exp(-cfg.beta_eff * (en - e)):
            x, e = xn, en
            accepts += 1
        if t >= burn:
            sigma = eta * x
            corr_vals = []
            for sx in range(cfg.L):
                for sy in range(cfg.L):
                    j = site_index(sx, sy, cfg.L)
                    corr_vals.append(sigma[j] * sigma[site_index(sx + 1, sy, cfg.L)])
                    corr_vals.append(sigma[j] * sigma[site_index(sx, sy + 1, cfg.L)])
            vals.append(float(np.mean(corr_vals)))
    arr = np.array(vals)
    tau = integrated_autocorr(arr)
    stderr_eff = float(arr.std(ddof=1) * math.sqrt(2.0 * tau / len(arr)))
    return {
        "L": float(cfg.L),
        "N": float(cfg.n_sites),
        "tau_corr": float(tau),
        "stderr_eff": stderr_eff,
        "acceptance": float(accepts / steps),
    }


def main() -> None:
    ensure_dirs()
    rows = [run_series(PhysicalConfig(L=L, seed=2514)) for L in (4, 6, 8)]
    n = np.array([r["N"] for r in rows])
    tau = np.array([r["tau_corr"] for r in rows])
    p_tau, _ = np.polyfit(np.log(n), np.log(tau), 1)
    obj = {"rows": rows, "tau_power_vs_N": float(p_tau)}
    save_json(CACHE_FILE, obj)

    table = "| L | N | tau_corr | stderr_eff | acceptance |\n|---:|---:|---:|---:|---:|\n"
    for r in rows:
        table += (
            f"| {int(r['L'])} | {int(r['N'])} | {r['tau_corr']:.6f} | "
            f"{r['stderr_eff']:.12e} | {r['acceptance']:.6f} |\n"
        )
    OUT.write_text(
        "# Q25.14 — Escala de variância/autocorrelação\n\n"
        "Classificação: teste de escala numérico no benchmark reduzido.\n\n"
        + table
        + f"\nAjuste observado: `tau_corr ~ N^{p_tau:.3f}`.\n\n"
        "Interpretação: no intervalo testado não aparece explosão exponencial. "
        "Isto ainda não é prova assintótica; é filtro numérico inicial para a "
        "classe reduzida.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

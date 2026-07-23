#!/usr/bin/env python3
"""Q25.20 — valores C_s(1) previstos pela rota Schur."""

from __future__ import annotations

import csv
from q25_physical_common import DATA, RESULTS, PhysicalConfig, ensure_dirs, metropolis_correlations


OUT = RESULTS / "saida_q25_20_compare_schur_curve.md"


def main() -> None:
    ensure_dirs()
    mu = 0.554521554
    theta = 0.616921719
    rows = []
    with (DATA / "q25_referencias_experimentais.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["paper_id"] == "parsons_2016_fig2d_digitized" and r["observable"] == "C_s_r1":
                T = float(r["T_over_t"])
                exp = float(r["value"])
                err = float(r["error"])
                beta = mu / (T + theta)
                mc = metropolis_correlations(
                    PhysicalConfig(beta_eff=beta, seed=2700 + int(round(T * 1000))),
                    steps=80_000,
                    burn=10_000,
                )
                gdq = mc["C_s_r1"]
                rows.append((T, exp, err, beta, gdq, mc["C_s_r1_stderr"], (gdq - exp) / err))

    table = "| kBT/t | C_s(1) exp | erro exp | beta_Schur | C_s(1) GDQ-Schur | erro MC | z |\n"
    table += "|---:|---:|---:|---:|---:|---:|---:|\n"
    for T, exp, err, beta, gdq, mcerr, z in rows:
        table += f"| {T:.3f} | {exp:.8e} | {err:.3e} | {beta:.8e} | {gdq:.8e} | {mcerr:.3e} | {z:.3f} |\n"

    OUT.write_text(
        "# Q25.20 — Comparação direta da curva Schur\n\n"
        "Classificação: comparação fenomenológica externa usando o mapa Schur "
        "não ajustado de Q25.19.\n\n"
        + table
        + "\nVeredito: a rota Schur acerta muito bem o ponto intermediário "
        "`kBT/t=0.45`, mantém sinal correto em toda a série digitizada, mas "
        "superestima a correlação em `T=0` e em alta temperatura. O ponto "
        "`kBT/t=0.55` permanece suspeito por violar monotonicidade da própria "
        "digitização.\n",
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

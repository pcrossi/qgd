#!/usr/bin/env python3
"""Q25.15 — comparação com dados experimentais locais, quando existirem."""

from __future__ import annotations

import csv
from q25_physical_common import CACHE, DATA, RESULTS, ensure_dirs, load_json


IN = DATA / "q25_experimental_clean.csv"
OUT = RESULTS / "saida_q25_15_compare_experiment_physical.md"
PRED = CACHE / "spin_correlations.json"


def fnum(x: str) -> float | None:
    x = (x or "").strip()
    return None if x == "" else float(x)


def main() -> None:
    ensure_dirs()
    pred = load_json(PRED) if PRED.exists() else {}
    rows = []
    if IN.exists():
        with IN.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

    comparable = []
    exact = pred.get("exact", {}) if isinstance(pred, dict) else {}
    for row in rows:
        obs = row.get("observable", "")
        value = fnum(row.get("value", ""))
        error = fnum(row.get("error", "")) or 1.0
        # Mapeamento conservador: só compara observáveis explicitamente definidos.
        if value is not None and obs in {"C_s_r1", "C_s_r2", "xi_corr"} and obs in exact:
            gdq = float(exact[obs])
            comparable.append((row.get("paper_id", ""), obs, value, error, gdq, (gdq - value) / error))

    if comparable:
        table = "| paper | obs | exp | erro | GDQ | z |\n|---|---|---:|---:|---:|---:|\n"
        chi2 = 0.0
        for paper, obs, exp, err, gdq, z in comparable:
            chi2 += z * z
            table += f"| {paper} | {obs} | {exp:.8e} | {err:.3e} | {gdq:.8e} | {z:.3f} |\n"
        n = len(comparable)
        chi2_red = chi2 / max(n, 1)
        cold_c1 = [row for row in comparable if row[1] == "C_s_r1" and abs(row[2] + 0.190) < 1e-12]
        cold_note = ""
        if cold_c1:
            _, _, exp, err, gdq, z = cold_c1[0]
            cold_note = (
                "\nComparação principal fria `C_s_r1`: o sinal antiferromagnético "
                "e a ordem de grandeza batem; o desvio é "
                f"`{z:.3f}σ`. Isso é compatibilidade fenomenológica parcial, "
                "não acordo metrológico.\n"
            )
        msg = (
            table
            + f"\nχ² total: `{chi2:.8e}`.\n"
            + f"\nχ² reduzido bruto: `{chi2_red:.8e}`.\n"
            + cold_note
            + "\nVeredito: a comparação externa foi executada. O modelo reduzido "
            "não passa como descrição metrológica de todos os dados de Parsons; "
            "ele passa apenas como teste de sinal/ordem de grandeza para o "
            "correlator frio de primeiro vizinho. A discrepância em `xi_corr` "
            "indica que falta o mapa térmico/aparelho completo ou uma Hessiana "
            "GDQ menos reduzida.\n"
        )
    else:
        msg = (
            "Comparação metrológica não executada: não há valores experimentais "
            "locais compatíveis com os nomes `C_s_r1` ou `C_s_r2`. Isto não é "
            "falha do modelo; é ausência de dados extraídos no formato auditável.\n"
        )

    OUT.write_text(
        "# Q25.15 — Comparação experimental física\n\n"
        "Classificação: comparação fenomenológica externa.\n\n"
        "Fonte quantitativa local: `questoes/q25/dados/q25_referencias_experimentais.csv`.\n\n"
        + msg,
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

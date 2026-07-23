#!/usr/bin/env python3
"""Q25.05 — comparador experimental.

Classificação: comparação fenomenológica quando houver dados locais.
Sem valores experimentais locais, o script registra bloqueio honesto.
"""

from __future__ import annotations

from pathlib import Path
import csv
import math


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados" / "q25_referencias_experimentais.csv"
OUT = ROOT / "resultados" / "saida_q25_05_compare_experiment.md"


def parse_float(text: str) -> float | None:
    text = (text or "").strip()
    if not text:
        return None
    return float(text)


def gdq_placeholder_prediction(row: dict[str, str]) -> float | None:
    """Predição operacional mínima para teste de pipeline.

    Retorna None porque a predição física GDQ requer o operador/domínio do
    problema e não deve ser fabricada a partir do alvo experimental.
    """
    return None


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    comparable = []
    for row in rows:
        value = parse_float(row.get("value", ""))
        error = parse_float(row.get("error", ""))
        pred = gdq_placeholder_prediction(row)
        if value is not None and pred is not None:
            sigma = error if error and error > 0 else 1.0
            comparable.append((row["paper_id"], value, pred, sigma, (pred - value) / sigma))

    if comparable:
        chi2 = sum(z * z for *_, z in comparable)
        content = (
            "| paper | exp | GDQ | sigma | z |\n|---|---:|---:|---:|---:|\n"
            + "".join(f"| {p} | {v:.8e} | {pred:.8e} | {sig:.3e} | {z:.3f} |\n" for p, v, pred, sig, z in comparable)
            + f"\nχ² total: `{chi2:.8e}`.\n"
        )
    else:
        content = (
            "Não há comparação quantitativa ainda. Motivo: os dados experimentais "
            "locais ainda não têm valores numéricos extraídos e/ou a predição GDQ "
            "do observável correspondente ainda não foi implementada. O script "
            "está correto como bloqueio reprodutível, não como resultado negativo.\n"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# Q25.05 — Comparação experimental\n\n"
        "Classificação: comparação fenomenológica externa.\n\n"
        + content,
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

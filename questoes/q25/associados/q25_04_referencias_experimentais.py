#!/usr/bin/env python3
"""Q25.04 — validação de dados experimentais locais.

Classificação: preparação de benchmark experimental.

O script não baixa artigos nem inventa números. Ele valida o CSV local onde os
dados extraídos manualmente dos papers serão congelados.
"""

from __future__ import annotations

from pathlib import Path
import csv


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados" / "q25_referencias_experimentais.csv"
OUT = ROOT / "resultados" / "saida_q25_04_referencias_experimentais.md"

REQUIRED = [
    "paper_id",
    "observable",
    "U_over_t",
    "T_over_t",
    "doping",
    "site_distance",
    "value",
    "error",
    "figure",
    "notes",
]


def parse_float(text: str) -> float | None:
    text = (text or "").strip()
    if text == "":
        return None
    return float(text)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        rows = list(reader)

    if missing:
        raise SystemExit(f"CSV invalido; colunas ausentes: {missing}")

    quantitative = 0
    parse_errors = []
    for i, row in enumerate(rows, start=2):
        try:
            value = parse_float(row["value"])
            error = parse_float(row["error"])
            if value is not None:
                quantitative += 1
            if error is not None and error < 0:
                parse_errors.append((i, "error negativo"))
        except ValueError as exc:
            parse_errors.append((i, str(exc)))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "# Q25.04 — Referências experimentais locais\n\n"
        "Classificação: preparação de benchmark experimental.\n\n"
        "| item | valor |\n|---|---:|\n"
        f"| arquivo | `{DATA}` |\n"
        f"| linhas | {len(rows)} |\n"
        f"| linhas quantitativas | {quantitative} |\n"
        f"| erros de parse | {len(parse_errors)} |\n\n"
        + (
            "Nenhum dado quantitativo foi extraído ainda; o arquivo contém apenas "
            "metadados e DOIs. A comparação experimental fica bloqueada até a "
            "extração manual dos valores das figuras/tabelas.\n"
            if quantitative == 0
            else "Há dados quantitativos locais prontos para comparação.\n"
        ),
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

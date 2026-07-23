#!/usr/bin/env python3
"""Q25.10 — extrai/valida dados experimentais locais."""

from __future__ import annotations

import csv
from pathlib import Path
from q25_physical_common import DATA, RESULTS, ensure_dirs


IN = DATA / "q25_referencias_experimentais.csv"
OUT = RESULTS / "saida_q25_10_extract_experimental_data.md"
CLEAN = DATA / "q25_experimental_clean.csv"


def fnum(x: str) -> float | None:
    x = (x or "").strip()
    return None if x == "" else float(x)


def main() -> None:
    ensure_dirs()
    with IN.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    quantitative = []
    errors = []
    for i, row in enumerate(rows, start=2):
        try:
            value = fnum(row.get("value", ""))
            error = fnum(row.get("error", ""))
            if value is not None:
                quantitative.append(row)
            if error is not None and error < 0:
                errors.append((i, "error negativo"))
        except Exception as exc:  # noqa: BLE001
            errors.append((i, str(exc)))

    if rows:
        with CLEAN.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(quantitative)

    OUT.write_text(
        "# Q25.10 — Dados experimentais locais\n\n"
        "Classificação: preparação de benchmark experimental.\n\n"
        "| item | valor |\n|---|---:|\n"
        f"| arquivo bruto | `{IN}` |\n"
        f"| arquivo limpo | `{CLEAN}` |\n"
        f"| linhas totais | {len(rows)} |\n"
        f"| linhas quantitativas | {len(quantitative)} |\n"
        f"| erros de validação | {len(errors)} |\n\n"
        + (
            "Ainda não há valores experimentais quantitativos locais. O benchmark "
            "físico será executado como validação interna e ficará bloqueado para "
            "comparação metrológica externa.\n"
            if not quantitative
            else "Há dados quantitativos locais prontos para comparação.\n"
        ),
        encoding="utf-8",
    )
    print(OUT)


if __name__ == "__main__":
    main()

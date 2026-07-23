#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `inventario logico` associada ao capítulo `26_logical_status`.
Inventário lógico do Capítulo 26.

Classificação:
    checagem documental / inventário.

Este script não calcula uma previsão física. Ele gera uma tabela autocontida
com a classificação lógica usada no capítulo: axiomas, definições, resultados
condicionais, reduções e programas futuros.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_inventario_logico.md"


@dataclass(frozen=True)
class Entry:
    name: str
    category: str
    status: str


ENTRIES = [
    Entry("ação oficial", "axioma", "fixa"),
    Entry("estrutura Hermitiana/Bismut", "axioma geométrico", "fixa"),
    Entry("contorno causal gamma", "dado de problema", "declarado"),
    Entry("rho=exp(-(f+fbar)/2)", "definição", "não reabrir localmente"),
    Entry("S_R=hbar(f-fbar)/(2i)", "definição", "não reabrir localmente"),
    Entry("U=rho/(4pi z_tau)^n", "definição", "não reabrir localmente"),
    Entry("continuidade de Madelung", "derivação", "setor canônico"),
    Entry("Hamilton-Jacobi-Bohm", "derivação", "setor canônico"),
    Entry("equação métrica ponderada", "derivação", "variacional"),
    Entry("ponte global-local", "teorema condicional", "seis lemas e colagem declarada"),
    Entry("herança de alpha", "teorema condicional", "normalização global"),
    Entry("três gerações", "teorema condicional", "classe topológica e três estômatos"),
    Entry("Yang-Mills efetivo", "redução efetiva", "domínio operacional de cor"),
    Entry("hidrogênio", "redução efetiva", "Dirac-Bismut estrutural"),
    Entry("decaimento alfa", "prova de conceito reduzida", "Schur/Riesz e canal alfa"),
    Entry("buraco negro regular", "redução efetiva", "covariante 8D futuro"),
    Entry("solver cosmológico integrado", "programa futuro", "metrologia conjunta"),
    Entry("aparelhos reais", "programa futuro", "contornos e materiais reais"),
]


def main() -> None:
    counts: dict[str, int] = {}
    for entry in ENTRIES:
        counts[entry.category] = counts.get(entry.category, 0) + 1

    lines: list[str] = []
    lines.append("# Saída — inventário lógico\n\n")
    lines.append("Classificação: checagem documental / inventário.\n\n")
    lines.append("## Entradas\n\n")
    lines.append("| item | categoria | status |\n")
    lines.append("|---|---|---|\n")
    for entry in ENTRIES:
        lines.append(f"| {entry.name} | {entry.category} | {entry.status} |\n")

    lines.append("\n## Contagem por categoria\n\n")
    lines.append("| categoria | quantidade |\n")
    lines.append("|---|---:|\n")
    for category, count in sorted(counts.items()):
        lines.append(f"| {category} | {count} |\n")

    lines.append("\n## Veredito\n\n")
    lines.append(
        "O inventário separa entradas fundamentais, definições, derivações, "
        "teoremas condicionais, reduções e programas futuros. Ele não deve ser "
        "lido como prova física, mas como controle de consistência editorial.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()


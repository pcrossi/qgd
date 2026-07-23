#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `comparacoes preservadas` associada ao capítulo `26_logical_status`.
Comparações numéricas preservadas no manuscrito.

Classificação:
    consolidação documental.

O script não recalcula os modelos físicos. Ele reúne números já incorporados
aos capítulos anteriores para verificar que o capítulo lógico mantém status e
comparações explícitos.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_comparacoes_preservadas.md"


@dataclass(frozen=True)
class Comparison:
    observable: str
    gdq: str
    reference: str
    error: str
    status: str


COMPARISONS = [
    Comparison("alpha^-1 médio", "137.036082448164", "137.035999", "6.08e-7 relativo", "herança estrutural"),
    Comparison("m_mu/m_e", "206.768593470629", "206.768283", "1.50e-6 relativo", "redução condicional"),
    Comparison("m_tau/m_e", "3477.446405098382", "3477.15", "8.52e-5 relativo", "redução condicional"),
    Comparison("v_GDQ", "246.111195996 GeV", "246.21965 GeV", "-0.044048%", "escala estrutural"),
    Comparison("r_p^surf", "0.840778765432 fm", "0.84087 fm", "-0.010850%", "raio estrutural"),
    Comparison("hidrogênio hiperfino", "1.420405718790905e9 Hz", "1.420405751768e9 Hz", "-32.977095 Hz", "metrologia líder"),
    Comparison("alfa RMS", "0.067894 décadas", "dataset diagnóstico", "—", "prova de conceito"),
    Comparison("rho_Lambda", "6.136532599384e-27 kg/m^3", "5.842445930612e-27 kg/m^3", "+5.033622%", "contorno cosmológico"),
]


def main() -> None:
    lines: list[str] = []
    lines.append("# Saída — comparações preservadas\n\n")
    lines.append("Classificação: consolidação documental.\n\n")
    lines.append("| observável | GDQ/reduzido | referência | erro | status |\n")
    lines.append("|---|---:|---:|---:|---|\n")
    for c in COMPARISONS:
        lines.append(f"| {c.observable} | {c.gdq} | {c.reference} | {c.error} | {c.status} |\n")

    lines.append("\n## Regra de leitura\n\n")
    lines.append(
        "Essas comparações reforçam rotas específicas. Elas não transformam "
        "reduções condicionais em provas variacionais completas.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()


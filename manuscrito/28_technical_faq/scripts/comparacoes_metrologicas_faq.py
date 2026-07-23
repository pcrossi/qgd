#!/usr/bin/env python3
"""Tabela metrológica curta do FAQ técnico.

Classificação:
    consolidação documental / comparação fenomenológica.

Este script não ajusta parâmetros. Ele apenas regenera, de forma autocontida,
a tabela curta de valores que o FAQ usa para explicar a diferença entre
comparação numérica e prova variacional completa.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_comparacoes_metrologicas_faq.md"


@dataclass(frozen=True)
class Comparison:
    observable: str
    gdq: float
    reference: float
    unit: str
    status: str

    @property
    def absolute_error(self) -> float:
        return self.gdq - self.reference

    @property
    def relative_error(self) -> float:
        return self.absolute_error / self.reference


COMPARISONS = [
    Comparison("alpha^-1", 137.036082448164, 137.035999, "adimensional", "herança estrutural"),
    Comparison("m_mu/m_e", 206.768593470629, 206.768283, "adimensional", "redução condicional"),
    Comparison("m_tau/m_e", 3477.446405098382, 3477.15, "adimensional", "redução condicional"),
    Comparison("v_EW", 246.111195996, 246.21965, "GeV", "escala estrutural"),
    Comparison("r_p", 0.840778765432, 0.84087, "fm", "raio estrutural"),
    Comparison(
        "nu_hfs_H",
        1_420_405_718.790905,
        1_420_405_751.768,
        "Hz",
        "metrologia líder",
    ),
    Comparison(
        "rho_Lambda",
        6.136532599384e-27,
        5.842445930612e-27,
        "kg/m^3",
        "contorno cosmológico",
    ),
]


def main() -> None:
    lines = ["# Saída — comparações metrológicas do FAQ\n\n"]
    lines.append("Classificação: consolidação documental / comparação fenomenológica.\n\n")
    lines.append("| observável | GDQ | referência | unidade | erro absoluto | erro relativo | status |\n")
    lines.append("|---|---:|---:|---|---:|---:|---|\n")
    for item in COMPARISONS:
        lines.append(
            "| "
            f"{item.observable} | "
            f"{item.gdq:.15g} | "
            f"{item.reference:.15g} | "
            f"{item.unit} | "
            f"{item.absolute_error:.12g} | "
            f"{item.relative_error:.12g} | "
            f"{item.status} |\n"
        )
    lines.append("\n## Regra de leitura\n\n")
    lines.append(
        "A tabela documenta compatibilidades preservadas. O status de cada linha "
        "continua determinado pela cadeia dedutiva correspondente, não apenas "
        "pela proximidade numérica.\n"
    )
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

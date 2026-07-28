#!/usr/bin/env python3
"""Classificador simples de resultados numéricos GDQ.

Classificação:
    ferramenta documental / exemplo de regra.

O objetivo é tornar explícito quando um cálculo deve ser chamado de avaliação
direta, teste de consistência, comparação fenomenológica ou previsão cega.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_classificacao_resultado.md"


@dataclass(frozen=True)
class Scenario:
    name: str
    formula_derived: bool
    target_used_before: bool
    parameters_frozen: bool
    comparison_performed: bool
    has_convergence: bool
    has_analytic_limit: bool
    apparatus_measured_independently: bool
    uncertainty_reported: bool
    boundary_sensitivity_reported: bool


SCENARIOS = [
    Scenario(
        "fórmula já derivada, sem dado alvo",
        True, False, False, False, False, True, False, False, False,
    ),
    Scenario(
        "malha refinada contra limite analítico",
        True, False, True, False, True, True, False, True, True,
    ),
    Scenario(
        "parâmetro inferido do alvo",
        False, True, False, True, False, False, False, False, False,
    ),
    Scenario(
        "fórmula congelada e comparação posterior",
        True, False, True, True, True, False, True, True, True,
    ),
    Scenario(
        "previsão calculada sem alvo, convergente e com aparelho medido",
        True, False, True, True, True, True, True, True, True,
    ),
]


def classify(s: Scenario) -> str:
    if s.target_used_before:
        return "engenharia inversa ou ajuste"
    blind_ready = (
        s.formula_derived
        and s.parameters_frozen
        and s.apparatus_measured_independently
        and s.has_convergence
        and s.uncertainty_reported
        and s.boundary_sensitivity_reported
    )
    if blind_ready and s.comparison_performed:
        return "elegível a previsão cega; força metrológica exige requisitos adicionais"
    if s.has_convergence and s.has_analytic_limit and not s.comparison_performed:
        return "teste de convergência e consistência"
    if s.formula_derived and s.has_convergence and not s.comparison_performed:
        return "teste de convergência"
    if s.formula_derived and s.has_convergence and s.parameters_frozen and s.comparison_performed:
        return "comparação fenomenológica controlada"
    if s.formula_derived and s.has_analytic_limit:
        return "teste de consistência"
    if s.formula_derived:
        return "avaliação direta"
    return "exploratório"


def main() -> None:
    lines = ["# Saída — classificador de resultado\n\n"]
    lines.append("Classificação: ferramenta documental / exemplo de regra.\n\n")
    lines.append("| cenário | classificação |\n")
    lines.append("|---|---|\n")
    for scenario in SCENARIOS:
        lines.append(f"| {scenario.name} | {classify(scenario)} |\n")
    lines.append("\n## Regra\n\n")
    lines.append("Se o alvo experimental entrou antes da fórmula, não chamar de previsão.\n")
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

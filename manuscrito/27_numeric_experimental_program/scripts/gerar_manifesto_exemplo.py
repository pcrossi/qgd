#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `gerar manifesto exemplo` associada ao capítulo `27_numeric_experimental_program`.
Gera um manifesto mínimo para scripts GDQ.

Classificação:
    ferramenta documental.

Este script não calcula um observável físico. Ele produz um modelo de saída
que todo novo script numérico/simbólico deve preencher para declarar domínio,
contorno, operador, projetor, parâmetros e uso de dados experimentais.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_manifesto_exemplo.md"

FIELDS = [
    ("Equação/funcional", "Qual parte de S_GDQ ou qual redução está sendo avaliada."),
    ("Background Phi_*", "Solução, ansatz reduzido ou fixture declarado."),
    ("Domínio", "Intervalo, variedade, malha ou espaço espectral."),
    ("Contorno", "Dirichlet, Neumann, Robin, DtN/Schur ou dado externo."),
    ("Vínculos", "Carga, fluxo, normalização, calibre, fase, bordos."),
    ("Operador/Hessiana", "K_phys, Jacobi, DtN, Schur ou operador reduzido."),
    ("Projetor físico", "Como modos de gauge/coordenada são removidos."),
    ("Fonte/aparelho", "J_app ou parâmetro externo independente."),
    ("Observável", "Grandeza comparada ou diagnosticada."),
    ("Parâmetros universais", "Constantes vindas da teoria."),
    ("Parâmetros de aparelho", "Dados independentes do experimento/material."),
    ("Parâmetros numéricos", "Malha, tolerância, solver, seed."),
    ("Uso de dados", "Se o alvo experimental entrou antes da comparação."),
    ("Classificação", "Avaliação, convergência, consistência, ajuste, comparação ou previsão."),
]


def main() -> None:
    lines = ["# Saída — manifesto mínimo de script GDQ\n\n"]
    lines.append("Classificação: ferramenta documental.\n\n")
    lines.append("| Campo | Conteúdo esperado |\n")
    lines.append("|---|---|\n")
    for field, description in FIELDS:
        lines.append(f"| {field} | {description} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("Um script que não consegue preencher esses campos ainda é exploratório.\n")
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()


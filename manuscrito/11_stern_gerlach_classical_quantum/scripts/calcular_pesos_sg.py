#!/usr/bin/env python3
"""
GDQ — Capítulo 11 / Pesos Stern--Gerlach

Objetivo:
    Calcular p_±=(1±a·n)/2 para vários ângulos entre preparação e aparelho.

Fonte teórica:
    manuscrito/11_stern_gerlach_classical_quantum/notes/pesos_born_sg.md
    manuscrito/11_stern_gerlach_classical_quantum/notes/

Classificação:
    Teste de consistência operacional. Não é previsão metrológica.

Saída:
    scripts/saida_calcular_pesos_sg.md
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_calcular_pesos_sg.md"

    angles = [0, 30, 60, 90, 120, 180]
    rows = []
    for deg in angles:
        theta = math.radians(deg)
        p_plus = math.cos(theta / 2) ** 2
        p_minus = math.sin(theta / 2) ** 2
        rows.append((deg, p_plus, p_minus, p_plus + p_minus))

    table = "\n".join(
        f"| {deg} | {pp:.12f} | {pm:.12f} | {s:.12f} |"
        for deg, pp, pm, s in rows
    )

    text = f"""# Saída — pesos angulares Stern--Gerlach

Classificação: teste de consistência operacional.

| theta graus | p_plus | p_minus | soma |
|---:|---:|---:|---:|
{table}

Interpretação: os pesos dependem do ângulo entre preparação e eixo do aparelho;
dois canais não implicam pesos iguais.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

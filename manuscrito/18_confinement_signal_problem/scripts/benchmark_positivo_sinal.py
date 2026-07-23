#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `benchmark positivo sinal` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / Benchmark positivo do problema do sinal.

Registra os números finais/reduzidos do benchmark do problema do sinal sem reexecutar a cadeia
histórica completa. Classificação: benchmark reduzido, não prova geral.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_benchmark_positivo_sinal.md"

    exact = -0.1698717343244
    mc = -0.16836
    stderr = 6.296327845454e-4
    z = (mc - exact) / stderr
    acceptance = 0.75515
    n_conf = 65536

    text = f"""# Saída — benchmark positivo do problema do sinal

Classificação: benchmark reduzido; não prova algorítmica geral.

| quantidade | valor |
|---|---:|
| configurações exatas | {n_conf} |
| C_s(1) exato | {exact:.15e} |
| C_s(1) MC | {mc:.15e} |
| stderr MC | {stderr:.15e} |
| z interno | {z:.6f} |
| aceitação | {acceptance:.12f} |

Interpretação: a medida é positiva e a correlação antiferromagnética aparece
por circulação/holonomia, não por peso negativo.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

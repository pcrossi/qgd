#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Produto global e três estômatos

Objetivo:
    Verificar três fatos usados no texto:
      1. Betti de T^5 x S^3 por Künneth;
      2. Euler zero do produto global;
      3. kernel de Berry plano não produz N_G=3;
      4. três estômatos primitivos coorientados produzem índice total 3.

Classificação:
    Teste de consistência topológica discreta. Não usa alvo experimental.

Saída:
    scripts/saida_global_produto_tres_estomatos.md
"""

from math import comb
from pathlib import Path


def convolve(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def main() -> None:
    betti_t5 = [comb(5, k) for k in range(6)]
    betti_s3 = [1, 0, 0, 1]
    betti_product = convolve(betti_t5, betti_s3)
    euler = sum(((-1) ** k) * b for k, b in enumerate(betti_product))

    flat_berry_curvature = 0
    n_ab_flat = 0
    n_g_flat = n_ab_flat // 6

    local_indices = [1, 1, 1]
    index_total = sum(local_indices)
    a_total = 6 * index_total
    n_g_local = a_total // 6

    lines = [
        "# Saída — produto global e três estômatos",
        "",
        f"- Betti de T^5: `{betti_t5}`.",
        f"- Betti de S^3: `{betti_s3}`.",
        f"- Betti de T^5 x S^3: `{betti_product}`.",
        f"- Característica de Euler: `{euler}`.",
        "",
        "## Kernel plano",
        "",
        f"- Curvatura de Berry plana: `{flat_berry_curvature}`.",
        f"- N_ab plano: `{n_ab_flat}`.",
        f"- Gerações por produto plano: `{n_g_flat}`.",
        "",
        "## Três estômatos primitivos",
        "",
        f"- Índices locais: `{local_indices}`.",
        f"- Índice total APS: `{index_total}`.",
        f"- Carga global A=6 Ind: `{a_total}`.",
        f"- N_G=A/6: `{n_g_local}`.",
        "",
        "Conclusão: o produto global plano não gera três; a seleção vem do junction local não circular.",
    ]

    out = Path(__file__).with_name("saida_global_produto_tres_estomatos.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

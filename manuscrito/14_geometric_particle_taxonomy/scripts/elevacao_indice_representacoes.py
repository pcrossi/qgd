#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Elevação do índice às representações

Objetivo:
    Verificar a contagem de componentes de Weyl de uma geração efetiva e a
    elevação aditiva para três unidades de índice.

Classificação:
    Verificação simbólica discreta. Não há ajuste, dado experimental ou
    calibração.

Saída:
    scripts/saida_elevacao_indice_representacoes.md
"""

from pathlib import Path


MULTIPLETS = [
    ("Q", 3, 2, "1/6"),
    ("u^c", 3, 1, "-2/3"),
    ("d^c", 3, 1, "1/3"),
    ("L", 1, 2, "-1/2"),
    ("e^c", 1, 1, "1"),
]


def main() -> None:
    total_one = sum(color * weak for _, color, weak, _ in MULTIPLETS)
    total_three = 3 * total_one

    lines = [
        "# Saída — elevação do índice às representações",
        "",
        "| Multiplete | dim cor | dim fraca | Y | componentes Weyl |",
        "|---|---:|---:|---:|---:|",
    ]

    for name, color, weak, hypercharge in MULTIPLETS:
        lines.append(
            f"| `{name}` | {color} | {weak} | {hypercharge} | {color * weak} |"
        )

    lines += [
        "",
        f"- Total por unidade local de índice: `{total_one}` componentes de Weyl.",
        f"- Total por três estômatos: `{total_three}` componentes de Weyl.",
        "",
        "Conclusão: a unidade APS local conta gerações; a hipercarga é uma linha separada.",
    ]

    out = Path(__file__).with_name("saida_elevacao_indice_representacoes.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

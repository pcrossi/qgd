#!/usr/bin/env python3
"""
GDQ — Capítulo 2 / Medida ponderada e dimensão do kernel.

Objetivo:
    Verificar de modo autocontido a conta dimensional usada no Capítulo 2:
    se o bulk local tem dimensão real d = 2n = 8, o fator de kernel plano
    associado à medida ponderada tem potência d/2 = n = 4.

Fonte teórica:
    manuscrito/02_geometrization/02.2 - Domínio fundamental e dimensão.md
    manuscrito/02_geometrization/02.5 - Medida ponderada e kernel de calor.md
    manuscrito/notes/geometrization/Medida GDQ, dimensão do kernel e variação.md

Classificação:
    Teste simbólico/ilustração dimensional. Não é previsão física.

Equação:
    K_d(z_tau) = (4*pi*z_tau)^(-d/2)
    U = rho * K_d(z_tau)

Domínio e contorno:
    Não há domínio diferencial; trata-se de checagem algébrica da potência.

Parâmetros:
    Universais/estruturais:
        d = 8
        n = d/2 = 4
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        nenhum

Saída:
    saida_verificar_dimensao_kernel.md

Observação:
    Nenhum alvo experimental é usado.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent


def kernel_power(real_dimension: int) -> float:
    """Retorna a potência d/2 do kernel plano em dimensão real d."""
    return real_dimension / 2


def main() -> None:
    real_dimension = 8
    complex_dimension = real_dimension // 2
    power = kernel_power(real_dimension)
    expected = complex_dimension
    ok = power == expected == 4

    lines: list[str] = []
    lines.append("# Saída — verificação da dimensão do kernel\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico/ilustração dimensional. Não é previsão física.\n\n")
    lines.append("## Entrada estrutural\n\n")
    lines.append(f"- Dimensão real do bulk local: `{real_dimension}`.\n")
    lines.append(f"- Dimensão complexa correspondente: `{complex_dimension}`.\n\n")
    lines.append("## Fórmula verificada\n\n")
    lines.append("Para um kernel plano em dimensão real $d$:\n\n")
    lines.append("$$\n")
    lines.append("K_d(z_\\tau)=(4\\pi z_\\tau)^{-d/2}.\n")
    lines.append("$$\n\n")
    lines.append("Logo, para $d=8$:\n\n")
    lines.append("$$\n")
    lines.append("K_8(z_\\tau)=(4\\pi z_\\tau)^{-4}.\n")
    lines.append("$$\n\n")
    lines.append("## Resultado\n\n")
    lines.append("| Quantidade | Valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $d$ | {real_dimension} |\n")
    lines.append(f"| $d/2$ | {power:.0f} |\n")
    lines.append(f"| $n$ | {complex_dimension} |\n")
    lines.append(f"| Potência esperada | {expected} |\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída confirma apenas a conta dimensional do kernel. ")
    lines.append("Ela não seleciona dinamicamente o bulk local.\n")

    out = OUT / "saida_verificar_dimensao_kernel.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()


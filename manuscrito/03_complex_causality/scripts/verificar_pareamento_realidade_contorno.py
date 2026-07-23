#!/usr/bin/env python3
"""
GDQ — Capítulo 3 / Pareamento conjugado e realidade da ação.

Objetivo:
    Ilustrar que, quando segmentos de contorno aparecem em pares conjugados,
    suas contribuições complexas somam uma quantidade real.

Fonte teórica:
    manuscrito/03_complex_causality/03.5 - Realidade da ação e conjugação do contorno.md
    manuscrito/notes/causality/Realidade de uma ação integrada em contorno complexo.md

Classificação:
    Teste simbólico de pareamento conjugado. Não é previsão física.

Equação:
    I_total = I + conjugate(I) = 2 Re(I)

Domínio e contorno:
    Modelo algébrico de dois ramos conjugados; sem EDP.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        amostras complexas arbitrárias.

Saída:
    saida_verificar_pareamento_realidade_contorno.md

Observação:
    Nenhum alvo experimental é usado. O teste ilustra o pareamento; a
    admissibilidade de um contorno físico é hipótese geométrica do capítulo.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent


def main() -> None:
    samples = [
        1.2 + 0.4j,
        -0.7 + 2.3j,
        0.0 - 1.1j,
        3.5 + 0.0j,
    ]
    rows = []
    for value in samples:
        paired = value + value.conjugate()
        rows.append((value, paired, abs(paired.imag)))

    ok = all(err < 1e-14 for _, _, err in rows)

    lines: list[str] = []
    lines.append("# Saída — pareamento conjugado e realidade\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico de pareamento conjugado. Não é previsão física.\n\n")
    lines.append("## Identidade\n\n")
    lines.append("Se um ramo contribui com $I$ e o ramo refletido contribui com $\\bar I$, então:\n\n")
    lines.append("$$\n")
    lines.append("I+\\bar I=2\\operatorname{Re}I.\n")
    lines.append("$$\n\n")
    lines.append("## Casos arbitrários\n\n")
    lines.append("| $I$ | $I+\\bar I$ | parte imaginária residual |\n")
    lines.append("|---:|---:|---:|\n")
    for value, paired, err in rows:
        lines.append(
            f"| `{value.real:.6g}{value.imag:+.6g}j` | "
            f"`{paired.real:.6g}{paired.imag:+.6g}j` | {err:.3e} |\n"
        )
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou: o pareamento conjugado produz contribuição real.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída não prova que todo contorno é admissível; apenas ilustra o mecanismo algébrico usado no teorema condicional.\n")

    out = OUT / "saida_verificar_pareamento_realidade_contorno.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()


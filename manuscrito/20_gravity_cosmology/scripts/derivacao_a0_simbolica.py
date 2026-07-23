#!/usr/bin/env python3
"""
Derivação simbólica e dimensional da aceleração crítica galáctica da GDQ.

Classificação:
    avaliação simbólica/dimensional de fórmula reduzida.

O script não ajusta parâmetros ao valor fenomenológico de MOND/RAR. Ele mostra:

1. o dado de contorno cosmológico R_H=c/H0;
2. a aceleração de horizonte a_H=c^2/R_H=cH0;
3. a projeção circular por ciclo, a0=a_H/(2*pi);
4. a distinção entre a escala principal e a escala auxiliar de de Sitter.

As comparações numéricas ficam no script `calcular_a0_galactico.py`.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_derivacao_a0_simbolica.md"


def main() -> None:
    lines = [
        "---",
        'title: "Saída — derivação simbólica de a0"',
        "---",
        "",
        "# Saída — derivação simbólica de $a_0$",
        "",
        "## Cadeia",
        "",
        "$$",
        "R_H=\\frac{c}{H_0}",
        "$$",
        "",
        "$$",
        "a_H=\\frac{c^2}{R_H}=cH_0",
        "$$",
        "",
        "$$",
        "a_0^{\\rm GDQ}=\\frac{a_H}{2\\pi}=\\frac{cH_0}{2\\pi}",
        "$$",
        "",
        "## Dimensão",
        "",
        "$$",
        "[cH_0]=\\frac{L}{T}\\frac{1}{T}=\\frac{L}{T^2}",
        "$$",
        "",
        "Logo $a_0^{\\rm GDQ}$ tem dimensão de aceleração.",
        "",
        "## Escala auxiliar",
        "",
        "$$",
        "a_{\\rm dS}^{(2\\pi)}=\\frac{cH_0\\sqrt{\\Omega_\\Lambda}}{2\\pi}",
        "$$",
        "",
        "Essa escala usa o fator de de Sitter e não é a definição principal de $a_0^{\\rm GDQ}$.",
        "",
        "## Classificação",
        "",
        "Verificação simbólica/dimensional. Nenhum valor experimental de MOND entra na dedução.",
        "",
    ]
    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

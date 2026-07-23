#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `comparar tensao raios confinamento` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / comparação de tensão por raios.

Compara a tensão reduzida sigma=pi*hbarc/r^2 para três raios:
0.86 fm, raio da hierarquia leptônica/estrutura bariônica e raio efetivo comprimido.
"""

from __future__ import annotations

from pathlib import Path
import math


def sigma(hbarc: float, r: float) -> float:
    return math.pi * hbarc / (r * r)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_comparar_tensao_raios_confinamento.md"

    hbarc = 0.1973269804
    ref = 0.89
    radii = [
        ("raio inicial 0.86 fm", 0.86),
        ("hierarquia leptônica e estrutura bariônica", 0.84077876545),
        ("efetivo comprimido", 0.8354),
    ]

    lines = [
        "# Saída — comparação de tensão por raios",
        "",
        "Classificação: comparação fenomenológica posterior.",
        "",
        "| caso | r fm | sigma GeV/fm | desvio vs 0.89 |",
        "|---|---:|---:|---:|",
    ]
    for label, r in radii:
        sig = sigma(hbarc, r)
        lines.append(f"| {label} | {r:.12f} | {sig:.12f} | {(sig-ref)/ref:.6%} |")
    lines += [
        "",
        "Interpretação: o raio efetivo comprimido praticamente fecha a escala de",
        "tensão, mas permanece setorial até ser rederivado no mesmo background do tubo.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

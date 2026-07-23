#!/usr/bin/env python3
"""Compara W on-shell dos ramos gaussiano exterior e cilíndrico."""

from __future__ import annotations

import argparse
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_comparar_acoes_estacionarias_sg.md"),
    )
    args = parser.parse_args()
    x_c = 1.5
    q2 = math.exp(-x_c) * (1.0 + x_c)
    f0_gaussian = math.log(q2)
    mean_x = (x_c**2 + 2.0 * x_c + 2.0) / (x_c + 1.0)
    bulk_gaussian = 2.0 * mean_x + f0_gaussian - 4.0
    boundary_gaussian = -3.0 * x_c / (1.0 + x_c)
    total_gaussian = bulk_gaussian + boundary_gaussian
    total_cylinder = 0.5 * math.log(math.pi) - 1.5
    difference = total_cylinder - total_gaussian
    lines = [
        "# Saída — comparação de ações estacionárias",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| $W_G$ bulk | {bulk_gaussian:.12e} |",
        f"| $W_G$ boundary | {boundary_gaussian:.12e} |",
        f"| $W_G$ total | {total_gaussian:.12e} |",
        f"| $W_{{\\rm cylinder}}$ | {total_cylinder:.12e} |",
        f"| $W_{{\\rm cylinder}}-W_G$ | {difference:.12e} |",
        "",
        f"- cilindro tem menor $W$: `{difference < 0}`",
        "",
        "Classificação: comparação reduzida de ramos estacionários; não é metrologia",
        "final de aparelho real.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

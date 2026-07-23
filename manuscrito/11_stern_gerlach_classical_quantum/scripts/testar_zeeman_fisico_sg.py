#!/usr/bin/env python3
"""Teste dimensional de Delta e v com dados externos de um aparelho SG."""

from __future__ import annotations

import argparse
import math
from pathlib import Path


E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
MU_B = 9.2740100657e-24
HBAR = 1.054571817e-34


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--g-geom", type=float, required=True)
    parser.add_argument("--b-perp-tesla", type=float, required=True)
    parser.add_argument("--gradient-tesla-per-m", type=float, required=True)
    parser.add_argument("--speed-m-per-s", type=float, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("saida_testar_zeeman_fisico_sg.md"),
    )
    args = parser.parse_args()
    gyromagnetic = abs(args.g_geom) * MU_B / HBAR
    delta = gyromagnetic * abs(args.b_perp_tesla)
    velocity = gyromagnetic * abs(args.speed_m_per_s * args.gradient_tesla_per_m)
    probability = math.exp(-math.pi * delta**2 / (2.0 * velocity))
    lines = [
        "# Saída — teste dimensional Zeeman para aparelho externo",
        "",
        "Parâmetros usados no teste:",
        "",
        f"- $g_{{\\rm geom}}={args.g_geom}$",
        f"- $B_\\perp={args.b_perp_tesla}\\,{{\\rm T}}$",
        f"- $\\nabla B_\\parallel={args.gradient_tesla_per_m}\\,{{\\rm T/m}}$",
        f"- $u={args.speed_m_per_s}\\,{{\\rm m/s}}$",
        "",
        "Resultado:",
        "",
        f"- $\\Delta={delta:.12e}\\,{{\\rm s}}^{{-1}}$",
        f"- $v={velocity:.12e}\\,{{\\rm s}}^{{-2}}$",
        f"- $\\Delta^2/v={delta**2/velocity:.12e}$",
        f"- $P_{{\\rm LZ}}={probability:.12e}$",
        "",
        "Este cálculo usa dados explícitos de aparelho. Ele testa a conversão",
        "dimensional do canal Zeeman geométrico, não fixa por si só a impedância",
        "microscópica $\\mathsf R_{\\rm SG}$.",
    ]
    report = "\n".join(lines) + "\n"
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

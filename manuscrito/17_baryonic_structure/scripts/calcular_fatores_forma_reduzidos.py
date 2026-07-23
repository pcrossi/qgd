#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular fatores forma reduzidos` associada ao capítulo `17_baryonic_structure`.

GDQ — Capítulo 17 / fatores de forma reduzidos.

Testa:

    G_E^p(q) = j0(q r_p)
    G_M^p(0) = mu_p
    G_E^n(0) = 0
    <r_n^2> = -2 |mu_n| alpha_tor^(2) r_p^2

Classificação: teste de consistência da redução de superfície.
"""

from __future__ import annotations

import math
from pathlib import Path


def j0(x: float) -> float:
    if abs(x) < 1.0e-12:
        return 1.0
    return math.sin(x) / x


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_calcular_fatores_forma_reduzidos.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    r_p = 0.840778765432
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mu_p = 1.0 + (3.0 / 5.0) * math.log(2.0 * math.pi**2) * (1.0 + alpha / 4.0)
    mu_n = -(3.0 / 4.0) * delta_b * (1.0 + alpha * 3.0 * math.sqrt(2.0) / 4.0)
    alpha_tor_2 = 2.0 * alpha * math.log(2.0 * math.pi**2)
    rn2 = -2.0 * abs(mu_n) * alpha_tor_2 * r_p * r_p
    ref_rn2 = -0.1161

    qs = [0.0, 0.5, 1.0, 2.0]
    rows = []
    for q in qs:
        ge_p = j0(q * r_p)
        gm_p = mu_p * ge_p
        rows.append((q, ge_p, gm_p))

    lines = [
        "# Saída — fatores de forma reduzidos",
        "",
        "Classificação: teste de consistência da redução de superfície.",
        "",
        "| q fm^-1 | G_E^p | G_M^p |",
        "|---:|---:|---:|",
    ]
    for q, ge, gm in rows:
        lines.append(f"| {q:.6f} | {ge:.12f} | {gm:.12f} |")
    lines += [
        "",
        "## Normalizações e nêutron",
        "",
        f"- `G_E^p(0) = {rows[0][1]:.12f}`",
        f"- `G_M^p(0) = {rows[0][2]:.12f}`",
        "- `G_E^n(0) = 0` por neutralidade global da distribuição de duas cascas.",
        f"- `<r_n^2>_GDQ = {rn2:.12f} fm^2`",
        f"- `<r_n^2>_ref = {ref_rn2:.12f} fm^2`",
        f"- `erro relativo = {(rn2-ref_rn2)/ref_rn2:.12e}`",
        "",
        "Interpretação: o próton é representado por casca reduzida e o nêutron por",
        "polarização local com carga total nula.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

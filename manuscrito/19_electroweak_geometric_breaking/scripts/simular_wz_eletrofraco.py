#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `simular wz eletrofraco` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / diagnóstico W-Z.

Calcula massas efetivas:

    mW = g v / 2
    mZ = v sqrt(g^2+g'^2) / 2

para cenários de transporte eletrofraco discutidos no transporte eletrofraco.

Classificação: diagnóstico reduzido. Não usa mW ou mZ como entrada.
"""

from __future__ import annotations

from pathlib import Path
import math


def masses(v: float, alpha_inv: float, sin2: float) -> tuple[float, float, float, float]:
    alpha = 1.0 / alpha_inv
    e = math.sqrt(4.0 * math.pi * alpha)
    s = math.sqrt(sin2)
    c = math.sqrt(1.0 - sin2)
    g = e / s
    gp = e / c
    m_w = 0.5 * g * v
    m_z = 0.5 * math.sqrt(g * g + gp * gp) * v
    return g, gp, m_w, m_z


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_simular_wz_eletrofraco.md"

    v = 246.111195996
    # Valores de referência usados nos diagnósticos anteriores do projeto.
    # Eles entram apenas depois do cálculo, para comparação; não entram na
    # construção de g, g', mW ou mZ.
    m_w_ref = 80.379
    m_z_ref = 91.1876
    ratio_ref = m_w_ref / m_z_ref

    cases = [
        ("ponto geométrico", 137.035999, 3.0 / 8.0),
        ("transporte 2/9", 137.035999, 2.0 / 9.0),
        ("resolução EW", 128.0, 3.0 / 8.0),
        ("resolução EW com 2/9", 128.0, 2.0 / 9.0),
    ]

    lines = [
        "# Saída — diagnóstico W/Z eletrofraco",
        "",
        "Classificação: diagnóstico reduzido; não é ajuste por $m_W$ ou $m_Z$.",
        "",
        f"Escala usada: $v={v:.12f}\\,\\mathrm{{GeV}}$.",
        "",
        "| caso | alpha_inv | sin2_theta | g | g_prime | m_W GeV | erro W | m_Z GeV | erro Z | erro razão |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, alpha_inv, sin2 in cases:
        g, gp, mw, mz = masses(v, alpha_inv, sin2)
        ratio = mw / mz
        err_w = (mw - m_w_ref) / m_w_ref
        err_z = (mz - m_z_ref) / m_z_ref
        err_ratio = (ratio - ratio_ref) / ratio_ref
        lines.append(
            f"| {name} | {alpha_inv:.6f} | {sin2:.12f} | {g:.6f} | {gp:.6f} | {mw:.4f} | {err_w:.4%} | {mz:.4f} | {err_z:.4%} | {err_ratio:.4%} |"
        )
    lines += [
        "",
        f"Referências usadas somente para comparação: $m_W={m_w_ref:.6f}\\,\\mathrm{{GeV}}$,",
        f"$m_Z={m_z_ref:.6f}\\,\\mathrm{{GeV}}$ e $m_W/m_Z={ratio_ref:.9f}$.",
        "",
        "Interpretação: $3/8$ é o ponto geométrico comum; $2/9$ representa a rota",
        "condicional de transporte global discutida no transporte eletrofraco. A comparação mostra onde",
        "a rota estrutural já aproxima os valores aceitos e onde ainda exige",
        "transporte global/Hessiana de contorno.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

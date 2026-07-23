#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `validar beta livre` associada ao capítulo `17_baryonic_structure`.

GDQ — Capítulo 17 / beta livre.

Verifica que Q_beta é endpoint cinemático:

    Q_beta = (Mn/Me - Mp/Me - 1) * m_e

e ilustra uma distribuição contínua simples de energia entre elétron e
antineutrino, sem fixar energia do antineutrino.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_validar_beta_livre.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    mp_me = 6.0 * math.pi**5 + alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)
    mn_me = mp_me + delta_b
    me_mev = 0.51099895000
    q_beta = (mn_me - mp_me - 1.0) * me_mev
    ref_mp_me = 1836.15267343
    ref_mn_me = 1838.68366173
    q_beta_ref = (ref_mn_me - ref_mp_me - 1.0) * me_mev

    fractions = [0.1, 0.5, 0.9]
    rows = []
    for f in fractions:
        e_e_kin = f * q_beta
        e_nu = (1.0 - f) * q_beta
        rows.append((f, e_e_kin, e_nu, e_e_kin + e_nu))

    lines = [
        "# Saída — beta livre",
        "",
        "Classificação: teste de consistência cinemática.",
        "",
        f"- `Q_beta reduzido GDQ = {q_beta:.12f} MeV`",
        f"- `Q_beta referência = {q_beta_ref:.12f} MeV`",
        f"- `diferença = {q_beta-q_beta_ref:.12e} MeV`",
        "",
        "| fração no elétron | K_e MeV | E_antineutrino+recoil MeV | soma MeV |",
        "|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(f"| {row[0]:.3f} | {row[1]:.12f} | {row[2]:.12f} | {row[3]:.12f} |")
    lines += [
        "",
        "Interpretação: o endpoint é energia disponível. O antineutrino é modo",
        "torsional neutro propagante e não carrega energia fixa igual a Q_beta.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

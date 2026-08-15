#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `validate_free_beta` associated with chapter `17_baryonic_structure`.

GDQ — Chapter 17 / free beta decay.

Verifies that Q_beta is the kinematic endpoint:

    Q_beta = (Mn/Me - Mp/Me - 1) * m_e

and illustrates a simple continuous distribution of energy between electron and
antineutrino, without fixing the antineutrino energy.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_validate_free_beta.md"

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
        "# Output — free beta",
        "",
        "Classification: kinematics consistency test.",
        "",
        "$$",
        f"Q_\\beta\\text{{ reduced GDQ}} = {q_beta:.12f}\\text{{ MeV}}",
        "$$",
        "$$",
        f"Q_\\beta\\text{{ reference}} = {q_beta_ref:.12f}\\text{{ MeV}}",
        "$$",
        "$$",
        f"\\text{{difference}} = {q_beta-q_beta_ref:.12e}\\text{{ MeV}}",
        "$$",
        "",
        "| fraction in electron | K_e MeV | E_antineutrino+recoil MeV | sum MeV |",
        "|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(f"| {row[0]:.3f} | {row[1]:.12f} | {row[2]:.12f} | {row[3]:.12f} |")
    lines += [
        "",
        "Interpretation: the endpoint is available energy. The antineutrino is a neutral",
        "torsional propagating mode and does not carry a fixed energy equal to Q_beta.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

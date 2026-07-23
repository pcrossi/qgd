#!/usr/bin/env python3
"""Q48 — recálculo hiperfino usando momento magnético do próton previsto pela Q40.

Classificação:
- avaliação direta/consistência cruzada Q40 -> Q48;
- comparação fenomenológica quando usa a_e experimental;
- não ajusta parâmetros pelo valor hiperfino.
"""

from __future__ import annotations

from math import log, pi
from pathlib import Path

import scipy.constants as C


OUT = Path(__file__).with_name("saida_hiperfina_mup_gdq_q48.md")

alpha = C.alpha
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
mu_B = C.physical_constants["Bohr magneton"][0]
mu_N = C.physical_constants["nuclear magneton"][0]
mu_p_exp_si = C.physical_constants["proton mag. mom."][0]
mu_p_exp_muN = mu_p_exp_si / mu_N
a_e_exp = C.physical_constants["electron mag. mom. anomaly"][0]
hfs_obs = 1420405751.768
r_p_fm = 0.84077876545


def reduced_mass(m1: float, m2: float) -> float:
    return m1 * m2 / (m1 + m2)


def mu_p_gdq_muN() -> float:
    kappa_p = (3.0 / 5.0) * log(2.0 * pi**2) * (1.0 + alpha / 4.0)
    return 1.0 + kappa_p


def hfs_fermi(mu_p_muN: float) -> float:
    mu_ep = reduced_mass(m_e, m_p)
    mu_p_over_muB = mu_p_muN * (mu_N / mu_B)
    return (
        (16.0 / 3.0)
        * alpha**2
        * c
        * C.Rydberg
        * (mu_ep / m_e) ** 3
        * mu_p_over_muB
    )


def zemach_fraction(r_z_fm: float) -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return -2.0 * alpha * (mu_ep * c / hbar) * (r_z_fm * 1e-15)


def rec_kin_fraction() -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return -0.5 * alpha**2 * (mu_ep / m_p)


def main() -> None:
    ae1 = alpha / (2.0 * pi)
    rz_shell = 4.0 * r_p_fm / 3.0
    dz = zemach_fraction(rz_shell)
    drec = rec_kin_fraction()

    mup_gdq = mu_p_gdq_muN()
    rows = []
    for label, mup, ae in [
        ("mu_p experimental, a_e^(1)", mu_p_exp_muN, ae1),
        ("mu_p GDQ/Q40, a_e^(1)", mup_gdq, ae1),
        ("mu_p GDQ/Q40, a_e experimental", mup_gdq, a_e_exp),
    ]:
        nu_f = hfs_fermi(mup)
        nu = nu_f * (1.0 + ae) * (1.0 + dz) * (1.0 + drec)
        rows.append((label, mup, ae, nu_f, nu, nu - hfs_obs, nu / hfs_obs - 1.0))

    text = [
        "# Saída — hiperfina Q48 com $\\mu_p$ da Q40",
        "",
        "Classificação: avaliação direta/consistência cruzada Q40→Q48.",
        "Nenhum parâmetro foi escolhido pelo valor da linha de 21 cm.",
        "",
        "## Momento magnético",
        "",
        "$$",
        "\\mu_p^{\\rm GDQ}",
        "=",
        "1+\\frac35\\ln(2\\pi^2)\\left(1+\\frac\\alpha4\\right).",
        "$$",
        "",
        f"- mu_p experimental = {mu_p_exp_muN:.15f} mu_N",
        f"- mu_p GDQ/Q40 = {mup_gdq:.15f} mu_N",
        f"- diferença relativa = {mup_gdq/mu_p_exp_muN-1.0:.15e}",
        "",
        "## Hiperfina com Zemach de casca e recuo cinemático",
        "",
        f"- r_Z = 4 r_p/3 = {rz_shell:.12f} fm",
        f"- delta_Z = {dz:.15e}",
        f"- delta_rec^kin = {drec:.15e}",
        "",
        "| caso | mu_p/mu_N | a_e usado | nu_F (Hz) | nu final (Hz) | diferença (Hz) | erro relativo |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        label, mup, ae, nu_f, nu, diff, rel = row
        text.append(
            f"| {label} | {mup:.12f} | {ae:.12e} | {nu_f:.6f} | {nu:.6f} | {diff:.6f} | {rel:.6e} |"
        )

    text += [
        "",
        "## Conclusão",
        "",
        "Usar o momento magnético geométrico da Q40 reduz substancialmente o",
        "resíduo hiperfino sem alterar o raio. Ainda resta um termo de ordem",
        "$10^{-5}$, que deve vir de recuo hiperfino completo, polarização",
        "protônica e Hessiana magnética local superior.",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()

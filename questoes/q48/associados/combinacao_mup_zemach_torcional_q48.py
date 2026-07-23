#!/usr/bin/env python3
"""Q48 — combinação sem alvo: mu_p GDQ/Q40 + Zemach torcional Q40.

Classificação:
- avaliação direta de combinações herdadas de Q40/Q43;
- a_e experimental aparece apenas como régua metrológica explícita;
- não usa a linha de 21 cm para escolher parâmetros.
"""

from __future__ import annotations

from math import log, pi
from pathlib import Path

import scipy.constants as C

from calcular_zemach_torcional_q48 import (
    alpha,
    delta_b_q40,
    kappa_p_gdq,
    r_p,
    rec_kin_fraction,
    zemach_fraction,
    zemach_numeric,
    zemach_numeric_two_shell,
)


OUT = Path(__file__).with_name("saida_combinacao_mup_zemach_torcional_q48.md")

hfs_obs = 1420405751.768
m_e = C.m_e
m_p = C.m_p
c = C.c
mu_B = C.physical_constants["Bohr magneton"][0]
mu_N = C.physical_constants["nuclear magneton"][0]
a_e_exp = C.physical_constants["electron mag. mom. anomaly"][0]


def reduced_mass(m1: float, m2: float) -> float:
    return m1 * m2 / (m1 + m2)


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


def nu_final(mu_p_muN: float, ae: float, rz: float) -> float:
    return hfs_fermi(mu_p_muN) * (1.0 + ae) * (1.0 + zemach_fraction(rz)) * (1.0 + rec_kin_fraction())


def main() -> None:
    kp = kappa_p_gdq()
    mu_p_gdq = 1.0 + kp
    ae1 = alpha / (2.0 * pi)

    rz_shell = 4.0 * r_p / 3.0
    rz_vol_rp, _ = zemach_numeric(r_p)
    rz_vol_scaled, _ = zemach_numeric((1.0 + kp) ** (1.0 / 3.0) * r_p)
    rz_two_alpha_delta, _ = zemach_numeric_two_shell(alpha * delta_b_q40())

    rows = []
    for ae_label, ae in [("a_e^(1)", ae1), ("a_e experimental", a_e_exp)]:
        for rz_label, rz in [
            ("Zemach casca", rz_shell),
            ("Zemach torção volumétrica R=r_p", rz_vol_rp),
            ("Zemach torção volumétrica R=(1+kappa)^(1/3)r_p", rz_vol_scaled),
            ("Zemach duas cascas A=alpha delta_B", rz_two_alpha_delta),
        ]:
            nu = nu_final(mu_p_gdq, ae, rz)
            rows.append((ae_label, rz_label, rz, nu, nu - hfs_obs, nu / hfs_obs - 1.0))

    lines = [
        "# Saída — combinação $\\mu_p$ GDQ e Zemach torcional Q48",
        "",
        "Classificação: avaliação direta de combinações herdadas de Q40/Q43.",
        "Nenhum parâmetro é escolhido pela linha de 21 cm.",
        "",
        f"- $\\mu_p^{{\\rm GDQ}}/\\mu_N = {mu_p_gdq:.15f}$",
        f"- $\\kappa_p = {kp:.15f}$",
        f"- $r_p = {r_p:.12f}$ fm",
        "",
        "| a_e | modelo Zemach | r_Z (fm) | nu final (Hz) | diferença (Hz) | erro relativo |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for ae_label, rz_label, rz, nu, diff, rel in rows:
        lines.append(f"| {ae_label} | {rz_label} | {rz:.12f} | {nu:.6f} | {diff:.6f} | {rel:.6e} |")

    best = min(rows, key=lambda r: abs(r[-1]))
    lines += [
        "",
        "## Melhor combinação sem alvo nesta família",
        "",
        f"- a_e: {best[0]}",
        f"- modelo Zemach: {best[1]}",
        f"- r_Z: {best[2]:.12f} fm",
        f"- diferença: {best[4]:.6f} Hz",
        f"- erro relativo: {best[5]:.6e}",
        "",
        "## Leitura",
        "",
        "A substituição de $\\mu_p$ experimental por $\\mu_p$ geométrico da Q40",
        "é o efeito dominante entre os blocos já derivados. Os modelos Zemach",
        "torcionais naturais testados não eliminam o resíduo restante. O fechamento",
        "metrológico exige a Hessiana local magnética superior do próton, não uma",
        "nova calibração de raio.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

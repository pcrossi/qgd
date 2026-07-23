#!/usr/bin/env python3
"""
GDQ — Capítulo 22 / Hidrogênio

Objetivo:
    Comparar a redução GDQ externa com a régua operacional Dirac--Coulomb/QED
    ligada de baixa energia.

Classificação:
    Comparação fenomenológica controlada. O formalismo externo não substitui a
    GDQ; ele é usado apenas como régua para o setor em que a Hessiana
    Dirac--Bismut reduz ao operador central de Coulomb.

Saída:
    saida_comparacao_gdq_dirac_operacional.md
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path

from scipy import constants as C


OUT = Path(__file__).with_name("saida_comparacao_gdq_dirac_operacional.md")


alpha = C.alpha
c = C.c
e = C.e
h = C.h
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
m_mu = C.physical_constants["muon mass"][0]
mu_B = C.physical_constants["Bohr magneton"][0]
mu_p = C.physical_constants["proton mag. mom."][0]

mu_ep = m_e * m_p / (m_e + m_p)
mu_mup = m_mu * m_p / (m_mu + m_p)
mu_c2_eV = mu_ep * c**2 / e


def dirac_energy_eV(n: int, kappa: int) -> float:
    gamma = sqrt(kappa * kappa - alpha * alpha)
    denom = n - abs(kappa) + gamma
    return mu_c2_eV / sqrt(1.0 + (alpha / denom) ** 2)


def binding_eV(n: int, kappa: int) -> float:
    return dirac_energy_eV(n, kappa) - mu_c2_eV


def eV_to_Hz(x_eV: float) -> float:
    return x_eV * e / h


def Hz_to_eV(x_hz: float) -> float:
    return h * x_hz / e


def fermi_hfs_hz() -> float:
    return (
        (16.0 / 3.0)
        * alpha**2
        * c
        * C.Rydberg
        * (mu_ep / m_e) ** 3
        * (mu_p / mu_B)
    )


def finite_size_eV(reduced_mass_kg: float, r_fm: float, n: int = 2) -> float:
    r = r_fm * 1e-15
    return ((2.0 / 3.0) * alpha**4 * reduced_mass_kg**3 * c**4 * r**2 / hbar**2 / n**3) / e


def main() -> None:
    hfs_obs_hz = 1_420_405_751.768
    lamb_ref_hz = 1_057.844e6
    r_p_fm = 0.84077876545
    r_z_fm = 4.0 * r_p_fm / 3.0

    fine_eV = binding_eV(2, -2) - binding_eV(2, +1)
    hfs0 = fermi_hfs_hz()
    ae1 = alpha / (2.0 * pi)
    delta_z = -2.0 * alpha * (mu_ep * c / hbar) * (r_z_fm * 1e-15)
    delta_rec = -0.5 * alpha**2 * (mu_ep / m_p)

    hfs_ae = hfs0 * (1.0 + ae1)
    hfs_z = hfs_ae * (1.0 + delta_z)
    hfs_rec = hfs_z * (1.0 + delta_rec)

    fs_h = finite_size_eV(mu_ep, r_p_fm)
    fs_muh = finite_size_eV(mu_mup, r_p_fm)

    lines = [
        "---",
        'title: "Saída — comparação GDQ e Dirac operacional"',
        "---",
        "",
        "# Saída — comparação GDQ e Dirac operacional",
        "",
        "Classificação: comparação fenomenológica controlada.",
        "",
        "| Observável | GDQ/redução atual | Régua operacional | Status |",
        "|---|---:|---:|---|",
        f"| $E_{{1s}}$ com massa reduzida | `{binding_eV(1, -1):.12f}` eV | Dirac--Coulomb | coincide por redução externa |",
        f"| $E_{{2s_{{1/2}}}}-E_{{2p_{{1/2}}}}$ Coulomb puro | `{0.0:.12e}` eV | `0` | Lamb requer campo próximo |",
        f"| $E_{{2p_{{3/2}}}}-E_{{2p_{{1/2}}}}$ | `{fine_eV:.12e}` eV | Dirac--Coulomb | estrutura fina líder |",
        f"| frequência fina $2p_{{3/2}}-2p_{{1/2}}$ | `{eV_to_Hz(fine_eV)/1e9:.9f}` GHz | Dirac--Coulomb | coincide no nível árvore |",
        f"| hiperfina Fermi | `{hfs0:.6f}` Hz | `{hfs_obs_hz:.6f}` Hz | erro `{hfs0/hfs_obs_hz-1:.6e}` |",
        f"| hiperfina com $a_e^{{(1)}}$ | `{hfs_ae:.6f}` Hz | `{hfs_obs_hz:.6f}` Hz | erro `{hfs_ae/hfs_obs_hz-1:.6e}` |",
        f"| hiperfina com Zemach de casca | `{hfs_z:.6f}` Hz | `{hfs_obs_hz:.6f}` Hz | erro `{hfs_z/hfs_obs_hz-1:.6e}` |",
        f"| hiperfina com recuo fino | `{hfs_rec:.6f}` Hz | `{hfs_obs_hz:.6f}` Hz | erro `{hfs_rec/hfs_obs_hz-1:.6e}` |",
        f"| Lamb $2s_{{1/2}}-2p_{{1/2}}$ | operador near/DtN | `{lamb_ref_hz/1e6:.3f}` MHz | metrologia condicional |",
        f"| tamanho finito H $2s$ | `{fs_h:.12e}` eV | fator de forma | usa $r_p$ geométrico |",
        f"| tamanho finito $\\mu H$ $2s$ | `{fs_muh*1e3:.9f}` meV | fator de forma | amplificação $\\mu^3$ |",
        "",
        "Leitura: a GDQ coincide com a régua Dirac--Coulomb no setor externo.",
        "As diferenças finas devem vir da Hessiana física de campo próximo, de",
        "DtN/Schur, dos fatores de forma e da resposta protônica, não de novos",
        "termos fundamentais adicionados à ação.",
        "",
        "Escala Lamb usada apenas como diagnóstico:",
        "",
        "$$",
        f"\\Delta E_{{\\rm Lamb}}^{{\\rm ref}}={Hz_to_eV(lamb_ref_hz):.12e}\\,{{\\rm eV}}.",
        "$$",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

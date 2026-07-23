#!/usr/bin/env python3
"""Q48 — comparação GDQ estrutural vs Modelo Padrão operacional.

Não calcula bound-state QED completa. O objetivo é separar:
- coincidência estrutural no limite Dirac-Coulomb;
- termos em que o Modelo Padrão/QED já possui cálculo metrológico;
- termos em que a GDQ exige a Hessiana de campo próximo.
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path

from scipy import constants as C


OUT = Path(__file__).with_name("saida_comparacao_gdq_modelo_padrao_q48.md")

alpha = C.alpha
c = C.c
e = C.e
h = C.h
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
m_mu = C.physical_constants["muon mass"][0]
Rinf = C.Rydberg
mu_B = C.physical_constants["Bohr magneton"][0]
mu_p = C.physical_constants["proton mag. mom."][0]

mu_ep = m_e * m_p / (m_e + m_p)
mu_mup = m_mu * m_p / (m_mu + m_p)
mu_c2_eV = mu_ep * c**2 / e


def dirac_energy_eV(n: int, kappa: int, mass_energy_eV: float = mu_c2_eV) -> float:
    gamma = sqrt(kappa * kappa - alpha * alpha)
    denom = n - abs(kappa) + gamma
    return mass_energy_eV / sqrt(1.0 + (alpha / denom) ** 2)


def bind(n: int, kappa: int) -> float:
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
        * Rinf
        * (mu_ep / m_e) ** 3
        * (mu_p / mu_B)
    )


def gdq_ae_leader() -> float:
    return alpha / (2.0 * pi)


def zemach_shell_fraction(r_p_fm: float = 0.84077876545) -> float:
    r_z = (4.0 * r_p_fm / 3.0) * 1e-15
    return -2.0 * alpha * (mu_ep * c / hbar) * r_z


def fine_recoil_fraction() -> float:
    return -0.5 * alpha**2 * (mu_ep / m_p)


def finite_size_eV(reduced_mass_kg: float, r_fm: float, n: int = 2) -> float:
    r = r_fm * 1e-15
    return ((2.0 / 3.0) * alpha**4 * reduced_mass_kg**3 * c**4 * r**2 / hbar**2 / n**3) / e


def main() -> None:
    fine_eV = bind(2, -2) - bind(2, +1)
    fine_hz = eV_to_Hz(fine_eV)

    # Referências experimentais/metrológicas usuais, usadas aqui como comparação,
    # não como entrada na construção GDQ.
    hfs_obs_hz = 1_420_405_751.768
    lamb_ref_hz = 1_057.844e6
    lamb_ref_eV = Hz_to_eV(lamb_ref_hz)

    hfs_gdq_leader = fermi_hfs_hz()
    hfs_gdq_plus_ae = hfs_gdq_leader * (1.0 + gdq_ae_leader())
    hfs_gdq_plus_ae_z = hfs_gdq_plus_ae * (1.0 + zemach_shell_fraction())
    hfs_gdq_plus_ae_z_rec = hfs_gdq_plus_ae_z * (1.0 + fine_recoil_fraction())
    fs_h_2s = finite_size_eV(mu_ep, 0.84077876545)
    fs_muh_2s = finite_size_eV(mu_mup, 0.84077876545)

    text = [
        "# Q48 — comparação GDQ x Modelo Padrão operacional",
        "",
        "Classificação: comparação fenomenológica/controlada. O Modelo Padrão em",
        "hidrogênio de baixa energia significa Dirac-Coulomb + QED ligada + dados",
        "nucleares. A GDQ não é substituída por esse formalismo; ele é usado como",
        "régua operacional.",
        "",
        "## Comparação numérica mínima",
        "",
        "| Observável | GDQ atual | Modelo Padrão/QED operacional | Diferença/status |",
        "|---|---:|---:|---|",
        f"| $E_{{1s}}$ líder com massa reduzida | {bind(1, -1):.12f} eV | mesmo Dirac-Coulomb | coincide por redução efetiva |",
        f"| $E_{{2s_{{1/2}}}}-E_{{2p_{{1/2}}}}$ no Coulomb puro | {0.0:.12e} eV | 0 no Dirac puro | Lamb exige correções além do Coulomb |",
        f"| $E_{{2p_{{3/2}}}}-E_{{2p_{{1/2}}}}$ | {fine_eV:.12e} eV | mesmo Dirac-Coulomb | coincide no nível árvore |",
        f"| frequência fina $2p_{{3/2}}-2p_{{1/2}}$ | {fine_hz/1e9:.9f} GHz | mesmo Dirac-Coulomb | coincide no nível árvore |",
        f"| hiperfina $1s$ líder | {hfs_gdq_leader:.6f} Hz | {hfs_obs_hz:.6f} Hz observado | erro líder {(hfs_gdq_leader/hfs_obs_hz-1):.6e}; faltam correções superiores |",
        f"| hiperfina $1s$ + $a_e^{{(1)}}=\\alpha/(2\\pi)$ | {hfs_gdq_plus_ae:.6f} Hz | {hfs_obs_hz:.6f} Hz observado | erro {(hfs_gdq_plus_ae/hfs_obs_hz-1):.6e}; faltam recuo/Zemach/Hessiana superior |",
        f"| hiperfina $1s$ + $a_e^{{(1)}}$ + Zemach casca | {hfs_gdq_plus_ae_z:.6f} Hz | {hfs_obs_hz:.6f} Hz observado | erro {(hfs_gdq_plus_ae_z/hfs_obs_hz-1):.6e}; falta recuo/Hessiana magnética superior |",
        f"| hiperfina $1s$ + $a_e^{{(1)}}$ + Zemach + recuo cinemático | {hfs_gdq_plus_ae_z_rec:.6f} Hz | {hfs_obs_hz:.6f} Hz observado | erro {(hfs_gdq_plus_ae_z_rec/hfs_obs_hz-1):.6e}; falta Hessiana magnética superior |",
        f"| Lamb $2s_{{1/2}}-2p_{{1/2}}$ | operador near/DtN ainda não avaliado | ~{lamb_ref_hz/1e6:.3f} MHz = {lamb_ref_eV:.12e} eV | lacuna metrológica GDQ explícita |",
        f"| tamanho finito H $2s$, $r_p=0.84077876545$ fm | {fs_h_2s:.12e} eV | mesma forma efetiva de fator de forma | depende de origem de $r_p$ |",
        f"| tamanho finito $\\mu H$ $2s$, mesmo $r_p$ | {fs_muh_2s*1e3:.9f} meV | mesma forma efetiva de fator de forma | amplificação $\\mu^3$ |",
        "",
        "## Leitura física",
        "",
        "1. No setor externo de campo fraco, a GDQ reduz ao mesmo operador",
        "   espinorial central que o Modelo Padrão usa como ponto de partida",
        "   operacional. Por isso espectro Dirac e estrutura fina líder coincidem.",
        "2. A diferença ontológica é onde moram as correções: na QED elas são",
        "   organizadas como loops, renormalização e potenciais efetivos; na GDQ",
        "   elas devem vir de Hessiana física, DtN/Schur, fator de forma e resposta",
        "   do background protônico.",
        "3. A Q48 já resolve a crítica da equação escalar: o objeto correto é",
        "   espinorial. A equação escalar legada fica como limite radial projetado.",
        "4. A GDQ ainda não deve declarar previsão metrológica completa do Lamb shift",
        "   enquanto $\\delta\\mathcal D_{\\rm near}$ não for calculado diretamente.",
        "",
        "## Veredito comparativo",
        "",
        "$$",
        "\\boxed{",
        "\\text{A GDQ iguala o Modelo Padrão no limite Dirac--Coulomb e oferece}",
        "}",
        "$$",
        "",
        "$$",
        "\\boxed{",
        "\\text{uma rota geométrica distinta para os termos que a QED chama de correções.}",
        "}",
        "$$",
        "",
        "O ponto ainda não fechado metrologicamente é exatamente o esperado:",
        "",
        "$$",
        "\\boxed{",
        "\\delta\\mathcal D_{\\rm near}",
        "\\text{ do background protônico.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()

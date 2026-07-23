#!/usr/bin/env python3
"""Q48 — hiperfina de Fermi, correções GDQ e tamanho finito.

Classificação:
- hiperfina usando mu_p experimental: comparação fenomenológica;
- tamanho finito usando r_p externo: comparação/calibração;
- as mesmas fórmulas tornam-se previsão condicional se mu_p e r_p vierem da GDQ.
- correção a_e = alpha/(2*pi): avaliação direta do canal líder Q43;
- resposta coletiva de superfície: avaliação reduzida da impedância Q40.
- correção de Zemach de casca GDQ: avaliação geométrica reduzida da
  distribuição de magnetização/charge superficial.
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path

from scipy import constants as C


OUT = Path(__file__).with_name("saida_hiperfina_tamanho_finito_q48.md")

alpha = C.alpha
c = C.c
h = C.h
hbar = C.hbar
e = C.e
m_e = C.m_e
m_p = C.m_p
Rinf = C.Rydberg
mu_B = C.physical_constants["Bohr magneton"][0]
mu_p = C.physical_constants["proton mag. mom."][0]

mu_ep = m_e * m_p / (m_e + m_p)
m_mu = C.physical_constants["muon mass"][0]
mu_mup = m_mu * m_p / (m_mu + m_p)
r_p_fm = 0.84077876545

# Q40 — impedância coletiva reduzida de superfície.
j0 = 1.712091781054
j1 = 1.341454657186
j2 = 1.063840998206


def fermi_hfs_hz(n: int = 1) -> float:
    return (
        (16.0 / 3.0)
        * alpha**2
        * c
        * Rinf
        * (mu_ep / m_e) ** 3
        * (mu_p / mu_B)
        / n**3
    )


def q40_collective_impedance(x: float) -> float:
    """I_sigma(x) from Q40 reduced collective surface impedance.

    x = q^2 / Lambda_E^2, Lambda_E = sqrt(12)/r_p.
    The result is dimensionless in the reduced surface model.
    """
    return -(
        j0**2 * x**2 / (1.0 + x)
        + j1**2 * x**2 / (1.0 + x) ** 2
        + j2**2 * x**3 / (1.0 + x) ** 2
    )


def q40_surface_fraction_for_hfs(r_fm: float = r_p_fm) -> tuple[float, float, float]:
    """Estimate the reduced Q40 collective surface fraction at atomic momentum.

    This is not a fit. It evaluates the already derived Q40 surface impedance at
    q ~ 1/a_B^*, the momentum scale sampled by the 1s contact density.
    """
    a0_eff = hbar / (mu_ep * c * alpha)
    q_atom_fm_inv = (1.0 / a0_eff) / 1e15
    lambda_e_fm_inv = sqrt(12.0) / r_fm
    x = (q_atom_fm_inv / lambda_e_fm_inv) ** 2
    return x, q40_collective_impedance(x), q_atom_fm_inv


def gdq_leading_anomaly() -> float:
    """Q43 leading geometric magnetic anomaly."""
    return alpha / (2.0 * pi)


def finite_size_energy_eV(reduced_mass_kg: float, r_fm: float, n: int = 2, z: int = 1) -> float:
    r = r_fm * 1e-15
    joule = (2.0 / 3.0) * (z * alpha) ** 4 * reduced_mass_kg**3 * c**4 * r**2 / hbar**2 / n**3
    return joule / e


def zemach_radius_thin_shell_fm(r_fm: float = r_p_fm) -> float:
    """Zemach radius for identical thin spherical electric/magnetic shells.

    r_Z = <|r-r'|> over two independent points on a sphere of radius r.
    The mean chord length on a sphere is 4r/3.
    """
    return 4.0 * r_fm / 3.0


def zemach_fraction(r_z_fm: float) -> float:
    """Leading Zemach fractional correction to the 1s hyperfine splitting."""
    r_z = r_z_fm * 1e-15
    return -2.0 * alpha * (mu_ep * c / hbar) * r_z


def main() -> None:
    r_values = [0.84077876545, 0.875, 0.8354]
    hfs = fermi_hfs_hz(1)
    hfs_obs = 1420_405_751.768  # Hz, valor clássico de referência metrológica
    ae_gdq = gdq_leading_anomaly()
    x_hfs, i_sigma_hfs, q_atom = q40_surface_fraction_for_hfs()
    hfs_plus_ae = hfs * (1.0 + ae_gdq)
    # The reduced Q40 collective impedance is evaluated multiplicatively as the
    # first surface-response correction. Its sign follows the Schur complement.
    hfs_plus_ae_surface = hfs_plus_ae * (1.0 + i_sigma_hfs)
    r_z_shell = zemach_radius_thin_shell_fm()
    delta_z = zemach_fraction(r_z_shell)
    hfs_plus_ae_zemach = hfs_plus_ae * (1.0 + delta_z)
    hfs_plus_all_reduced = hfs_plus_ae * (1.0 + i_sigma_hfs + delta_z)
    residual_after_reduced = hfs_obs / hfs_plus_all_reduced - 1.0

    text = [
        "# Saída — hiperfina e tamanho finito Q48",
        "",
        "## Hiperfina 1s",
        "",
        "Classificação: comparação fenomenológica se `mu_p` é experimental.",
        "",
        f"- mu_p/mu_B = {mu_p/mu_B:.15e}",
        f"- nu_F(1s) = {hfs:.6f} Hz",
        f"- referência 21 cm = {hfs_obs:.6f} Hz",
        f"- diferença = {hfs-hfs_obs:.6f} Hz",
        f"- erro relativo = {(hfs/hfs_obs-1):.6e}",
        "",
        "## Correções adicionadas",
        "",
        "### 1. Canal magnético líder da GDQ/Q43",
        "",
        f"- a_e^GDQ,(1) = alpha/(2*pi) = {ae_gdq:.15e}",
        f"- nu_F * (1 + a_e) = {hfs_plus_ae:.6f} Hz",
        f"- diferença após a_e = {hfs_plus_ae-hfs_obs:.6f} Hz",
        f"- erro relativo após a_e = {(hfs_plus_ae/hfs_obs-1):.6e}",
        "",
        "### 2. Resposta coletiva de superfície Q40 avaliada na escala atômica",
        "",
        f"- q_atom ~ 1/a_B* = {q_atom:.15e} fm^-1",
        f"- x = q_atom^2/Lambda_E^2 = {x_hfs:.15e}",
        f"- I_sigma(x) = {i_sigma_hfs:.15e}",
        f"- nu_F * (1 + a_e) * (1 + I_sigma) = {hfs_plus_ae_surface:.6f} Hz",
        f"- diferença após superfície reduzida = {hfs_plus_ae_surface-hfs_obs:.6f} Hz",
        f"- erro relativo após superfície reduzida = {(hfs_plus_ae_surface/hfs_obs-1):.6e}",
        "",
        "A correção de superfície coletiva da Q40 começa em q^4. Na escala atômica",
        "ela é praticamente nula. Portanto ela não deve ser usada para absorver o",
        "resíduo hiperfino. O resíduo remanescente exige os canais de recuo,",
        "Zemach/magnetização distribuída e termos superiores da Hessiana magnética.",
        "",
        "### 3. Zemach geométrico de casca superficial GDQ",
        "",
        "Modelo reduzido: distribuição elétrica e magnética como cascas finas na",
        "superfície protônica. Para duas cascas esféricas idênticas, o raio de",
        "Zemach é a corda média na esfera: r_Z = 4 r_p / 3.",
        "",
        f"- r_Z^shell = 4 r_p/3 = {r_z_shell:.12f} fm",
        f"- delta_Z = -2 alpha (mu c/hbar) r_Z = {delta_z:.15e}",
        f"- nu_F * (1 + a_e) * (1 + delta_Z) = {hfs_plus_ae_zemach:.6f} Hz",
        f"- diferença após a_e + Zemach = {hfs_plus_ae_zemach-hfs_obs:.6f} Hz",
        f"- erro relativo após a_e + Zemach = {(hfs_plus_ae_zemach/hfs_obs-1):.6e}",
        "",
        "### 4. Combinação reduzida adicionada",
        "",
        f"- nu_F * (1 + a_e) * (1 + I_sigma + delta_Z) = {hfs_plus_all_reduced:.6f} Hz",
        f"- diferença após efeitos reduzidos = {hfs_plus_all_reduced-hfs_obs:.6f} Hz",
        f"- erro relativo após efeitos reduzidos = {(hfs_plus_all_reduced/hfs_obs-1):.6e}",
        f"- fração residual a ser explicada por recuo/Hessiana magnética superior = {residual_after_reduced:.15e}",
        "",
        "## Tamanho finito",
        "",
        "| r_p (fm) | Delta E_fs H 2s (eV) | Delta E_fs muH 2s (meV) | amplificação mu/e |",
        "|---:|---:|---:|---:|",
    ]
    for r in r_values:
        de_e = finite_size_energy_eV(mu_ep, r, n=2)
        de_mu = finite_size_energy_eV(mu_mup, r, n=2)
        text.append(f"| {r:.12f} | {de_e:.12e} | {de_mu*1e3:.9f} | {de_mu/de_e:.6e} |")

    text += [
        "",
        "O deslocamento cresce como mu^3. Por isso o hidrogênio muônico é muito",
        "mais sensível ao raio/fator de forma do próton.",
        "",
    ]
    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()

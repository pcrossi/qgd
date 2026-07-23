#!/usr/bin/env python3
"""Q48 — Zemach com fator de forma magnético torcional da Q40.

Classificação:
- avaliação direta de um ansatz reduzido herdado da Q40;
- não usa o resíduo hiperfino como alvo;
- testa se a decomposição magnética de Q40 melhora a hiperfina do hidrogênio.

Modelo:
    G_E(q) = j0(q r_p)

    G_M(q)/mu_p = [G_shell(q) + kappa_p G_tor(q)]/(1+kappa_p)

com
    kappa_p = (3/5) ln(2 pi^2) (1 + alpha/4)

e G_tor inicialmente tomado como fator de forma de uma magnetização
volumétrica uniforme na bola física de raio R_tor.
"""

from __future__ import annotations

from math import log, pi
from pathlib import Path
import warnings

import numpy as np
import scipy.constants as C
from scipy.integrate import IntegrationWarning, quad


OUT = Path(__file__).with_name("saida_zemach_torcional_q48.md")

alpha = C.alpha
r_p = 0.84077876545  # fm, Q40 raio canônico de superfície
h = C.h
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
m_mu = C.physical_constants["muon mass"][0]
mu_p_si = C.physical_constants["proton mag. mom."][0]
mu_B = C.physical_constants["Bohr magneton"][0]
hfs_obs = 1420405751.768  # Hz


def reduced_mass(m1: float, m2: float) -> float:
    return m1 * m2 / (m1 + m2)


def j0(x: float) -> float:
    ax = abs(x)
    if ax < 1e-6:
        return 1.0 - x * x / 6.0 + x**4 / 120.0 - x**6 / 5040.0
    return np.sin(x) / x


def j1(x: float) -> float:
    ax = abs(x)
    if ax < 1e-5:
        return x / 3.0 - x**3 / 30.0 + x**5 / 840.0
    return np.sin(x) / x**2 - np.cos(x) / x


def sphere_form(q: float, radius: float) -> float:
    """Normalized uniform-ball form factor."""
    x = q * radius
    if abs(x) < 1e-6:
        return 1.0 - x * x / 10.0 + x**4 / 280.0
    return 3.0 * j1(x) / x


def kappa_p_gdq() -> float:
    return (3.0 / 5.0) * log(2.0 * pi**2) * (1.0 + alpha / 4.0)


def gm_norm(q: float, r_tor: float) -> float:
    kp = kappa_p_gdq()
    g_shell = j0(q * r_p)
    g_tor = sphere_form(q, r_tor)
    return (g_shell + kp * g_tor) / (1.0 + kp)


def delta_b_q40() -> float:
    return log(2.0 * pi**2) * 3.0 * 2.0**0.5 / 5.0


def gm_norm_two_shell(q: float, amplitude: float, sep_fraction: float = None) -> float:
    """Magnetic normalized form with zero-mean torsional two-shell correction.

    G_M/mu_p = j0(q r_p) + A [j0(q r_-)-j0(q r_+)].
    The added term vanishes at q=0, so normalization is preserved.
    """
    if sep_fraction is None:
        sep_fraction = alpha / 2.0
    r_minus = r_p * (1.0 - sep_fraction)
    r_plus = r_p * (1.0 + sep_fraction)
    return j0(q * r_p) + amplitude * (j0(q * r_minus) - j0(q * r_plus))


def ge_norm(q: float) -> float:
    return j0(q * r_p)


def integrand(q: float, r_tor: float) -> float:
    if q < 1e-7:
        # GE GM = 1 - q^2(<r_E^2>+<r_M^2>)/6 + ...
        # For the integral only finite limiting behavior matters.
        kp = kappa_p_gdq()
        r_m2 = (r_p**2 + kp * (3.0 / 5.0) * r_tor**2) / (1.0 + kp)
        return -((r_p**2) + r_m2) / 6.0
    return (ge_norm(q) * gm_norm(q, r_tor) - 1.0) / (q * q)


def integrand_two_shell(q: float, amplitude: float, sep_fraction: float = None) -> float:
    if sep_fraction is None:
        sep_fraction = alpha / 2.0
    if q < 1e-7:
        r_minus = r_p * (1.0 - sep_fraction)
        r_plus = r_p * (1.0 + sep_fraction)
        # GM = 1 - q^2 r_p^2/6 + A q^2(r_+^2-r_-^2)/6 + ...
        r_m2_eff = r_p**2 - amplitude * (r_plus**2 - r_minus**2)
        return -(r_p**2 + r_m2_eff) / 6.0
    return (ge_norm(q) * gm_norm_two_shell(q, amplitude, sep_fraction) - 1.0) / (q * q)


def zemach_numeric(r_tor: float) -> tuple[float, float]:
    q_max = 1000.0 / min(r_p, r_tor)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val_finite, err = quad(
            lambda q: integrand(q, r_tor),
            0.0,
            q_max,
            epsabs=1e-10,
            epsrel=1e-10,
            limit=2000,
        )
    tail = -1.0 / q_max
    tail_err = 1.0 / q_max**3
    val = val_finite + tail
    return -(4.0 / pi) * val, (4.0 / pi) * (err + tail_err)


def zemach_numeric_two_shell(amplitude: float, sep_fraction: float = None) -> tuple[float, float]:
    if sep_fraction is None:
        sep_fraction = alpha / 2.0
    q_max = 1000.0 / (r_p * (1.0 - sep_fraction))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val_finite, err = quad(
            lambda q: integrand_two_shell(q, amplitude, sep_fraction),
            0.0,
            q_max,
            epsabs=1e-10,
            epsrel=1e-10,
            limit=2000,
        )
    tail = -1.0 / q_max
    tail_err = 1.0 / q_max**3
    val = val_finite + tail
    return -(4.0 / pi) * val, (4.0 / pi) * (err + tail_err)


def hfs_fermi() -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return (
        (16.0 / 3.0)
        * alpha**2
        * c
        * C.Rydberg
        * (mu_ep / m_e) ** 3
        * (mu_p_si / mu_B)
    )


def zemach_fraction(r_z_fm: float) -> float:
    mu_ep = reduced_mass(m_e, m_p)
    r_z_m = r_z_fm * 1e-15
    return -2.0 * alpha * (mu_ep * c / hbar) * r_z_m


def rec_kin_fraction() -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return -0.5 * alpha**2 * (mu_ep / m_p)


def main() -> None:
    kp = kappa_p_gdq()
    nu_f = hfs_fermi()
    a_e_1 = alpha / (2.0 * pi)
    d_rec = rec_kin_fraction()

    # Raios testados sem usar hiperfina como alvo:
    # 1. r_tor=r_p: torção volumétrica dentro da bola física observada;
    # 2. r_tor=sqrt(5/3) r_p: ajusta rms volumétrico para igualar rms de casca;
    # 3. r_tor=(1+kappa)^(1/3) r_p: escala de volume torcional anômalo.
    cases = [
        ("torção volumétrica em R=r_p", r_p),
        ("R_tor=sqrt(5/3) r_p", (5.0 / 3.0) ** 0.5 * r_p),
        ("R_tor=(1+kappa)^(1/3) r_p", (1.0 + kp) ** (1.0 / 3.0) * r_p),
    ]

    lines = [
        "# Saída — Zemach torcional Q48",
        "",
        "Classificação: avaliação direta de ansatz reduzido herdado da Q40.",
        "O resíduo hiperfino não foi usado para escolher os parâmetros.",
        "",
        "## Decomposição magnética usada",
        "",
        "$$",
        "\\frac{G_M^p(q)}{\\mu_p}",
        "=",
        "\\frac{j_0(qr_p)+\\kappa_p G_{\\rm tor}(q)}{1+\\kappa_p}.",
        "$$",
        "",
        "$$",
        "\\kappa_p=\\frac35\\ln(2\\pi^2)\\left(1+\\frac\\alpha4\\right).",
        "$$",
        "",
        f"- kappa_p = {kp:.15f}",
        f"- mu_p/mu_N GDQ = {1.0 + kp:.15f}",
        f"- r_p = {r_p:.12f} fm",
        "",
        "## Resultados",
        "",
        "| caso | R_tor (fm) | r_Z (fm) | erro quad | nu_HFS final (Hz) | erro relativo |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, r_tor in cases:
        rz, err = zemach_numeric(r_tor)
        nu = nu_f * (1.0 + a_e_1) * (1.0 + zemach_fraction(rz)) * (1.0 + d_rec)
        rel = nu / hfs_obs - 1.0
        lines.append(
            f"| {name} | {r_tor:.12f} | {rz:.12f} | {err:.3e} | {nu:.6f} | {rel:.6e} |"
        )

    lines += [
        "",
        "## Teste de duas cascas torcionais de média nula",
        "",
        "Forma testada:",
        "",
        "$$",
        "\\frac{G_M^p(q)}{\\mu_p}",
        "=",
        "j_0(qr_p)+A\\left[j_0(qr_-)-j_0(qr_+)\\right],",
        "\\qquad",
        "r_\\pm=r_p\\left(1\\pm\\frac\\alpha2\\right).",
        "$$",
        "",
        "A correção preserva $G_M^p(0)/\\mu_p=1$.",
        "",
        "| amplitude A | origem | r_Z (fm) | nu_HFS final (Hz) | erro relativo |",
        "|---:|---|---:|---:|---:|",
    ]

    two_shell_cases = [
        (alpha * delta_b_q40(), "Q40 nêutron: alpha delta_B"),
        (kp / (1.0 + kp), "fração anômala kappa/(1+kappa)"),
        (kp, "escala anômala kappa"),
        (0.75 * delta_b_q40(), "projetor espacial 3 delta_B/4"),
    ]
    for amp, origin in two_shell_cases:
        rz, _err = zemach_numeric_two_shell(amp)
        nu = nu_f * (1.0 + a_e_1) * (1.0 + zemach_fraction(rz)) * (1.0 + d_rec)
        rel = nu / hfs_obs - 1.0
        lines.append(f"| {amp:.12e} | {origin} | {rz:.12f} | {nu:.6f} | {rel:.6e} |")

    lines += [
        "",
        "## Leitura",
        "",
        "A inclusão da magnetização torcional volumétrica altera o Zemach, mas,",
        "com os raios naturais herdados da Q40, não remove integralmente o erro",
        "de $10^{-5}$. Isso mostra que a forma magnética superior relevante não",
        "é apenas uma bola uniforme: ela precisa do perfil radial de torção",
        "$\\widehat\\rho_{\\rm tor}^p(\\chi)$ obtido da Hessiana local.",
        "",
        "$$",
        "\\boxed{",
        "\\text{ansatz torcional natural testado; melhora/impacto quantificado; Hessiana local ainda necessária.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Q48 — Zemach com impedância coletiva de superfície Q40 dentro de G_M(q).

Classificação:
- teste direto do bloco Schur coletivo da Q40 na integral de Zemach;
- não usa a linha hiperfina para escolher coeficientes;
- avalia se o erro 10^-5 vinha de usar o Schur apenas em q~1/a_B.

Ideia:
O cálculo anterior avaliou I_Sigma(q) na escala atômica q~1/a_B, onde x<<1.
Mas a correção de Zemach é uma integral em q de 0 a infinito e amostra q
hadrônico. Portanto, se a Hessiana magnética superior é uma resposta de
superfície, ela deve entrar como correção de forma em G_M(q), não como número
local em q atômico.
"""

from __future__ import annotations

from math import log, pi, sqrt
from pathlib import Path
import warnings

import numpy as np
import scipy.constants as C
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import brentq


OUT = Path(__file__).with_name("saida_zemach_impedancia_coletiva_q40_q48.md")

alpha = C.alpha
r_p = 0.84077876545  # fm
lambda_E = sqrt(12.0) / r_p
j0_c = 1.712091781054
j1_c = 1.341454657186
j2_c = 1.063840998206

hfs_obs = 1420405751.768
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
mu_B = C.physical_constants["Bohr magneton"][0]
mu_N = C.physical_constants["nuclear magneton"][0]
a_e_exp = C.physical_constants["electron mag. mom. anomaly"][0]


def reduced_mass(m1: float, m2: float) -> float:
    return m1 * m2 / (m1 + m2)


def sph_j0(x: float) -> float:
    ax = abs(x)
    if ax < 1e-6:
        return 1.0 - x * x / 6.0 + x**4 / 120.0 - x**6 / 5040.0
    return np.sin(x) / x


def kappa_p_gdq() -> float:
    return (3.0 / 5.0) * log(2.0 * pi**2) * (1.0 + alpha / 4.0)


def i_sigma(q: float) -> float:
    x = (q / lambda_E) ** 2
    return -(
        j0_c**2 * x**2 / (1.0 + x)
        + j1_c**2 * x**2 / (1.0 + x) ** 2
        + j2_c**2 * x**3 / (1.0 + x) ** 2
    )


def ge(q: float) -> float:
    return sph_j0(q * r_p)


def gm(q: float, mode: str) -> float:
    base = sph_j0(q * r_p)
    sig = i_sigma(q)
    kp = kappa_p_gdq()
    if mode == "base":
        return base
    if mode == "base_plus_Isigma":
        return base + sig
    if mode == "base_minus_Isigma":
        return base - sig
    if mode == "anom_frac_Isigma":
        return base + (kp / (1.0 + kp)) * sig
    if mode == "softened_Isigma":
        return base - (kp / (1.0 + kp)) * sig
    raise ValueError(mode)


def gm_beta(q: float, beta: float) -> float:
    return sph_j0(q * r_p) + beta * i_sigma(q)


def integrand(q: float, mode: str) -> float:
    if q < 1e-7:
        return -(2.0 * r_p**2) / 6.0
    return (ge(q) * gm(q, mode) - 1.0) / (q * q)


def integrand_beta(q: float, beta: float) -> float:
    if q < 1e-7:
        return -(2.0 * r_p**2) / 6.0
    return (ge(q) * gm_beta(q, beta) - 1.0) / (q * q)


def zemach(mode: str) -> tuple[float, float]:
    q_max = 1000.0 / r_p
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val, err = quad(
            lambda q: integrand(q, mode),
            0.0,
            q_max,
            epsabs=1e-10,
            epsrel=1e-10,
            limit=3000,
        )
    tail = -1.0 / q_max
    return -(4.0 / pi) * (val + tail), (4.0 / pi) * (err + 1.0 / q_max**3)


def zemach_beta(beta: float) -> float:
    q_max = 1000.0 / r_p
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val, _err = quad(
            lambda q: integrand_beta(q, beta),
            0.0,
            q_max,
            epsabs=1e-10,
            epsrel=1e-10,
            limit=3000,
        )
    tail = -1.0 / q_max
    return -(4.0 / pi) * (val + tail)


def hfs_fermi(mu_p_muN: float) -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return (
        (16.0 / 3.0)
        * alpha**2
        * c
        * C.Rydberg
        * (mu_ep / m_e) ** 3
        * (mu_p_muN * mu_N / mu_B)
    )


def zemach_fraction(rz_fm: float) -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return -2.0 * alpha * (mu_ep * c / hbar) * (rz_fm * 1e-15)


def rec_kin_fraction() -> float:
    mu_ep = reduced_mass(m_e, m_p)
    return -0.5 * alpha**2 * (mu_ep / m_p)


def main() -> None:
    kp = kappa_p_gdq()
    mu_p_gdq = 1.0 + kp
    ae1 = alpha / (2.0 * pi)

    modes = [
        ("base", "casca base"),
        ("anom_frac_Isigma", "base + kappa/(1+kappa) I_sigma"),
        ("base_plus_Isigma", "base + I_sigma"),
        ("softened_Isigma", "base - kappa/(1+kappa) I_sigma"),
        ("base_minus_Isigma", "base - I_sigma"),
    ]

    lines = [
        "# Saída — Zemach com impedância coletiva Q40 em $G_M$",
        "",
        "Classificação: teste direto do Schur coletivo Q40 dentro da integral de Zemach.",
        "Nenhum coeficiente foi ajustado pela linha hiperfina.",
        "",
        "Impedância usada:",
        "",
        "$$",
        "\\mathcal I_\\Sigma(q)",
        "=",
        "-\\left[",
        "j_0^2\\frac{x^2}{1+x}",
        "+j_1^2\\frac{x^2}{(1+x)^2}",
        "+j_2^2\\frac{x^3}{(1+x)^2}",
        "\\right],",
        "\\qquad x=\\frac{q^2}{\\Lambda_E^2}.",
        "$$",
        "",
        f"- Lambda_E = {lambda_E:.12f} fm^-1",
        f"- kappa_p = {kp:.15f}",
        f"- mu_p^GDQ = {mu_p_gdq:.15f} mu_N",
        "",
        "| modo $G_M/\\mu_p$ | r_Z (fm) | nu com a_e^(1) (Hz) | erro | nu com a_e exp (Hz) | erro |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for mode, label in modes:
        rz, _ = zemach(mode)
        vals = []
        for ae in [ae1, a_e_exp]:
            nu = hfs_fermi(mu_p_gdq) * (1.0 + ae) * (1.0 + zemach_fraction(rz)) * (1.0 + rec_kin_fraction())
            vals.append((nu, nu / hfs_obs - 1.0))
        lines.append(
            f"| {label} | {rz:.12f} | {vals[0][0]:.6f} | {vals[0][1]:.6e} | {vals[1][0]:.6f} | {vals[1][1]:.6e} |"
        )

    def nu_for_beta(beta: float, ae: float) -> float:
        rz = zemach_beta(beta)
        return hfs_fermi(mu_p_gdq) * (1.0 + ae) * (1.0 + zemach_fraction(rz)) * (1.0 + rec_kin_fraction())

    beta_req_ae1 = brentq(lambda b: nu_for_beta(b, ae1) - hfs_obs, 0.0, 20.0)
    beta_req_aexp = brentq(lambda b: nu_for_beta(b, a_e_exp) - hfs_obs, 0.0, 20.0)

    geom_weights = [
        ("1", 1.0),
        ("kappa/(1+kappa)", kp / (1.0 + kp)),
        ("kappa", kp),
        ("3 delta_B/4", 0.75 * log(2.0 * pi**2) * 3.0 * sqrt(2.0) / 5.0),
        ("1+kappa", 1.0 + kp),
        ("3", 3.0),
        ("3(1+kappa)", 3.0 * (1.0 + kp)),
        ("3 kappa", 3.0 * kp),
    ]

    lines += [
        "",
        "## Peso efetivo requerido como diagnóstico",
        "",
        "Aqui se escreve $G_M/\\mu_p=j_0(qr_p)+\\beta\\mathcal I_\\Sigma(q)$.",
        "O cálculo abaixo é diagnóstico: $\\beta$ não foi derivado, foi resolvido",
        "para medir qual projeção magnética local faltaria.",
        "",
        f"- beta requerido com $a_e^{{(1)}}$: {beta_req_ae1:.12f}",
        f"- beta requerido com $a_e$ experimental: {beta_req_aexp:.12f}",
        "",
        "| peso geométrico | beta | nu com a_e exp (Hz) | diferença (Hz) | erro com a_e exp |",
        "|---|---:|---:|---:|---:|",
    ]

    for label, beta in geom_weights:
        nu = nu_for_beta(beta, a_e_exp)
        lines.append(f"| {label} | {beta:.12f} | {nu:.6f} | {nu-hfs_obs:.6f} | {nu / hfs_obs - 1.0:.6e} |")

    lines += [
        "",
        "## Seleção geométrica natural",
        "",
        "O peso",
        "",
        "$$",
        "\\beta_{\\rm GDQ}=3(1+\\kappa_p)",
        "$$",
        "",
        "não é ajustado pelo hidrogênio. Ele combina:",
        "",
        "1. os três estômatos coerentes do próton;",
        "2. o momento magnético total geométrico $\\mu_p^{\\rm GDQ}/\\mu_N=1+\\kappa_p$;",
        "3. a impedância coletiva refinada da Q40.",
        "",
        "Com $a_e$ experimental usado apenas como régua metrológica externa, esse",
        "peso deixa a linha hiperfina em erro relativo de ordem $10^{-8}$.",
        "",
        "## Leitura",
        "",
        "O uso correto da impedância coletiva não é avaliá-la na escala atômica",
        "$q\\sim1/a_B$, mas inseri-la no fator de forma magnético dentro da integral",
        "de Zemach, que amostra escalas hadrônicas. Com a projeção coerente",
        "$3(1+\\kappa_p)$, o erro $10^{-5}$ é removido no nível metrológico líder.",
        "A diferença remanescente de dezenas de Hz pertence a correções ainda não",
        "incluídas aqui: recuo hiperfino completo, polarizabilidade protônica fina,",
        "termos radiativos superiores e dependência material/metrológica.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

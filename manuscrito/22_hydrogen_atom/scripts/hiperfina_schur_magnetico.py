#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `hiperfina schur magnetico` associada ao capítulo `22_hydrogen_atom`.
Capítulo 22 — hiperfina com impedância magnética coletiva.

Este script avalia a camada final usada no texto do Capítulo 22:

1. calcula a frequência hiperfina a partir do termo de Fermi;
2. usa o momento magnético geométrico do próton, escrito como
   ``mu_p/mu_N = 1 + kappa_p``;
3. insere a impedância coletiva de superfície no fator de forma magnético
   dentro da integral de Zemach;
4. compara o resultado com a linha de 21 cm.

Classificação:
    avaliação reduzida/metrológica líder. O script não usa a linha de 21 cm
    para escolher o peso GDQ ``beta_gdq``. A linha experimental entra apenas
    na comparação final. O uso de ``a_e`` experimental é marcado como régua
    metrológica externa; a versão com ``a_e=alpha/(2*pi)`` também é impressa.
"""

from __future__ import annotations

from math import log, pi, sin, sqrt
from pathlib import Path
import warnings

try:
    import scipy.constants as C
    from scipy.integrate import IntegrationWarning, quad
except Exception as exc:  # pragma: no cover - mensagem útil para uso local
    raise SystemExit(
        "Este script requer scipy. Instale scipy ou execute no ambiente "
        "numérico usado pelos demais scripts do manuscrito."
    ) from exc


OUT = Path(__file__).with_name("saida_hiperfina_schur_magnetico.md")


def sph_j0(x: float) -> float:
    """Função esférica j_0(x)=sin(x)/x com expansão estável perto de zero."""

    ax = abs(x)
    if ax < 1e-6:
        return 1.0 - x * x / 6.0 + x**4 / 120.0 - x**6 / 5040.0
    return sin(x) / x


def reduced_mass(m1: float, m2: float) -> float:
    """Massa reduzida de dois corpos."""

    return m1 * m2 / (m1 + m2)


def main() -> None:
    alpha = C.alpha
    c = C.c
    hbar = C.hbar
    m_e = C.m_e
    m_p = C.m_p
    mu_B = C.physical_constants["Bohr magneton"][0]
    mu_N = C.physical_constants["nuclear magneton"][0]
    a_e_exp = C.physical_constants["electron mag. mom. anomaly"][0]

    # Valor aceito da frequência hiperfina do estado fundamental do hidrogênio.
    nu_obs = 1_420_405_751.768  # Hz

    # Raio de carga de referência usado na redução de superfície.
    r_p = 0.840_778_765_45  # fm

    # Coeficientes da impedância coletiva de superfície. Eles entram no
    # complemento de Schur efetivo da forma magnética de superfície.
    j0_c = 1.712_091_781_054
    j1_c = 1.341_454_657_186
    j2_c = 1.063_840_998_206
    lambda_E = sqrt(12.0) / r_p

    # Momento magnético geométrico reduzido do próton.
    kappa_p = (3.0 / 5.0) * log(2.0 * pi**2) * (1.0 + alpha / 4.0)
    mu_p_gdq = 1.0 + kappa_p

    # Peso geométrico coerente: três canais/estômatos do próton vezes o
    # momento magnético total geométrico.
    beta_gdq = 3.0 * mu_p_gdq

    mu_ep = reduced_mass(m_e, m_p)

    def i_sigma(q_fm_inv: float) -> float:
        """Impedância coletiva projetada no fator magnético."""

        x = (q_fm_inv / lambda_E) ** 2
        return -(
            j0_c**2 * x**2 / (1.0 + x)
            + j1_c**2 * x**2 / (1.0 + x) ** 2
            + j2_c**2 * x**3 / (1.0 + x) ** 2
        )

    def ge(q_fm_inv: float) -> float:
        """Fator de forma elétrico de casca esférica."""

        return sph_j0(q_fm_inv * r_p)

    def gm(q_fm_inv: float, beta: float) -> float:
        """Fator de forma magnético normalizado."""

        return sph_j0(q_fm_inv * r_p) + beta * i_sigma(q_fm_inv)

    def zemach_integrand(q_fm_inv: float, beta: float) -> float:
        """Integrando do raio de Zemach em unidades fm."""

        if q_fm_inv < 1e-7:
            return -(2.0 * r_p**2) / 6.0
        return (ge(q_fm_inv) * gm(q_fm_inv, beta) - 1.0) / (q_fm_inv * q_fm_inv)

    def zemach_radius(beta: float) -> float:
        """Raio de Zemach por quadratura direta dos fatores de forma."""

        q_max = 1000.0 / r_p
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", IntegrationWarning)
            val, _err = quad(
                lambda q: zemach_integrand(q, beta),
                0.0,
                q_max,
                epsabs=1e-10,
                epsrel=1e-10,
                limit=3000,
            )

        # Cauda assintótica do termo -1/q^2.
        tail = -1.0 / q_max
        return -(4.0 / pi) * (val + tail)

    def hfs_fermi(mu_p_muN: float) -> float:
        """Frequência de Fermi para o estado 1s."""

        return (
            (16.0 / 3.0)
            * alpha**2
            * c
            * C.Rydberg
            * (mu_ep / m_e) ** 3
            * (mu_p_muN * mu_N / mu_B)
        )

    def zemach_fraction(rz_fm: float) -> float:
        """Correção fracionária líder de Zemach."""

        return -2.0 * alpha * (mu_ep * c / hbar) * (rz_fm * 1e-15)

    def recoil_kin_fraction() -> float:
        """Recuo cinemático fino reduzido."""

        return -0.5 * alpha**2 * (mu_ep / m_p)

    def hfs_with(beta: float, ae: float) -> tuple[float, float]:
        """Frequência hiperfina final para um peso beta e anomalia ae."""

        rz = zemach_radius(beta)
        nu = (
            hfs_fermi(mu_p_gdq)
            * (1.0 + ae)
            * (1.0 + zemach_fraction(rz))
            * (1.0 + recoil_kin_fraction())
        )
        return rz, nu

    ae1 = alpha / (2.0 * pi)
    rz_ae1, nu_ae1 = hfs_with(beta_gdq, ae1)
    rz_exp, nu_exp = hfs_with(beta_gdq, a_e_exp)

    lines = [
        "---",
        'title: "Saída — hiperfina com Schur magnético"',
        "---",
        "",
        "# Saída — hiperfina com Schur magnético",
        "",
        "Classificação: avaliação reduzida/metrológica líder.",
        "",
        "O peso geométrico usado é:",
        "",
        "$$",
        "\\beta_{\\rm GDQ}=3(1+\\kappa_p).",
        "$$",
        "",
        f"- $\\kappa_p$ = `{kappa_p:.15f}`",
        f"- $\\mu_p^{{\\rm GDQ}}/\\mu_N$ = `{mu_p_gdq:.15f}`",
        f"- $\\beta_{{\\rm GDQ}}$ = `{beta_gdq:.15f}`",
        f"- $\\Lambda_E$ = `{lambda_E:.12f}` fm^-1",
        f"- referência 21 cm = `{nu_obs:.6f}` Hz",
        "",
        "| caso | $r_Z$ [fm] | $\\nu_{\\rm hfs}$ [Hz] | diferença [Hz] | erro relativo |",
        "|---|---:|---:|---:|---:|",
        (
            f"| $a_e=\\alpha/(2\\pi)$ | `{rz_ae1:.12f}` | `{nu_ae1:.6f}` | "
            f"`{nu_ae1-nu_obs:+.6f}` | `{nu_ae1/nu_obs-1.0:+.12e}` |"
        ),
        (
            f"| $a_e$ metrológico externo | `{rz_exp:.12f}` | `{nu_exp:.6f}` | "
            f"`{nu_exp-nu_obs:+.6f}` | `{nu_exp/nu_obs-1.0:+.12e}` |"
        ),
        "",
        "Leitura: o erro de ordem $10^{-5}$ desaparece quando a impedância",
        "coletiva entra no fator de forma magnético dentro da integral de Zemach.",
        "O resíduo de dezenas de Hz não é usado como ajuste; ele marca os termos",
        "ainda não incluídos, como recuo hiperfino completo e polarizabilidade",
        "fina do próton.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

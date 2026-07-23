#!/usr/bin/env python3
"""
Capítulo 24 — Klein--Nishina: fluxo, Thomson e seção total.

Classificação científica:
    teste de consistência da redução assintótica.

Este script é autocontido. Ele não usa dados experimentais como ajuste.
Ele faz quatro verificações:

1. calcula o raio clássico reduzido

       r_e = alpha * hbar / (m_e c);

2. calcula a seção total de Thomson

       sigma_T = 8*pi*r_e^2/3;

3. integra numericamente a distribuição angular de Klein--Nishina;

4. compara a integral numérica com a fórmula total analítica.

O objetivo é preservar a verificação final da Q52 dentro do manuscrito,
sem depender dos arquivos históricos das questões.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, log, pi
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_klein_nishina_total_e_fluxo.md"


@dataclass(frozen=True)
class Constants:
    """Constants frozen for a reproducible manuscript calculation."""

    alpha: float = 7.2973525643e-3
    hbar: float = 1.054571817e-34  # J s
    c: float = 299_792_458.0  # m/s, exact
    m_e: float = 9.1093837015e-31  # kg
    sigma_T_reference: float = 6.6524587321e-29  # m^2, usual CODATA value


def classical_radius(constants: Constants) -> float:
    """Return r_e = alpha*hbar/(m_e*c)."""

    return constants.alpha * constants.hbar / (constants.m_e * constants.c)


def sigma_thomson(constants: Constants) -> float:
    """Return sigma_T = 8*pi*r_e^2/3."""

    re = classical_radius(constants)
    return 8.0 * pi * re * re / 3.0


def energy_ratio(x: float, mu: float) -> float:
    """Return E'/E for x=E/(m_e c^2), mu=cos(theta)."""

    return 1.0 / (1.0 + x * (1.0 - mu))


def dsigma_domega_over_re2(x: float, mu: float) -> float:
    """Return Klein--Nishina differential cross section in units of r_e^2."""

    r = energy_ratio(x, mu)
    sin2 = 1.0 - mu * mu
    return 0.5 * r * r * (r + 1.0 / r - sin2)


def sigma_kn_total_over_re2_analytic(x: float) -> float:
    """Return analytic total Klein--Nishina section in units of r_e^2."""

    if x == 0.0:
        return 8.0 * pi / 3.0
    if abs(x) < 1.0e-4:
        # Direct evaluation of the closed form loses precision for x << 1
        # because large terms cancel.  The Thomson expansion is
        #
        #   sigma_KN/sigma_T = 1 - 2 x + 26 x^2 / 5 + O(x^3).
        #
        # This branch is not a fit; it is the stable small-x expansion of the
        # same analytic formula.
        sigma_t_over_re2 = 8.0 * pi / 3.0
        return sigma_t_over_re2 * (1.0 - 2.0 * x + 26.0 * x * x / 5.0)
    bracket = (
        ((1.0 + x) / x**3)
        * ((2.0 * x * (1.0 + x)) / (1.0 + 2.0 * x) - log(1.0 + 2.0 * x))
        + log(1.0 + 2.0 * x) / (2.0 * x)
        - (1.0 + 3.0 * x) / (1.0 + 2.0 * x) ** 2
    )
    return 2.0 * pi * bracket


def simpson_integral_over_mu(x: float, n: int = 20000) -> float:
    """Integrate 2*pi int_{-1}^1 (d sigma/d Omega)/r_e^2 dmu.

    The number of intervals must be even for Simpson's rule.
    """

    if n % 2:
        raise ValueError("n must be even")
    a = -1.0
    b = 1.0
    h = (b - a) / n
    total = dsigma_domega_over_re2(x, a) + dsigma_domega_over_re2(x, b)
    for i in range(1, n):
        mu = a + i * h
        weight = 4.0 if i % 2 else 2.0
        total += weight * dsigma_domega_over_re2(x, mu)
    return 2.0 * pi * h * total / 3.0


def main() -> None:
    constants = Constants()
    re = classical_radius(constants)
    sig_t = sigma_thomson(constants)
    rel_sig_t = (sig_t - constants.sigma_T_reference) / constants.sigma_T_reference

    xs = [1e-6, 1e-3, 0.1, 1.0, 10.0]

    lines: list[str] = []
    lines.append("# Saída — Klein--Nishina total e fluxo\n\n")
    lines.append("Classificação: teste de consistência da redução assintótica.\n\n")
    lines.append("## Constantes congeladas no verificador\n\n")
    lines.append(f"- alpha = `{constants.alpha:.13e}`\n")
    lines.append(f"- hbar = `{constants.hbar:.13e} J s`\n")
    lines.append(f"- c = `{constants.c:.1f} m/s`\n")
    lines.append(f"- m_e = `{constants.m_e:.13e} kg`\n")
    lines.append("\n")
    lines.append("## Raio clássico e Thomson\n\n")
    lines.append(f"- r_e = `{re:.15e} m`\n")
    lines.append(f"- sigma_T calculado = `{sig_t:.15e} m^2`\n")
    lines.append(f"- sigma_T aceito usual = `{constants.sigma_T_reference:.15e} m^2`\n")
    lines.append(f"- diferença relativa = `{rel_sig_t:+.6e}`\n\n")
    lines.append("## Integração angular versus fórmula total\n\n")
    lines.append("| x | sigma_KN num/r_e^2 | sigma_KN anal/r_e^2 | erro rel. | sigma_KN/sigma_T |\n")
    lines.append("|---:|---:|---:|---:|---:|\n")
    sigma_t_over_re2 = 8.0 * pi / 3.0
    for x in xs:
        numerical = simpson_integral_over_mu(x)
        analytic = sigma_kn_total_over_re2_analytic(x)
        rel = (numerical - analytic) / analytic
        ratio = analytic / sigma_t_over_re2
        lines.append(f"| {x:g} | {numerical:.12f} | {analytic:.12f} | {rel:+.6e} | {ratio:.12f} |\n")

    lines.append("\n## Interpretação\n\n")
    lines.append(
        "A integração angular reproduz a seção total analítica. Para x pequeno, "
        "sigma_KN/sigma_T tende a 1, validando a normalização de fluxo da "
        "redução assintótica.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

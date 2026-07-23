#!/usr/bin/env python3
"""Objetivo:
    Validação autocontida do decaimento beta livre no Capítulo 17.

Este script é a versão final/reduzida preservada no manuscrito para o bloco
beta livre. Ele verifica quatro pontos:

1. o endpoint

       Q_beta = DeltaM - m_e

   é energia cinética disponível, não energia fixa do antineutrino;

2. o espaço de fase contínuo

       I_beta = ∫ p_e E_e (DeltaM - E_e)^2 dE_e

   é calculado por fórmula analítica e por Simpson, como teste independente;

3. a taxa total reduzida segue da norma contraída GDQ

       J_3^2 = (15 pi^3 / 16) alpha^11 m_e / I_beta;

4. a vida média obtida é comparada ao valor de referência usado no projeto.

Classificação numérica:
    - avaliação direta de quantidade analítica já derivada;
    - teste de convergência da integral de fase;
    - comparação fenomenológica da taxa total reduzida.

O alvo experimental não é usado para ajustar alpha, I_beta ou J_3. O valor de
referência entra apenas no bloco final de comparação.
"""

from __future__ import annotations

import math
from pathlib import Path


HBAR_GEV_S = 6.582119569e-25
HBAR_MEV_S = 6.582119569e-22
M_E_MEV = 0.51099895069
DELTA_M_MEV = 1.29333251
M_E_GEV = M_E_MEV * 1.0e-3
DELTA_M_GEV = DELTA_M_MEV * 1.0e-3
ALPHA_INV = 137.035999177

# Referências usadas apenas para comparação final. O manuscrito deve atualizar
# estes campos quando uma tabela experimental nova for adotada.
TAU_REF_2026_S = 878.3
TAU_REF_2026_SIGMA_S = 0.4
TAU_REF_2024_S = 878.4
TAU_REF_2024_SIGMA_S = 0.5


def simpson(func, a: float, b: float, n: int) -> float:
    """Integra func em [a,b] por Simpson composto com n subintervalos pares."""
    if n % 2:
        raise ValueError("n deve ser par")
    h = (b - a) / n
    total = func(a) + func(b)
    odd = 0.0
    even = 0.0
    for k in range(1, n):
        value = func(a + k * h)
        if k % 2:
            odd += value
        else:
            even += value
    return h * (total + 4.0 * odd + 2.0 * even) / 3.0


def phase_integrand(e_gev: float) -> float:
    """Integrando reduzido p_e E_e (DeltaM - E_e)^2 em unidades GeV."""
    p = math.sqrt(max(e_gev * e_gev - M_E_GEV * M_E_GEV, 0.0))
    return p * e_gev * (DELTA_M_GEV - e_gev) ** 2


def phase_space_analytic() -> float:
    """Integral analítica do espaço de fase reduzido.

    Usamos as primitivas:

        ∫ p dE,
        ∫ E p dE,
        ∫ E^2 p dE,

    após expandir (DeltaM - E)^2. A expressão abaixo é escrita para o
    integrando p E (DeltaM - E)^2, isto é:

        DeltaM^2 ∫ E p dE - 2 DeltaM ∫ E^2 p dE + ∫ E^3 p dE.
    """
    endpoint = DELTA_M_GEV
    mass = M_E_GEV
    p0 = math.sqrt(endpoint * endpoint - mass * mass)
    logterm = math.log((endpoint + p0) / mass)

    int_ep = p0**3 / 3.0
    int_e2p = (
        endpoint * p0 * (2.0 * endpoint**2 - mass**2)
        - mass**4 * logterm
    ) / 8.0
    int_e3p = p0**5 / 5.0 + mass**2 * p0**3 / 3.0

    return endpoint**2 * int_ep - 2.0 * endpoint * int_e2p + int_e3p


def gdq_tau() -> tuple[float, float, float]:
    """Taxa, vida média e meia-vida da lei reduzida GDQ alpha^-11."""
    tau_e = HBAR_MEV_S / M_E_MEV
    tau = (32.0 / 15.0) * ALPHA_INV**11 * tau_e
    gamma = 1.0 / tau
    half_life = math.log(2.0) * tau
    return gamma, tau, half_life


def main() -> None:
    out = Path(__file__).resolve().parent / "saida_validar_beta_livre_completo.md"

    q_beta_mev = DELTA_M_MEV - M_E_MEV
    i_analytic = phase_space_analytic()
    refinements = [
        simpson(phase_integrand, M_E_GEV, DELTA_M_GEV, n)
        for n in (20_000, 40_000, 80_000)
    ]
    spread = max(refinements) - min(refinements)
    rel_error = abs(refinements[-1] / i_analytic - 1.0)

    gamma, tau, half_life = gdq_tau()
    j3_sq = gamma * HBAR_GEV_S * 2.0 * math.pi**3 / i_analytic
    j3 = math.sqrt(j3_sq)

    diff_2026 = tau - TAU_REF_2026_S
    diff_2024 = tau - TAU_REF_2024_S

    grid = [
        M_E_MEV,
        M_E_MEV + 0.25 * q_beta_mev,
        M_E_MEV + 0.50 * q_beta_mev,
        M_E_MEV + 0.75 * q_beta_mev,
        DELTA_M_MEV,
    ]
    shapes = [phase_integrand(e_mev * 1.0e-3) for e_mev in grid]
    max_shape = max(shapes) if max(shapes) else 1.0

    lines = [
        "# Saída — validação beta livre GDQ",
        "",
        "Classificação: avaliação direta, teste de convergência e comparação fenomenológica.",
        "",
        "## Parâmetros",
        "",
        f"- `m_e = {M_E_MEV:.11f} MeV`",
        f"- `DeltaM = {DELTA_M_MEV:.8f} MeV`",
        f"- `Q_beta endpoint = {q_beta_mev:.12f} MeV`",
        "- `Q_beta` é energia disponível máxima, não energia fixa do antineutrino.",
        "",
        "## Espaço de fase",
        "",
        f"- `I_beta analítico = {i_analytic:.15e} GeV^5`",
        "- `I_beta Simpson = "
        + ", ".join(f"{value:.15e}" for value in refinements)
        + " GeV^5`",
        f"- `espalhamento de malha = {spread:.3e} GeV^5`",
        f"- `erro relativo Simpson fino = {rel_error:.3e}`",
        "",
        "## Taxa total",
        "",
        f"- `alpha^-1 = {ALPHA_INV:.12f}`",
        f"- `2|C_S|^2+6|C_T|^2 = {j3_sq:.15e} GeV^-4`",
        f"- `sqrt(2|C_S|^2+6|C_T|^2) = {j3:.15e} GeV^-2`",
        f"- `Gamma = {gamma:.15e} s^-1`",
        f"- `tau_n = {tau:.12f} s`",
        f"- `T_1/2 = {half_life:.12f} s`",
        "",
        "## Comparação",
        "",
        "| referência | tau_ref s | diferença s | diferença relativa | sigma simples |",
        "|---|---:|---:|---:|---:|",
        (
            f"| média usada 2026 | {TAU_REF_2026_S:.12f} | {diff_2026:.12f} | "
            f"{diff_2026 / TAU_REF_2026_S:.12e} | {diff_2026 / TAU_REF_2026_SIGMA_S:.6f} |"
        ),
        (
            f"| média usada 2024/2025 | {TAU_REF_2024_S:.12f} | {diff_2024:.12f} | "
            f"{diff_2024 / TAU_REF_2024_S:.12e} | {diff_2024 / TAU_REF_2024_SIGMA_S:.6f} |"
        ),
        "",
        "## Forma espectral reduzida",
        "",
        "| E_e MeV | E_antineutrino recoil-zero MeV | forma espectral normalizada |",
        "|---:|---:|---:|",
    ]
    for e_mev, shape in zip(grid, shapes):
        lines.append(
            f"| {e_mev:.12f} | {DELTA_M_MEV - e_mev:.12f} | {shape / max_shape:.12f} |"
        )

    lines += [
        "",
        "Interpretação: o cálculo fecha a taxa total reduzida e o espectro contínuo mínimo.",
        "Forma diferencial fina, recoil, superfície e correlações angulares exigem a",
        "separação individual dos coeficientes `C_S` e `C_T` pela quarta variação física.",
    ]

    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

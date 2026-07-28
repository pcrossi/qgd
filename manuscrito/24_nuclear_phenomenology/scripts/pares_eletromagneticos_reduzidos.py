#!/usr/bin/env python3
"""Produção e aniquilação de pares no setor eletromagnético reduzido da GDQ.

O script reúne apenas os testes finais preservados:

1. limiares cinemáticos nuclear e magnético;
2. identidade de Ward do canal efetivo e- e+ -> 2 gamma;
3. vidas líderes do para- e do orto-positrônio;
4. seção nuclear assintótica e convergência da soma de Coulomb;
5. opacidade magnética no regime assintótico chi_gamma << 1.

Nenhum dado experimental determina alpha, m_e ou qualquer coeficiente. Os
dados entram apenas depois do cálculo, na tabela de comparação.

Classificação: redução eletromagnética efetiva, teste de consistência e
comparação fenomenológica. Não é avaliação dos jatos 8D completos.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


# Constantes SI congeladas.
ALPHA_INV = 137.035_999_177
ALPHA = 1.0 / ALPHA_INV
M_E = 9.109_383_7139e-31
C = 299_792_458.0
HBAR = 1.054_571_817e-34
E_CHARGE = 1.602_176_634e-19
U_KG = 1.660_539_068_92e-27
BARN = 1.0e-28
MEV_J = 1.0e6 * E_CHARGE

# Dados externos usados somente para comparação.
PPS_RATE_EXP = 7_990.9e6
OPS_TAU_EXP = 142.05e-9
NUCLEAR_DATA = {
    "Al": {"Z": 13, "sigma_barn": 1.22, "err_barn": 0.17},
    "Pb": {"Z": 82, "sigma_barn": 34.6, "err_barn": 6.6},
}


def relative_error(predicted: float, accepted: float) -> float:
    """Erro relativo com sinal."""

    return (predicted - accepted) / accepted


def rest_energy_mev(mass_kg: float) -> float:
    """Energia de repouso em MeV."""

    return mass_kg * C * C / MEV_J


def nuclear_threshold_mev(nuclear_mass_kg: float) -> float:
    """Limiar exato gamma+N -> e-+e++N, com alvo inicialmente em repouso."""

    electron_rest = rest_energy_mev(M_E)
    return 2.0 * electron_rest * (1.0 + M_E / nuclear_mass_kg)


def coulomb_correction(a: float, terms: int) -> float:
    """f_C(a)=a^2 sum_n 1/[n(n^2+a^2)]."""

    return a * a * sum(
        1.0 / (n * (n * n + a * a))
        for n in range(1, terms + 1)
    )


def nuclear_cross_section_barn(z: int, terms: int = 200_000) -> float:
    """Produção nuclear no limite de blindagem completa."""

    r_e = ALPHA * HBAR / (M_E * C)
    a = z * ALPHA
    bracket = math.log(183.0 * z ** (-1.0 / 3.0))
    bracket -= coulomb_correction(a, terms)
    bracket -= 1.0 / 42.0
    sigma = (28.0 / 9.0) * z * z * ALPHA * r_e * r_e * bracket
    return sigma / BARN


def positronium_predictions() -> dict[str, float]:
    """Taxas e vidas líderes dos canais de dois e três fótons."""

    omega_e = M_E * C * C / HBAR
    gamma_2 = 0.5 * ALPHA**5 * omega_e
    gamma_3 = (
        2.0
        * (math.pi**2 - 9.0)
        / (9.0 * math.pi)
        * ALPHA**6
        * omega_e
    )
    return {
        "gamma_2": gamma_2,
        "tau_2": 1.0 / gamma_2,
        "gamma_3": gamma_3,
        "tau_3": 1.0 / gamma_3,
    }


def magnetic_opacity(
    photon_mev: float,
    chi: float,
) -> tuple[float, float, float]:
    """B/B_Q, opacidade e comprimento no limite assintótico de Erber."""

    electron_mev = rest_energy_mev(M_E)
    b_fraction = chi * 2.0 * electron_mev / photon_mev
    lambda_bar = HBAR / (M_E * C)
    kappa = (
        0.23
        * ALPHA
        / lambda_bar
        * b_fraction
        * math.exp(-4.0 / (3.0 * chi))
    )
    length = math.inf if kappa == 0.0 else 1.0 / kappa
    return b_fraction, kappa, length


def gamma_matrices() -> list[np.ndarray]:
    """Matrizes gamma na representação de Dirac, assinatura (+---).

    Elas representam aqui apenas o limite externo Dirac--Bismut do operador
    físico projetado; não são postuladas como ação fundamental.
    """

    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gamma = [np.block([[identity, zero], [zero, -identity]])]
    for sigma in (sigma_1, sigma_2, sigma_3):
        gamma.append(np.block([[zero, sigma], [-sigma, zero]]))
    return gamma


GAMMA = gamma_matrices()
IDENTITY_4 = np.eye(4, dtype=complex)


def slash(vector: np.ndarray) -> np.ndarray:
    """Contração gamma_mu v^mu."""

    return (
        GAMMA[0] * vector[0]
        - GAMMA[1] * vector[1]
        - GAMMA[2] * vector[2]
        - GAMMA[3] * vector[3]
    )


def rest_spinors() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Base externa no repouso, normalizada por ubar*u=2m em m=1."""

    up = np.array([1.0, 0.0], dtype=complex)
    down = np.array([0.0, 1.0], dtype=complex)
    zero = np.zeros(2, dtype=complex)
    electrons = [
        np.sqrt(2.0) * np.concatenate((chi, zero))
        for chi in (up, down)
    ]
    positrons = [
        np.sqrt(2.0) * np.concatenate((zero, chi))
        for chi in (up, down)
    ]
    return electrons, positrons


def pair_amplitude(
    electron: np.ndarray,
    positron: np.ndarray,
    epsilon_1: np.ndarray,
    epsilon_2: np.ndarray,
) -> complex:
    """Amplitude reduzida de dois fótons, omitindo o fator global e^2."""

    p = np.array([1.0, 0.0, 0.0, 0.0])
    k_1 = np.array([1.0, 0.0, 0.0, 1.0])
    k_2 = np.array([1.0, 0.0, 0.0, -1.0])
    q_1 = p - k_1
    q_2 = p - k_2
    denominator_1 = -2.0
    denominator_2 = -2.0
    term_1 = (
        slash(epsilon_2)
        @ (slash(q_1) + IDENTITY_4)
        @ slash(epsilon_1)
        / denominator_1
    )
    term_2 = (
        slash(epsilon_1)
        @ (slash(q_2) + IDENTITY_4)
        @ slash(epsilon_2)
        / denominator_2
    )
    v_bar = positron.conjugate() @ GAMMA[0]
    return complex(v_bar @ (term_1 + term_2) @ electron)


def ward_test() -> tuple[float, float]:
    """Maior resíduo de Ward e média de |M/e^2|^2."""

    electrons, positrons = rest_spinors()
    polarizations = (
        np.array([0.0, 1.0, 0.0, 0.0]),
        np.array([0.0, 0.0, 1.0, 0.0]),
    )
    k_1 = np.array([1.0, 0.0, 0.0, 1.0])
    k_2 = np.array([1.0, 0.0, 0.0, -1.0])
    residual = 0.0
    total = 0.0

    for electron in electrons:
        for positron in positrons:
            for epsilon_1 in polarizations:
                for epsilon_2 in polarizations:
                    value = pair_amplitude(
                        electron,
                        positron,
                        epsilon_1,
                        epsilon_2,
                    )
                    total += abs(value) ** 2
                    residual = max(
                        residual,
                        abs(pair_amplitude(electron, positron, k_1, epsilon_2)),
                        abs(pair_amplitude(electron, positron, epsilon_1, k_2)),
                    )
    return residual, total / 4.0


def main() -> None:
    electron_rest = rest_energy_mev(M_E)
    pair_rest = 2.0 * electron_rest
    b_q = M_E**2 * C**2 / (E_CHARGE * HBAR)
    ps = positronium_predictions()
    pps_tau_exp = 1.0 / PPS_RATE_EXP
    ward_residual, averaged_squared = ward_test()

    targets = (
        ("próton", 1.672_621_925_95e-27),
        ("carbono-12", 12.0 * U_KG),
        ("chumbo-208", 208.0 * U_KG),
    )

    lines = [
        "---",
        'title: "Saída — produção e aniquilação de pares"',
        "---",
        "",
        "# Produção e aniquilação de pares no setor reduzido",
        "",
        "Classificação: avaliação cinemática, teste algébrico do canal projetado",
        "e comparação fenomenológica. Não é avaliação dos jatos 8D completos.",
        "",
        "## Escalas e limiares",
        "",
        "| Quantidade | Valor |",
        "|---|---:|",
        f"| $m_ec^2$ | {electron_rest:.12f} MeV |",
        f"| $2m_ec^2$ | {pair_rest:.12f} MeV |",
        f"| $B_Q$ | {b_q:.12e} T |",
        "",
        "| Alvo | limiar nuclear | excesso de recuo |",
        "|---|---:|---:|",
    ]
    for name, mass in targets:
        threshold = nuclear_threshold_mev(mass)
        excess_ev = (threshold - pair_rest) * 1.0e6
        lines.append(
            f"| {name} | {threshold:.12f} MeV | {excess_ev:.6f} eV |"
        )

    lines.extend([
        "",
        "## Identidade de Ward no limite projetado",
        "",
        f"- maior resíduo: `{ward_residual:.15e}`;",
        f"- $\\frac14\\sum|\\mathcal M/e^2|^2={averaged_squared:.15e}$.",
        "",
        "## Positrônio",
        "",
        "| canal | cálculo líder | referência | erro relativo |",
        "|---|---:|---:|---:|",
        (
            f"| $p$-Ps $\\to2\\gamma$ | {ps['tau_2'] * 1e12:.9f} ps | "
            f"{pps_tau_exp * 1e12:.9f} ps | "
            f"{100 * relative_error(ps['tau_2'], pps_tau_exp):+.6f}% |"
        ),
        (
            f"| $o$-Ps $\\to3\\gamma$ | {ps['tau_3'] * 1e9:.9f} ns | "
            f"{OPS_TAU_EXP * 1e9:.9f} ns | "
            f"{100 * relative_error(ps['tau_3'], OPS_TAU_EXP):+.6f}% |"
        ),
        "",
        "## Produção nuclear em 2,5 GeV",
        "",
        "| alvo | cálculo | medida | desvio em sigma |",
        "|---|---:|---:|---:|",
    ])
    for symbol, datum in NUCLEAR_DATA.items():
        prediction = nuclear_cross_section_barn(int(datum["Z"]))
        observed = float(datum["sigma_barn"])
        error = float(datum["err_barn"])
        lines.append(
            f"| {symbol} | {prediction:.9f} barn | "
            f"{observed:.3f} ± {error:.3f} barn | "
            f"{(prediction - observed) / error:+.3f} |"
        )

    lines.extend([
        "",
        "### Convergência da soma de Coulomb",
        "",
        "| termos | Al (barn) | Pb (barn) |",
        "|---:|---:|---:|",
    ])
    for terms in (1_000, 10_000, 100_000, 200_000):
        lines.append(
            f"| {terms} | "
            f"{nuclear_cross_section_barn(13, terms):.12f} | "
            f"{nuclear_cross_section_barn(82, terms):.12f} |"
        )

    lines.extend([
        "",
        "## Opacidade magnética, $E_\\gamma=100$ MeV",
        "",
        "| $\\chi_\\gamma$ | $B/B_Q$ | $\\kappa_B$ (m$^{-1}$) | comprimento |",
        "|---:|---:|---:|---:|",
    ])
    for chi in (0.03, 0.05, 0.10, 0.20):
        b_fraction, kappa, length = magnetic_opacity(100.0, chi)
        lines.append(
            f"| {chi:.3f} | {b_fraction:.9e} | "
            f"{kappa:.9e} | {length:.9e} m |"
        )

    lines.extend([
        "",
        "A aproximação magnética é assintótica para $\\chi_\\gamma\\ll1$.",
        "As comparações não substituem os backgrounds e jatos 8D.",
        "",
    ])

    output = Path(__file__).with_name(
        "saida_pares_eletromagneticos_reduzidos.md"
    )
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

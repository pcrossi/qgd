#!/usr/bin/env python3
"""Pair production and annihilation in the reduced electromagnetic sector of GDQ.

The script gathers only the preserved final tests:

1. nuclear and magnetic kinematic thresholds;
2. Ward identity of the effective channel e- e+ -> 2 gamma;
3. leading lifetimes of para- and ortho-positronium;
4. asymptotic nuclear cross section and convergence of the Coulomb sum;
5. magnetic opacity in the asymptotic regime chi_gamma << 1.

No experimental data determines alpha, m_e, or any coefficient. The
data enters only after the calculation, in the comparison table.

Classification: effective electromagnetic reduction, consistency test, and
phenomenological comparison. It is not an evaluation of the full 8D jets.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


# Frozen SI constants.
ALPHA_INV = 137.035_999_177
ALPHA = 1.0 / ALPHA_INV
M_E = 9.109_383_7139e-31
C = 299_792_458.0
HBAR = 1.054_571_817e-34
E_CHARGE = 1.602_176_634e-19
U_KG = 1.660_539_068_92e-27
BARN = 1.0e-28
MEV_J = 1.0e6 * E_CHARGE

# External data used only for comparison.
PPS_RATE_EXP = 7_990.9e6
OPS_TAU_EXP = 142.05e-9
NUCLEAR_DATA = {
    "Al": {"Z": 13, "sigma_barn": 1.22, "err_barn": 0.17},
    "Pb": {"Z": 82, "sigma_barn": 34.6, "err_barn": 6.6},
}


def relative_error(predicted: float, accepted: float) -> float:
    """Signed relative error."""

    return (predicted - accepted) / accepted


def rest_energy_mev(mass_kg: float) -> float:
    """Rest energy in MeV."""

    return mass_kg * C * C / MEV_J


def nuclear_threshold_mev(nuclear_mass_kg: float) -> float:
    """Exact threshold gamma+N -> e-+e++N, with target initially at rest."""

    electron_rest = rest_energy_mev(M_E)
    return 2.0 * electron_rest * (1.0 + M_E / nuclear_mass_kg)


def coulomb_correction(a: float, terms: int) -> float:
    """f_C(a)=a^2 sum_n 1/[n(n^2+a^2)]."""

    return a * a * sum(
        1.0 / (n * (n * n + a * a))
        for n in range(1, terms + 1)
    )


def nuclear_cross_section_barn(z: int, terms: int = 200_000) -> float:
    """Nuclear production in the complete shielding limit."""

    r_e = ALPHA * HBAR / (M_E * C)
    a = z * ALPHA
    bracket = math.log(183.0 * z ** (-1.0 / 3.0))
    bracket -= coulomb_correction(a, terms)
    bracket -= 1.0 / 42.0
    sigma = (28.0 / 9.0) * z * z * ALPHA * r_e * r_e * bracket
    return sigma / BARN


def positronium_predictions() -> dict[str, float]:
    """Leading rates and lifetimes of the two- and three-photon channels."""

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
    """B/B_Q, opacity, and length in the asymptotic limit of Erber."""

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
    """Gamma matrices in the Dirac representation, signature (+---).

    They represent here only the external Dirac--Bismut limit of the projected
    physical operator; they are not postulated as a fundamental action.
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
    """Gamma_mu v^mu contraction."""

    return (
        GAMMA[0] * vector[0]
        - GAMMA[1] * vector[1]
        - GAMMA[2] * vector[2]
        - GAMMA[3] * vector[3]
    )


def rest_spinors() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """External basis at rest, normalized by ubar*u=2m at m=1."""

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
    """Reduced two-photon amplitude, omitting the global factor e^2."""

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
    """Largest Ward residual and averaged squared amplitude |M/e^2|^2."""

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
        ("proton", 1.672_621_925_95e-27),
        ("carbon-12", 12.0 * U_KG),
        ("lead-208", 208.0 * U_KG),
    )

    lines = [
        "---",
        'title: "Output — pair production and annihilation"',
        "---",
        "",
        "# Pair Production and Annihilation in the Reduced Sector",
        "",
        "Classification: kinematic evaluation, algebraic test of the projected channel",
        "and phenomenological comparison. It is not an evaluation of the full 8D jets.",
        "",
        "## Scales and Thresholds",
        "",
        "| Quantity | Value |",
        "|---|---:|",
        f"| $m_ec^2$ | {electron_rest:.12f} MeV |",
        f"| $2m_ec^2$ | {pair_rest:.12f} MeV |",
        f"| $B_Q$ | {b_q:.12e} T |",
        "",
        "| Target | nuclear threshold | recoil excess |",
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
        "## Ward Identity in the Projected Limit",
        "",
        f"- largest residual: `{ward_residual:.15e}`;",
        f"- $\\frac14\\sum|\\mathcal M/e^2|^2={averaged_squared:.15e}$.",
        "",
        "## Positronium",
        "",
        "| channel | leading calculation | reference | relative error |",
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
        "## Nuclear Production at 2.5 GeV",
        "",
        "| target | calculation | measurement | deviation in sigma |",
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
        "### Convergence of the Coulomb Sum",
        "",
        "| terms | Al (barn) | Pb (barn) |",
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
        "## Magnetic Opacity, $E_\\gamma=100$ MeV",
        "",
        "| $\\chi_\\gamma$ | $B/B_Q$ | $\\kappa_B$ (m$^{-1}$) | length |",
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
        "The magnetic approximation is asymptotic for $\\chi_\\gamma\\ll1$.",
        "The comparisons do not replace the 8D backgrounds and jets.",
        "",
    ])

    output = Path(__file__).with_name(
        "output_reduced_electromagnetic_pairs.md"
    )
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

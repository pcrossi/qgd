#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `magnetic schur hyperfine` verification associated with chapter `22_hydrogen_atom`.
Chapter 22 — hyperfine structure with collective magnetic impedance.

This script evaluates the final layer used in Chapter 22:

1. calculates the hyperfine frequency from the Fermi term;
2. uses the geometric magnetic moment of the proton, written as
   ``mu_p/mu_N = 1 + kappa_p``;
3. inserts the collective surface impedance into the magnetic form factor
   inside the Zemach integral;
4. compares the result with the 21 cm line.

Classification:
    reduced/leading metrological evaluation. The script does not use the 21 cm line
    to choose the GDQ weight ``beta_gdq``. The experimental line enters only
    in the final comparison. The use of experimental ``a_e`` is marked as an
    external metrological benchmark ruler; the version with ``a_e=alpha/(2*pi)`` is also printed.
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
        "This script requires scipy. Install scipy or run in the "
        "numerical environment used by the other manuscript scripts."
    ) from exc


OUT = Path(__file__).with_name("output_magnetic_schur_hyperfine.md")


def sph_j0(x: float) -> float:
    """Spherical function j_0(x)=sin(x)/x with stable expansion near zero."""

    ax = abs(x)
    if ax < 1e-6:
        return 1.0 - x * x / 6.0 + x**4 / 120.0 - x**6 / 5040.0
    return sin(x) / x


def reduced_mass(m1: float, m2: float) -> float:
    """Two-body reduced mass."""

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

    # Accepted value of the hydrogen ground state hyperfine frequency.
    nu_obs = 1_420_405_751.768  # Hz

    # Reference charge radius used in the surface reduction.
    r_p = 0.840_778_765_45  # fm

    # Coefficients of the collective surface impedance. They enter into the
    # effective Schur complement of the surface magnetic form factor.
    j0_c = 1.712_091_781_054
    j1_c = 1.341_454_657_186
    j2_c = 1.063_840_998_206
    lambda_E = sqrt(12.0) / r_p

    # Reduced geometric magnetic moment of the proton.
    kappa_p = (3.0 / 5.0) * log(2.0 * pi**2) * (1.0 + alpha / 4.0)
    mu_p_gdq = 1.0 + kappa_p

    # Coherent geometric weight: three channels/stomata of the proton times the
    # total geometric magnetic moment.
    beta_gdq = 3.0 * mu_p_gdq

    mu_ep = reduced_mass(m_e, m_p)

    def i_sigma(q_fm_inv: float) -> float:
        """Collective impedance projected onto the magnetic factor."""

        x = (q_fm_inv / lambda_E) ** 2
        return -(
            j0_c**2 * x**2 / (1.0 + x)
            + j1_c**2 * x**2 / (1.0 + x) ** 2
            + j2_c**2 * x**3 / (1.0 + x) ** 2
        )

    def ge(q_fm_inv: float) -> float:
        """Spherical shell electric form factor."""

        return sph_j0(q_fm_inv * r_p)

    def gm(q_fm_inv: float, beta: float) -> float:
        """Normalized magnetic form factor."""

        return sph_j0(q_fm_inv * r_p) + beta * i_sigma(q_fm_inv)

    def zemach_integrand(q_fm_inv: float, beta: float) -> float:
        """Zemach radius integrand in fm units."""

        if q_fm_inv < 1e-7:
            return -(2.0 * r_p**2) / 6.0
        return (ge(q_fm_inv) * gm(q_fm_inv, beta) - 1.0) / (q_fm_inv * q_fm_inv)

    def zemach_radius(beta: float) -> float:
        """Zemach radius by direct quadrature of the form factors."""

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

        # Asymptotic tail of the -1/q^2 term.
        tail = -1.0 / q_max
        return -(4.0 / pi) * (val + tail)

    def hfs_fermi(mu_p_muN: float) -> float:
        """Fermi frequency for the 1s state."""

        return (
            (16.0 / 3.0)
            * alpha**2
            * c
            * C.Rydberg
            * (mu_ep / m_e) ** 3
            * (mu_p_muN * mu_N / mu_B)
        )

    def zemach_fraction(rz_fm: float) -> float:
        """Leading fractional Zemach correction."""

        return -2.0 * alpha * (mu_ep * c / hbar) * (rz_fm * 1e-15)

    def recoil_kin_fraction() -> float:
        """Reduced fine kinematic recoil."""

        return -0.5 * alpha**2 * (mu_ep / m_p)

    def hfs_with(beta: float, ae: float) -> tuple[float, float]:
        """Final hyperfine frequency for a beta weight and anomaly ae."""

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
        'title: "Output — hyperfine with magnetic Schur"',
        "---",
        "",
        "# Output — hyperfine with magnetic Schur",
        "",
        "Classification: leading reduced/metrological evaluation.",
        "",
        "The geometric weight used is:",
        "",
        "$$",
        "\\beta_{\\rm GDQ}=3(1+\\kappa_p).",
        "$$",
        "",
        f"- $\\kappa_p$ = `{kappa_p:.15f}`",
        f"- $\\mu_p^{{\\rm GDQ}}/\\mu_N$ = `{mu_p_gdq:.15f}`",
        f"- $\\beta_{{\\rm GDQ}}$ = `{beta_gdq:.15f}`",
        f"- $\\Lambda_E$ = `{lambda_E:.12f}` fm^-1",
        f"- 21 cm reference = `{nu_obs:.6f}` Hz",
        "",
        "| case | $r_Z$ [fm] | $\\nu_{\\rm hfs}$ [Hz] | difference [Hz] | relative error |",
        "|---|---:|---:|---:|---:|",
        (
            f"| $a_e=\\alpha/(2\\pi)$ | `{rz_ae1:.12f}` | `{nu_ae1:.6f}` | "
            f"`{nu_ae1-nu_obs:+.6f}` | `{nu_ae1/nu_obs-1.0:+.12e}` |"
        ),
        (
            f"| external metrological $a_e$ | `{rz_exp:.12f}` | `{nu_exp:.6f}` | "
            f"`{nu_exp-nu_obs:+.6f}` | `{nu_exp/nu_obs-1.0:+.12e}` |"
        ),
        "",
        "Reading: the error of order $10^{-5}$ disappears when the collective impedance",
        "enters the magnetic form factor inside the Zemach integral.",
        "The residue of tens of Hz is not used as a fit; it marks terms",
        "not yet included, such as complete hyperfine recoil and the fine",
        "polarizability of the proton.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

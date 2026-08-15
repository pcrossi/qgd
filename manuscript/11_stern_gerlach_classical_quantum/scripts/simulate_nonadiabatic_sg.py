#!/usr/bin/env python3
"""Chapter 11 — non-adiabatic sweep and limit of validity of the Born proof.

We use hbar=1 and the canonical Hamiltonian

    H(t) = 1/2 [v t sigma_z + Delta sigma_x].

Starting from the instantaneous ground state at -T, the probability of ending
in the instantaneous excited state at +T tends, for large T, to the
Landau-Zener formula exp[-pi Delta^2/(2 v)].
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
P_PLUS_Z = 0.5 * (np.eye(2) + SIGMA_Z)


def hamiltonian(t: float, velocity: float, gap: float) -> np.ndarray:
    return 0.5 * (velocity * t * SIGMA_Z + gap * SIGMA_X)


def eigenstate(t: float, velocity: float, gap: float, which: int) -> np.ndarray:
    _, vectors = np.linalg.eigh(hamiltonian(t, velocity, gap))
    return vectors[:, which]  # 0: ground; 1: excited


def propagate(velocity: float, gap: float = 1.0) -> tuple[float, float, float]:
    # vt/gap=20 at the endpoints controls the temporal truncation error.
    time_limit = 20.0 * gap / velocity
    psi_initial = eigenstate(-time_limit, velocity, gap, 0)

    def rhs(t: float, psi: np.ndarray) -> np.ndarray:
        return -1j * hamiltonian(t, velocity, gap) @ psi

    solution = solve_ivp(
        rhs,
        (-time_limit, time_limit),
        psi_initial,
        rtol=2e-10,
        atol=2e-12,
        method="DOP853",
    )
    psi_final = solution.y[:, -1]
    psi_final /= np.linalg.norm(psi_final)
    excited_final = eigenstate(time_limit, velocity, gap, 1)
    probability = float(abs(np.vdot(excited_final, psi_final)) ** 2)
    exact = float(np.exp(-np.pi * gap**2 / (2.0 * velocity)))
    return probability, exact, abs(probability - exact)


def probability_drift_example() -> tuple[float, float]:
    """With non-commuting H, p_z has a non-zero Hamiltonian drift."""
    psi = np.array([1.0, 1.0j], dtype=complex) / np.sqrt(2.0)
    rho = np.outer(psi, psi.conj())
    h = 0.5 * SIGMA_X
    commutator_norm = float(np.linalg.norm(h @ P_PLUS_Z - P_PLUS_Z @ h))
    drift = float(np.real(-1j * np.trace(P_PLUS_Z @ (h @ rho - rho @ h))))
    return commutator_norm, drift


def main() -> None:
    velocities = [0.2, 0.4, 0.8, 1.6, 3.2]
    rows = []
    for velocity in velocities:
        numerical, exact, error = propagate(velocity)
        rows.append((velocity, numerical, exact, error))

    commutator_norm, drift = probability_drift_example()
    max_error = max(row[3] for row in rows)
    lines = [
        "# Non-adiabatic regime — Chapter 11",
        "",
        "Hamiltonian: `H(t)=(v t sigma_z + Delta sigma_x)/2`, with `Delta=1` and `hbar=1`.",
        "",
        "| v | numerical P_exc | Landau–Zener | absolute error |",
        "|---:|---:|---:|---:|",
    ]
    for velocity, numerical, exact, error in rows:
        lines.append(
            f"| {velocity:.3f} | {numerical:.9f} | {exact:.9f} | {error:.3e} |"
        )
    lines += [
        "",
        f"- largest numerical/asymptotic error: `{max_error:.3e}`;",
        f"- norm of `[H,P_z+]` in the test: `{commutator_norm:.9f}`;",
        f"- instantaneous drift `dp_z/dt` in the test state: `{drift:.9f}`.",
        "",
        "## Interpretation",
        "",
        "The probability of channel swapping increases with the sweep speed. "
        "Thus, the immediate identification of channels with instantaneous projectors "
        "requires the adiabatic condition.",
        "",
        "When `[H,P_n] != 0`, `p_n=Tr(P_n rho)` receives the drift "
        "`-i Tr(P_n[H,rho]) dt` and ceases to be a martingale. Therefore, the first-passage "
        "proof of the Born rule remains valid in the documented adiabatic/QND measurement "
        "sector, but cannot be transferred without modification to an apparatus whose direction "
        "varies rapidly.",
        "",
        "This test validates the reduced two-level dynamics. It does not yet fix "
        "`Delta` or `v` in physical units from the GDQ background.",
        "",
    ]
    report = "\n".join(lines)
    Path(__file__).with_name("output_nonadiabatic_sg.md").write_text(
        report, encoding="utf-8"
    )
    print(report)


if __name__ == "__main__":
    main()

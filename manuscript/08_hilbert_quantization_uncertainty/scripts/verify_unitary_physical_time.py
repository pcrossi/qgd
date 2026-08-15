#!/usr/bin/env python3
"""
Reduced verification of unitariety in physical time in Chapter 8.

Classification: algebraic/numerical consistency test.

The script does not prove the sectorial OS reconstruction of GDQ. It verifies,
in self-contained finite matrices, the relationships used in the text:

1. if H is Hermitian, U(t)=exp(-i t H / hbar) is unitary;
2. the Euclidean semigroup T(a)=exp(-a H / hbar) is contractive when H>=0;
3. a non-Hermitian effective Hamiltonian in a projected sector can decay;
4. the same physics can come from a total Hermitian evolution that preserves the
   norm, when the leakage channel is included.

This illustrates the GDQ distinction: Euclidean flow/contraction in tau is not
probability loss in physical time t.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def hermitian_exponential(H: np.ndarray, factor: complex) -> np.ndarray:
    """Calculates exp(factor*H) via Hermitian diagonalization."""
    evals, evecs = np.linalg.eigh(H)
    return (evecs * np.exp(factor * evals)) @ evecs.conj().T


def norm(v: np.ndarray) -> float:
    """Hermitian quadratic norm."""
    return float(np.vdot(v, v).real)


def main() -> None:
    hbar = 1.0
    t = 2.7
    a = 1.3

    # Positive Hamiltonian in a reconstructed physical sector of finite dimension.
    H = np.array(
        [
            [0.35, 0.12 - 0.03j, 0.0],
            [0.12 + 0.03j, 1.10, 0.20],
            [0.0, 0.20, 2.30],
        ],
        dtype=complex,
    )

    eig_H = np.linalg.eigvalsh(H)
    if np.min(eig_H) < -1e-12:
        raise RuntimeError("H should be positive for the Euclidean part.")

    U = hermitian_exponential(H, factor=-1j * t / hbar)
    T = hermitian_exponential(H, factor=-a / hbar)

    psi = np.array([1.0, 0.7 - 0.2j, -0.3j], dtype=complex)
    psi = psi / np.sqrt(norm(psi))

    unitarity_error = np.linalg.norm(U.conj().T @ U - np.eye(H.shape[0]))
    norm_before = norm(psi)
    norm_after_unitary = norm(U @ psi)

    # Since H>=0, the largest singular eigenvalue of T_E(a) is exp(-a E_min).
    contraction_norm = np.linalg.norm(T, ord=2)
    norm_after_euclidean = norm(T @ psi)

    # Projected effective sector with width Gamma: non-Hermitian.
    E0 = 0.8
    Gamma = 0.45
    H_eff = E0 - 0.5j * Gamma
    amp_projected = np.exp(-1j * H_eff * t / hbar)
    survival_projected = abs(amp_projected) ** 2
    expected_survival = np.exp(-Gamma * t / hbar)

    # Minimum unitary dilation: a Hermitian two-level system exchanges
    # probability between observed channel P and channel Q.
    g = 0.31
    H_total = np.array([[E0, g], [g, E0 + 0.05]], dtype=complex)
    U_total = hermitian_exponential(H_total, factor=-1j * t / hbar)
    state0 = np.array([1.0, 0.0], dtype=complex)
    state_t = U_total @ state0
    total_norm_error = abs(norm(state_t) - 1.0)
    projected_probability = abs(state_t[0]) ** 2
    leaked_probability = abs(state_t[1]) ** 2
    probability_balance_error = abs(projected_probability + leaked_probability - 1.0)

    lines = [
        "---",
        'title: "Output — verify unitariety in physical time"',
        "---",
        "",
        "# Output — verify unitariety in physical time",
        "",
        "Classification: algebraic/numerical consistency test.",
        "",
        "## Data",
        "",
        f"- dimension of the closed sector: {H.shape[0]}",
        f"- eigenvalues of $H$: {', '.join(f'{x:.12f}' for x in eig_H)}",
        f"- physical time used: $t={t}$",
        f"- Euclidean parameter used: $a={a}$",
        "",
        "## Results",
        "",
        "| Quantity | Value | Interpretation |",
        "|---|---:|---|",
        f"| error $\\|U^\\dagger U-I\\|$ | {unitarity_error:.3e} | must be close to zero |",
        f"| initial norm $\\|\\psi\\|^2$ | {norm_before:.12f} | normalized |",
        f"| norm after $U(t)$ | {norm_after_unitary:.12f} | preserved |",
        f"| spectral norm of $T_E(a)$ | {contraction_norm:.12f} | Euclidean contraction |",
        f"| norm after $T_E(a)$ | {norm_after_euclidean:.12f} | dampening in Euclidean parameter |",
        f"| projected non-Hermitian survival | {survival_projected:.12f} | decays in the partial sector |",
        f"| $\\exp(-\\Gamma t/\\hbar)$ | {expected_survival:.12f} | analytical reference |",
        f"| total norm error in the extended Hermitian model | {total_norm_error:.3e} | total closed preserves norm |",
        f"| probability in channel $P$ | {projected_probability:.12f} | observed channel |",
        f"| probability leaked to $Q$ | {leaked_probability:.12f} | unobserved channel |",
        f"| error of balance $P+Q=1$ | {probability_balance_error:.3e} | total conservation |",
        "",
        "## Physical Reading",
        "",
        "The test separates three facts. The group $U(t)$ preserves the norm when $H$ is",
        "Hermitian. The Euclidean semigroup $T_E(a)$ is contractive when $H\\ge0$.",
        "A projected sector can decay without the total closed dynamics ceasing to be",
        "unitary.",
        "",
    ]

    out = Path(__file__).with_name("output_verify_unitary_physical_time.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

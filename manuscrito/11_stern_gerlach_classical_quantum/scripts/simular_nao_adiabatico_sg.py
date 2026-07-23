#!/usr/bin/env python3
"""Capítulo 11 — varredura não adiabática e limite de validade da prova de Born.

Usamos hbar=1 e o Hamiltoniano canônico

    H(t) = 1/2 [v t sigma_z + Delta sigma_x].

Partindo do estado fundamental instantâneo em -T, a probabilidade de terminar
no estado excitado instantâneo em +T tende, para T grande, à fórmula de
Landau-Zener exp[-pi Delta^2/(2 v)].
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
    return vectors[:, which]  # 0: fundamental; 1: excitado


def propagate(velocity: float, gap: float = 1.0) -> tuple[float, float, float]:
    # vt/gap=20 nos extremos controla o erro de truncamento temporal.
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
    """Com H não comutante, p_z possui deriva Hamiltoniana não nula."""
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
        "# Regime não adiabático — Capítulo 11",
        "",
        "Hamiltoniano: `H(t)=(v t sigma_z + Delta sigma_x)/2`, com `Delta=1` e `hbar=1`.",
        "",
        "| v | P_exc numérica | Landau–Zener | erro absoluto |",
        "|---:|---:|---:|---:|",
    ]
    for velocity, numerical, exact, error in rows:
        lines.append(
            f"| {velocity:.3f} | {numerical:.9f} | {exact:.9f} | {error:.3e} |"
        )
    lines += [
        "",
        f"- maior erro numérico/assintótico: `{max_error:.3e}`;",
        f"- norma de `[H,P_z+]` no teste: `{commutator_norm:.9f}`;",
        f"- deriva instantânea `dp_z/dt` no estado de teste: `{drift:.9f}`.",
        "",
        "## Interpretação",
        "",
        "A probabilidade de troca de canal cresce com a velocidade da varredura. "
        "Logo, a identificação imediata dos canais com os projetores instantâneos "
        "exige a condição adiabática.",
        "",
        "Quando `[H,P_n] != 0`, `p_n=Tr(P_n rho)` recebe a deriva "
        "`-i Tr(P_n[H,rho]) dt` e deixa de ser martingal. Portanto, a prova de "
        "primeiro alcance da regra de Born continua válida no setor de medição "
        "adiabática/QND documentado, mas não pode ser transportada sem alteração "
        "para um aparelho cuja direção varia rapidamente.",
        "",
        "Este teste valida a dinâmica reduzida de dois níveis. Ele ainda não fixa "
        "`Delta` ou `v` em unidades físicas a partir do background GDQ.",
        "",
    ]
    report = "\n".join(lines)
    Path(__file__).with_name("saida_nonadiabatic_sg.md").write_text(
        report, encoding="utf-8"
    )
    print(report)


if __name__ == "__main__":
    main()

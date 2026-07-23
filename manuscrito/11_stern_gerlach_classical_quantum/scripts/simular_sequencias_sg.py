#!/usr/bin/env python3
"""Capítulo 11 — Sequências de medidas Stern–Gerlach compatíveis e incompatíveis."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from simular_feixe_sg_completo import sample_channels


AXES = {
    "x": np.array([1.0, 0.0, 0.0]),
    "y": np.array([0.0, 1.0, 0.0]),
    "z": np.array([0.0, 0.0, 1.0]),
}


def measure_stage(
    states: np.ndarray,
    axis: np.ndarray,
    *,
    gamma: float,
    epsilon: float,
    dt: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    probabilities = 0.5 * (1.0 + states @ axis)
    outcomes = np.zeros(states.shape[0], dtype=np.int8)

    # Há poucos valores distintos nas sequências cartesianas; simular cada
    # grupo preserva a SDE e evita uma rotina heterogênea desnecessária.
    rounded = np.round(probabilities, 12)
    for group_index, value in enumerate(np.unique(rounded)):
        idx = np.flatnonzero(rounded == value)
        sampled, _ = sample_channels(
            float(value),
            idx.size,
            gamma,
            epsilon,
            dt,
            10.0,
            seed + 10007 * group_index,
        )
        outcomes[idx] = sampled

    new_states = outcomes[:, None] * axis[None, :]
    return outcomes, new_states


def run_sequence(
    labels: list[str],
    n_particles: int,
    seed: int,
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    states = np.tile(AXES["z"], (n_particles, 1))
    outcomes_all: list[np.ndarray] = []
    states_all: list[np.ndarray] = []
    for stage, label in enumerate(labels):
        outcomes, states = measure_stage(
            states,
            AXES[label],
            gamma=1.0,
            epsilon=0.005,
            dt=0.0005,
            seed=seed + 7919 * stage,
        )
        outcomes_all.append(outcomes)
        states_all.append(states.copy())
    return outcomes_all, states_all


def fraction_plus(values: np.ndarray) -> float:
    return float(np.mean(values > 0))


def conditional_plus(
    later: np.ndarray, earlier: np.ndarray, earlier_value: int
) -> float:
    mask = earlier == earlier_value
    return float(np.mean(later[mask] > 0))


def main() -> None:
    n_particles = 40000
    compatible, _ = run_sequence(["z", "z"], n_particles, 43001)
    incompatible, _ = run_sequence(["z", "x", "z"], n_particles, 44001)

    z1, z2 = compatible
    iz1, x2, z3 = incompatible
    correlation_xz = float(np.mean(x2 * z3))

    lines = [
        "# Sequências Stern–Gerlach — Capítulo 11",
        "",
        f"- partículas por sequência: {n_particles}",
        "",
        "## Sequência compatível z -> z",
        "",
        f"- P(z1=+): {fraction_plus(z1):.8f}",
        f"- P(z2=+): {fraction_plus(z2):.8f}",
        f"- fidelidade z2=z1: {float(np.mean(z2 == z1)):.8f}",
        "",
        "## Sequência incompatível z -> x -> z",
        "",
        f"- P(z1=+): {fraction_plus(iz1):.8f}",
        f"- P(x2=+): {fraction_plus(x2):.8f}",
        f"- P(z3=+): {fraction_plus(z3):.8f}",
        f"- P(z3=+ | x2=+): {conditional_plus(z3, x2, 1):.8f}",
        f"- P(z3=+ | x2=-): {conditional_plus(z3, x2, -1):.8f}",
        f"- correlação <x2*z3>: {correlation_xz:.8f}",
        "",
        "## Alvos",
        "",
        "- z -> z preserva o resultado com probabilidade 1;",
        "- após a medida x, os dois resultados x têm probabilidade 1/2;",
        "- a medida z final volta a produzir 1/2 e 1/2;",
        "- a correlação entre x intermediário e z final é nula.",
        "",
    ]
    report = "\n".join(lines)
    output = Path(__file__).with_name("saida_sequences_sg.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()


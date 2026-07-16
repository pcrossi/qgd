#!/usr/bin/env python3
"""Q28 — seleção numérica do junction torsional elementar.

Este script testa o funcional horizontal reduzido derivado da conservação de
Noether. Ele não injeta N=3 nem ângulos de 120 graus. Para cada N, minimiza
várias condições iniciais aleatórias, calcula a Hessiana angular exata e
remove o modo de rotação global.

Classificação: teste numérico do teorema reduzido, não avaliação da Hessiana
multicítrica completa da ação GDQ.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


@dataclass
class Result:
    number: int
    energy: float
    closure: float
    eigenvalues: np.ndarray
    internal_zeros: int
    positive_gap: float
    angles: np.ndarray
    success_rate: float


def unit_vectors(angles: np.ndarray) -> np.ndarray:
    return np.column_stack((np.cos(angles), np.sin(angles)))


def closure_energy(free_angles: np.ndarray) -> float:
    """E=|sum T_a|²/2, fixando theta_0=0 para remover rotação."""
    angles = np.concatenate(([0.0], free_angles))
    resultant = np.sum(unit_vectors(angles), axis=0)
    return 0.5 * float(resultant @ resultant)


def closure_gradient(free_angles: np.ndarray) -> np.ndarray:
    angles = np.concatenate(([0.0], free_angles))
    vectors = unit_vectors(angles)
    resultant = np.sum(vectors, axis=0)
    rotated = np.column_stack((-np.sin(angles), np.cos(angles)))
    return rotated[1:] @ resultant


def angular_hessian(angles: np.ndarray) -> np.ndarray:
    """Hessiana exata no ponto de fechamento sum T_a=0."""
    vectors = unit_vectors(angles)
    return vectors @ vectors.T


def analyze_number(number: int, seeds: int = 64) -> Result:
    rng = np.random.default_rng(1729 + number)
    candidates = []
    successes = 0

    for _ in range(seeds):
        initial = rng.uniform(-np.pi, np.pi, size=number - 1)
        solution = minimize(
            closure_energy,
            initial,
            jac=closure_gradient,
            method="BFGS",
            options={"gtol": 1.0e-12, "maxiter": 3000},
        )
        energy = closure_energy(solution.x)
        if energy < 1.0e-16:
            successes += 1
        candidates.append((energy, solution.x))

    energy, free_angles = min(candidates, key=lambda item: item[0])
    angles = np.mod(np.concatenate(([0.0], free_angles)), 2.0 * np.pi)
    resultant = np.sum(unit_vectors(angles), axis=0)
    closure = float(np.linalg.norm(resultant))

    hessian = angular_hessian(angles)
    eigenvalues = np.linalg.eigvalsh(hessian)
    tolerance = 1.0e-8
    nullity = int(np.count_nonzero(np.abs(eigenvalues) < tolerance))
    internal_zeros = max(0, nullity - 1)  # quocienta rotação comum
    positive = eigenvalues[eigenvalues > tolerance]
    positive_gap = float(np.min(positive)) if positive.size else 0.0

    return Result(
        number=number,
        energy=energy,
        closure=closure,
        eigenvalues=eigenvalues,
        internal_zeros=internal_zeros,
        positive_gap=positive_gap,
        angles=np.sort(angles),
        success_rate=successes / seeds,
    )


def circular_separations(angles: np.ndarray) -> np.ndarray:
    ordered = np.sort(np.mod(angles, 2.0 * np.pi))
    return np.diff(np.concatenate((ordered, [ordered[0] + 2.0 * np.pi])))


def main() -> None:
    print("=" * 88)
    print("Q28 — SELEÇÃO NUMÉRICA DO JUNCTION TORSIONAL")
    print("=" * 88)
    print("Funcional: E_close = 1/2 |sum_a T_a|^2, |T_a|=1")
    print("Rotação global removida durante a minimização: theta_1=0")
    print()

    results = [analyze_number(number) for number in range(2, 9)]

    print("N | fechamento   | sucesso | zeros internos | gap positivo | autovalores")
    print("-" * 88)
    for result in results:
        eig_text = np.array2string(result.eigenvalues, precision=6, suppress_small=True)
        print(
            f"{result.number:1d} | {result.closure:11.3e} | "
            f"{result.success_rate:7.3f} | {result.internal_zeros:13d} | "
            f"{result.positive_gap:12.6f} | {eig_text}"
        )

    result3 = next(result for result in results if result.number == 3)
    separations3 = circular_separations(result3.angles)
    print("\n[N=3 emergente]")
    print("ângulos (graus):", np.degrees(result3.angles))
    print("separações (graus):", np.degrees(separations3))
    print("espectro:", result3.eigenvalues)

    # Resultado oficial já derivado para o modo homogêneo do raio.
    tau = 1.0
    radial_gap = 3.0 / (2.0 * tau)
    print("\n[Modo radial homogêneo da ação oficial]")
    print(f"tau={tau:.1f}, lambda_r0=3/(2 tau)={radial_gap:.6f}")

    noncollinear_isolated = [
        result.number
        for result in results
        if result.number >= 3
        and result.closure < 1.0e-8
        and result.internal_zeros == 0
    ]
    print("\n[Veredito reduzido]")
    print("junctions não colineares, fechados e isolados:", noncollinear_isolated)

    assert noncollinear_isolated == [3]
    assert np.allclose(separations3, 2.0 * np.pi / 3.0, atol=1.0e-7)
    assert np.allclose(result3.eigenvalues, [0.0, 1.5, 1.5], atol=1.0e-7)
    assert radial_gap > 0.0

    print("N=3 selecionado sem fixar previamente os ângulos.")
    print("Este teste cobre o bloco horizontal; a completação espectral está em")
    print("q28/espectro_completo_hessiana_tres_centros.py.")


if __name__ == "__main__":
    main()

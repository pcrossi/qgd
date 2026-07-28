#!/usr/bin/env python3
"""
Capítulo 9 — Verificação autocontida da calibração por imersão invariante.

Classificação:
  1. Riccati versus solução analítica: teste de consistência.
  2. Schur versus solução analítica: teste de convergência.
  3. Recuperação de lambda em dados sintéticos: calibração/engenharia
     controlada de fixture.
  4. Conjunto não usado na calibração: validação metodológica.

Este programa NÃO calcula um aparelho físico e NÃO contém uma previsão
experimental. Os parâmetros abaixo são números didáticos congelados.

Dependência externa: NumPy.
"""

from __future__ import annotations

import math
import numpy as np


def resposta_analitica(length: float, a: float, potential: float, r0: float) -> float:
    """DtN exato do canal -a u'' + V u = 0 com Robin R(0)=r0."""
    mass = math.sqrt(potential / a)
    scale = a * mass
    tanh = math.tanh(mass * length)
    return scale * (r0 + scale * tanh) / (scale + r0 * tanh)


def resposta_riccati_rk4(
    length: float,
    a: float,
    potential: float,
    r0: float,
    steps: int = 20_000,
) -> float:
    """Integra R' = V - R²/a pelo método clássico de Runge--Kutta."""
    h = length / steps
    response = r0

    def rhs(value: float) -> float:
        return potential - value * value / a

    for _ in range(steps):
        k1 = rhs(response)
        k2 = rhs(response + 0.5 * h * k1)
        k3 = rhs(response + 0.5 * h * k2)
        k4 = rhs(response + h * k3)
        response += h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    return response


def resposta_schur_fe(
    length: float,
    a: float,
    potential: float,
    r0: float,
    elements: int,
) -> float:
    """
    Discretiza o funcional quadrático com elementos lineares e elimina todos
    os nós internos. O escalar restante é o complemento de Schur no bordo.
    """
    h = length / elements
    size = elements + 1
    stiffness = np.zeros((size, size), dtype=float)

    gradient = (a / h) * np.array([[1.0, -1.0], [-1.0, 1.0]])
    mass = (potential * h / 6.0) * np.array([[2.0, 1.0], [1.0, 2.0]])
    local = gradient + mass

    for left in range(elements):
        nodes = np.array([left, left + 1])
        stiffness[np.ix_(nodes, nodes)] += local

    # Condição Robin no início do canal.
    stiffness[0, 0] += r0

    internal = np.arange(elements)
    boundary = elements
    k_ii = stiffness[np.ix_(internal, internal)]
    k_ib = stiffness[internal, boundary]
    k_bb = stiffness[boundary, boundary]
    return float(k_bb - k_ib @ np.linalg.solve(k_ii, k_ib))


def leitura_modelo(
    source: np.ndarray,
    length: float,
    object_response: float,
    a: float,
    potential: float,
    r0: float,
) -> np.ndarray:
    """Mapa linear de fonte clássica para leitura macroscópica do fixture."""
    apparatus_response = resposta_analitica(length, a, potential, r0)
    return source / (object_response + apparatus_response)


def calibrar_length(
    source: np.ndarray,
    observed: np.ndarray,
    sigma: np.ndarray,
    object_response: float,
    a: float,
    potential: float,
    r0: float,
    grid: np.ndarray,
) -> tuple[float, float]:
    """Minimiza chi² numa grade previamente especificada."""
    chi2 = []
    for length in grid:
        predicted = leitura_modelo(
            source, length, object_response, a, potential, r0
        )
        chi2.append(float(np.sum(((observed - predicted) / sigma) ** 2)))
    best = int(np.argmin(chi2))
    return float(grid[best]), float(chi2[best])


def main() -> None:
    # Fixture metodológico congelado.
    a = 1.7
    potential = 2.3
    r0 = 0.8
    length = 1.25
    object_response = 0.65

    exact = resposta_analitica(length, a, potential, r0)
    riccati = resposta_riccati_rk4(length, a, potential, r0)

    print("# Capítulo 9 — Saída da verificação")
    print()
    print("## 1. Consistência Riccati")
    print()
    print(f"- resposta analítica: `{exact:.12f}`")
    print(f"- resposta RK4: `{riccati:.12f}`")
    print(f"- erro absoluto: `{abs(riccati - exact):.3e}`")
    print()
    print("## 2. Convergência do complemento de Schur")
    print()
    print("| elementos | resposta Schur | erro absoluto |")
    print("|---:|---:|---:|")
    for elements in (20, 40, 80, 160, 320):
        schur = resposta_schur_fe(length, a, potential, r0, elements)
        print(f"| {elements} | {schur:.12f} | {abs(schur - exact):.3e} |")

    # Dados sintéticos determinísticos. Calibração e validação são separados.
    true_length = 0.93
    source_cal = np.array([0.4, 0.8, 1.3, 1.9])
    source_test = np.array([0.55, 1.05, 1.6, 2.2])
    # Ruídos fixos evitam qualquer dependência de gerador aleatório.
    noise_cal = np.array([1.0, -0.6, 0.4, -0.8]) * 2.0e-4
    noise_test = np.array([-0.7, 0.5, -0.3, 0.9]) * 2.0e-4
    sigma_cal = np.full(source_cal.shape, 2.0e-4)

    observed_cal = (
        leitura_modelo(
            source_cal, true_length, object_response, a, potential, r0
        )
        + noise_cal
    )
    observed_test = (
        leitura_modelo(
            source_test, true_length, object_response, a, potential, r0
        )
        + noise_test
    )

    grid = np.linspace(0.50, 1.40, 9001)
    estimated, chi2 = calibrar_length(
        source_cal,
        observed_cal,
        sigma_cal,
        object_response,
        a,
        potential,
        r0,
        grid,
    )
    predicted_test = leitura_modelo(
        source_test, estimated, object_response, a, potential, r0
    )
    rmse_test = float(np.sqrt(np.mean((predicted_test - observed_test) ** 2)))

    # Informação de Fisher local por diferença central.
    delta = 1.0e-5
    dy = (
        leitura_modelo(
            source_cal, estimated + delta, object_response, a, potential, r0
        )
        - leitura_modelo(
            source_cal, estimated - delta, object_response, a, potential, r0
        )
    ) / (2.0 * delta)
    fisher = float(np.sum((dy / sigma_cal) ** 2))

    print()
    print("## 3. Calibração sintética e validação separada")
    print()
    print(f"- lambda verdadeiro do fixture: `{true_length:.6f}`")
    print(f"- lambda calibrado: `{estimated:.6f}`")
    print(f"- erro de calibração: `{estimated - true_length:+.3e}`")
    print(f"- chi² de calibração: `{chi2:.6f}`")
    print(f"- informação de Fisher local: `{fisher:.6e}`")
    print(f"- RMSE no conjunto de teste congelado: `{rmse_test:.6e}`")
    print()
    print("## 4. Classificação")
    print()
    print(
        "Teste de consistência + convergência + calibração sintética. "
        "Não é previsão física nem comparação experimental."
    )


if __name__ == "__main__":
    main()

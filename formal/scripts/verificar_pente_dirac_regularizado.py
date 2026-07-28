#!/usr/bin/env python3
"""
Verificação numérica da forma regularizada do pente de Dirac.

Classificação:
    teste de consistência numérica de uma identidade analítica conhecida.

O programa compara as duas representações equivalentes, para epsilon > 0:

    sum_n exp(-epsilon*n^2) exp(i*n*theta)

e

    sqrt(pi/epsilon)
    sum_k exp(-(theta - 2*pi*k)^2/(4*epsilon)).

A primeira é a série de Fourier amortecida. A segunda é o trem periódico de
gaussianas obtido pela soma de Poisson. No limite epsilon -> 0, a igualdade
converge, no sentido de distribuições, ao pente de Dirac de período 2*pi.

O teste NÃO deriva a integralidade dos índices. Essa integralidade vem antes,
do fechamento global da fase U(1), formalizado em
GDQ/PhaseQuantization.lean.
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path


OUT = Path(__file__).with_name("saida_verificar_pente_dirac_regularizado.md")


def fourier_side(theta: float, epsilon: float, cutoff: int) -> complex:
    """Série de Fourier regularizada, truncada simetricamente."""
    return sum(
        math.exp(-epsilon * n * n) * cmath.exp(1j * n * theta)
        for n in range(-cutoff, cutoff + 1)
    )


def gaussian_side(theta: float, epsilon: float, cutoff: int) -> float:
    """Trem periódico de gaussianas, truncado simetricamente."""
    prefactor = math.sqrt(math.pi / epsilon)
    return prefactor * sum(
        math.exp(-((theta - 2.0 * math.pi * k) ** 2) / (4.0 * epsilon))
        for k in range(-cutoff, cutoff + 1)
    )


def main() -> None:
    thetas = [0.0, 0.2, 1.0, math.pi, 2.0 * math.pi - 0.2]
    epsilons = [0.5, 0.2, 0.08]

    # Os cortes são independentes porque as duas séries decaem em escalas
    # diferentes.
    n_cutoff = 120
    k_cutoff = 20

    rows: list[tuple[float, float, complex, float, float]] = []
    for epsilon in epsilons:
        for theta in thetas:
            lhs = fourier_side(theta, epsilon, n_cutoff)
            rhs = gaussian_side(theta, epsilon, k_cutoff)
            error = abs(lhs - rhs)
            rows.append((epsilon, theta, lhs, rhs, error))

    max_error = max(row[-1] for row in rows)

    lines = [
        "# Saída — pente de Dirac regularizado",
        "",
        "Classificação: teste de consistência numérica da soma de Poisson.",
        "",
        f"- corte de Fourier: $|n|\\le {n_cutoff}$;",
        f"- corte do trem gaussiano: $|k|\\le {k_cutoff}$;",
        f"- erro absoluto máximo: ${max_error:.3e}$.",
        "",
        "| $\\varepsilon$ | $\\theta$ | lado Fourier (real) | parte imaginária | lado gaussiano | erro |",
        "|---:|---:|---:|---:|---:|---:|",
    ]

    for epsilon, theta, lhs, rhs, error in rows:
        lines.append(
            f"| {epsilon:.3f} | {theta:.9f} | {lhs.real:.12e} | "
            f"{lhs.imag:.3e} | {rhs:.12e} | {error:.3e} |"
        )

    lines += [
        "",
        "A parte imaginária é nula a erro de arredondamento pela simetria",
        "$n\\leftrightarrow -n$. A concordância verifica a identidade",
        "regularizada; o limite em deltas continua sendo distribucional.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

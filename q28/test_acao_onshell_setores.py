#!/usr/bin/env python3
"""Compara a ação topológica mínima nos setores A múltiplos de seis."""

import math


def action(A: int, coefficient: float = 1.0, weight: float = 1.0) -> float:
    return 8.0 * math.pi**2 * coefficient * weight * abs(A)


def main() -> None:
    sectors = tuple(range(0, 31, 6))
    values = [(A, A // 6, action(A)) for A in sectors]

    print("# Q28 — ação on-shell homogênea")
    print()
    print("A  N_G  I_A/(8 pi^2 C w)")
    for A, generations, _ in values:
        print(f"{A:2d} {generations:4d} {A:18d}")

    absolute_minimum = min(values, key=lambda row: row[2])
    nonzero_minimum = min(values[1:], key=lambda row: row[2])

    print()
    print(f"mínimo absoluto: A={absolute_minimum[0]}")
    print(f"mínimo não trivial: A={nonzero_minimum[0]}")
    print("A=18 não é selecionado pela forma quadrática homogênea.")

    assert absolute_minimum[0] == 0
    assert nonzero_minimum[0] == 6
    assert action(18) == 3 * action(6)


if __name__ == "__main__":
    main()

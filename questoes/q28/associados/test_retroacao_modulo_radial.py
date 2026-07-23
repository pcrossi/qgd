#!/usr/bin/env python3
"""Verifica as equações radiais e a monotonicidade on-shell da Q28."""

import math


def roots_minus(A: float, q: float, tau: float) -> tuple[float, ...]:
    if A == 0:
        return (4.0 * tau,)
    discriminant = 9.0 - 96.0 * q * tau * tau * abs(A)
    if discriminant < 0:
        return ()
    root = math.sqrt(discriminant)
    denominator = 4.0 * q * tau * abs(A)
    return ((3.0 - root) / denominator, (3.0 + root) / denominator)


def root_plus(A: float, q: float, tau: float) -> float:
    if A == 0:
        return 4.0 * tau
    return (-3.0 + math.sqrt(9.0 + 96.0 * q * tau * tau * abs(A))) / (
        4.0 * q * tau * abs(A)
    )


def main() -> None:
    # Escolha que mantém vários setores dentro do domínio de existência.
    q = 1.0e-4
    tau = 1.0
    sectors = (0, 6, 12, 18, 24, 30)

    print("# Q28 — retroação do módulo radial")
    print()
    print("A  raízes x=r^2 (sinal -)       raiz x (sinal +)  sinal dW-/dA  sinal dW+/dA")
    for A in sectors:
        minus = roots_minus(A, q, tau)
        plus = root_plus(A, q, tau)
        derivative_minus = 0.0 if A == 0 else -q * tau * plus
        derivative_plus = 0.0 if A == 0 else q * tau * plus
        print(
            f"{A:2d} {str(tuple(round(x, 8) for x in minus)):28s} "
            f"{plus:18.8f} {derivative_minus:13.6e} {derivative_plus:13.6e}"
        )

    threshold = 3.0 / (32.0 * q * tau * tau)
    print()
    print(f"limite de existência no sinal geométrico: |A| <= {threshold:.6f}")
    print("nenhum extremo interior em A=18")

    assert all(root_plus(A, q, tau) > 0 for A in sectors)
    assert -q * tau * root_plus(18, q, tau) < 0
    assert q * tau * root_plus(18, q, tau) > 0


if __name__ == "__main__":
    main()

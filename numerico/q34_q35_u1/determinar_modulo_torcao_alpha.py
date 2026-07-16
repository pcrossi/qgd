#!/usr/bin/env python3
"""Determinação condicional do módulo torsional a partir de Re_Q = alpha."""

from math import pi, sqrt


def solve(alpha: float = 1.0 / 137.0, n_b: int = 1) -> dict[str, float]:
    if alpha <= 0.0 or alpha >= 1.0 / 3.0:
        raise ValueError("A solução física exige 0 < alpha < 1/3.")
    if n_b == 0:
        raise ValueError("O setor torsional exige n_B diferente de zero.")

    r4 = n_b**2 / (12.0 * pi**2 * alpha)
    radius = r4**0.25

    # V(R,b)=-12 pi^2/R^5+(pi^2/6)b^2/R^9 e V'(R)=0.
    b2 = 40.0 * r4
    b_abs = sqrt(b2)

    x = radius**2
    tau = x**3 / (4.0 * x**2 - n_b**2 / pi**2)
    lambda_hat = tau**-0.5
    collar_ratio = pi * sqrt(tau)

    # Convenção do relatório: kappa=3/4 em unidades hbar=1.
    spin_condensate_abs = b_abs / (3.0 / 4.0)

    return {
        "R4": r4,
        "R": radius,
        "b2": b2,
        "abs_b": b_abs,
        "abs_S_hbar_1": spin_condensate_abs,
        "tau_em_dimless": tau,
        "lambda_em_hat": lambda_hat,
        "L_over_ell_C": collar_ratio,
    }


if __name__ == "__main__":
    for key, value in solve().items():
        print(f"{key}={value:.15g}")

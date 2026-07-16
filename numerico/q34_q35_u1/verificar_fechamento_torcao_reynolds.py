#!/usr/bin/env python3
"""Verifica as identidades do fechamento torsão--Reynolds da Q35."""

import math


def solve(alpha: float, n_b: int = 1) -> dict[str, float]:
    if not (0.0 < alpha < 1.0 / 3.0):
        raise ValueError("a solução positiva exige 0<alpha<1/3")
    x = abs(n_b) / (math.sqrt(12.0) * math.pi * math.sqrt(alpha))
    radius = math.sqrt(x)
    tau = x**3 / (4.0 * x**2 - n_b**2 / math.pi**2)
    reynolds = n_b**2 / (12.0 * math.pi**2 * radius**4)
    stationary = x**3 - 4.0 * tau * x**2 + tau * n_b**2 / math.pi**2
    return {
        "alpha": alpha,
        "radius": radius,
        "tau": tau,
        "lambda_hat": 1.0 / math.sqrt(tau),
        "length_hat": math.pi * math.sqrt(tau),
        "reynolds": reynolds,
        "stationary_residual": stationary,
    }


def main() -> int:
    scenarios = [
        ("baixa energia — aproximação 1/137", 1.0 / 137.0),
        (
            "fórmula cosmológica histórica",
            (9.0 / (8.0 * math.pi**4)) * ((math.pi**5 / 1920.0) ** 0.25),
        ),
        ("referência metrológica externa", 1.0 / 137.035999084),
        ("benchmark efetivo de alta energia — LHC", 1.0 / 128.0),
    ]
    for name, alpha in scenarios:
        row = solve(alpha)
        assert abs(row["reynolds"] - alpha) < 1e-14
        assert abs(row["stationary_residual"]) < 1e-14
        print(name)
        print(f"  alpha={alpha:.15e}")
        print(f"  R={row['radius']:.12f}")
        print(f"  tau_EM={row['tau']:.12f}")
        print(f"  Lambda_hat={row['lambda_hat']:.12f}")
        print(f"  L_hat={row['length_hat']:.12f}")
        print(f"  resíduo={row['stationary_residual']:.3e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

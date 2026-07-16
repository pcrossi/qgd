#!/usr/bin/env python3
"""Verifica os coeficientes locais da polarização U(1) da Q34."""

from __future__ import annotations

import math
from pathlib import Path

from solve_polarizacao_u1 import Config, pi_scalar


def coefficients(alpha: float, eta: float) -> tuple[float, float, float]:
    common = alpha * math.exp(-eta) / math.pi
    a1 = common / 15.0
    a2 = -common * (1.0 + eta) / 140.0
    a3 = common * (2.0 + 2.0 * eta + eta**2) / 1890.0
    return a1, a2, a3


def series(r: float, abc: tuple[float, float, float]) -> float:
    a1, a2, a3 = abc
    return a1 * r + a2 * r**2 + a3 * r**3


def main() -> int:
    alpha = 1.0 / 137.0
    eta = 0.2749005225136263
    cfg = Config(alpha0=alpha, eta=eta, n_gauss=512)
    abc = coefficients(alpha, eta)
    rs = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]
    rows = []
    for r in rs:
        exact = pi_scalar(r, cfg)
        local = series(r, abc)
        error = abs(local - exact)
        relative = error / abs(exact)
        rows.append((r, exact, local, error, relative))

    # Uma série truncada após r^3 deve apresentar erro absoluto O(r^4).
    orders = []
    for first, second in zip(rows[:-1], rows[1:]):
        p = math.log(first[3] / second[3]) / math.log(first[0] / second[0])
        orders.append(p)

    assert rows[-1][4] < 1e-9
    assert min(orders[-2:]) > 3.8

    output = Path(__file__).with_name("saida_coeficientes_locais_u1.md")
    lines = [
        "# Verificação dos coeficientes locais $U(1)$ — Q34",
        "",
        "## Classificação",
        "",
        "**Avaliação direta e teste de consistência** da expansão local da",
        "polarização já derivada.",
        "",
        "$$",
        f"\\alpha_0=1/137,\\qquad\\eta={eta:.12f}.",
        "$$",
        "",
        "$$",
        f"A_1={abc[0]:.14e},\\quad A_2={abc[1]:.14e},"
        f"\\quad A_3={abc[2]:.14e}.",
        "$$",
        "",
        "| $r$ | integral exata | série até $r^3$ | erro absoluto | erro relativo |",
        "|---:|---:|---:|---:|---:|",
    ]
    for r, exact, local, error, relative in rows:
        lines.append(
            f"| {r:.1e} | {exact:.14e} | {local:.14e} | "
            f"{error:.3e} | {relative:.3e} |"
        )
    lines += [
        "",
        "Ordens efetivas do erro entre refinamentos:",
        "",
        ", ".join(f"{p:.5f}" for p in orders) + ".",
        "",
        "A aproximação converge com erro $O(r^4)$, como exigido pela truncagem.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"A1={abc[0]:.14e}")
    print(f"A2={abc[1]:.14e}")
    print(f"A3={abc[2]:.14e}")
    print(f"menor erro relativo={rows[-1][4]:.3e}")
    print(f"ordens finais={orders[-2:]}")
    print(f"Relatório: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

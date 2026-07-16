#!/usr/bin/env python3
"""Teste diagnóstico do problema variacional de I_H no operador axial da Q42.

Resolve, em forma fraca,

    K u = c,
    K = -(1/w) d/dx (w du/dx) + 2,
    w = exp(-x^2/4),

com Robin em x=0 e Dirichlet no corte x=L. Calcula

    I_H/C_(1/2) = I[u] / C[u].

Os kernels usados são diagnósticos e não representam ainda a colagem física.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


@dataclass(frozen=True)
class Result:
    n: int
    robin: float
    case: str
    ratio: float
    susceptibility: float
    energy_for_unit_circulation: float
    residual: float


def normalized_kernel(x: np.ndarray, quad: np.ndarray, sigma: float | None) -> np.ndarray:
    if sigma is None:
        raw = np.ones_like(x)
    else:
        raw = np.exp(-0.5 * (x / sigma) ** 2)
    return raw / float(np.sum(quad * raw))


def assemble(n: int, length: float, robin: float):
    x = np.linspace(0.0, length, n)
    h = x[1] - x[0]
    w = np.exp(-x**2 / 4.0)
    n_unknown = n - 1  # u(L)=0

    quad = np.full(n_unknown, h)
    quad[0] = 0.5 * h
    weighted_quad = quad * w[:n_unknown]

    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []

    def add(i: int, j: int, value: float) -> None:
        rows.append(i)
        cols.append(j)
        data.append(value)

    # Stiffness integral int w u' v'. Includes the final edge to u(L)=0.
    for edge in range(n - 1):
        w_mid = np.exp(-((x[edge] + x[edge + 1]) * 0.5) ** 2 / 4.0)
        coeff = w_mid / h
        left = edge
        right = edge + 1
        if left < n_unknown:
            add(left, left, coeff)
        if right < n_unknown:
            add(right, right, coeff)
            add(left, right, -coeff)
            add(right, left, -coeff)

    # Potential 2 * int w u v, mass-lumped.
    for i in range(n_unknown):
        add(i, i, 2.0 * weighted_quad[i])

    # Robin contribution w(0) R u(0) v(0).
    add(0, 0, robin * w[0])

    matrix = coo_matrix((data, (rows, cols)), shape=(n_unknown, n_unknown)).tocsr()
    return x[:n_unknown], weighted_quad, matrix


def solve_case(
    n: int,
    robin: float,
    case: str,
    sigma_c: float,
    sigma_i: float | None,
    length: float = 8.0,
) -> Result:
    x, weighted_quad, matrix = assemble(n, length, robin)
    c = normalized_kernel(x, weighted_quad, sigma_c)
    i_kernel = normalized_kernel(x, weighted_quad, sigma_i)
    load = weighted_quad * c
    u = spsolve(matrix, load)

    susceptibility = float(np.sum(weighted_quad * c * u))
    i_response = float(np.sum(weighted_quad * i_kernel * u))
    ratio = i_response / susceptibility
    energy = 0.5 / susceptibility
    residual = float(np.linalg.norm(matrix @ u - load) / np.linalg.norm(load))
    return Result(n, robin, case, ratio, susceptibility, energy, residual)


def main() -> None:
    cases = (
        ("i=c (sigma 0.4)", 0.4, 0.4),
        ("i mais largo (1.0)", 0.4, 1.0),
        ("i uniforme", 0.4, None),
    )
    grids = (400, 800, 1600, 3200)
    robins = (0.0, 1.0, 5.0)

    results: list[Result] = []
    for robin in robins:
        for case, sigma_c, sigma_i in cases:
            for n in grids:
                results.append(solve_case(n, robin, case, sigma_c, sigma_i))

    print("=" * 104)
    print("GDQ — TESTE VARIACIONAL DO PERFIL TORSIONAL I_H")
    print("=" * 104)
    print("Kernels diagnósticos; C_(1/2)=1 por normalização.\n")
    print("Robin  caso                    N      I_H/C      susceptibilidade  E_min       resíduo")
    print("-" * 104)
    for result in results:
        print(
            f"{result.robin:<6.1f} "
            f"{result.case:<23} "
            f"{result.n:<6d} "
            f"{result.ratio:<10.7f} "
            f"{result.susceptibility:<16.9f} "
            f"{result.energy_for_unit_circulation:<11.7f} "
            f"{result.residual:.3e}"
        )

    print("\n[Convergência N=1600 -> 3200]")
    for robin in robins:
        for case, _, _ in cases:
            r1600 = next(r for r in results if r.robin == robin and r.case == case and r.n == 1600)
            r3200 = next(r for r in results if r.robin == robin and r.case == case and r.n == 3200)
            print(
                f"R={robin:<3.0f} {case:<23} "
                f"|delta ratio|={abs(r3200.ratio-r1600.ratio):.3e}  "
                f"|delta chi|={abs(r3200.susceptibility-r1600.susceptibility):.3e}"
            )

    same_kernel_error = max(
        abs(r.ratio - 1.0) for r in results if r.case.startswith("i=c")
    )
    print("\n[Verificações]")
    print(f"erro máximo no caso identidade i=c : {same_kernel_error:.3e}")
    print("todas as susceptibilidades positivas:", all(r.susceptibility > 0 for r in results))
    print("todas as energias positivas         :", all(r.energy_for_unit_circulation > 0 for r in results))
    print("\nStatus: diagnóstico de sensibilidade; c_H e i_H físicos ainda não derivados.")


if __name__ == "__main__":
    main()

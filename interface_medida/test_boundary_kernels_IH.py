#!/usr/bin/env python3
"""Resposta de L_H a circulação localizada no bordo do estômato."""

from __future__ import annotations

import numpy as np
from scipy.sparse.linalg import spsolve

from test_variacional_IH import assemble, normalized_kernel


def solve(n: int, robin: float, length: float = 8.0) -> dict[str, float]:
    x, weighted_quad, matrix = assemble(n, length, robin)

    # Unit boundary source in the weak equation. Its circulation functional is
    # the trace C[u] = u(0).
    load = np.zeros_like(x)
    load[0] = 1.0
    u = spsolve(matrix, load)

    c_response = float(u[0])
    i_uniform = normalized_kernel(x, weighted_quad, None)
    i_local = normalized_kernel(x, weighted_quad, 0.4)

    response_uniform = float(np.sum(weighted_quad * i_uniform * u))
    response_local = float(np.sum(weighted_quad * i_local * u))

    residual = float(np.linalg.norm(matrix @ u - load) / np.linalg.norm(load))
    return {
        "n": float(n),
        "robin": robin,
        "trace": c_response,
        "z_uniform": response_uniform / c_response,
        "z_local": response_local / c_response,
        "energy": 0.5 / c_response,
        "residual": residual,
    }


def main() -> None:
    grids = (400, 800, 1600, 3200, 6400)
    robins = (0.0, 1.0, 5.0)
    results = [solve(n, robin) for robin in robins for n in grids]

    print("=" * 96)
    print("GDQ — TESTE DOS KERNELS DE BORDO E VOLUME PARA I_H")
    print("=" * 96)
    print("lambda_T A_D = 1; kernels magnéticos normalizados.\n")
    print("Robin N      C_response   Z_uniforme   Z_local(0.4)  E_min      resíduo")
    print("-" * 96)
    for r in results:
        print(
            f"{r['robin']:<5.1f} "
            f"{int(r['n']):<6d} "
            f"{r['trace']:<12.8f} "
            f"{r['z_uniform']:<12.8f} "
            f"{r['z_local']:<13.8f} "
            f"{r['energy']:<10.7f} "
            f"{r['residual']:.3e}"
        )

    print("\n[Convergência N=3200 -> 6400]")
    for robin in robins:
        a = next(r for r in results if r["robin"] == robin and int(r["n"]) == 3200)
        b = next(r for r in results if r["robin"] == robin and int(r["n"]) == 6400)
        print(
            f"R={robin:<3.0f} "
            f"delta C={abs(b['trace']-a['trace']):.3e}  "
            f"delta Z_unif={abs(b['z_uniform']-a['z_uniform']):.3e}  "
            f"delta Z_loc={abs(b['z_local']-a['z_local']):.3e}"
        )

    print("\nStatus: diagnóstico; lambda_T, A_D e o kernel magnético físico continuam abertos.")


if __name__ == "__main__":
    main()

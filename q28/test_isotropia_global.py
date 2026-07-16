#!/usr/bin/env python3
"""Teste exato do subespaço invariante de H^4(T^5) sob isotropia orientada."""

import sympy as sp


def main() -> None:
    # Pela dualidade de Poincaré, H^4(T^5;Z) transforma como R em H^1
    # para R orientada. As inversões duplas já bastam para testar invariância.
    generators = []
    for j in range(1, 5):
        diagonal = [1] * 5
        diagonal[0] = -1
        diagonal[j] = -1
        generators.append(sp.diag(*diagonal))

    constraints = sp.Matrix.vstack(*(R - sp.eye(5) for R in generators))
    kernel = constraints.nullspace()

    print("posto das restrições =", constraints.rank())
    print("dimensão do setor invariante =", len(kernel))
    print("base do setor invariante =", kernel)
    assert constraints.rank() == 5
    assert kernel == []
    print("A = 0 sob isotropia global orientada.")

    # No background térmico, e5 é preservado e apenas T4 é isotropizado.
    thermal_generators = []
    for j in range(1, 4):
        diagonal = [1] * 5
        diagonal[0] = -1
        diagonal[j] = -1
        thermal_generators.append(sp.diag(*diagonal))
    thermal_constraints = sp.Matrix.vstack(
        *(R - sp.eye(5) for R in thermal_generators)
    )
    thermal_kernel = thermal_constraints.nullspace()
    print("dimensão do setor térmico invariante =", len(thermal_kernel))
    print("base do setor térmico invariante =", thermal_kernel)
    assert thermal_kernel == [sp.Matrix([0, 0, 0, 0, 1])]
    print("Background térmico: a4 = A PD(e5), com A inteiro não fixado.")


if __name__ == "__main__":
    main()

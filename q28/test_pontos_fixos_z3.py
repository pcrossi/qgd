#!/usr/bin/env python3
"""Contagem exata dos fixos da rotação Z3 em toros de Eisenstein."""

import sympy as sp


def main() -> None:
    # Multiplicação por omega na base integral (1, omega), omega^2+omega+1=0.
    matrix = sp.Matrix([[0, -1], [1, -1]])
    one_plane = abs(int((sp.eye(2) - matrix).det()))
    print("fixos em dimensão complexa 1 =", one_plane)
    assert one_plane == 3

    for complex_dimension in range(1, 5):
        fixed_points = one_plane**complex_dimension
        print(
            f"ação diagonal em dimensão complexa {complex_dimension}: "
            f"{fixed_points} fixos"
        )
        assert fixed_points == 3**complex_dimension

    print("A ordem três do grupo não fixa universalmente três pontos.")


if __name__ == "__main__":
    main()


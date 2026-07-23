#!/usr/bin/env python3
"""Teste exato da seleção A=6k e do índice global da Q28."""


def index(A: int, winding: int = 1) -> int:
    numerator = A * winding
    if numerator % 6:
        raise ValueError("a classe não define índice integral")
    return numerator // 6


def main() -> None:
    admissible = [(A, index(A)) for A in range(-24, 25) if A % 6 == 0]
    print("setores admissíveis (A, índice):", admissible)
    assert index(6) == 1
    assert index(18) == 3
    assert min(A for A, _ in admissible if A > 0) == 6
    try:
        index(1)
    except ValueError:
        pass
    else:
        raise AssertionError("A=1 não pode produzir índice integral")
    print("Setor positivo primitivo: A=6, índice=1.")
    print("A=18 exige multiplicidade global independente k=3.")


if __name__ == "__main__":
    main()


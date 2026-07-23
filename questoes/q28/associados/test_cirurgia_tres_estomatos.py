#!/usr/bin/env python3
"""Testes da aditividade assinada na cirurgia de três estômatos."""


def total_index(orientations: tuple[int, ...], complement: int = 0, glue: int = 0) -> int:
    if any(sign not in (-1, 1) for sign in orientations):
        raise ValueError("cada orientação deve ser +1 ou -1")
    return complement + sum(orientations) + glue


def main() -> None:
    assert total_index((1, 1, 1)) == 3
    assert total_index((1, 1, -1)) == 1
    assert total_index((1, -1, -1)) == -1
    assert total_index((-1, -1, -1)) == -3

    index = total_index((1, 1, 1))
    global_charge = 6 * index
    print("índice coorientado =", index)
    print("carga global A =", global_charge)
    assert global_charge == 18
    print("A=18 é condicional a três componentes primitivas coorientadas.")


if __name__ == "__main__":
    main()


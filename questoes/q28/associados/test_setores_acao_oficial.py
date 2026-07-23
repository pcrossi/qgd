#!/usr/bin/env python3
"""Teste estrutural da seleção de setores da conexão métrica da Q28."""


def generation_index(A: int, winding: int = 1) -> float:
    return A * winding / 6


def main() -> None:
    sectors = tuple(range(-30, 31, 6))
    table = [(A, generation_index(A)) for A in sectors]

    print("# Q28 — setores topológicos da ação oficial")
    print()
    print("A  N_G=A/6")
    for A, index in table:
        print(f"{A:3d} {index:6.1f}")

    selected = [A for A, index in table if index == 3]
    print()
    print(f"setor que produz N_G=3: {selected}")
    print("A equação local admite setores; a seleção exige ação on-shell e bordas.")

    assert selected == [18]


if __name__ == "__main__":
    main()

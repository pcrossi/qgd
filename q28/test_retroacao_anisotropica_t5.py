#!/usr/bin/env python3
"""Verifica a minimização exata da anisotropia toroidal da Q28."""

import math


def energy(x: float, n12: int, n34: int, coefficient: float = 1.0) -> float:
    return coefficient * (n12 * n12 * x + n34 * n34 / x)


def main() -> None:
    pairs = ((1, 1), (1, 3), (2, 3), (3, 6), (6, 3))

    print("# Q28 — retroação anisotrópica de T5")
    print()
    print("n12 n34 x_* E(x_*) 2|n12 n34| Hessiana")
    for n12, n34 in pairs:
        x_star = abs(n34 / n12)
        on_shell = energy(x_star, n12, n34)
        bound = 2 * abs(n12 * n34)
        hessian = 2 * n34 * n34 / x_star**3
        print(
            f"{n12:3d} {n34:3d} {x_star:6.3f} {on_shell:8.3f} "
            f"{bound:14.3f} {hessian:9.3f}"
        )
        assert math.isclose(on_shell, bound, rel_tol=1e-12)
        assert hessian > 0

    print()
    print("A forma é estabilizada; a ação on-shell permanece linear em |A|.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Checagens topológicas elementares das rotas de localização da Q28."""

from math import comb


def main() -> None:
    betti_t5 = [comb(5, k) for k in range(6)]
    betti_s3 = [1, 0, 0, 1]
    betti_product = [0] * 9
    for i, bi in enumerate(betti_t5):
        for j, bj in enumerate(betti_s3):
            betti_product[i + j] += bi * bj

    euler = sum((-1) ** k * b for k, b in enumerate(betti_product))
    print("Betti(T5xS3) =", betti_product)
    print("Euler(T5xS3) =", euler)
    assert betti_product == [1, 5, 10, 11, 10, 11, 10, 5, 1]
    assert euler == 0

    # Em uma família suave, k é constante; somente cruzamentos/cirurgias
    # contribuem ao fluxo espectral relativo.
    crossings = []
    spectral_flow = sum(sign * multiplicity for sign, multiplicity in crossings)
    assert spectral_flow == 0
    print("Background fechado/suave: localização líquida = 0.")
    print("k=3 requer fluxo espectral relativo calculado igual a 3.")


if __name__ == "__main__":
    main()


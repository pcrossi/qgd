#!/usr/bin/env python3
"""Verifica pesos universais do bloco vetor--jacobiano em a4 e a6."""

from fractions import Fraction

import numpy as np


def main() -> int:
    # a4: traços relativos ao invariante F^delta F^gamma K_delta_gamma.
    tr_e2_vec = Fraction(4)
    tr_o2_vec = Fraction(-4)
    tr_o2_ghost = Fraction(-1)

    a4_vec = (180 * tr_e2_vec + 30 * tr_o2_vec) / 360
    a4_ghost = 30 * tr_o2_ghost / 360
    a4_total = a4_vec - 2 * a4_ghost

    assert a4_vec == Fraction(5, 3)
    assert a4_ghost == Fraction(-1, 12)
    assert a4_total == Fraction(11, 6)
    # (4*pi)^-2 * 11/6 = 11/(96*pi^2).

    # a6 integrado: pesos puros de Omega antes do fator 1/360.
    omega_multiplicity = 4 - 2
    weights = {
        "DkFij_DkFij": -4 * omega_multiplicity,
        "DjFij_DkFik": 2 * omega_multiplicity,
        "Fij_Fjk_Fki": -12 * omega_multiplicity,
        "DiE_DiE": -30,
        "E3": 60,
        "E_Omega2": 30,
    }
    assert weights == {
        "DkFij_DkFij": -8,
        "DjFij_DkFik": 4,
        "Fij_Fjk_Fki": -24,
        "DiE_DiE": -30,
        "E3": 60,
        "E_Omega2": 30,
    }

    # Contrações vetoriais com matrizes não comutativas aleatórias.
    rng = np.random.default_rng(34)
    dimension = 4
    rank = 3
    field = np.zeros((dimension, dimension, rank, rank))
    derivative = np.zeros((dimension, dimension, dimension, rank, rank))
    for mu in range(dimension):
        for nu in range(mu + 1, dimension):
            value = rng.normal(size=(rank, rank))
            field[mu, nu] = value
            field[nu, mu] = -value
            for rho in range(dimension):
                dvalue = rng.normal(size=(rank, rank))
                derivative[rho, mu, nu] = dvalue
                derivative[rho, nu, mu] = -dvalue

    e_matrix = np.block(
        [[2.0 * field[rho, nu] for nu in range(dimension)]
         for rho in range(dimension)]
    )
    tr_e3 = np.trace(e_matrix @ e_matrix @ e_matrix)
    cubic = sum(
        np.trace(field[mu, nu] @ field[nu, rho] @ field[rho, mu])
        for mu in range(dimension)
        for nu in range(dimension)
        for rho in range(dimension)
    )
    assert abs(tr_e3 - 8.0 * cubic) < 1e-10

    de_square = 0.0
    df_square = 0.0
    for k in range(dimension):
        de = np.block(
            [[2.0 * derivative[k, rho, nu] for nu in range(dimension)]
             for rho in range(dimension)]
        )
        de_square += np.trace(de @ de)
        df_square += sum(
            np.trace(derivative[k, mu, nu] @ derivative[k, mu, nu])
            for mu in range(dimension)
            for nu in range(dimension)
        )
    assert abs(de_square + 4.0 * df_square) < 1e-10

    e_omega2 = 0.0
    for mu in range(dimension):
        for nu in range(dimension):
            omega = np.kron(np.eye(dimension), field[mu, nu])
            e_omega2 += np.trace(e_matrix @ omega @ omega)
    assert abs(e_omega2) < 1e-10

    # Redução racional após Bianchi: A=2B-4C.
    coeff_a = Fraction(112)
    coeff_b = Fraction(4)
    coeff_c = Fraction(456)
    reduced_b = 2 * coeff_a + coeff_b
    reduced_c = -4 * coeff_a + coeff_c
    assert reduced_b == 228
    assert reduced_c == 8
    assert reduced_b / 360 == Fraction(19, 30)
    assert reduced_c / 360 == Fraction(1, 45)

    print(f"a4 vetor: {a4_vec}")
    print(f"a4 jacobiano escalar: {a4_ghost}")
    print(f"a4 vetor - 2 jacobianos: {a4_total}")
    print("pesos brutos integrados de a6:")
    for name, value in weights.items():
        print(f"  {name}: {value}/360")
    print("contrações: tr(DE)^2=-4 tr(DF)^2, tr(E^3)=8 tr(F^3), tr(E Omega^2)=0")
    print("redução final: (19/30) B + (1/45) C")
    print("Todos os testes racionais passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

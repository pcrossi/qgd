#!/usr/bin/env python3
"""Q57 — avaliação direta das escalas de aceleração cosmológica.

Classificação numérica:
- avaliação direta de fórmulas reduzidas já declaradas;
- teste de consistência dimensional;
- comparação fenomenológica com a escala MOND/RAR.

Nenhum parâmetro é ajustado ao valor empírico de MOND.
"""

from math import pi, sqrt


def main() -> None:
    c = 299_792_458.0
    mpc = 3.0856775814913673e22

    # Mesmo contorno cosmológico usado na Q56.
    H0_planck = 67.4 * 1000.0 / mpc
    H0_local = 73.0 * 1000.0 / mpc
    omega_lambda = 0.6847

    # Escalas candidatas distintas. A inconsistência legada vinha de misturá-las.
    a_H_planck = c * H0_planck
    a_H_local = c * H0_local
    a_Lambda_planck = a_H_planck * sqrt(omega_lambda)

    a0_H_planck = a_H_planck / (2.0 * pi)
    a0_H_local = a_H_local / (2.0 * pi)
    a0_Lambda_planck = a_Lambda_planck / (2.0 * pi)

    # Valor fenomenológico típico usado em MOND/RAR.
    a0_mond = 1.20e-10

    rows = [
        ("c H0 Planck", a_H_planck, None),
        ("c H0 Planck / 2pi", a0_H_planck, a0_mond),
        ("c H0 local / 2pi", a0_H_local, a0_mond),
        ("c H0 sqrt(Omega_Lambda)", a_Lambda_planck, None),
        ("c H0 sqrt(Omega_Lambda) / 2pi", a0_Lambda_planck, a0_mond),
    ]

    print("# Saída — Q57: escalas de aceleração")
    print()
    print("| Quantidade | Valor [m/s²] | Erro relativo vs 1.20e-10 |")
    print("| --- | ---: | ---: |")
    for name, value, target in rows:
        if target is None:
            err = "—"
        else:
            err = f"{(value / target - 1.0):+.6%}"
        print(f"| {name} | {value:.12e} | {err} |")

    print()
    print("Correção aritmética explícita:")
    print(f"(c H0 sqrt(Omega_Lambda))/(2pi) = {a0_Lambda_planck:.12e} m/s²")
    print("Portanto, se o numerador for 5.46e-10, a divisão por 2pi dá ~8.69e-11,")
    print("não 1.21e-10.")

    print()
    print("Rota GDQ adotada para Q57:")
    print("a0_GDQ = c^2/(2pi R_H) = c H0/(2pi), usando o mesmo horizonte R_H da Q56.")
    print(f"Com H0=67.4 km/s/Mpc: a0_GDQ = {a0_H_planck:.12e} m/s².")


if __name__ == "__main__":
    main()

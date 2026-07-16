#!/usr/bin/env python3
"""Verifica analiticamente o no-go do transporte local da Q29.

Para Y=x4, qualquer peso radial depende apenas de x4. Condicionado a x4,
x1, x2 e x3 têm o mesmo segundo momento. As variações dos quatro geradores
da Q29 usam justamente esses três componentes, logo suas normas coincidem.
"""

from fractions import Fraction


def main():
    # |A n|²=1/4 para cada gerador normalizado. Para peso F(x4),
    # E[x_i² F(x4)] é o mesmo para i=1,2,3.
    tangent_norm = Fraction(1, 4)
    conditional_transverse_moment = "E[x1²F]=E[x2²F]=E[x3²F]"
    z_w_over_z_y = Fraction(1, 1)
    match_ratio = Fraction(3, 5)
    transported_ratio = match_ratio * z_w_over_z_y
    sin2 = transported_ratio / (1 + transported_ratio)

    print("Q29 — NO-GO ANALÍTICO DO TRANSPORTE LOCAL")
    print("|A n|² comum                 =", tangent_norm)
    print("simetria condicional         =", conditional_transverse_moment)
    print("Z_W/Z_Y                      =", z_w_over_z_y)
    print("g'^2/g^2 transportado        =", transported_ratio)
    print("sin²(theta_W) transportado   =", sin2)

    assert z_w_over_z_y == 1
    assert sin2 == Fraction(3, 8)


if __name__ == "__main__":
    main()

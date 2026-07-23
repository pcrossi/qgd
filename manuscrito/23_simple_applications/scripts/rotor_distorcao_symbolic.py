#!/usr/bin/env python3
"""
GDQ — Capítulo 23 / Rotor molecular

Objetivo:
    Verificar simbolicamente a distorção centrífuga líder a partir da
    minimização radial do rotor molecular reduzido.

Classificação:
    Verificação simbólica da derivação. Não usa dados experimentais.

Modelo:
    E(R;J) = L^2/(2*mu*R^2) + (1/2)*mu*omega^2*(R-R0)^2

    Com R=R0+x e baixa rotação, minimizar em x produz:

    E_J = B J(J+1) - D [J(J+1)]^2 + ...

    B = hbar^2/(2*mu*R0^2)
    D = hbar^4/(2*mu^3*omega^2*R0^6)

Saída:
    saida_rotor_distorcao_symbolic.md
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


OUT = Path(__file__).with_name("saida_rotor_distorcao_symbolic.md")


def main() -> None:
    L2, mu, R0, omega, x = sp.symbols("L2 mu R0 omega x", positive=True)

    # Expansão até x^2. O termo x^2 multiplicado por L2 só afetaria ordem L6
    # após substituir x*=O(L2), então não entra no coeficiente líder D~L4.
    E = L2 / (2 * mu * R0**2) - L2 * x / (mu * R0**3) + sp.Rational(1, 2) * mu * omega**2 * x**2
    x_star = sp.solve(sp.diff(E, x), x)[0]
    E_eff = sp.expand(E.subs(x, x_star))

    B_coeff = sp.simplify(sp.diff(E_eff, L2).subs(L2, 0))
    D_coeff = sp.simplify(-sp.diff(E_eff, L2, 2).subs(L2, 0) / 2)

    expected_B = 1 / (2 * mu * R0**2)
    expected_D = 1 / (2 * mu**3 * omega**2 * R0**6)

    lines = [
        "---",
        'title: "Saída — derivação simbólica da distorção do rotor"',
        "---",
        "",
        "# Saída — derivação simbólica da distorção do rotor",
        "",
        "Classificação: verificação simbólica da redução radial harmônica.",
        "",
        "Energia expandida:",
        "",
        "$$",
        "E(x)=\\frac{L^2}{2\\mu R_0^2}-\\frac{L^2}{\\mu R_0^3}x+\\frac12\\mu\\omega_e^2x^2.",
        "$$",
        "",
        "Mínimo radial:",
        "",
        "$$",
        f"x_\\ast={sp.latex(x_star)}.",
        "$$",
        "",
        "Energia efetiva:",
        "",
        "$$",
        f"E_{{\\rm eff}}={sp.latex(E_eff)}.",
        "$$",
        "",
        "Coeficientes em $E=B_L L^2-D_L L^4+\\cdots$:",
        "",
        "$$",
        f"B_L={sp.latex(B_coeff)},\\qquad D_L={sp.latex(D_coeff)}.",
        "$$",
        "",
        "Checagem contra a forma esperada:",
        "",
        "$$",
        f"B_L-B_{{\\rm exp}}={sp.latex(sp.simplify(B_coeff-expected_B))},",
        "\\qquad",
        f"D_L-D_{{\\rm exp}}={sp.latex(sp.simplify(D_coeff-expected_D))}.",
        "$$",
        "",
        "Como $L^2=\\hbar^2J(J+1)$:",
        "",
        "$$",
        "D=\\frac{\\hbar^4}{2\\mu^3\\omega_e^2R_0^6}.",
        "$$",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

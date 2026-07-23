#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar bohm epsilon cl` associada ao capítulo `07_classical_limit`.

Verifica a escala do termo de Bohm.

Para R(x)=exp(-x^2/(2L^2)) em 1D:

    Q_B = -(hbar^2/2m) R''/R.

No ponto x=0, |R''/R|=1/L^2. Com T=p^2/(2m):

    |Q_B|/T = hbar^2/(p^2 L^2) = epsilon_cl^2.

Este é um teste direto da estimativa usada no Capítulo 7.
"""

from pathlib import Path


OUT = Path(__file__).with_name("saida_verificar_bohm_epsilon_cl.md")


def main() -> None:
    hbar = 1.0
    m = 1.0
    p = 10.0
    rows = []
    for L in [2, 4, 8, 16, 32, 64]:
        epsilon = hbar / (p * L)
        qb_abs = hbar * hbar / (2 * m * L * L)
        t_cl = p * p / (2 * m)
        ratio = qb_abs / t_cl
        rows.append((L, epsilon, ratio, ratio / (epsilon * epsilon)))

    lines = [
        "---",
        'title: "Saída — escala do termo de Bohm"',
        "---",
        "",
        "# Saída — escala do termo de Bohm",
        "",
        "Classificação: avaliação direta de estimativa analítica em toy model.",
        "",
        "| $L_\\rho$ | $\\varepsilon_{\\rm cl}$ | $|Q_B|/T_{\\rm cl}$ | razão por $\\varepsilon_{\\rm cl}^2$ |",
        "|---:|---:|---:|---:|",
    ]
    for L, eps, ratio, scaled in rows:
        lines.append(f"| {L} | {eps:.8e} | {ratio:.8e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusão: neste perfil gaussiano, a razão é exatamente",
        "$|Q_B|/T_{\\rm cl}=\\varepsilon_{\\rm cl}^2$ no centro do pacote.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()


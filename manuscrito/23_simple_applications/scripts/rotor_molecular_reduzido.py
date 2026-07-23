#!/usr/bin/env python3
"""Capítulo 23 — rotor molecular reduzido.

Objetivo:
    Avaliar o espectro rotacional ideal e a distorção centrífuga líder para
    uma molécula de referência, usando constantes espectroscópicas como dados
    externos.

Classificação:
    Comparação fenomenológica. B e omega_e são dados externos; a previsão
    absoluta exigiria derivá-los da Hessiana da ponte molecular.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).with_name("saida_rotor_molecular_reduzido.md")


def main() -> None:
    # Monóxido de carbono 12C16O, valores aproximados de referência
    # espectroscópica em cm^-1. Eles entram como dados externos, não como
    # parâmetros derivados aqui.
    B_cm = 1.931_280_87
    omega_e_cm = 2169.813_58
    D_cm_gdq = 4.0 * B_cm**3 / omega_e_cm**2

    # Valor típico tabulado para comparação de ordem de grandeza.
    D_cm_ref = 6.121e-6

    lines = [
        "---",
        'title: "Saída — rotor molecular reduzido"',
        "---",
        "",
        "# Saída — rotor molecular reduzido",
        "",
        "- molécula de comparação: CO;",
        f"- $B$ externo = `{B_cm:.8f}` cm^-1;",
        f"- $\\omega_e$ externo = `{omega_e_cm:.8f}` cm^-1;",
        f"- $D_{{\\rm GDQ}}=4B^3/\\omega_e^2$ = `{D_cm_gdq:.12e}` cm^-1;",
        f"- $D$ referência típica = `{D_cm_ref:.12e}` cm^-1;",
        f"- erro relativo = `{D_cm_gdq/D_cm_ref-1.0:+.12e}`;",
        "- classificação: comparação fenomenológica.",
        "",
        "| $J$ | $E_J=BJ(J+1)$ [cm^-1] | $E_J$ com distorção [cm^-1] | correção [cm^-1] |",
        "|---:|---:|---:|---:|",
    ]
    for j in range(0, 11):
        x = j * (j + 1)
        rigid = B_cm * x
        corr = D_cm_gdq * x * x
        lines.append(f"| {j} | `{rigid:.12f}` | `{rigid-corr:.12f}` | `{-corr:.12e}` |")

    lines += [
        "",
        "Interpretação: a forma $J(J+1)$ vem do domínio angular $S^2$; a constante",
        "$D$ fica próxima à ordem espectroscópica quando $B$ e $\\omega_e$ são dados.",
        "Para previsão GDQ, esses dados devem vir da Hessiana molecular.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

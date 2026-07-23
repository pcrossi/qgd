#!/usr/bin/env python3
"""
GDQ — Capítulo 19 / No-go produto, Berger e colar

Objetivo:
    Registrar numericamente os diagnósticos negativos consolidados:
      - produto/local preserva Z_W/Z_Y=1 e sin²(theta_W)=3/8;
      - modo Berger homogêneo tem Hessiana efetiva negativa;
      - fóton no colar cilíndrico infinito tem norma divergente.

Classificação:
    Teste de consistência/no-go. Resultado negativo preservado.

Saída:
    scripts/saida_no_go_berger_colar.md
"""

from pathlib import Path


def main() -> None:
    z_ratio_product = 1.0
    gprime2_over_g2_match = 3.0 / 5.0
    sin2_product = gprime2_over_g2_match * z_ratio_product / (
        1.0 + gprime2_over_g2_match * z_ratio_product
    )

    hq_eff = -2.67090856
    collar_lengths = [1.0, 10.0, 100.0, 1000.0]
    photon_norm_density = 1.0

    lines = [
        "# Saída — no-go produto/Berger/colar",
        "",
        "Classificação: teste de consistência com resultado negativo.",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| Z_W/Z_Y no produto local | {z_ratio_product:.12f} |",
        f"| sin2_theta no produto local | {sin2_product:.12f} |",
        f"| H_q_eff Berger | {hq_eff:.8f} |",
        "",
        "## Norma fotônica no colar cilíndrico",
        "",
        "| comprimento L | norma proporcional |",
        "|---:|---:|",
    ]

    for length in collar_lengths:
        lines.append(f"| {length:.1f} | {photon_norm_density * length:.1f} |")

    lines += [
        "",
        "Interpretação: no colar infinito a norma cresce sem limite; logo o ansatz cilíndrico não localiza o fóton e não prediz alpha.",
    ]

    out = Path(__file__).with_name("saida_no_go_berger_colar.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

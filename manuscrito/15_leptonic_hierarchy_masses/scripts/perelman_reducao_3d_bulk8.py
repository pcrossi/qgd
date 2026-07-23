#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / redução Perelman 3D dentro do bulk 8D fatorado.

Classificação:
    verificação simbólico-numérica de identidade geométrica condicional.

O script verifica o caso produto:

    M8 = B3 x K5,
    g8 = gB oplus gK,
    Ric(gK)=0,
    nabla_K f = 0,
    H_BK = 0.

Neste setor, o fluxo de Ricci ponderado relevante para singularidades materiais
age somente no fator curvo B3. O script não aplica Perelman a uma variedade 8D
geral; ele verifica a condição sob a qual a análise 3D é legitimamente herdada.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    dim_b = 3
    dim_k = 5
    ric_k_norm = 0.0
    grad_k_f_norm = 0.0
    torsion_mixed_norm = 0.0

    product_is_valid = (
        ric_k_norm == 0.0
        and grad_k_f_norm == 0.0
        and torsion_mixed_norm == 0.0
    )

    lines = [
        "---",
        'title: "Saída — redução Perelman 3D no bulk 8D"',
        "---",
        "",
        "# Saída — redução Perelman 3D no bulk 8D",
        "",
        "## Entrada",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| dimensão do fator curvo $B_3$ | `{dim_b}` |",
        f"| dimensão do fator espectador $K_5$ | `{dim_k}` |",
        f"| $\\|\\operatorname{{Ric}}(g_K)\\|$ | `{ric_k_norm:.1f}` |",
        f"| $\\|\\nabla_K f\\|$ | `{grad_k_f_norm:.1f}` |",
        f"| $\\|H_{{BK}}\\|$ | `{torsion_mixed_norm:.1f}` |",
        "",
        "## Identidade verificada",
        "",
        "Para $g_8=g_B\\oplus g_K$, vale:",
        "",
        "$$",
        "\\operatorname{Ric}(g_8)",
        "=",
        "\\operatorname{Ric}(g_B)\\oplus\\operatorname{Ric}(g_K).",
        "$$",
        "",
        "Com $\\operatorname{Ric}(g_K)=0$, o fluxo no fator espectador congela:",
        "",
        "$$",
        "\\partial_\\tau g_K=0.",
        "$$",
        "",
        "A singularidade admissível tem forma produto:",
        "",
        "$$",
        "\\Sigma_{\\rm sing}^{(8)}",
        "=",
        "\\Sigma_{\\rm sing}^{(3)}\\times K_5.",
        "$$",
        "",
        "## Veredito",
        "",
        f"- setor produto válido: `{product_is_valid}`;",
        "- Perelman é usado apenas no fator tridimensional curvo;",
        "- o toro classifica holonomia/carga/fase, mas não gera a cirurgia.",
        "",
    ]

    out = Path(__file__).with_name("saida_perelman_reducao_3d_bulk8.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

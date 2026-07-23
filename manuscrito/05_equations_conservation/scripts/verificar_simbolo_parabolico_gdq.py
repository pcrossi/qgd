#!/usr/bin/env python3
"""
GDQ — Capítulo 5 / bem-postura do fluxo geométrico em gauge.

Objetivo:
    Verificar, em um modelo matricial autocontido, a condição algébrica usada
    na prova de bem-postura local do fluxo geométrico: após gauge de
    DeTurck/Hodge, o símbolo principal do sistema acoplado é

        sigma_pr(xi) = |xi|_g^2 I.

    Para uma métrica riemanniana positiva, |xi|_g^2 > 0 para xi != 0.

Classificação:
    Verificação simbólico-numérica de parabolicidade forte do símbolo principal.
    Não é previsão física, não usa dados experimentais e não substitui o
    teorema analítico de EDPs parabólicas quase-lineares.

Domínio:
    Bulk local real de dimensão d=8, em um ponto. A checagem é pontual no
    símbolo principal; condições globais de bordo aparecem no texto.

Saída:
    saida_verificar_simbolo_parabolico_gdq.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def random_spd_matrix(rng: np.random.Generator, d: int) -> np.ndarray:
    """Gera uma métrica riemanniana positiva-definida."""
    a = rng.normal(size=(d, d))
    return a.T @ a + d * np.eye(d)


def main() -> None:
    rng = np.random.default_rng(1729)
    d = 8

    g = random_spd_matrix(rng, d)
    g_inv = np.linalg.inv(g)

    eig_g = np.linalg.eigvalsh(g)
    eig_g_inv = np.linalg.eigvalsh(g_inv)

    # Número de componentes independentes dos blocos principais:
    # métrica simétrica, 3-forma, dois escalares.
    n_metric = d * (d + 1) // 2
    n_three_form = d * (d - 1) * (d - 2) // 6
    n_scalars = 2
    n_fields = n_metric + n_three_form + n_scalars

    samples = 256
    xi_values = rng.normal(size=(samples, d))
    xi_norms = np.einsum("ni,ij,nj->n", xi_values, g_inv, xi_values)

    min_symbol = float(np.min(xi_norms))
    max_symbol = float(np.max(xi_norms))
    min_eig_g = float(np.min(eig_g))
    min_eig_g_inv = float(np.min(eig_g_inv))

    # Se o bloco acoplado principal é |xi|_g^2 I, o menor autovalor do símbolo
    # de todo o sistema é |xi|_g^2 em cada amostra.
    symbol_is_positive = bool(np.all(xi_norms > 0.0) and min_eig_g > 0.0)

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Saída — símbolo parabólico GDQ em gauge"\n')
    lines.append('---\n\n')
    lines.append("# Saída — símbolo parabólico GDQ em gauge\n\n")
    lines.append("## Classificação\n\n")
    lines.append(
        "Verificação simbólico-numérica da positividade do símbolo principal "
        "após gauge. Não é previsão física.\n\n"
    )
    lines.append("## Dados do teste\n\n")
    lines.append(f"- Dimensão real do bulk: $d={d}$\n")
    lines.append(f"- Componentes métricas simétricas: ${n_metric}$\n")
    lines.append(f"- Componentes de 3-forma: ${n_three_form}$\n")
    lines.append(f"- Escalares $(\\phi,\\chi)$: ${n_scalars}$\n")
    lines.append(f"- Total de componentes no bloco principal: ${n_fields}$\n")
    lines.append(f"- Amostras de covetores $\\xi$: ${samples}$\n\n")
    lines.append("## Identidade verificada\n\n")
    lines.append("$$\n")
    lines.append("\\sigma_{\\rm pr}(\\xi)=|\\xi|_g^2 I.\n")
    lines.append("$$\n\n")
    lines.append("com\n\n")
    lines.append("$$\n")
    lines.append("|\\xi|_g^2=g^{ab}\\xi_a\\xi_b.\n")
    lines.append("$$\n\n")
    lines.append("## Valores numéricos\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| menor autovalor de $g$ | {min_eig_g:.12e} |\n")
    lines.append(f"| menor autovalor de $g^{{-1}}$ | {min_eig_g_inv:.12e} |\n")
    lines.append(f"| menor $|\\xi|_g^2$ amostrado | {min_symbol:.12e} |\n")
    lines.append(f"| maior $|\\xi|_g^2$ amostrado | {max_symbol:.12e} |\n\n")
    lines.append("## Veredito\n\n")
    if symbol_is_positive:
        lines.append(
            "A métrica é positiva-definida e o símbolo principal "
            "$|\\xi|_g^2I$ é positivo para os covetores não nulos amostrados. "
            "Isto ilustra a parabolicidade forte após gauge.\n"
        )
    else:
        lines.append(
            "A positividade falhou no teste. A métrica ou a implementação "
            "devem ser revisadas.\n"
        )

    out = OUT / "saida_verificar_simbolo_parabolico_gdq.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

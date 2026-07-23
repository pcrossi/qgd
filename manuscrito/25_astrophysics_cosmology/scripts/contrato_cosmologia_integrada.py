#!/usr/bin/env python3
"""
Contrato autocontido para o solver cosmológico integrado da GDQ.

Classificação:
    verificação estrutural/simbólica de arquitetura de solver.

Este script não calcula CMB, BAO, BBN ou lentes. Ele registra, de forma
executável, a cadeia mínima que um solver metrológico futuro deve obedecer:

    S_GDQ -> Phi_cos* -> K_cos^phys -> observáveis cosmológicos.

A utilidade prática é impedir que cada anomalia cosmológica receba um fator
próprio ajustado depois. O mesmo conjunto P_cos deve alimentar todos os blocos.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_contrato_cosmologia_integrada.md"


def main() -> None:
    entradas = [
        "Phi_cos*=(g,J,H,f,U)_cos",
        "R_H",
        "eta_b",
        "T_0",
        "P_prim",
        "B_contorno",
    ]
    observaveis = [
        "H(z)",
        "SN",
        "BAO",
        "CMB",
        "BBN/litio",
        "lentes",
        "crescimento",
        "birrefringencia",
    ]
    proibicoes = [
        "fator independente para Hubble",
        "fator independente para litio",
        "fator independente para Bullet Cluster",
        "fator independente para birrefringencia",
        "troca de contorno depois da comparacao",
    ]

    lines = [
        "---",
        'title: "Saída — contrato de cosmologia integrada"',
        "---",
        "",
        "# Saída — contrato de cosmologia integrada",
        "",
        "## Entrada única",
        "",
        "$$",
        "\\mathcal P_{\\rm cos}=(\\Phi_*^{\\rm cos},R_H,\\eta_b,T_0,\\mathcal P_{\\rm prim},\\mathcal B_{\\rm contorno})",
        "$$",
        "",
        "| Item | Papel |",
        "|---|---|",
    ]
    for item in entradas:
        lines.append(f"| `{item}` | dado congelado antes da comparação |")

    lines += [
        "",
        "## Cadeia comum",
        "",
        "$$",
        "\\mathcal S_{\\rm GDQ}\\to\\Phi_*^{\\rm cos}\\to K_{\\rm cos}^{\\rm phys}\\to\\delta\\Phi_{\\rm cos}\\to\\text{observáveis}",
        "$$",
        "",
        "$$",
        "K_{\\rm cos}^{\\rm phys}=P_{\\rm cos}^{\\rm phys}\\operatorname{Hess}\\mathcal S_{\\rm GDQ}P_{\\rm cos}^{\\rm phys}",
        "$$",
        "",
        "$$",
        "K_{\\rm cos}^{\\rm phys}\\delta\\Phi_{\\rm cos}=J_{\\rm bar}+J_\\gamma+J_\\nu+J_H",
        "$$",
        "",
        "## Observáveis obrigatórios",
        "",
        "| Observável | Deve usar |",
        "|---|---|",
    ]
    for obs in observaveis:
        lines.append(f"| `{obs}` | o mesmo `P_cos` e o mesmo background |")

    lines += [
        "",
        "## Proibições de fechamento",
        "",
        "| Proibição | Motivo |",
        "|---|---|",
    ]
    for item in proibicoes:
        lines.append(f"| `{item}` | quebraria a cosmologia integrada |")

    lines += [
        "",
        "## Classificação",
        "",
        "Formulação estrutural fechada. Solver metrológico conjunto permanece extensão futura.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

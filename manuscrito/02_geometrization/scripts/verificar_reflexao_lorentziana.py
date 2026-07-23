#!/usr/bin/env python3
"""
GDQ — Capítulo 2 / Reflexão lorentziana por forma-relógio.

Objetivo:
    Ilustrar linearmente a afirmação usada no Capítulo 2: dada uma métrica
    positiva q no setor projetado e uma forma-relógio unitária theta, a métrica
    efetiva h = q - 2 theta tensor theta tem assinatura (-,+,+,+).

Fonte teórica:
    manuscrito/02_geometrization/02.10 - Do bulk Riemanniano ao espaço-tempo físico.md
    manuscrito/02_geometrization/axiom_to_theorem_audit.md
    manuscrito/notes/geometrization/Forma relogio sincronizacao e assinatura lorentziana.md

Classificação:
    Ilustração linear/teste simbólico. Não é previsão física.

Equação:
    h_ab = q_ab - 2 theta_a theta_b
    com theta unitária em q.

Domínio e contorno:
    Espaço vetorial tangente de dimensão 4; sem EDP e sem contorno.

Parâmetros:
    Universais:
        q = identidade euclidiana 4x4
        theta = (1,0,0,0)
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        autovalores calculados por álgebra linear.

Saída:
    saida_verificar_reflexao_lorentziana.md

Observação:
    Nenhum alvo experimental é usado. A seleção física de theta pertence ao
    argumento de sincronização/forma-relógio, não a este teste linear.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def signature(eigenvalues: np.ndarray, tol: float = 1e-12) -> tuple[int, int, int]:
    """Conta autovalores negativos, positivos e nulos."""
    neg = int(np.sum(eigenvalues < -tol))
    pos = int(np.sum(eigenvalues > tol))
    zero = int(len(eigenvalues) - neg - pos)
    return neg, pos, zero


def main() -> None:
    q = np.eye(4)
    theta = np.array([1.0, 0.0, 0.0, 0.0])
    norm_theta = float(theta @ np.linalg.inv(q) @ theta)
    h = q - 2.0 * np.outer(theta, theta)
    eig_q = np.linalg.eigvalsh(q)
    eig_h = np.linalg.eigvalsh(h)
    sig_q = signature(eig_q)
    sig_h = signature(eig_h)
    ok = abs(norm_theta - 1.0) < 1e-12 and sig_h == (1, 3, 0)

    lines: list[str] = []
    lines.append("# Saída — reflexão lorentziana por forma-relógio\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração linear/teste simbólico. Não é previsão física.\n\n")
    lines.append("## Construção\n\n")
    lines.append("Parte-se de uma métrica positiva $q$ e de uma forma-relógio unitária $\\theta$.\n\n")
    lines.append("$$\n")
    lines.append("h_{ab}=q_{ab}-2\\theta_a\\theta_b.\n")
    lines.append("$$\n\n")
    lines.append("Neste teste:\n\n")
    lines.append("$$\n")
    lines.append("q=I_4,\n")
    lines.append("\\qquad\n")
    lines.append("\\theta=(1,0,0,0).\n")
    lines.append("$$\n\n")
    lines.append("## Resultado\n\n")
    lines.append(f"- Norma de $\\theta$ em $q$: `{norm_theta:.12g}`.\n")
    lines.append(f"- Autovalores de $q$: `{eig_q.tolist()}`.\n")
    lines.append(f"- Autovalores de $h$: `{eig_h.tolist()}`.\n")
    lines.append(f"- Assinatura de $q$ `(neg,pos,zero)`: `{sig_q}`.\n")
    lines.append(f"- Assinatura de $h$ `(neg,pos,zero)`: `{sig_h}`.\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A checagem passou: a assinatura efetiva é $(-,+,+,+)$.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída ilustra apenas a álgebra da reflexão. ")
    lines.append("A seleção física de $\\theta$ vem do argumento de simultaneidade, ")
    lines.append("sincronização e orientação causal discutido no texto.\n")

    out = OUT / "saida_verificar_reflexao_lorentziana.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

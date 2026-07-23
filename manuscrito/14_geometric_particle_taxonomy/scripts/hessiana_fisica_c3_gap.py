#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Hessiana física C3 e gap reduzido

Objetivo:
    Calcular explicitamente a Hessiana angular vinculada do junction C3, o
    projetor que remove a rotação global, o bloco radial homogêneo, o
    complemento de Schur e o gap físico reduzido.

Classificação:
    Avaliação direta de operadores reduzidos derivados no texto. Não há uso
    de dados experimentais nem ajuste.

Saída:
    scripts/saida_hessiana_fisica_c3_gap.md
"""

from pathlib import Path
import numpy as np


def main() -> None:
    tau = 1.0
    kappa_rel = 1.0
    tension = 1.0
    theta = np.array([0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0])

    d_constraint = tension * np.vstack((-np.sin(theta), np.cos(theta)))
    h_theta = kappa_rel * d_constraint.T @ d_constraint

    ones = np.ones((3, 1))
    p_phys = np.eye(3) - (ones @ ones.T) / 3.0
    h_projected = p_phys.T @ h_theta @ p_phys

    eig_all = np.linalg.eigvalsh(h_theta)
    eig_projected = np.linalg.eigvalsh(h_projected)
    eig_physical = eig_projected[eig_projected > 1e-10]

    k_radial = (3.0 / (2.0 * tau)) * np.eye(3)
    j_theta_r = np.zeros((3, 3))
    h_schur = h_theta - j_theta_r @ np.linalg.inv(k_radial) @ j_theta_r.T
    eig_schur = np.linalg.eigvalsh(p_phys.T @ h_schur @ p_phys)
    eig_schur_physical = eig_schur[eig_schur > 1e-10]

    non_homogeneous_gap = 1.0 / (2.0 * tau)
    reduced_gap = min(float(np.min(eig_schur_physical)), non_homogeneous_gap)

    lines = [
        "# Saída — Hessiana física C3 e gap reduzido",
        "",
        "## Parâmetros normalizados",
        "",
        f"- tau: `{tau}`",
        f"- kappa_rel: `{kappa_rel}`",
        f"- T: `{tension}`",
        "",
        "## Espectro angular",
        "",
        f"- Autovalores de H_theta: `{eig_all.tolist()}`",
        f"- Autovalores físicos após projeção: `{eig_physical.tolist()}`",
        "",
        "## Schur",
        "",
        "- J_theta_r é nulo pela conservação da classe primitiva de fluxo.",
        f"- Autovalores físicos do complemento de Schur: `{eig_schur_physical.tolist()}`",
        "",
        "## Gap",
        "",
        f"- Gap não homogêneo gaussiano: `{non_homogeneous_gap}`",
        f"- Gap reduzido final: `{reduced_gap}`",
        "",
        "Conclusão: após remover a rotação global, o junction C3 tem dois modos relativos positivos e gap reduzido positivo.",
    ]

    out = Path(__file__).with_name("saida_hessiana_fisica_c3_gap.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

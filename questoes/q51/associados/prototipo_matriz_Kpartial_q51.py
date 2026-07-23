#!/usr/bin/env python3
"""Q51 — protótipo matricial de K_partial^phys e projetor alfa.

Classificação:
    - fixture matemático / validação de mecanismo;
    - não previsão física;
    - objetivo: demonstrar que qualquer peso 0<=p<=1 pode ser realizado como
      norma quadrática de um projetor espectral ortogonal.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "saida_prototipo_matriz_Kpartial_q51.md"


def build_K_from_weight(p: float, gap_alpha: float = 0.0, gap_orth: float = 1.0, gap_res: float = 3.0) -> np.ndarray:
    """Minimal 3x3 surface Hessian realizing a projection weight p.

    Basis:
        e0: bare 4N cluster mode
        e1: daughter surface mode
        e2: residual collective surface mode

    The alpha spectral vector is:
        v_alpha = sqrt(p) e0 + sqrt(1-p) e1.

    Then ||P_alpha e0||^2 = p.
    """
    p = min(max(p, 0.0), 1.0)
    v_alpha = np.array([math.sqrt(p), math.sqrt(1.0 - p), 0.0])
    v_orth = np.array([math.sqrt(1.0 - p), -math.sqrt(p), 0.0])
    v_res = np.array([0.0, 0.0, 1.0])
    V = np.column_stack([v_alpha, v_orth, v_res])
    D = np.diag([gap_alpha, gap_orth, gap_res])
    return V @ D @ V.T


def main() -> None:
    cases = [
        ("U-238", 0.000000),
        ("U-234", 0.938269),
        ("U-232", 0.630933),
        ("Th-232", 0.000000),
        ("Ra-226", 0.812735),
        ("Po-212", 0.507847),
    ]

    phi_alpha = np.array([1.0, 0.0, 0.0])

    lines = []
    lines.append("# Saída — protótipo matricial de K_partial Q51\n\n")
    lines.append("Classificação: fixture matemático, não previsão.\n\n")
    lines.append(
        "Base: $e_0$ modo nu $4N$, $e_1$ modo do núcleo filho, "
        "$e_2$ modo coletivo residual.\n\n"
    )
    lines.append("Autovetor alfa realizado:\n\n")
    lines.append("$$\n")
    lines.append("v_\\alpha=\\sqrt p\\,e_0+\\sqrt{1-p}\\,e_1.\n")
    lines.append("$$\n\n")
    lines.append("Então:\n\n")
    lines.append("$$\n")
    lines.append("\\|P_\\alpha e_0\\|^2=p.\n")
    lines.append("$$\n\n")
    lines.append("| Núcleo | p_req | p_model | autovalores K | autovetor alfa |\n")
    lines.append("| --- | ---: | ---: | --- | ---: |\n")

    for name, p_req in cases:
        K = build_K_from_weight(p_req)
        vals, vecs = np.linalg.eigh(K)
        idx = int(np.argmin(vals))
        v_alpha = vecs[:, idx]
        P_alpha = np.outer(v_alpha, v_alpha)
        projected = P_alpha @ phi_alpha
        p_model = float(projected @ projected)
        vals_text = ", ".join(f"{v:.3f}" for v in vals)
        v_text = ", ".join(f"{v:.3f}" for v in v_alpha)
        lines.append(f"| {name} | {p_req:.6f} | {p_model:.6f} | `{vals_text}` | `{v_text}` |\n")

    lines.append("\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "O protótipo mostra que pesos nulos, quase unitários e intermediários "
        "são exatamente normas quadráticas de projetores espectrais. Isso "
        "valida o mecanismo matemático, mas a matriz acima é construída a "
        "partir dos pesos requeridos; portanto é fixture, não previsão.\n\n"
    )
    lines.append(
        "O próximo passo físico é substituir essa matriz por blocos calculados "
        "da Hessiana de superfície do background nuclear.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

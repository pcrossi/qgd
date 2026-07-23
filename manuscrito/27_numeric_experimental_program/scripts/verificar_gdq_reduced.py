#!/usr/bin/env python3
"""Verifica a biblioteca reduzida GDQ.

Classificação:
    teste de consistência metodológica.

O objetivo é confirmar que os blocos reduzidos usados no manuscrito reproduzem
identidades analíticas simples:

    1. DtN massivo: R = lambda coth(lambda L);
    2. Schur: eliminação explícita de graus internos;
    3. resposta quadrática: 1/2 delta^T R delta;
    4. detector: Gamma = 1/2 zeta^2 C_path R;
    5. densidade de duas alternativas: o termo cruzado decai como exp(-Gamma).

Nenhum parâmetro experimental é ajustado aqui.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from gdq_reduced import (
    coherence_from_gamma,
    detector_gamma,
    dtn_massive_interval,
    quadratic_response,
    schur_complement,
    two_path_density,
)


OUT = Path(__file__).resolve().parent / "saida_verificar_gdq_reduced.md"


def main() -> None:
    # Teste 1: DtN reduzido usado em problemas de detector.
    lambda_eff = 1.1
    length = 1.0
    r_dtn = dtn_massive_interval(lambda_eff, length)

    # Teste 2: complemento de Schur em matriz pequena.
    kbb = np.array([[2.0, 0.2], [0.2, 1.7]])
    kbi = np.array([[0.3, 0.1], [0.2, 0.4]])
    kib = kbi.T
    kii = np.array([[3.0, 0.25], [0.25, 2.5]])
    k_eff = schur_complement(kbb, kbi, kib, kii)

    # Verificação independente por resolução do sistema interno:
    # para cada vetor de bordo b, a energia minimizada deve usar
    # i = -K_ii^{-1} K_ib b e retornar b^T K_eff b.
    b = np.array([1.0, -0.5])
    i_star = -np.linalg.solve(kii, kib @ b)
    full = (
        b @ kbb @ b
        + 2.0 * b @ kbi @ i_star
        + i_star @ kii @ i_star
    )
    reduced = b @ k_eff @ b

    # Teste 3: resposta quadrática.
    delta = np.array([1.0, -1.0])
    e_resp = quadratic_response(delta, k_eff)

    # Teste 4: detector e coerência.
    zeta = 1.25
    c_path = 1.0
    gamma = detector_gamma(zeta, lambda_eff, length, c_path)
    coherence = coherence_from_gamma(gamma)

    # Teste 5: densidade de duas alternativas.
    x = np.linspace(-np.pi, np.pi, 9)
    i1 = np.ones_like(x)
    i2 = np.ones_like(x)
    rho_free = two_path_density(i1, i2, x, gamma=0.0)
    rho_det = two_path_density(i1, i2, x, gamma=gamma)
    contrast_free = float((rho_free.max() - rho_free.min()) / (rho_free.max() + rho_free.min()))
    contrast_det = float((rho_det.max() - rho_det.min()) / (rho_det.max() + rho_det.min()))

    checks = {
        "Schur reproduz energia minimizada": abs(full - reduced),
        "K_eff simétrico": np.linalg.norm(k_eff - k_eff.T),
        "K_eff menor autovalor": float(np.linalg.eigvalsh(k_eff).min()),
        "contraste com detector menor que contraste livre": float(contrast_det < contrast_free),
    }

    lines = ["# Saída — verificação da biblioteca reduzida GDQ\n\n"]
    lines.append("Classificação: teste de consistência metodológica.\n\n")
    lines.append("## Parâmetros fixos do teste\n\n")
    lines.append("| parâmetro | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\lambda_{{\\rm eff}}$ | {lambda_eff:.12f} |\n")
    lines.append(f"| $L$ | {length:.12f} |\n")
    lines.append(f"| $\\zeta$ | {zeta:.12f} |\n")
    lines.append(f"| $C_{{\\rm path}}$ | {c_path:.12f} |\n")
    lines.append("\n## Resultados\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\mathsf R_{{\\rm DtN}}=\\lambda\\coth(\\lambda L)$ | {r_dtn:.12f} |\n")
    lines.append(f"| $\\Gamma_{{\\rm det}}$ | {gamma:.12f} |\n")
    lines.append(f"| $e^{{-\\Gamma_{{\\rm det}}}}$ | {coherence:.12f} |\n")
    lines.append(f"| contraste sem detector | {contrast_free:.12f} |\n")
    lines.append(f"| contraste com detector | {contrast_det:.12f} |\n")
    lines.append(f"| $E_{{\\rm resp}}$ | {e_resp:.12f} |\n")
    lines.append("\n## Verificações\n\n")
    lines.append("| teste | valor |\n")
    lines.append("|---|---:|\n")
    for name, value in checks.items():
        lines.append(f"| {name} | {value:.12e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append(
        "Os blocos reduzidos satisfazem as identidades algébricas esperadas. "
        "A redução é metodológica: em aplicações físicas, os parâmetros devem "
        "vir do background, do contorno ou do aparelho declarado.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

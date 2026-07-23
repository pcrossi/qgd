#!/usr/bin/env python3
"""
Verificação reduzida de unitariedade em tempo físico no Capítulo 8.

Classificação: teste de consistência algébrica/numerica.

O script não prova a reconstrução OS setorial da GDQ. Ele verifica, em matrizes
finitas autocontidas, as relações usadas no texto:

1. se H é Hermitiano, U(t)=exp(-i t H / hbar) é unitário;
2. o semigrupo euclidiano T(a)=exp(-a H / hbar) é contrativo quando H>=0;
3. um Hamiltoniano efetivo não Hermitiano em setor projetado pode decair;
4. a mesma física pode vir de uma evolução total Hermitiana que preserva a
   norma, quando o canal de escape é incluído.

Isso ilustra a distinção GDQ: fluxo/contração euclidiana em tau não é perda de
probabilidade em tempo físico t.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def hermitian_exponential(H: np.ndarray, factor: complex) -> np.ndarray:
    """Calcula exp(factor*H) por diagonalização Hermitiana."""
    evals, evecs = np.linalg.eigh(H)
    return (evecs * np.exp(factor * evals)) @ evecs.conj().T


def norm(v: np.ndarray) -> float:
    """Norma quadrática Hermitiana."""
    return float(np.vdot(v, v).real)


def main() -> None:
    hbar = 1.0
    t = 2.7
    a = 1.3

    # Hamiltoniano positivo em um setor físico reconstruído de dimensão finita.
    H = np.array(
        [
            [0.35, 0.12 - 0.03j, 0.0],
            [0.12 + 0.03j, 1.10, 0.20],
            [0.0, 0.20, 2.30],
        ],
        dtype=complex,
    )

    eig_H = np.linalg.eigvalsh(H)
    if np.min(eig_H) < -1e-12:
        raise RuntimeError("H deveria ser positivo para a parte euclidiana.")

    U = hermitian_exponential(H, factor=-1j * t / hbar)
    T = hermitian_exponential(H, factor=-a / hbar)

    psi = np.array([1.0, 0.7 - 0.2j, -0.3j], dtype=complex)
    psi = psi / np.sqrt(norm(psi))

    unitarity_error = np.linalg.norm(U.conj().T @ U - np.eye(H.shape[0]))
    norm_before = norm(psi)
    norm_after_unitary = norm(U @ psi)

    # Como H>=0, o maior autovalor singular de T_E(a) é exp(-a E_min).
    contraction_norm = np.linalg.norm(T, ord=2)
    norm_after_euclidean = norm(T @ psi)

    # Setor efetivo projetado com largura Gamma: não Hermitiano.
    E0 = 0.8
    Gamma = 0.45
    H_eff = E0 - 0.5j * Gamma
    amp_projected = np.exp(-1j * H_eff * t / hbar)
    survival_projected = abs(amp_projected) ** 2
    expected_survival = np.exp(-Gamma * t / hbar)

    # Dilatação unitária mínima: um sistema de dois níveis Hermitiano troca
    # probabilidade entre canal observado P e canal Q.
    g = 0.31
    H_total = np.array([[E0, g], [g, E0 + 0.05]], dtype=complex)
    U_total = hermitian_exponential(H_total, factor=-1j * t / hbar)
    state0 = np.array([1.0, 0.0], dtype=complex)
    state_t = U_total @ state0
    total_norm_error = abs(norm(state_t) - 1.0)
    projected_probability = abs(state_t[0]) ** 2
    leaked_probability = abs(state_t[1]) ** 2
    probability_balance_error = abs(projected_probability + leaked_probability - 1.0)

    lines = [
        "---",
        'title: "Saída — verificar unitariedade em tempo físico"',
        "---",
        "",
        "# Saída — verificar unitariedade em tempo físico",
        "",
        "Classificação: teste de consistência algébrica/numerica.",
        "",
        "## Dados",
        "",
        f"- dimensão do setor fechado: {H.shape[0]}",
        f"- autovalores de $H$: {', '.join(f'{x:.12f}' for x in eig_H)}",
        f"- tempo físico usado: $t={t}$",
        f"- parâmetro euclidiano usado: $a={a}$",
        "",
        "## Resultados",
        "",
        "| Quantidade | Valor | Interpretação |",
        "|---|---:|---|",
        f"| erro $\\|U^\\dagger U-I\\|$ | {unitarity_error:.3e} | deve ser próximo de zero |",
        f"| norma inicial $\\|\\psi\\|^2$ | {norm_before:.12f} | normalizada |",
        f"| norma após $U(t)$ | {norm_after_unitary:.12f} | preservada |",
        f"| norma espectral de $T_E(a)$ | {contraction_norm:.12f} | contração euclidiana |",
        f"| norma após $T_E(a)$ | {norm_after_euclidean:.12f} | amortecimento em parâmetro euclidiano |",
        f"| sobrevivência projetada não Hermitiana | {survival_projected:.12f} | decai no setor parcial |",
        f"| $\\exp(-\\Gamma t/\\hbar)$ | {expected_survival:.12f} | referência analítica |",
        f"| erro de norma total no modelo Hermitiano ampliado | {total_norm_error:.3e} | total fechado preserva norma |",
        f"| probabilidade no canal $P$ | {projected_probability:.12f} | canal observado |",
        f"| probabilidade vazada para $Q$ | {leaked_probability:.12f} | canal não observado |",
        f"| erro de balanço $P+Q=1$ | {probability_balance_error:.3e} | conservação total |",
        "",
        "## Leitura física",
        "",
        "O teste separa três fatos. O grupo $U(t)$ preserva norma quando $H$ é",
        "Hermitiano. O semigrupo euclidiano $T_E(a)$ é contrativo quando $H\\ge0$.",
        "Um setor projetado pode decair sem que a dinâmica total fechada deixe de ser",
        "unitária.",
        "",
    ]

    out = Path(__file__).with_name("saida_verificar_unitariedade_tempo_fisico.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
GDQ — Capítulo 9 / Emaranhamento reduzido e no-signalling

Objetivo:
    Verificar, no setor projetivo reconstruído, três propriedades usadas como
    alvo operacional para a formulação GDQ do emaranhamento:

        1. estado singlete não fatorável;
        2. correlação ideal E(a,b) = -a.b;
        3. marginais locais independentes da escolha distante.

Importante:
    Este script não é uma simulação completa de aparelhos GDQ reais. Ele é o
    teste reduzido do setor operacional que uma derivação por Hessiana
    multipartida deve reproduzir.

Classificação:
    Teste de consistência operacional reduzido.

Saída:
    scripts/saida_verificar_emaranhamento_no_signalling.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v)
    if n == 0.0:
        raise ValueError("vetor nulo")
    return v / n


def joint_probability(s: int, t: int, a: np.ndarray, b: np.ndarray) -> float:
    """Probabilidade singlete reduzida: P(s,t|a,b)."""
    return 0.25 * (1.0 - s * t * float(np.dot(a, b)))


def correlation(a: np.ndarray, b: np.ndarray) -> float:
    return sum(
        s * t * joint_probability(s, t, a, b)
        for s in (-1, 1)
        for t in (-1, 1)
    )


def marginal_A(s: int, a: np.ndarray, b: np.ndarray) -> float:
    return sum(joint_probability(s, t, a, b) for t in (-1, 1))


def marginal_B(t: int, a: np.ndarray, b: np.ndarray) -> float:
    return sum(joint_probability(s, t, a, b) for s in (-1, 1))


def schmidt_singular_values_singlet() -> np.ndarray:
    coeff = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex) / np.sqrt(2.0)
    return np.linalg.svd(coeff, compute_uv=False)


def chsh_value() -> float:
    a0 = unit(np.array([1.0, 0.0, 0.0]))
    a1 = unit(np.array([0.0, 1.0, 0.0]))
    b0 = unit(np.array([1.0, 1.0, 0.0]))
    b1 = unit(np.array([1.0, -1.0, 0.0]))
    return (
        correlation(a0, b0)
        + correlation(a0, b1)
        + correlation(a1, b0)
        - correlation(a1, b1)
    )


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_emaranhamento_no_signalling.md"

    axes_a = [
        unit(np.array([1.0, 0.0, 0.0])),
        unit(np.array([0.0, 1.0, 0.0])),
        unit(np.array([1.0, 1.0, 0.0])),
    ]
    axes_b = [
        unit(np.array([1.0, 0.0, 0.0])),
        unit(np.array([0.0, 1.0, 0.0])),
        unit(np.array([1.0, -1.0, 0.0])),
    ]

    rows = []
    max_corr_error = 0.0
    max_marginal_A_variation = 0.0
    max_marginal_B_variation = 0.0

    for i, a in enumerate(axes_a):
        marginals_A_for_b = []
        for j, b in enumerate(axes_b):
            e_val = correlation(a, b)
            target = -float(np.dot(a, b))
            max_corr_error = max(max_corr_error, abs(e_val - target))
            ma_plus = marginal_A(1, a, b)
            mb_plus = marginal_B(1, a, b)
            marginals_A_for_b.append(ma_plus)
            rows.append((i, j, float(np.dot(a, b)), e_val, target, ma_plus, mb_plus))
        max_marginal_A_variation = max(
            max_marginal_A_variation,
            max(marginals_A_for_b) - min(marginals_A_for_b),
        )

    for b in axes_b:
        vals = [marginal_B(1, a, b) for a in axes_a]
        max_marginal_B_variation = max(max_marginal_B_variation, max(vals) - min(vals))

    sv = schmidt_singular_values_singlet()
    factorable_rank_one_error = float(min(abs(sv[0]), abs(sv[1])))
    chsh = chsh_value()

    table = "\n".join(
        f"| {i} | {j} | {dot:.12f} | {e:.12f} | {target:.12f} | {ma:.12f} | {mb:.12f} |"
        for i, j, dot, e, target, ma, mb in rows
    )

    text = f"""# Saída — emaranhamento reduzido e no-signalling

Classificação: teste de consistência operacional reduzido.

## Não fatoração

Valores singulares de Schmidt do singlete:

| índice | valor |
|---:|---:|
| 0 | {sv[0]:.12f} |
| 1 | {sv[1]:.12f} |

Como os dois valores são não nulos, o estado não tem posto de Schmidt 1 e não
é produto. O menor valor singular preservado é:

$$
{factorable_rank_one_error:.12f}.
$$

## Correlação e marginais

| eixo A | eixo B | $a\\cdot b$ | $E(a,b)$ | alvo $-a\\cdot b$ | $P(+|a,b)$ em A | $P(+|a,b)$ em B |
|---:|---:|---:|---:|---:|---:|---:|
{table}

## Erros

| teste | valor |
|---|---:|
| erro máximo em $E(a,b)+a\\cdot b$ | {max_corr_error:.12e} |
| variação máxima da marginal A ao trocar B | {max_marginal_A_variation:.12e} |
| variação máxima da marginal B ao trocar A | {max_marginal_B_variation:.12e} |
| valor CHSH reduzido | {chsh:.12f} |
| alvo $-2\\sqrt 2$ | {-2.0*np.sqrt(2.0):.12f} |

## Interpretação

O teste mostra que a correlação conjunta depende dos dois eixos, mas as
marginais locais permanecem iguais a $1/2$. Isso é compatibilidade operacional
com no-signalling no setor projetivo reduzido. A GDQ completa ainda deve
derivar os aparelhos reais por $K_{{AB}}^{{\\rm phys}}$, $\\mathsf R_A$ e
$\\mathsf R_B$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

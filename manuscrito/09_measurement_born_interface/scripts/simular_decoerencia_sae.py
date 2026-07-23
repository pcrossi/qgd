#!/usr/bin/env python3
"""
GDQ — Capítulo 9 / Modelo S+A+E reduzido.

Classificação: redução efetiva de medição. Não é cálculo da Hessiana oficial.

Objetivo:
    Verificar em um modelo finito autocontido:

    1. supressão de termos fora da diagonal quando estados ambientais
       associados a registros se tornam ortogonais;
    2. decaimento exponencial de coerência por gap setorial;
    3. repetibilidade ideal após condicionamento em um registro.

Fonte interna:
    - 09.4 - Sistema, aparelho, ambiente e registros.md
    - 09.6 - Decoerência, bacias dinâmicas e resultado único.md
    - notes/bacias_dinamicas_resultado_unico.md
    - notes/teorema_assintotico_registros_gdq.md

Saída:
    manuscrito/09_measurement_born_interface/scripts/saida_simular_decoerencia_sae.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def projector(v: np.ndarray) -> np.ndarray:
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_simular_decoerencia_sae.md"

    c0 = np.sqrt(0.37)
    c1 = np.sqrt(0.63) * np.exp(0.3j)
    overlaps = np.array([1.0, 0.5, 0.1, 0.01, 0.0])

    rows = []
    for eta in overlaps:
        rho_reduced = np.array(
            [
                [abs(c0) ** 2, c0 * np.conj(c1) * eta],
                [np.conj(c0) * c1 * eta, abs(c1) ** 2],
            ],
            dtype=complex,
        )
        coherence = abs(rho_reduced[0, 1])
        rows.append((eta, coherence, rho_reduced[0, 0].real, rho_reduced[1, 1].real))

    # Modelo assintótico reduzido: |Gamma_01(tau)| <= C exp(-Delta tau).
    delta_meas = 1.75
    C = 1.0
    tau_values = np.array([0.0, 0.5, 1.0, 2.0, 4.0])
    gap_rows = [(tau, C * np.exp(-delta_meas * tau)) for tau in tau_values]

    # Repetibilidade ideal: condicionar no projetor P0 torna repetição certa.
    psi_s = np.array([c0, c1], dtype=complex)
    rho_s = projector(psi_s)
    P0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    p0 = float(np.trace(rho_s @ P0).real)
    rho_cond_0 = P0 @ rho_s @ P0 / p0
    repeat_p0 = float(np.trace(rho_cond_0 @ P0).real)
    repeat_error = abs(repeat_p0 - 1.0)

    table = "\n".join(
        f"| {eta:.3f} | {coh:.12f} | {p0_row:.12f} | {p1_row:.12f} |"
        for eta, coh, p0_row, p1_row in rows
    )
    gap_table = "\n".join(
        f"| {tau:.3f} | {gamma:.12e} |"
        for tau, gamma in gap_rows
    )

    text = f"""---
title: "Saída — simular decoerência S+A+E"
---

# Saída — simular decoerência S+A+E

Classificação: redução efetiva de medição.

## Coeficientes iniciais

- $|c_0|^2 = {abs(c0) ** 2:.12f}$
- $|c_1|^2 = {abs(c1) ** 2:.12f}$

## Supressão por ortogonalização ambiental

| sobreposição ambiental eta | coerência reduzida | p0 | p1 |
|---:|---:|---:|---:|
{table}

## Decaimento por gap setorial

Usando $|\\Gamma_{{01}}(\\tau)|\\le C e^{{-\\Delta_{{\\rm meas}}\\tau}}$ com
$C={C:.3f}$ e $\\Delta_{{\\rm meas}}={delta_meas:.3f}$:

| tau | limite para $|\\Gamma_{{01}}|$ |
|---:|---:|
{gap_table}

## Repetibilidade ideal

Após condicionar no registro 0:

| teste | valor |
|---|---:|
| $p_0=\\operatorname{{Tr}}(\\rho_S P_0)$ | {p0:.12f} |
| $\\operatorname{{Tr}}(\\rho_{{S|0}}P_0)$ | {repeat_p0:.12f} |
| erro de repetibilidade | {repeat_error:.12e} |

## Interpretação

Quando a sobreposição ambiental tende a zero, os termos de interferência
desaparecem, mas os pesos diagonais permanecem iguais aos pesos operacionais
de Born. O gap setorial fornece supressão exponencial assintótica. Após
condicionamento em um registro, a repetição ideal do mesmo projetor dá
probabilidade 1.

Isso ainda não seleciona sozinho o evento individual; a seleção ontológica
exige bacias reais do aparelho/ambiente.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
GDQ — Chapter 9 / Reduced S+A+E Model.

Classification:
    effective reduction of measurement. Not a calculation of the official Hessian.

Objective:
    Verify in a finite self-contained model:

    1. suppression of off-diagonal terms when environmental states
       associated with records become orthogonal;
    2. exponential decay of coherence by sectorial gap;
    3. ideal repeatability after conditioning on a record.

Internal source:
    - 09.4 - System, apparatus, environment and records.md
    - 09.6 - Decoherence, dynamical basins and unique outcome.md
    - notes/dynamical_basins_unique_outcome.md
    - notes/asymptotic_theorem_gdq_records.md

Output:
    manuscript/09_measurement_born_interface/scripts/output_simulate_decoherence_sae.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def projector(v: np.ndarray) -> np.ndarray:
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_simulate_decoherence_sae.md"

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

    # Reduced asymptotic model: |Gamma_01(tau)| <= C exp(-Delta tau).
    delta_meas = 1.75
    C = 1.0
    tau_values = np.array([0.0, 0.5, 1.0, 2.0, 4.0])
    gap_rows = [(tau, C * np.exp(-delta_meas * tau)) for tau in tau_values]

    # Ideal repeatability: conditioning on projector P0 makes repetition certain.
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
title: "Output — simulate S+A+E decoherence"
---

# Output — simulate S+A+E decoherence

Classification: effective reduction of measurement.

## Initial coefficients

- $|c_0|^2 = {abs(c0) ** 2:.12f}$
- $|c_1|^2 = {abs(c1) ** 2:.12f}$

## Suppression by environmental orthogonalization

| environmental overlap eta | reduced coherence | p0 | p1 |
|---:|---:|---:|---:|
{table}

## Decay by sectorial gap

Using $|\\Gamma_{{01}}(\\tau)|\\le C e^{{-\\Delta_{{\\rm meas}}\\tau}}$ with
$C={C:.3f}$ and $\\Delta_{{\\rm meas}}={delta_meas:.3f}$:

| tau | bound for $|\\Gamma_{{01}}|$ |
|---:|---:|
{gap_table}

## Ideal repeatability

After conditioning on record 0:

| test | value |
|---|---:|
| $p_0=\\operatorname{{Tr}}(\\rho_S P_0)$ | {p0:.12f} |
| $\\operatorname{{Tr}}(\\rho_{{S|0}}P_0)$ | {repeat_p0:.12f} |
| repeatability error | {repeat_error:.12e} |

## Interpretation

When the environmental overlap tends to zero, the interference terms
disappear, but the diagonal weights remain equal to the operational
Born weights. The sectorial gap provides asymptotic exponential suppression.
After conditioning on a record, the ideal repetition of the same projector gives
probability 1.

This still does not select the individual event on its own; ontological selection
requires real basins of the apparatus/environment.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

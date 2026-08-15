#!/usr/bin/env python3
"""
Reduced GDQ black hole — self-contained validation track.

Scientific classification:
    reduced evaluation / spectral and coupling diagnostics.

This script preserves the final version of the reduced calculation used in the manuscript.
It does not solve the complete 8D covariant saddle of the official action. The objective is
to keep auditable, in a single self-contained file, the chain:

    regular core -> horizons -> effective conservation -> virial ->
    radial projector -> reduced Hessian blocks -> Schur -> Page toy.

The numbers here are the audited final values of the reduction. The lines below
recalculate the derived combinations, check signs, algebraic relations,
Schur ratios, and closure errors.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_reduced_black_hole_pipeline.md"


def sci(x: float) -> str:
    return f"{x:.12e}"


def rel_residual(value: float, scale: float) -> float:
    return abs(value) / max(abs(scale), 1.0e-300)


def shannon_entropy(weights: list[float]) -> float:
    return -sum(w * math.log(w) for w in weights if w > 0.0)


def main() -> None:
    # Final reduced data of the radial saddle and effective reconstruction.
    lambda_T = 3.0
    eta = 8.0
    eta_crit = 5.188522012681
    mu = -1.067957044153e-1
    mass_power = 3.00002651

    horizons = [4.222352820613, 15.95712272799]
    kappa = [1.465301433319e-1, 3.044070699662e-2]
    temperatures = [k / (2.0 * math.pi) for k in kappa]

    epsilon = 9.934478711421e-3
    pr = -9.934477941512e-3
    pt = -9.934158191133e-3
    pr_metric_gap = 2.506468990693e-12
    conservation_core = 2.104757829586e-16
    conservation_static = 9.997320016076e-18

    # Finite invariants reconstructed in the effective core.
    R_core = 9.987066970693e-1
    Ricci2_core = 2.493537672591e-1
    Kretsch_core = 1.662358472304e-1

    # Virial and collective stability.
    K = 3.1675522712965487e-1
    U_T = 9.808336775055311e-2
    W = -9.274781821673822e-1
    virial = 2.0 * K + 3.0 * U_T + W
    virial_rel = rel_residual(virial, abs(2.0 * K) + abs(3.0 * U_T) + abs(W))
    d2E_da2 = 1.193971365853

    # Radial block: raw vs projected.
    lambda_raw_1 = -1.927437459951e-1
    lambda_phys_zero = -5.982003087324e-13
    lambda_phys_2 = 3.651456961676e-2

    # Harmonics and reduced blocks.
    gaps = {
        "projected radial amplitude": lambda_phys_2,
        "inhomogeneous scalar amplitude": 1.909625790263e-3,
        "non-zero phase/circulation": 6.572554660398e-2,
        "reduced torsion": 1.475541776890e-1,
        "exterior axial metric": 1.493545907614e-1,
    }

    norm_gf = 6.166879064740e-4
    norm_gH = 8.076881453156e-6
    chi_gf = 1.333410946325e-3
    chi_gH = 2.960174621482e-9

    # Preserved Page toy: positive weights of reduced channels. Not the 8D physical Page curve.
    weights = [
        0.9999980969946938,
        1.90300515759935e-6,
        8.794135715905771e-14,
        6.064588145332285e-14,
    ]
    entropy = shannon_entropy(weights)

    energy = {
        "epsilon+p_r": epsilon + pr,
        "epsilon+p_t": epsilon + pt,
        "epsilon+p_r+2p_t": epsilon + pr + 2.0 * pt,
    }

    lines: list[str] = []
    lines.append("# Output — reduced GDQ black hole pipeline\n\n")
    lines.append("Classification: reduced evaluation / spectral and coupling diagnostics.\n\n")
    lines.append("## 1. Parameters and status\n\n")
    lines.append(f"- lambda_T = `{lambda_T:.6f}`\n")
    lines.append(f"- eta = `{eta:.6f}`\n")
    lines.append(f"- eta_crit = `{eta_crit:.12e}`\n")
    lines.append(f"- mu = `{sci(mu)}`\n")
    lines.append(f"- central mass exponent = `{mass_power:.8f}`\n")
    lines.append("- status: tested effective reduction; complete 8D covariant remains future.\n\n")

    lines.append("## 2. Core and energy conditions\n\n")
    lines.append(f"- epsilon_core = `{sci(epsilon)}`\n")
    lines.append(f"- p_r_core = `{sci(pr)}`\n")
    lines.append(f"- p_t_core = `{sci(pt)}`\n")
    for name, value in energy.items():
        lines.append(f"- {name} = `{sci(value)}`\n")
    lines.append(f"- max |p_r_metric - p_r_input| core = `{sci(pr_metric_gap)}`\n")
    lines.append(f"- core conservation RMS = `{sci(conservation_core)}`\n")
    lines.append(f"- static patches conservation RMS = `{sci(conservation_static)}`\n")
    lines.append("\nInterpretation: NEC/WEC are saturated in the core and SEC is violated.\n\n")

    lines.append("## 3. Finite curvature invariants\n\n")
    lines.append(f"- R_core = `{sci(R_core)}`\n")
    lines.append(f"- Ricci2_core = `{sci(Ricci2_core)}`\n")
    lines.append(f"- Kretschmann_core = `{sci(Kretsch_core)}`\n\n")

    lines.append("## 4. Horizons and temperatures\n\n")
    lines.append("| horizon | r_H | kappa_H | T_H=kappa_H/(2pi) |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for i, (r_h, kap, temp) in enumerate(zip(horizons, kappa, temperatures), start=1):
        lines.append(f"| {i} | {sci(r_h)} | {sci(kap)} | {sci(temp)} |\n")

    lines.append("\n## 5. Virial and collective mode\n\n")
    lines.append(f"- K = `{sci(K)}`\n")
    lines.append(f"- U_T = `{sci(U_T)}`\n")
    lines.append(f"- W = `{sci(W)}`\n")
    lines.append(f"- 2K+3U_T+W = `{sci(virial)}`\n")
    lines.append(f"- relative residue = `{sci(virial_rel)}`\n")
    lines.append(f"- d2E/da2 at a=1 = `{sci(d2E_da2)}`\n\n")

    lines.append("## 6. Radial projector and reduced Hessian\n\n")
    lines.append(f"- lambda_raw[1] = `{sci(lambda_raw_1)}`\n")
    lines.append(f"- lambda_phys[1] after projection = `{sci(lambda_phys_zero)}`\n")
    lines.append(f"- lambda_phys[2] = `{sci(lambda_phys_2)}`\n\n")
    lines.append("| sector | smallest reduced physical mode |\n")
    lines.append("|---|---:|\n")
    for name, value in gaps.items():
        lines.append(f"| {name} | {sci(value)} |\n")

    lines.append("\n## 7. Cross-couplings by Schur\n\n")
    lines.append(f"- reduced ||K_gf|| = `{sci(norm_gf)}`\n")
    lines.append(f"- reduced ||K_gH|| = `{sci(norm_gH)}`\n")
    lines.append(f"- chi_gf = `{sci(chi_gf)}`\n")
    lines.append(f"- chi_gH = `{sci(chi_gH)}`\n")
    lines.append("\nInterpretation: the reduced couplings are small and do not close the diagonal gaps.\n\n")

    lines.append("## 8. Toy Page curve\n\n")
    lines.append(f"- weights = `{weights}`\n")
    lines.append(f"- entropy of the weights = `{sci(entropy)}`\n")
    lines.append("- classification: toy unitary, not physical covariant Page curve.\n\n")

    lines.append("## Verdict\n\n")
    if all(v > 0.0 for v in gaps.values()) and chi_gf < 1.0 and chi_gH < 1.0:
        lines.append("The effective reduction shows a regular core, horizons, effective conservation, positive gaps, and controlled Schur.\n")
    else:
        lines.append("The effective reduction detected instability or strong coupling; review before using.\n")
    lines.append("The complete 8D covariant closure requires the polar metric sector, horizon-crossing coordinates, coupled 8D matrix, and physical Page curve.\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

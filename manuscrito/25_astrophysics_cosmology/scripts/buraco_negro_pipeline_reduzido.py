#!/usr/bin/env python3
"""
Buraco negro GDQ reduzido — trilha autocontida de validação.

Classificação científica:
    avaliação reduzida / diagnóstico espectral e de acoplamentos.

Este script preserva a versão final do cálculo reduzido usado no manuscrito.
Ele não resolve a sela covariante 8D completa da ação oficial. O objetivo é
manter auditável, em um único arquivo autocontido, a cadeia:

    core regular -> horizontes -> conservação efetiva -> virial ->
    projetor radial -> blocos reduzidos da Hessiana -> Schur -> Page toy.

Os números aqui são os valores finais auditados da redução. As linhas abaixo
recalculam as combinações derivadas, checam sinais, relações algébricas,
razões de Schur e erros de fechamento.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_buraco_negro_pipeline_reduzido.md"


def sci(x: float) -> str:
    return f"{x:.12e}"


def rel_residual(value: float, scale: float) -> float:
    return abs(value) / max(abs(scale), 1.0e-300)


def shannon_entropy(weights: list[float]) -> float:
    return -sum(w * math.log(w) for w in weights if w > 0.0)


def main() -> None:
    # Dados reduzidos finais da sela radial e reconstrução efetiva.
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

    # Invariantes finitos reconstruídos no core efetivo.
    R_core = 9.987066970693e-1
    Ricci2_core = 2.493537672591e-1
    Kretsch_core = 1.662358472304e-1

    # Virial e estabilidade coletiva.
    K = 3.1675522712965487e-1
    U_T = 9.808336775055311e-2
    W = -9.274781821673822e-1
    virial = 2.0 * K + 3.0 * U_T + W
    virial_rel = rel_residual(virial, abs(2.0 * K) + abs(3.0 * U_T) + abs(W))
    d2E_da2 = 1.193971365853

    # Bloco radial: bruto vs projetado.
    lambda_raw_1 = -1.927437459951e-1
    lambda_phys_zero = -5.982003087324e-13
    lambda_phys_2 = 3.651456961676e-2

    # Harmônicos e blocos reduzidos.
    gaps = {
        "amplitude radial projetada": lambda_phys_2,
        "amplitude escalar nao homogenea": 1.909625790263e-3,
        "fase/circulacao nao-zero": 6.572554660398e-2,
        "torcao reduzida": 1.475541776890e-1,
        "metrico axial exterior": 1.493545907614e-1,
    }

    norm_gf = 6.166879064740e-4
    norm_gH = 8.076881453156e-6
    chi_gf = 1.333410946325e-3
    chi_gH = 2.960174621482e-9

    # Page toy: canais positivos da redução. Não é a Page curve física 8D.
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
    lines.append("# Saída — pipeline reduzido de buraco negro GDQ\n\n")
    lines.append("Classificação: avaliação reduzida / diagnóstico espectral e de acoplamentos.\n\n")
    lines.append("## 1. Parâmetros e status\n\n")
    lines.append(f"- lambda_T = `{lambda_T:.6f}`\n")
    lines.append(f"- eta = `{eta:.6f}`\n")
    lines.append(f"- eta_crit = `{eta_crit:.12e}`\n")
    lines.append(f"- mu = `{sci(mu)}`\n")
    lines.append(f"- expoente central de massa = `{mass_power:.8f}`\n")
    lines.append("- status: redução efetiva testada; covariante 8D completo permanece futuro.\n\n")

    lines.append("## 2. Core e condições de energia\n\n")
    lines.append(f"- epsilon_core = `{sci(epsilon)}`\n")
    lines.append(f"- p_r_core = `{sci(pr)}`\n")
    lines.append(f"- p_t_core = `{sci(pt)}`\n")
    for name, value in energy.items():
        lines.append(f"- {name} = `{sci(value)}`\n")
    lines.append(f"- max |p_r_metric - p_r_input| core = `{sci(pr_metric_gap)}`\n")
    lines.append(f"- RMS conservação core = `{sci(conservation_core)}`\n")
    lines.append(f"- RMS conservação patches estáticos = `{sci(conservation_static)}`\n")
    lines.append("\nInterpretação: NEC/WEC são saturadas no core e SEC é violada.\n\n")

    lines.append("## 3. Invariantes de curvatura finitos\n\n")
    lines.append(f"- R_core = `{sci(R_core)}`\n")
    lines.append(f"- Ricci2_core = `{sci(Ricci2_core)}`\n")
    lines.append(f"- Kretschmann_core = `{sci(Kretsch_core)}`\n\n")

    lines.append("## 4. Horizontes e temperaturas\n\n")
    lines.append("| horizonte | r_H | kappa_H | T_H=kappa_H/(2pi) |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for i, (r_h, kap, temp) in enumerate(zip(horizons, kappa, temperatures), start=1):
        lines.append(f"| {i} | {sci(r_h)} | {sci(kap)} | {sci(temp)} |\n")

    lines.append("\n## 5. Virial e modo coletivo\n\n")
    lines.append(f"- K = `{sci(K)}`\n")
    lines.append(f"- U_T = `{sci(U_T)}`\n")
    lines.append(f"- W = `{sci(W)}`\n")
    lines.append(f"- 2K+3U_T+W = `{sci(virial)}`\n")
    lines.append(f"- resíduo relativo = `{sci(virial_rel)}`\n")
    lines.append(f"- d2E/da2 em a=1 = `{sci(d2E_da2)}`\n\n")

    lines.append("## 6. Projetor radial e Hessiana reduzida\n\n")
    lines.append(f"- lambda_raw[1] = `{sci(lambda_raw_1)}`\n")
    lines.append(f"- lambda_phys[1] após projeção = `{sci(lambda_phys_zero)}`\n")
    lines.append(f"- lambda_phys[2] = `{sci(lambda_phys_2)}`\n\n")
    lines.append("| setor | menor modo físico reduzido |\n")
    lines.append("|---|---:|\n")
    for name, value in gaps.items():
        lines.append(f"| {name} | {sci(value)} |\n")

    lines.append("\n## 7. Acoplamentos cruzados por Schur\n\n")
    lines.append(f"- ||K_gf|| reduzido = `{sci(norm_gf)}`\n")
    lines.append(f"- ||K_gH|| reduzido = `{sci(norm_gH)}`\n")
    lines.append(f"- chi_gf = `{sci(chi_gf)}`\n")
    lines.append(f"- chi_gH = `{sci(chi_gH)}`\n")
    lines.append("\nInterpretação: os acoplamentos reduzidos são pequenos e não fecham os gaps diagonais.\n\n")

    lines.append("## 8. Page toy\n\n")
    lines.append(f"- pesos = `{weights}`\n")
    lines.append(f"- entropia dos pesos = `{sci(entropy)}`\n")
    lines.append("- classificação: toy unitário, não Page curve física covariante.\n\n")

    lines.append("## Veredito\n\n")
    if all(v > 0.0 for v in gaps.values()) and chi_gf < 1.0 and chi_gH < 1.0:
        lines.append("A redução efetiva mostra core regular, horizontes, conservação efetiva, gaps positivos e Schur controlado.\n")
    else:
        lines.append("A redução efetiva detectou instabilidade ou acoplamento forte; revisar antes de usar.\n")
    lines.append("O fechamento covariante 8D completo exige setor métrico polar, coordenadas atravessantes de horizonte, matriz acoplada 8D e Page curve física.\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

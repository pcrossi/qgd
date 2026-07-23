#!/usr/bin/env python3
"""
Q53 — execução reduzida do plano de massas/escalas inerciais neutras.

Classificação:
- avaliação direta de uma cadeia GDQ reduzida/candidata;
- não substitui a Hessiana neutra 8D completa;
- não usa Delta m^2 como entrada.

Entradas GDQ usadas:
- canal beta neutro já identificado em Q50;
- escala beta neutra S_nu = alpha^7 Q_beta^2;
- impedância neutra legada chi_nu = 0.48 exp(-alpha/4);
- terceiro autovalor geométrico candidato lambda_3 = 6*pi/5.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


OUT = Path("questoes/q53/associados")
OUT.mkdir(parents=True, exist_ok=True)


alpha = 1.0 / 137.035999177
Q_beta_eV = 0.782333559310e6

# NuFIT 6.0, NO, IC19 sem SK-atm. Referência externa para comparação.
ref = {
    "theta12_deg": 33.68,
    "theta23_deg": 48.5,
    "theta13_deg": 8.52,
    "delta_cp_deg": 177.0,
    "dm21": 7.49e-5,
    "dm31": 2.534e-3,
}


def pmns(theta12: float, theta23: float, theta13: float, delta: float) -> np.ndarray:
    c12, s12 = math.cos(theta12), math.sin(theta12)
    c23, s23 = math.cos(theta23), math.sin(theta23)
    c13, s13 = math.cos(theta13), math.sin(theta13)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * e_minus],
            [
                -s12 * c23 - c12 * s23 * s13 * e_plus,
                c12 * c23 - s12 * s23 * s13 * e_plus,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * e_plus,
                -c12 * s23 - s12 * c23 * s13 * e_plus,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


chi_nu = 0.48 * math.exp(-alpha / 4.0)

# Ângulos crus do legado, usados somente para montar a matriz folha--modo.
theta12 = math.atan(1.0 / math.sqrt(2.0))
theta23 = math.pi / 4.0
theta13 = math.asin(chi_nu / math.pi)
delta_cp = 3.84
U_gdq = pmns(theta12, theta23, theta13, delta_cp)

# Gram reduzido: a base é tomada ortonormal após normalização por G^nu.
# Isso é uma escolha de execução reduzida; na Hessiana completa G^nu deve ser
# calculado por integral ponderada.
G = np.eye(3)

# Escala beta neutra: usa a supressão alpha^7 do canal torsional neutro e o
# endpoint de energia disponível do decaimento beta. Não usa dados de oscilação.
S_nu_eV2 = alpha**7 * Q_beta_eV**2

# Espectro reduzido candidato:
# lambda_1 = 0: modo neutro base sem estômato;
# lambda_2 = chi_nu^2/2: primeira quebra por impedância/leakage neutro;
# lambda_3 = 6*pi/5: candidato geométrico global de fechamento 6/5 do canal
#                    de folhas/toro. Esse é o ponto que precisa de derivação
#                    variacional para virar previsão forte.
lambda_vals = np.array([0.0, 0.5 * chi_nu**2, 6.0 * math.pi / 5.0])

dm21_gdq = S_nu_eV2 * (lambda_vals[1] - lambda_vals[0])
dm31_gdq = S_nu_eV2 * (lambda_vals[2] - lambda_vals[0])
masses_no = np.sqrt(S_nu_eV2 * lambda_vals)

# Bloco K^nu em base de folhas: K = G U Lambda U^\dagger G,
# com G=I no reduzido.
K = U_gdq @ np.diag(lambda_vals) @ U_gdq.conj().T
herm_err = np.linalg.norm(K - K.conj().T)
unitarity_err = np.linalg.norm(U_gdq.conj().T @ U_gdq - np.eye(3))

np.savez(
    OUT / "dados_execucao_massas_neutras_q53.npz",
    alpha=alpha,
    Q_beta_eV=Q_beta_eV,
    chi_nu=chi_nu,
    theta_deg=np.array([math.degrees(theta12), math.degrees(theta23), math.degrees(theta13), math.degrees(delta_cp)]),
    U_gdq=U_gdq,
    G=G,
    K=K,
    lambda_vals=lambda_vals,
    S_nu_eV2=S_nu_eV2,
    masses_no=masses_no,
    dm21_gdq=dm21_gdq,
    dm31_gdq=dm31_gdq,
)


def rel_err(x: float, y: float) -> float:
    return (x - y) / y


md = OUT / "saida_execucao_massas_neutras_q53.md"
with md.open("w", encoding="utf-8") as f:
    f.write("# Q53 — Execução reduzida do plano de massas neutras\n\n")
    f.write("## Classificação\n\n")
    f.write("Avaliação direta de uma cadeia GDQ reduzida/candidata. Não é ainda a Hessiana neutra 8D completa.\n\n")
    f.write("## Entradas GDQ congeladas antes da comparação\n\n")
    f.write(f"- `alpha = {alpha:.15e}`\n")
    f.write(f"- `Q_beta = {Q_beta_eV:.12e} eV`\n")
    f.write(f"- `S_nu = alpha^7 Q_beta^2 = {S_nu_eV2:.12e} eV^2`\n")
    f.write(f"- `chi_nu = 0.48 exp(-alpha/4) = {chi_nu:.12e}`\n")
    f.write("- espectro reduzido candidato:\n\n")
    f.write("$$\n")
    f.write("\\lambda = \\left(0,\\frac{\\chi_\\nu^2}{2},\\frac{6\\pi}{5}\\right).\n")
    f.write("$$\n\n")
    f.write("O fator $6\\pi/5$ é o ponto ainda condicional: precisa ser derivado da Hessiana/colagem neutra para virar previsão forte.\n\n")

    f.write("## Autovalores geométricos\n\n")
    f.write("| i | lambda_i |\n|---:|---:|\n")
    for i, lam in enumerate(lambda_vals, start=1):
        f.write(f"| {i} | {lam:.12e} |\n")

    f.write("\n## Escalas inerciais neutras resultantes\n\n")
    f.write("| modo | massa reduzida GDQ (eV) |\n|---:|---:|\n")
    for i, m in enumerate(masses_no, start=1):
        f.write(f"| {i} | {m:.12e} |\n")
    f.write(f"| soma | {masses_no.sum():.12e} |\n")

    f.write("\n## Diferenças quadradas\n\n")
    f.write("| quantidade | GDQ reduzido | NuFIT 6.0 NO | erro relativo |\n|---|---:|---:|---:|\n")
    f.write(f"| dm21 | {dm21_gdq:.12e} | {ref['dm21']:.12e} | {rel_err(dm21_gdq, ref['dm21']):+.6e} |\n")
    f.write(f"| dm31 | {dm31_gdq:.12e} | {ref['dm31']:.12e} | {rel_err(dm31_gdq, ref['dm31']):+.6e} |\n")

    f.write("\n## Matriz folha--modo usada\n\n")
    f.write("| parâmetro | valor |\n|---|---:|\n")
    f.write(f"| theta12 | {math.degrees(theta12):.9f} deg |\n")
    f.write(f"| theta23 | {math.degrees(theta23):.9f} deg |\n")
    f.write(f"| theta13 | {math.degrees(theta13):.9f} deg |\n")
    f.write(f"| delta_CP legado | {math.degrees(delta_cp):.9f} deg |\n")
    f.write(f"| erro unitariedade | {unitarity_err:.3e} |\n")

    f.write("\n## Bloco K^nu reduzido reconstruído\n\n")
    f.write(f"- erro hermiticidade: `{herm_err:.3e}`\n\n")
    f.write("Parte real:\n\n")
    for row in K.real:
        f.write("- " + "  ".join(f"{x:.12e}" for x in row) + "\n")
    f.write("\nParte imaginária:\n\n")
    for row in K.imag:
        f.write("- " + "  ".join(f"{x:.12e}" for x in row) + "\n")

    f.write("\n## Veredito da execução\n\n")
    f.write("A cadeia reduzida produz a ordem correta e excelente acordo em `dm31`; `dm21` fica a poucos por cento.\n")
    f.write("A pendência física é derivar diretamente o autovalor superior `6*pi/5` e a primeira quebra `chi_nu^2/2` da Hessiana neutra oficial.\n")
    f.write("Até essa derivação, o resultado é candidato GDQ reduzido, não fechamento metrológico final.\n")

print(md)

#!/usr/bin/env python3
"""Q53 — sensibilidade dos coeficientes reduzidos das escalas neutras."""

import math
from pathlib import Path


OUT = Path("questoes/q53/associados")

alpha = 1.0 / 137.035999177
Q_beta_eV = 0.782333559310e6
dm21_ref = 7.49e-5
dm31_ref = 2.534e-3

S = alpha**7 * Q_beta_eV**2
chi0 = 12.0 / 25.0
chi = chi0 * math.exp(-alpha / 4.0)
lambda2 = 0.5 * chi**2
lambda3 = 6.0 * math.pi / 5.0

lambda2_req = dm21_ref / S
lambda3_req = dm31_ref / S

rows = [
    ("lambda2 requerido", lambda2_req, ""),
    ("lambda2 GDQ reduzido", lambda2, ""),
    ("lambda2 erro rel", (lambda2 - lambda2_req) / lambda2_req, ""),
    ("lambda3 requerido", lambda3_req, ""),
    ("lambda3 6pi/5", lambda3, ""),
    ("lambda3 erro rel", (lambda3 - lambda3_req) / lambda3_req, ""),
    ("chi requerido para dm21", math.sqrt(2.0 * lambda2_req), ""),
    ("chi GDQ", chi, ""),
    ("fator axial requerido lambda3/(2pi)", lambda3_req / (2.0 * math.pi), ""),
    ("fator axial GDQ 3/5", 3.0 / 5.0, ""),
]

md = OUT / "saida_sensibilidade_coeficientes_q53.md"
with md.open("w", encoding="utf-8") as f:
    f.write("# Q53 — Sensibilidade dos coeficientes neutros\n\n")
    f.write("## Escala fixa\n\n")
    f.write(f"- `S_nu = alpha^7 Q_beta^2 = {S:.12e} eV^2`\n\n")
    f.write("## Coeficientes requeridos versus GDQ reduzido\n\n")
    f.write("| item | valor |\n|---|---:|\n")
    for name, val, _ in rows:
        f.write(f"| {name} | {val:.12e} |\n")
    f.write("\n## Leitura\n\n")
    f.write("- O coeficiente superior requerido corresponde a `lambda3/(2pi) = ")
    f.write(f"{lambda3_req/(2*math.pi):.12e}`, próximo de `3/5 = 0.6`.\n")
    f.write("- O coeficiente GDQ `6pi/5` gera erro relativo de ")
    f.write(f"{(lambda3-lambda3_req)/lambda3_req:+.6e} em `dm31`.\n")
    f.write("- O canal `chi=(12/25)exp(-alpha/4)` gera erro relativo de ")
    f.write(f"{(lambda2-lambda2_req)/lambda2_req:+.6e} em `dm21`.\n")
    f.write("- Portanto, o gargalo principal é derivar o bloco bicanal de interface que corrige `lambda2`, não o modo superior.\n")

print(md)

#!/usr/bin/env python3
"""
GDQ — Capítulo 2 / Mapa Perelman--Madelung local.

Objetivo:
    Verificar, em casos numéricos simples e sem alvo experimental, três fatos:

    1. o mapa direto/inverso entre f e (rho, S_R) é exato no domínio rho > 0;
    2. a presença de rho = 0 torna f = -log(rho) + i S_R/hbar singular;
    3. a superposição é linear em Psi, não nos pares (rho, S_R).

Fonte teórica:
    manuscrito/02_geometrization/02.4 - Campo complexo, densidade e fase.md
    manuscrito/notes/geometrization/Mapa Perelman-Madelung local e limites.md

Classificação:
    Teste simbólico/numérico de identidade constitutiva e não linearidade
    da transformação de Madelung. Não é previsão física.

Equações:
    rho = exp(-(f + fbar)/2)
    S_R = hbar(f - fbar)/(2i)
    f = -log(rho) + i S_R/hbar
    Psi = sqrt(rho) exp(i S_R/hbar)

Domínio e contorno:
    Checagem pontual em domínio regular rho > 0; não há operador diferencial.

Parâmetros:
    Universais:
        hbar > 0, usado como unidade simbólica.
    Dados de aparelho/experimento:
        nenhum.
    Numéricos:
        pares arbitrários (rho, S_R) e fases arbitrárias.

Saída:
    saida_verificar_mapa_perelman_madelung.md
"""

from __future__ import annotations

from pathlib import Path
import cmath
import math


OUT = Path(__file__).resolve().parent


def forward_inverse_case(rho: float, s_r: float, hbar: float = 1.0) -> dict[str, float]:
    """Testa f -> (rho,S_R) -> f em um ponto regular."""
    f = -math.log(rho) + 1j * s_r / hbar
    fbar = f.conjugate()
    rho_back = cmath.exp(-(f + fbar) / 2.0).real
    sr_back = (hbar * (f - fbar) / (2j)).real
    f_back = -math.log(rho_back) + 1j * sr_back / hbar
    return {
        "rho": rho,
        "S_R": s_r,
        "rho_back": rho_back,
        "S_R_back": sr_back,
        "err_rho": abs(rho - rho_back),
        "err_SR": abs(s_r - sr_back),
        "err_f": abs(f - f_back),
    }


def superposition_case(rho1: float, s1: float, rho2: float, s2: float, hbar: float = 1.0) -> dict[str, float]:
    """Mostra que rho(Psi1+Psi2) não é rho1+rho2 em geral."""
    psi1 = math.sqrt(rho1) * cmath.exp(1j * s1 / hbar)
    psi2 = math.sqrt(rho2) * cmath.exp(1j * s2 / hbar)
    psi = psi1 + psi2
    rho_super = abs(psi) ** 2
    rho_naive = rho1 + rho2
    interference = 2.0 * math.sqrt(rho1 * rho2) * math.cos((s1 - s2) / hbar)
    phase = hbar * cmath.phase(psi)
    return {
        "rho1": rho1,
        "rho2": rho2,
        "delta_phase": (s1 - s2) / hbar,
        "rho_super": rho_super,
        "rho_naive": rho_naive,
        "interference": interference,
        "phase": phase,
        "check_error": abs(rho_super - (rho_naive + interference)),
    }


def main() -> None:
    regular_rows = [
        forward_inverse_case(0.2, 0.7),
        forward_inverse_case(1.5, -1.2),
        forward_inverse_case(3.0, 2.4),
    ]
    sup_rows = [
        superposition_case(1.0, 0.0, 1.0, math.pi),
        superposition_case(1.0, 0.0, 1.0, math.pi / 2.0),
        superposition_case(0.7, 0.3, 0.2, -0.8),
    ]
    ok_regular = all(r["err_rho"] < 1e-14 and r["err_SR"] < 1e-14 and r["err_f"] < 1e-14 for r in regular_rows)
    ok_super = all(r["check_error"] < 1e-14 for r in sup_rows)

    lines: list[str] = []
    lines.append("# Saída — mapa Perelman--Madelung local\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico/numérico de identidade constitutiva e não linearidade de Madelung. Não é previsão física.\n\n")

    lines.append("## 1. Mapa direto e inverso no domínio $\\rho>0$\n\n")
    lines.append("| $\\rho$ | $S_R$ | $\\rho$ reconstruída | $S_R$ reconstruído | erro $\\rho$ | erro $S_R$ | erro $f$ |\n")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in regular_rows:
        lines.append(
            f"| {r['rho']:.12g} | {r['S_R']:.12g} | {r['rho_back']:.12g} | "
            f"{r['S_R_back']:.12g} | {r['err_rho']:.3e} | {r['err_SR']:.3e} | {r['err_f']:.3e} |\n"
        )

    lines.append("\n## 2. Nó $\\rho=0$\n\n")
    lines.append("No mapa inverso, $f=-\\ln\\rho+iS_R/\\hbar$. Para $\\rho=0$, $\\ln\\rho$ diverge. Portanto o nó não pertence ao domínio regular.\n\n")

    lines.append("## 3. Superposição\n\n")
    lines.append("A verificação usa:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{12}=|\\Psi_1+\\Psi_2|^2=\\rho_1+\\rho_2+2\\sqrt{\\rho_1\\rho_2}\\cos((S_1-S_2)/\\hbar).\n")
    lines.append("$$\n\n")
    lines.append("| $\\rho_1$ | $\\rho_2$ | $\\Delta S/\\hbar$ | $|\\Psi_1+\\Psi_2|^2$ | $\\rho_1+\\rho_2$ | interferência | erro identidade |\n")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in sup_rows:
        lines.append(
            f"| {r['rho1']:.12g} | {r['rho2']:.12g} | {r['delta_phase']:.12g} | "
            f"{r['rho_super']:.12g} | {r['rho_naive']:.12g} | {r['interference']:.12g} | {r['check_error']:.3e} |\n"
        )

    lines.append("\n## Veredito\n\n")
    if ok_regular and ok_super:
        lines.append("As checagens passaram: o mapa é localmente invertível em $\\rho>0$ e a superposição é não linear em $(\\rho,S_R)$.\n")
    else:
        lines.append("Alguma checagem falhou.\n")
    lines.append("\nNenhum alvo experimental foi usado.\n")

    out = OUT / "saida_verificar_mapa_perelman_madelung.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

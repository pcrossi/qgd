#!/usr/bin/env python3
"""
GDQ — Capítulo 2 / Decomposição do campo f.

Objetivo:
    Verificar simbolicamente as identidades constitutivas
    rho = exp(-(f + fbar)/2) e S_R = hbar(f - fbar)/(2i),
    usando a parametrização f = -S_I/hbar + i S_R/hbar.

Fonte teórica:
    manuscrito/02_geometrization/02.4 - Campo complexo, densidade e fase.md
    manuscrito/notes/geometrization/Decomposição do campo f em densidade e fase.md

Classificação:
    Teste simbólico de identidade constitutiva. Não é previsão física.

Equação:
    f = -S_I/hbar + i S_R/hbar
    fbar = -S_I/hbar - i S_R/hbar
    rho = exp(-(f + fbar)/2)
    S_R = hbar(f - fbar)/(2i)

Domínio e contorno:
    Checagem algébrica pontual; sem operador diferencial.

Parâmetros:
    Universais:
        hbar > 0 simbólico
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        nenhum

Saída:
    saida_verificar_decomposicao_f_symbolic.md

Observação:
    Nenhum alvo experimental é usado.
"""

from __future__ import annotations

from pathlib import Path
import cmath
import math


OUT = Path(__file__).resolve().parent


def check_case(hbar: float, s_i: float, s_r: float) -> dict[str, float | complex]:
    """Avalia uma instância numérica arbitrária da identidade algébrica."""
    f = -s_i / hbar + 1j * s_r / hbar
    fbar = f.conjugate()
    rho_from_f = cmath.exp(-(f + fbar) / 2).real
    rho_expected = math.exp(s_i / hbar)
    sr_from_f = (hbar * (f - fbar) / (2j)).real
    return {
        "hbar": hbar,
        "S_I": s_i,
        "S_R": s_r,
        "f": f,
        "rho_from_f": rho_from_f,
        "rho_expected": rho_expected,
        "S_R_from_f": sr_from_f,
        "err_rho": abs(rho_from_f - rho_expected),
        "err_SR": abs(sr_from_f - s_r),
    }


def main() -> None:
    rows = [
        check_case(1.0, -0.3, 0.7),
        check_case(2.0, 1.1, -0.4),
        check_case(0.5, 0.2, 1.3),
    ]
    ok = all(float(r["err_rho"]) < 1e-14 and float(r["err_SR"]) < 1e-14 for r in rows)

    lines: list[str] = []
    lines.append("# Saída — verificação da decomposição de $f$\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico de identidade constitutiva. Não é previsão física.\n\n")
    lines.append("## Identidades verificadas\n\n")
    lines.append("$$\n")
    lines.append("f=-\\frac{S_I}{\\hbar}+i\\frac{S_R}{\\hbar},\n")
    lines.append("\\qquad\n")
    lines.append("\\bar f=-\\frac{S_I}{\\hbar}-i\\frac{S_R}{\\hbar}.\n")
    lines.append("$$\n\n")
    lines.append("Daí:\n\n")
    lines.append("$$\n")
    lines.append("\\rho=e^{-(f+\\bar f)/2}=e^{S_I/\\hbar}\n")
    lines.append("$$\n\n")
    lines.append("e\n\n")
    lines.append("$$\n")
    lines.append("S_R=\\frac{\\hbar}{2i}(f-\\bar f).\n")
    lines.append("$$\n\n")
    lines.append("## Casos numéricos arbitrários\n\n")
    lines.append("| $\\hbar$ | $S_I$ | $S_R$ | $\\rho(f)$ | $e^{S_I/\\hbar}$ | erro $\\rho$ | erro $S_R$ |\n")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in rows:
        lines.append(
            f"| {float(r['hbar']):.6g} | {float(r['S_I']):.6g} | "
            f"{float(r['S_R']):.6g} | {float(r['rho_from_f']):.12g} | "
            f"{float(r['rho_expected']):.12g} | {float(r['err_rho']):.3e} | "
            f"{float(r['err_SR']):.3e} |\n"
        )
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída verifica apenas a identidade constitutiva. ")
    lines.append("Ela não deriva a ação oficial nem a dinâmica de $f$.\n")

    out = OUT / "saida_verificar_decomposicao_f_symbolic.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()


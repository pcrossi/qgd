#!/usr/bin/env python3
"""
Q51 — benchmark reduzido de decaimento alfa.

Classificação:
    - teste de consistência / comparação fenomenológica;
    - NÃO é previsão cega, pois a frequência de tentativa e a métrica
      exponencial ainda não foram derivadas diretamente da Hessiana GDQ.

Objetivo:
    Comparar:
      1. Gamow com nu0 fixo;
      2. métrica exponencial legada com nu0 fixo;
      3. Gamow com frequência interna reduzida;
      4. métrica exponencial legada com frequência interna reduzida.

    O dataset abaixo é diagnóstico e deve ser substituído por tabela auditada
    NUBASE/AME antes de qualquer conclusão metrológica.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


HBAR_C = 197.3269804  # MeV fm
ALPHA = 1.0 / 137.035999084
M_ALPHA = 3727.3794066  # MeV/c^2
U_TO_MEV = 931.49410242
YEAR_S = 365.25 * 24.0 * 3600.0
C_FM_S = 2.99792458e23  # fm/s
OUT = Path(__file__).resolve().parent / "saida_benchmark_alpha_q51.md"


@dataclass(frozen=True)
class AlphaCase:
    name: str
    A_parent: int
    Z_parent: int
    q_alpha_mev: float
    half_life_s: float


CASES = [
    # Valores de uso diagnóstico. Trocar por tabela NUBASE/AME auditada.
    AlphaCase("U-238", 238, 92, 4.26975, 4.468e9 * YEAR_S),
    AlphaCase("U-234", 234, 92, 4.858, 2.455e5 * YEAR_S),
    AlphaCase("U-232", 232, 92, 5.414, 68.9 * YEAR_S),
    AlphaCase("Th-232", 232, 90, 4.083, 1.405e10 * YEAR_S),
    AlphaCase("Ra-226", 226, 88, 4.871, 1600.0 * YEAR_S),
    AlphaCase("Po-212", 212, 84, 8.954, 2.99e-7),
]


def reduced_mass_mev(A_parent: int) -> float:
    """Reduced mass alpha-daughter in MeV/c^2."""
    a_d = A_parent - 4
    m_d = a_d * U_TO_MEV
    return M_ALPHA * m_d / (M_ALPHA + m_d)


def nuclear_radius_fm(A_parent: int, r0: float = 1.20) -> float:
    """Touching radius alpha + daughter."""
    a_d = A_parent - 4
    return r0 * (a_d ** (1.0 / 3.0) + 4.0 ** (1.0 / 3.0))


def coulomb_mev_fm(Z_parent: int) -> float:
    """Coulomb constant C such that V=C/r, daughter charge times alpha charge."""
    z_d = Z_parent - 2
    return 2.0 * z_d * ALPHA * HBAR_C


def simpson_integral(func, a: float, b: float, n: int = 20000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        s += (4.0 if i % 2 else 2.0) * func(x)
    return s * h / 3.0


def action_w(case: AlphaCase, geometric: bool = False) -> float:
    mu = reduced_mass_mev(case.A_parent)
    c = coulomb_mev_fm(case.Z_parent)
    q = case.q_alpha_mev
    r1 = nuclear_radius_fm(case.A_parent)
    r2 = c / q
    if r2 <= r1:
        return 0.0

    def integrand(r: float) -> float:
        v_minus_q = c / r - q
        if v_minus_q <= 0:
            return 0.0
        base = math.sqrt(2.0 * mu * v_minus_q) / HBAR_C
        if not geometric:
            return base
        g_rr = math.exp(-(ALPHA ** 2) * (c / r) / q)
        return base * math.sqrt(g_rr)

    return 2.0 * simpson_integral(integrand, r1, r2)


def half_life_from_action(w: float, nu0: float) -> float:
    return math.log(2.0) / nu0 * math.exp(w)


def internal_attempt_frequency(case: AlphaCase) -> float:
    """Reduced internal attempt frequency v/(2R).

    Classification: reduced GDQ-inspired estimate. It is not yet the final
    Hessian eigenfrequency, but it removes the isotope-independent constant
    nu0 and uses only the channel kinematics and the finite nuclear boundary.
    """
    mu = reduced_mass_mev(case.A_parent)
    beta = math.sqrt(2.0 * case.q_alpha_mev / mu)
    radius = nuclear_radius_fm(case.A_parent)
    return C_FM_S * beta / (2.0 * radius)


def rms_log10(pred, exp) -> float:
    diffs = [math.log10(p) - math.log10(e) for p, e in zip(pred, exp)]
    return math.sqrt(sum(d * d for d in diffs) / len(diffs))


def build_report() -> str:
    # Frequência efetiva legada. Na Q51 final deve sair da Hessiana interna.
    nu0 = 1.0e21
    models = {
        "Gamow_nu0": [],
        "GDQexp_nu0": [],
        "Gamow_nu_int": [],
        "GDQexp_nu_int": [],
    }
    exp = []
    rows = []

    for c in CASES:
        w0 = action_w(c, geometric=False)
        wg = action_w(c, geometric=True)
        nu_int = internal_attempt_frequency(c)
        t_gamow_nu0 = half_life_from_action(w0, nu0)
        t_gdq_nu0 = half_life_from_action(wg, nu0)
        t_gamow_nu_int = half_life_from_action(w0, nu_int)
        t_gdq_nu_int = half_life_from_action(wg, nu_int)
        models["Gamow_nu0"].append(t_gamow_nu0)
        models["GDQexp_nu0"].append(t_gdq_nu0)
        models["Gamow_nu_int"].append(t_gamow_nu_int)
        models["GDQexp_nu_int"].append(t_gdq_nu_int)
        exp.append(c.half_life_s)
        rows.append(
            (
                c.name,
                c.q_alpha_mev,
                math.log10(c.half_life_s),
                math.log10(t_gamow_nu0),
                math.log10(t_gdq_nu0),
                math.log10(t_gamow_nu_int),
                math.log10(t_gdq_nu_int),
                nu_int,
                w0,
                math.log(c.half_life_s * nu_int / math.log(2.0)),
            )
        )

    rms = {name: rms_log10(vals, exp) for name, vals in models.items()}
    base = rms["Gamow_nu0"]

    lines = []
    lines.append("# Saída — benchmark reduzido Q51\n")
    lines.append("Classificação: teste de consistência/comparação fenomenológica.\n")
    lines.append(
        "A frequência interna reduzida ainda não é a frequência final da "
        "Hessiana; é a primeira substituição não ajustável de `nu0`.\n"
    )
    lines.append(f"- alpha = `{ALPHA:.15e}`\n")
    lines.append(f"- nu0 efetivo legado = `{nu0:.6e} s^-1`\n")
    lines.append(
        "- frequência interna usada: "
        "`nu_int = c sqrt(2 Q_alpha/mu)/(2 R_N)`\n"
    )
    lines.append(
        "| Núcleo | Q_alpha (MeV) | log10 T_exp | Gamow nu0 | GDQexp nu0 | "
        "Gamow nu_int | GDQexp nu_int | nu_int (s^-1) | Delta W_req | S_alpha_eff |\n"
    )
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n")
    for row in rows:
        delta_w_req = row[9] - row[8]
        s_alpha_eff = math.exp(-delta_w_req)
        lines.append(
            f"| {row[0]} | {row[1]:.5f} | {row[2]:.6f} | "
            f"{row[3]:.6f} | {row[4]:.6f} | {row[5]:.6f} | "
            f"{row[6]:.6f} | {row[7]:.6e} | {delta_w_req:.6f} | "
            f"{s_alpha_eff:.6f} |\n"
        )
    lines.append("\n")
    lines.append("| Modelo | RMS décadas | Melhoria contra Gamow nu0 |\n")
    lines.append("| --- | ---: | ---: |\n")
    for name in ("Gamow_nu0", "GDQexp_nu0", "Gamow_nu_int", "GDQexp_nu_int"):
        improvement = 1.0 - rms[name] / base if base else float("nan")
        lines.append(f"| {name} | {rms[name]:.6f} | {100.0 * improvement:.3f}% |\n")
    lines.append("\n")
    lines.append("## Veredito numérico\n\n")
    lines.append(
        "A troca de `nu0` constante por `nu_int` melhora levemente a série, "
        "sem usar alvo experimental núcleo por núcleo.\n\n"
    )
    lines.append(
        "A métrica exponencial legada com expoente `alpha^2 V/Q` continua "
        "não produzindo melhora estatística. Portanto, o próximo avanço real "
        "deve vir da impedância Schur/DtN alfa--núcleo e não apenas do ansatz "
        "exponencial.\n"
    )
    lines.append("\n")
    lines.append("## Diagnóstico do termo faltante\n\n")
    lines.append(
        "`Delta W_req` é a correção de ação necessária para que Gamow com "
        "`nu_int` coincida com a meia-vida experimental. Ela não foi usada "
        "como ajuste; serve apenas para dimensionar o canal Schur/DtN ausente.\n\n"
    )
    lines.append(
        "O padrão não é uma constante universal: U-238 e Th-232 já exigem "
        "correções muito pequenas, enquanto Po-212 exige correção maior. Isso "
        "indica dependência de estrutura nuclear/deformação/canal de contorno.\n"
    )
    lines.append("\n")
    lines.append(
        "`S_alpha_eff=exp(-Delta W_req)` é a leitura de overlap/preformação "
        "efetiva que a Hessiana de superfície deve substituir por uma "
        "previsão direta. Valores maiores que 1 indicam que a frequência, o "
        "raio ou o dataset diagnóstico ainda precisam refinamento; não devem "
        "ser interpretados literalmente como probabilidade.\n"
    )
    return "".join(lines)


def main() -> None:
    report = build_report()
    print(report)
    OUT.write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()

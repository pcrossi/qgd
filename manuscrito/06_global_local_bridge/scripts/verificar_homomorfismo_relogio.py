#!/usr/bin/env python3
"""
GDQ — Capítulo 6 / Homomorfismo causal do relógio.

Objetivo:
    Verificar de forma autocontida a construção usada no Capítulo 6:
    se o relógio físico t forma o grupo aditivo de translações e o parâmetro
    de fluxo tau pertence ao grupo multiplicativo positivo, a compatibilidade
    de grupo impõe f(t1+t2)=f(t1)f(t2). Sob regularidade, a solução é
    f(t)=exp(kappa t), isto é, tau_gamma(t)=tau0 exp(kappa t).

Fonte teórica:
    manuscrito/06_global_local_bridge/06.8 - Relógio, corrente e continuidade no laboratório.md
    manuscrito/notes/equations/Auditoria do termo canonico rho d_t S_R.md

Classificação:
    Verificação simbólico-numérica de consistência. Não é previsão física.

Equação:
    f(t1+t2)=f(t1)f(t2)
    tau_gamma(t)=tau0 exp(kappa t)
    gamma^*(d tau/tau)=kappa dt

Domínio e contorno:
    Grupo aditivo real do tempo local e grupo multiplicativo real positivo
    do parâmetro de escala; sem EDP e sem contorno espacial.

Parâmetros:
    Universais/estruturais:
        forma logarítmica d tau/tau.
    Dados de aparelho/experimento:
        nenhum.
    Numéricos:
        tau0 e kappa escolhidos apenas para teste algébrico.

Saída:
    saida_verificar_homomorfismo_relogio.md

Observação:
    O teste verifica a forma matemática do homomorfismo. Ele não deriva sozinho
    a dinâmica física completa do aparelho nem fixa kappa metrologicamente.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_homomorfismo_relogio.md")


def main() -> None:
    tau0 = 2.0
    kappa = 0.37
    pairs = [(-1.0, 0.25), (0.1, 0.9), (1.0, 2.0), (-0.4, 1.7)]
    rows = []
    for t1, t2 in pairs:
        f1 = math.exp(kappa * t1)
        f2 = math.exp(kappa * t2)
        f12 = math.exp(kappa * (t1 + t2))
        defect = abs(f12 - f1 * f2)
        rows.append((t1, t2, f12, f1 * f2, defect))

    dt = 1e-5
    t = 0.8
    tau = lambda x: tau0 * math.exp(kappa * x)
    numerical_pullback = (math.log(tau(t + dt)) - math.log(tau(t - dt))) / (2 * dt)

    lines = [
        "---",
        'title: "Saída — homomorfismo causal do relógio"',
        "---",
        "",
        "# Saída — homomorfismo causal do relógio",
        "",
        "Classificação: verificação simbólico-numérica de consistência.",
        "",
        f"Parâmetros didáticos: $\\tau_0={tau0}$, $\\kappa={kappa}$.",
        "",
        "| $t_1$ | $t_2$ | $f(t_1+t_2)$ | $f(t_1)f(t_2)$ | defeito |",
        "|---:|---:|---:|---:|---:|",
    ]
    for t1, t2, f12, prod, defect in rows:
        lines.append(f"| {t1:.2f} | {t2:.2f} | {f12:.12f} | {prod:.12f} | {defect:.3e} |")

    lines += [
        "",
        f"Derivada numérica de $\\log\\tau_\\gamma(t)$ em $t={t}$: `{numerical_pullback:.12f}`.",
        "",
        "Conclusão: o pullback da forma logarítmica satisfaz",
        "$\\gamma^*(d\\tau/\\tau)=\\kappa dt$ no relógio exponencial.",
        "Isto verifica a forma matemática do teorema condicional; não deriva por",
        "si só a dinâmica física completa do aparelho.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

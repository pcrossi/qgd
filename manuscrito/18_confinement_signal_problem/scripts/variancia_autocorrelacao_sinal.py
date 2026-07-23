#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `variancia autocorrelacao sinal` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / escala de autocorrelação.

Ajusta leis de potência aos dados reduzidos preservados:

    tau_corr ~ N^p
    1/gap ~ N^p_gap

Classificação: teste de escala numérico reduzido.
"""

from __future__ import annotations

from pathlib import Path
import math


def fit_power(xs: list[float], ys: list[float]) -> tuple[float, float]:
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    p = sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / sum((x - mx) ** 2 for x in lx)
    c = math.exp(my - p * mx)
    return c, p


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_variancia_autocorrelacao_sinal.md"

    n = [16, 36, 64]
    tau = [8.241905, 17.523244, 30.118337]
    c_tau, p_tau = fit_power(n, tau)

    n2 = [4, 8, 16, 32, 64]
    inv_gap = [2.222222, 7.587141, 29.193492, 115.652077, 461.494514]
    c_gap, p_gap = fit_power(n2, inv_gap)

    text = f"""# Saída — autocorrelação e variância do problema do sinal

Classificação: teste de escala numérico reduzido.

| ajuste | C | expoente |
|---|---:|---:|
| tau_corr ~ C N^p | {c_tau:.12e} | {p_tau:.6f} |
| 1/gap ~ C N^p | {c_gap:.12e} | {p_gap:.6f} |

Interpretação: os dados reduzidos indicam escala polinomial no intervalo
testado. Isso não é prova assintótica geral.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

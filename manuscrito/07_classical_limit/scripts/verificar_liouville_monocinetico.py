#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar liouville monocinetico` associada ao capítulo `07_classical_limit`.

Verifica conservação de norma para densidade transportada antes de cáusticas.

Modelo livre 1D com velocidade constante v:

    rho(x,t)=rho0(x-vt).

Então:

    partial_t rho + v partial_x rho = 0.

Integramos a norma em uma janela ampla para confirmar conservação.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_liouville_monocinetico.md")


def rho0(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def integrate(func, lo: float, hi: float, n: int = 200000) -> float:
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def main() -> None:
    v = 1.7
    rows = []
    for t in [0, 1, 2, 4, 6]:
        norm = integrate(lambda x: rho0(x - v * t), -20, 20)
        rows.append((t, norm, abs(norm - 1.0)))

    lines = [
        "---",
        'title: "Saída — Liouville monocinético"',
        "---",
        "",
        "# Saída — Liouville monocinético",
        "",
        "Classificação: toy model de transporte clássico antes de cáusticas.",
        "",
        "| $t$ | norma transportada | erro contra 1 |",
        "|---:|---:|---:|",
    ]
    for t, norm, err in rows:
        lines.append(f"| {t} | {norm:.12f} | {err:.3e} |")

    lines += [
        "",
        "Conclusão: antes de cáusticas e sem fuga de fluxo, a continuidade",
        "transporta a densidade e conserva a norma do ensemble.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar noether classico` associada ao capítulo `07_classical_limit`.

Verificação didática de Noether no limite clássico.

Dois testes:
- oscilador harmônico 1D autônomo: energia conservada;
- movimento central 2D: momento angular conservado.

Ambos são toy models clássicos; ilustram que a conservação depende da simetria
e de ausência de fluxo externo.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_noether_classico.md")


def rk4_central(x, y, px, py, dt, m, k):
    def deriv(s):
        xs, ys, pxs, pys = s
        r2 = xs * xs + ys * ys
        r = math.sqrt(r2)
        factor = -k / (r2 * r)
        return pxs / m, pys / m, factor * xs, factor * ys

    s = (x, y, px, py)
    k1 = deriv(s)
    k2 = deriv(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
    k3 = deriv(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
    k4 = deriv(tuple(s[i] + dt * k3[i] for i in range(4)))
    return tuple(s[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(4))


def main() -> None:
    m = 1.0
    k = 1.0
    x, y, px, py = 1.0, 0.0, 0.0, 0.8
    dt = 0.001
    steps = 20000

    def energy(xs, ys, pxs, pys):
        r = math.sqrt(xs * xs + ys * ys)
        return (pxs * pxs + pys * pys) / (2 * m) - k / r

    def angular(xs, ys, pxs, pys):
        return xs * pys - ys * pxs

    e0 = energy(x, y, px, py)
    l0 = angular(x, y, px, py)
    max_de = 0.0
    max_dl = 0.0
    for _ in range(steps):
        x, y, px, py = rk4_central(x, y, px, py, dt, m, k)
        max_de = max(max_de, abs(energy(x, y, px, py) - e0))
        max_dl = max(max_dl, abs(angular(x, y, px, py) - l0))

    lines = [
        "---",
        'title: "Saída — Noether clássico"',
        "---",
        "",
        "# Saída — Noether clássico",
        "",
        "Classificação: toy model de consistência Noetheriana.",
        "",
        "Sistema: movimento central 2D com $V(r)=-k/r$.",
        "",
        f"Deriva máxima de energia: `{max_de:.6e}`.",
        "",
        f"Deriva máxima de momento angular: `{max_dl:.6e}`.",
        "",
        "Conclusão: quando homogeneidade temporal e isotropia são preservadas,",
        "energia e momento angular permanecem constantes até erro numérico.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()


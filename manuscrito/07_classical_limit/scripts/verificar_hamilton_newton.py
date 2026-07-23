#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar hamilton newton` associada ao capítulo `07_classical_limit`.

Verifica Hamilton -> Newton para H=p^2/(2m)+kx^2/2.

Equações de Hamilton:

    xdot = p/m
    pdot = -kx

implicam:

    m xddot = -kx.

Integramos numericamente e comparamos com a solução analítica.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_hamilton_newton.md")


def rk4_step(x, p, dt, m, k):
    def f(state):
        xs, ps = state
        return ps / m, -k * xs

    k1x, k1p = f((x, p))
    k2x, k2p = f((x + 0.5 * dt * k1x, p + 0.5 * dt * k1p))
    k3x, k3p = f((x + 0.5 * dt * k2x, p + 0.5 * dt * k2p))
    k4x, k4p = f((x + dt * k3x, p + dt * k3p))
    xn = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    pn = p + dt * (k1p + 2 * k2p + 2 * k3p + k4p) / 6
    return xn, pn


def main() -> None:
    m = 2.0
    k = 8.0
    omega = math.sqrt(k / m)
    x0, p0 = 1.0, 0.3
    dt = 0.001
    steps = 10000
    x, p = x0, p0
    max_err = 0.0
    max_energy_drift = 0.0
    e0 = p0 * p0 / (2 * m) + 0.5 * k * x0 * x0

    for n in range(steps + 1):
        t = n * dt
        xa = x0 * math.cos(omega * t) + (p0 / (m * omega)) * math.sin(omega * t)
        max_err = max(max_err, abs(x - xa))
        e = p * p / (2 * m) + 0.5 * k * x * x
        max_energy_drift = max(max_energy_drift, abs(e - e0))
        if n < steps:
            x, p = rk4_step(x, p, dt, m, k)

    lines = [
        "---",
        'title: "Saída — Hamilton para Newton"',
        "---",
        "",
        "# Saída — Hamilton para Newton",
        "",
        "Classificação: toy model de consistência dinâmica.",
        "",
        f"$m={m}$, $k={k}$, $\\omega={omega:.6f}$, passo $dt={dt}$.",
        "",
        f"Erro máximo em $x(t)$ contra solução analítica: `{max_err:.6e}`.",
        "",
        f"Deriva máxima de energia: `{max_energy_drift:.6e}`.",
        "",
        "Conclusão: as características de Hamilton reproduzem a dinâmica de",
        "Newton no potencial quadrático, como usado no Capítulo 7.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()


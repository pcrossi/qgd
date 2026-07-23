#!/usr/bin/env python3
"""Q52 — avaliação direta da fórmula de Klein–Nishina.

Classificação numérica:
  - avaliação direta de quantidade conhecida;
  - teste de consistência de limite Thomson;
  - não é derivação da amplitude a partir da ação.

A derivação física fica no documento da questão. Este script apenas congela
normalização, razão de energias e comportamento angular.
"""

from math import cos, pi


def energy_ratio(x: float, theta: float) -> float:
    """E'/E for Compton scattering with x = E/(m c^2)."""
    return 1.0 / (1.0 + x * (1.0 - cos(theta)))


def klein_nishina_over_re2(x: float, theta: float) -> float:
    """(dσ/dΩ)/r_e^2."""
    r = energy_ratio(x, theta)
    return 0.5 * r * r * (r + 1.0 / r - (1.0 - cos(theta) ** 2))


def thomson_over_re2(theta: float) -> float:
    """Classical Thomson unpolarized angular factor."""
    return 0.5 * (1.0 + cos(theta) ** 2)


angles_deg = [0, 30, 60, 90, 120, 150, 180]
xs = [1e-6, 0.1, 1.0, 10.0]

print("# Q52 — Teste da fórmula de Klein–Nishina")
print()
print("Normalização usada:")
print()
print("dσ/dΩ = (r_e^2/2) (E'/E)^2 [E'/E + E/E' - sin^2(theta)]")
print()

for x in xs:
    print(f"## x = E/(m c^2) = {x:g}")
    print()
    print("| theta(deg) | E'/E | KN/r_e^2 | Thomson/r_e^2 | diferença rel. |")
    print("|---:|---:|---:|---:|---:|")
    for deg in angles_deg:
        theta = pi * deg / 180.0
        r = energy_ratio(x, theta)
        kn = klein_nishina_over_re2(x, theta)
        th = thomson_over_re2(theta)
        rel = (kn - th) / th if th != 0 else 0.0
        print(f"| {deg:3d} | {r:.12f} | {kn:.12f} | {th:.12f} | {rel:+.6e} |")
    print()

theta = pi / 2.0
for x in [1e-3, 1e-4, 1e-5, 1e-6]:
    kn = klein_nishina_over_re2(x, theta)
    th = thomson_over_re2(theta)
    print(f"limite Thomson theta=90°, x={x:g}: diferença relativa={(kn-th)/th:+.6e}")

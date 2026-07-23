#!/usr/bin/env python3
"""
GDQ — Capítulo 10 / resíduo de Cauchy e Hopf

Objetivo:
    Verificar numericamente que a conexão logarítmica de uma seção spinorial
    local s(z)=z^(1/2) tem circulação normalizada 1/2 ao redor do defeito.

Construção:
    Omega_S = (1/2) dz/z. Em uma volta z(theta)=r exp(i theta),
    dz/z = i dtheta. Logo:

        (1/(2 pi i)) int Omega_S = 1/2.

    O script integra numericamente essa expressão para diferentes raios. O
    resultado não deve depender de r, desde que o laço não cruze o núcleo.

Classificação:
    Teste simbólico-numérico de uma identidade topológica. Não é previsão
    metrológica.

Saída:
    scripts/saida_verificar_residuo_hopf_cauchy.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def residue_integral(radius: float, n: int = 200_000) -> complex:
    """Integra Omega=(1/2) dz/z no círculo |z|=radius."""
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dtheta = 2.0 * np.pi / n
    z = radius * np.exp(1j * theta)
    dz = 1j * z * dtheta
    omega = 0.5 * dz / z
    integral = np.sum(omega)
    return integral / (2.0 * np.pi * 1j)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_residuo_hopf_cauchy.md"

    radii = [0.05, 0.1, 0.3, 0.7, 1.0]
    rows = []
    for r in radii:
        val = residue_integral(r)
        rows.append((r, val.real, val.imag, abs(val - 0.5)))

    table = "\n".join(
        f"| {r:.3f} | {re:.12f} | {im:.12e} | {err:.12e} |"
        for r, re, im, err in rows
    )

    text = f"""# Saída — verificar resíduo Hopf/Cauchy

Classificação: teste simbólico-numérico de identidade topológica.

Integral testada:

$$
\\frac{{1}}{{2\\pi i}}\\oint_{{|z|=r}} \\frac12\\frac{{dz}}{{z}}.
$$

| raio r | Re(integral) | Im(integral) | erro para 1/2 |
|---:|---:|---:|---:|
{table}

Interpretação: a circulação normalizada é $1/2$ e independe do raio do laço.
Isso representa a meia-monodromia spinorial de Hopf ao redor do estômato.
"""
    out.write_text(text, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

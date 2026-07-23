#!/usr/bin/env python3
"""
GDQ — Capítulo 1 / Difusão variável de Nelson-Itô.

Objetivo:
    Verificar numericamente, em um domínio periódico 1D, as identidades
    diferenciais usadas na redução estocástica com difusão variável:

        D(x) = nu0 / Omega(x)

        ∂_t rho = -∂_x(b rho) + ∂_x^2(D rho)

    e a expansão de Itô:

        ∂_x^2(D rho) = D rho'' + 2 D' rho' + rho D''.

    Também verifica a forma da velocidade osmótica:

        u = D ∂_x ln rho + ∂_x D
          = D(∂_x ln rho - ∂_x ln Omega).

Fonte teórica:
    manuscrito/01_initial_problem/01.8 - Difusão universal e inércia geométrica.md
    manuscrito/notes/derivations/Difusão variável de Nelson na GDQ.md

Classificação:
    Teste simbólico-numérico de identidade diferencial em domínio periódico.
    Não é previsão física e não usa dados experimentais.

Domínio e contorno:
    Círculo 1D x ∈ [0, 2π), com diferenças espectrais por FFT e periodicidade.

Parâmetros:
    Universais:
        nu0 = 0.5 em unidades reduzidas.
    Dados de aparelho/experimento:
        nenhum.
    Numéricos:
        N = 2048 pontos; perfis suaves positivos rho e Omega.

Saída:
    saida_verificar_difusao_variavel_ito.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def spectral_derivative(values: np.ndarray, order: int = 1) -> np.ndarray:
    """Derivada espectral periódica em [0, 2π)."""
    n = values.size
    k = np.fft.fftfreq(n, d=1.0 / n)
    return np.fft.ifft((1j * k) ** order * np.fft.fft(values)).real


def main() -> None:
    n = 2048
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    nu0 = 0.5

    rho = 1.2 + 0.25 * np.cos(x) + 0.10 * np.sin(2.0 * x)
    omega = 1.5 + 0.20 * np.sin(x) + 0.07 * np.cos(3.0 * x)
    drift = 0.3 * np.sin(x) - 0.1 * np.cos(2.0 * x)

    d = nu0 / omega

    rho_x = spectral_derivative(rho, 1)
    rho_xx = spectral_derivative(rho, 2)
    d_x = spectral_derivative(d, 1)
    d_xx = spectral_derivative(d, 2)

    ito_direct = spectral_derivative(d * rho, 2)
    ito_expanded = d * rho_xx + 2.0 * d_x * rho_x + rho * d_xx
    ito_error = float(np.max(np.abs(ito_direct - ito_expanded)))

    fp_conservative = -spectral_derivative(drift * rho, 1) + ito_direct
    fp_expanded = -spectral_derivative(drift * rho, 1) + ito_expanded
    fp_error = float(np.max(np.abs(fp_conservative - fp_expanded)))

    u_from_d = d * spectral_derivative(np.log(rho), 1) + d_x
    u_from_omega = d * (
        spectral_derivative(np.log(rho), 1)
        - spectral_derivative(np.log(omega), 1)
    )
    u_error = float(np.max(np.abs(u_from_d - u_from_omega)))

    omitted_terms = ito_direct - d * rho_xx
    omitted_norm = float(np.max(np.abs(omitted_terms)))
    ito_norm = float(np.max(np.abs(ito_direct)))
    omitted_relative = omitted_norm / ito_norm

    ok = ito_error < 1e-9 and fp_error < 1e-9 and u_error < 1e-9

    lines: list[str] = []
    lines.append("# Saída — difusão variável de Nelson--Itô\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico-numérico de identidade diferencial em domínio periódico. Não é previsão física.\n\n")
    lines.append("## Identidades testadas\n\n")
    lines.append("$$\n")
    lines.append("D=\\nu_0\\Omega^{-1}.\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("\\partial_x^2(D\\rho)\n")
    lines.append("=D\\rho''+2D'\\rho'+\\rho D''.\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("u=D\\partial_x\\ln\\rho+\\partial_xD\n")
    lines.append("=D(\\partial_x\\ln\\rho-\\partial_x\\ln\\Omega).\n")
    lines.append("$$\n\n")
    lines.append("## Parâmetros numéricos\n\n")
    lines.append("- Domínio periódico: $[0,2\\pi)$\n")
    lines.append(f"- Malha: $N={n}$\n")
    lines.append(f"- $\\nu_0={nu0}$ em unidades reduzidas\n\n")
    lines.append("## Erros máximos\n\n")
    lines.append("| teste | erro máximo |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| expansão de Itô | {ito_error:.6e} |\n")
    lines.append(f"| Fokker--Planck conservativa vs expandida | {fp_error:.6e} |\n")
    lines.append(f"| velocidade osmótica variável | {u_error:.6e} |\n\n")
    lines.append("## Tamanho dos termos omitidos se $\\Omega$ for tratado como constante\n\n")
    lines.append("| quantidade | valor |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\lVert\\partial_x^2(D\\rho)-D\\rho''\\rVert_\\infty$ | {omitted_norm:.6e} |\n")
    lines.append(f"| fração relativa ao termo completo | {omitted_relative:.6e} |\n\n")
    lines.append("## Veredito\n\n")
    if ok:
        lines.append("As identidades passaram. Os termos com gradientes de $\\Omega$ são necessários quando $\\Omega$ varia.\n")
    else:
        lines.append("Alguma identidade falhou; revisar discretização ou fórmulas.\n")
    lines.append("\nNenhum alvo experimental foi usado.\n")

    out = OUT / "saida_verificar_difusao_variavel_ito.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

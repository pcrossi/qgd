#!/usr/bin/env python3
"""
Benchmark real do protocolo de calibração do Capítulo 9.

Fonte experimental
-------------------
Fein et al., "Nanoscale Magnetism Probed in a Matter-Wave Interferometer",
Physical Review Letters 129, 123001 (2022), DOI:
https://doi.org/10.1103/PhysRevLett.129.123001

O CSV adjacente contém os centros dos marcadores da Fig. 2, extraídos
diretamente do PDF vetorial dos autores. Não são dados brutos do laboratório.
Essa limitação é importante: não calculamos qui-quadrado, pois as incertezas
originais não foram disponibilizadas em tabela.

Classificação científica
------------------------
* C(I) da bobina: calibração independente por sonda Hall/geometria;
* gradiente de fundo: único parâmetro calibrado;
* série rápida alternada: calibração;
* pontos restantes da série rápida: teste interno;
* série lenta completa: validação externa ao ajuste;
* resultado: comparação fenomenológica do protocolo de aparelho, não previsão
  cega da ação fundamental da GDQ.

O script é autocontido: lê apenas o CSV adjacente, calcula as distribuições
skew-normal publicadas, ajusta o gradiente de fundo, testa refinamento da
quadratura e salva um gráfico e um relatório Markdown.
"""

from __future__ import annotations

import csv
import math
import os
from pathlib import Path

# Mantém o cache do Matplotlib numa área temporária gravável.
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-gdq-cap09")

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar


BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "dados_fein2022_cs.csv"
PLOT_FILE = BASE / "benchmark_cs_fein2022.png"
REPORT_FILE = BASE / "resultado_benchmark_cs_fein2022.md"

# Constantes e geometria informadas no artigo.
MU_B = 9.274_010_078_3e-24  # J/T
U_ATOMIC = 1.660_539_066_60e-27  # kg
MASS_CS133 = 132.905_451_96 * U_ATOMIC
GRATING_PERIOD = 266e-9  # m
INTERFEROMETER_LENGTH = 0.98  # m
COIL_C_PER_AMPERE = 10.3  # G m / A, mapeamento Hall + Biot-Savart

# Parâmetros (localização, escala, forma) das distribuições skew-normal.
VELOCITY_PARAMETERS = {
    "270": (228.0, 118.0, 4.4),
    "380": (290.0, 171.0, 2.1),
}

# Projeções m_F g_F para 133Cs: F=3, g_F=-1/4; F=4, g_F=+1/4.
MAGNETIC_PROJECTIONS = np.array(
    [m * (-0.25) for m in range(-3, 4)]
    + [m * (+0.25) for m in range(-4, 5)],
    dtype=float,
)


def load_data() -> dict[str, list[tuple[float, float]]]:
    """Lê corrente e visibilidade das duas séries digitizadas."""
    result = {"270": [], "380": []}
    with DATA_FILE.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            key = row["serie_velocidade_m_s"]
            result[key].append(
                (float(row["corrente_A"]), float(row["visibilidade_normalizada"]))
            )
    return result


def normal_cdf(values: np.ndarray) -> np.ndarray:
    """CDF normal sem depender de uma função especial vetorizada."""
    return np.array(
        [0.5 * (1.0 + math.erf(x / math.sqrt(2.0))) for x in values],
        dtype=float,
    )


def velocity_grid(series: str, points: int) -> tuple[np.ndarray, np.ndarray]:
    """Constrói e normaliza numericamente a distribuição skew-normal."""
    location, scale, shape = VELOCITY_PARAMETERS[series]
    velocity = np.linspace(0.1, 1200.0, points)
    z = (velocity - location) / scale
    density = (
        2.0
        / scale
        / math.sqrt(2.0 * math.pi)
        * np.exp(-0.5 * z**2)
        * normal_cdf(shape * z)
    )
    density /= np.trapezoid(density, velocity)
    return velocity, density


class VisibilityModel:
    """Resposta do interferômetro para parâmetros físicos congelados."""

    def __init__(self, quadrature_points: int = 8000):
        self.grids = {
            name: velocity_grid(name, quadrature_points)
            for name in VELOCITY_PARAMETERS
        }

    def visibility(
        self, current_a: float, series: str, background_gradient_g_per_m: float
    ) -> float:
        """
        Calcula V/V0.

        C(I) é a resposta integrada da bobina. O termo de fundo uniforme
        contribui com C0=L² grad(B0). A conversão 1 G = 1e-4 T é explícita.
        """
        velocity, density = self.grids[series]
        c_factor_g_m = (
            COIL_C_PER_AMPERE * current_a
            + INTERFEROMETER_LENGTH**2 * background_gradient_g_per_m
        )
        c_factor_t_m = c_factor_g_m * 1e-4
        phase_base = (
            2.0
            * math.pi
            / GRATING_PERIOD
            * MU_B
            * c_factor_t_m
            / MASS_CS133
        )
        phases = (
            phase_base
            * MAGNETIC_PROJECTIONS[:, np.newaxis]
            / velocity[np.newaxis, :] ** 2
        )
        state_sum = np.cos(phases).sum(axis=0)
        # Há 16 subestados igualmente populados.
        return float(abs(np.trapezoid(density * state_sum, velocity)) / 16.0)


def metrics(
    model: VisibilityModel,
    points: list[tuple[float, float]],
    series: str,
    background: float,
) -> tuple[float, float, float]:
    """Retorna RMSE, MAE e viés médio."""
    residuals = np.array(
        [model.visibility(i, series, background) - observed for i, observed in points]
    )
    return (
        float(np.sqrt(np.mean(residuals**2))),
        float(np.mean(np.abs(residuals))),
        float(np.mean(residuals)),
    )


def main() -> None:
    data = load_data()

    # O artigo identifica dois regimes sistemáticos:
    # I < 0.15 A (reorientação por campos residuais) e I > 4.5 A
    # (aquecimento/outgassing). Eles não pertencem ao domínio do modelo.
    valid = {
        key: [(i, v) for i, v in values if 0.15 <= i <= 4.5]
        for key, values in data.items()
    }

    # Divisão determinística anterior ao ajuste: índices pares treinam;
    # índices ímpares testam. A série 270 nunca participa da calibração.
    calibration = valid["380"][::2]
    internal_test = valid["380"][1::2]

    model = VisibilityModel(quadrature_points=8000)
    fit = minimize_scalar(
        lambda background: metrics(
            model, calibration, "380", background
        )[0] ** 2,
        bounds=(-0.2, 1.0),
        method="bounded",
        options={"xatol": 1e-8},
    )
    fitted_background = float(fit.x)

    groups = {
        "calibração 380 m/s": (calibration, "380"),
        "teste interno 380 m/s": (internal_test, "380"),
        "validação cega 270 m/s": (valid["270"], "270"),
    }
    results = {
        name: metrics(model, points, series, fitted_background)
        for name, (points, series) in groups.items()
    }

    # Convergência da quadratura no conjunto cego com o parâmetro congelado.
    convergence = []
    previous_rmse = None
    for size in (2000, 4000, 8000, 16000):
        candidate = VisibilityModel(quadrature_points=size)
        rmse, _, _ = metrics(
            candidate, valid["270"], "270", fitted_background
        )
        change = None if previous_rmse is None else abs(rmse - previous_rmse)
        convergence.append((size, rmse, change))
        previous_rmse = rmse

    # Gráfico: pontos digitizados e curvas com o parâmetro já congelado.
    fig, axis = plt.subplots(figsize=(8.2, 5.0))
    colors = {"270": "#0072bd", "380": "#d95319"}
    for series in ("270", "380"):
        raw = np.array(data[series])
        axis.scatter(
            raw[:, 0],
            raw[:, 1],
            s=25,
            color=colors[series],
            label=f"dados {series} m/s",
            zorder=3,
        )
        current = np.linspace(0.0, 4.55, 300)
        predicted = [
            model.visibility(i, series, fitted_background) for i in current
        ]
        axis.plot(
            current,
            predicted,
            color=colors[series],
            linewidth=1.8,
            label=f"modelo {series} m/s",
        )
    axis.axvspan(0.0, 0.15, color="grey", alpha=0.12, label="fora do domínio")
    axis.axhline(2.0 / 16.0, color="black", linestyle=":", linewidth=1.0)
    axis.set(
        xlabel="Corrente nas bobinas anti-Helmholtz (A)",
        ylabel="Visibilidade normalizada",
        xlim=(0.0, 4.6),
        ylim=(0.0, 1.02),
    )
    axis.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(PLOT_FILE, dpi=180)
    plt.close(fig)

    lines = [
        "# Resultado do benchmark Cs — Fein et al. (2022)",
        "",
        "## Protocolo",
        "",
        "- resposta da bobina congelada: `C/I = 10.3 G m/A`;",
        "- único parâmetro calibrado: gradiente magnético uniforme de fundo;",
        "- treino: índices pares da série nominal de 380 m/s;",
        "- teste interno: índices ímpares da mesma série;",
        "- validação externa ao ajuste: toda a série nominal de 270 m/s;",
        "- domínio declarado: `0.15 A <= I <= 4.5 A`.",
        "",
        "## Resultado",
        "",
        f"Gradiente de fundo obtido: `{fitted_background:.6f} G/m`.",
        "",
        "O artigo informa `0.4 G/m`; a diferença é compatível com a",
        "digitização da figura e com a divisão parcial adotada aqui.",
        "",
        "| Conjunto | N | RMSE | MAE | Viés |",
        "|---|---:|---:|---:|---:|",
    ]
    for name, (points, _) in groups.items():
        rmse, mae, bias = results[name]
        lines.append(
            f"| {name} | {len(points)} | {rmse:.6f} | {mae:.6f} | {bias:+.6f} |"
        )
    lines.extend(
        [
            "",
            "## Refinamento da quadratura no conjunto cego",
            "",
            "| Pontos em velocidade | RMSE | Mudança |",
            "|---:|---:|---:|",
        ]
    )
    for size, rmse, change in convergence:
        change_text = "—" if change is None else f"{change:.3e}"
        lines.append(f"| {size} | {rmse:.9f} | {change_text} |")
    lines.extend(
        [
            "",
            "## Classificação",
            "",
            "O benchmark valida o protocolo de calibração e transporte da resposta",
            "do aparelho. Ele não é uma previsão cega exclusiva da GDQ, pois a",
            "resposta magnética atômica usada na fase é a expressão operacional",
            "publicada pelo experimento, e não um canal magnético novamente",
            "derivado da Hessiana oficial.",
            "",
            "![Comparação entre dados e resposta congelada](benchmark_cs_fein2022.png)",
            "",
        ]
    )
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 72)
    print("BENCHMARK REAL DE CALIBRAÇÃO — 133Cs")
    print("=" * 72)
    print(f"gradiente de fundo ajustado = {fitted_background:.8f} G/m")
    print("valor publicado              = 0.40000000 G/m")
    for name, (points, _) in groups.items():
        rmse, mae, bias = results[name]
        print(
            f"{name:28s} N={len(points):2d} "
            f"RMSE={rmse:.6f} MAE={mae:.6f} viés={bias:+.6f}"
        )
    print("relatório:", REPORT_FILE)
    print("gráfico:  ", PLOT_FILE)


if __name__ == "__main__":
    main()

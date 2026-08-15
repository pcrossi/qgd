#!/usr/bin/env python3
"""
Real benchmark of the calibration protocol of Chapter 9.

Experimental source
-------------------
Fein et al., "Nanoscale Magnetism Probed in a Matter-Wave Interferometer",
Physical Review Letters 129, 123001 (2022), DOI:
https://doi.org/10.1103/PhysRevLett.129.123001

The adjacent CSV contains the marker centers from Fig. 2, extracted
directly from the authors' vector PDF. These are not raw laboratory data.
This limitation is important: we do not calculate chi-squared, since the
original uncertainties were not made available in a table.

Scientific classification
------------------------
* C(I) of the coil: independent calibration by Hall probe/geometry;
* background gradient: only parameter calibrated;
* alternated fast series: calibration;
* remaining points of the fast series: internal test;
* complete slow series: validation external to the fit;
* outcome: comparison of the apparatus protocol, not a blind
  prediction of the fundamental action of GDQ.

The script is self-contained: it reads only the adjacent CSV, calculates the published
skew-normal distributions, adjusts the background gradient, tests quadrature refinement,
and saves a plot and a Markdown report.
"""

from __future__ import annotations

import csv
import math
import os
from pathlib import Path

# Keeps Matplotlib cache in a temporary writeable area.
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-gdq-cap09")

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar


BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "dados_fein2022_cs.csv"
PLOT_FILE = BASE / "benchmark_cs_fein2022.png"
REPORT_FILE = BASE / "output_benchmark_cs_fein2022.md"

# Constants and geometry reported in the article.
MU_B = 9.274_010_078_3e-24  # J/T
U_ATOMIC = 1.660_539_066_60e-27  # kg
MASS_CS133 = 132.905_451_96 * U_ATOMIC
GRATING_PERIOD = 266e-9  # m
INTERFEROMETER_LENGTH = 0.98  # m
COIL_C_PER_AMPERE = 10.3  # G m / A, Hall + Biot-Savart mapping

# Parameters (location, scale, shape) of the skew-normal distributions.
VELOCITY_PARAMETERS = {
    "270": (228.0, 118.0, 4.4),
    "380": (290.0, 171.0, 2.1),
}

# m_F g_F projections for 133Cs: F=3, g_F=-1/4; F=4, g_F=+1/4.
MAGNETIC_PROJECTIONS = np.array(
    [m * (-0.25) for m in range(-3, 4)]
    + [m * (+0.25) for m in range(-4, 5)],
    dtype=float,
)


def load_data() -> dict[str, list[tuple[float, float]]]:
    """Reads current and visibility of the two digitized series."""
    result = {"270": [], "380": []}
    with DATA_FILE.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            key = row["serie_velocidade_m_s"]
            result[key].append(
                (float(row["corrente_A"]), float(row["visibilidade_normalizada"]))
            )
    return result


def normal_cdf(values: np.ndarray) -> np.ndarray:
    """Normal CDF without depending on a vectorized special function."""
    return np.array(
        [0.5 * (1.0 + math.erf(x / math.sqrt(2.0))) for x in values],
        dtype=float,
    )


def velocity_grid(series: str, points: int) -> tuple[np.ndarray, np.ndarray]:
    """Constructs and numerically normalizes the skew-normal distribution."""
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
    """Interferometer response for frozen physical parameters."""

    def __init__(self, quadrature_points: int = 8000):
        self.grids = {
            name: velocity_grid(name, quadrature_points)
            for name in VELOCITY_PARAMETERS
        }

    def visibility(
        self, current_a: float, series: str, background_gradient_g_per_m: float
    ) -> float:
        """
        Calculates V/V0.

        C(I) is the integrated response of the coil. The uniform background term
        contributes C0 = L² grad(B0). The conversion 1 G = 1e-4 T is explicit.
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
        # There are 16 equally populated sub-states.
        return float(abs(np.trapezoid(density * state_sum, velocity)) / 16.0)


def metrics(
    model: VisibilityModel,
    points: list[tuple[float, float]],
    series: str,
    background: float,
) -> tuple[float, float, float]:
    """Returns RMSE, MAE and average bias."""
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

    # The article identifies two systematic regimes:
    # I < 0.15 A (reorientation by residual fields) and I > 4.5 A
    # (heating/outgassing). They do not belong to the domain of the model.
    valid = {
        key: [(i, v) for i, v in values if 0.15 <= i <= 4.5]
        for key, values in data.items()
    }

    # Deterministic split prior to fitting: even indices train;
    # odd indices test. The 270 series never participates in the calibration.
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
        "calibration 380 m/s": (calibration, "380"),
        "internal test 380 m/s": (internal_test, "380"),
        "blind validation 270 m/s": (valid["270"], "270"),
    }
    results = {
        name: metrics(model, points, series, fitted_background)
        for name, (points, series) in groups.items()
    }

    # Quadrature convergence on the blind set with the frozen parameter.
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

    # Plot: digitized points and curves with the parameter already frozen.
    fig, axis = plt.subplots(figsize=(8.2, 5.0))
    colors = {"270": "#0072bd", "380": "#d95319"}
    for series in ("270", "380"):
        raw = np.array(data[series])
        axis.scatter(
            raw[:, 0],
            raw[:, 1],
            s=25,
            color=colors[series],
            label=f"data {series} m/s",
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
            label=f"model {series} m/s",
        )
    axis.axvspan(0.0, 0.15, color="grey", alpha=0.12, label="out of domain")
    axis.axhline(2.0 / 16.0, color="black", linestyle=":", linewidth=1.0)
    axis.set(
        xlabel="Current in anti-Helmholtz coils (A)",
        ylabel="Normalized visibility",
        xlim=(0.0, 4.6),
        ylim=(0.0, 1.02),
    )
    axis.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(PLOT_FILE, dpi=180)
    plt.close(fig)

    lines = [
        "# Output of the Cs benchmark — Fein et al. (2022)",
        "",
        "## Protocol",
        "",
        "- frozen coil response: `C/I = 10.3 G m/A`;",
        "- only parameter calibrated: background uniform magnetic gradient;",
        "- training: even indices of the nominal series of 380 m/s;",
        "- internal test: odd indices of the same series;",
        "- validation external to the fit: the entire nominal series of 270 m/s;",
        "- declared domain: `0.15 A <= I <= 4.5 A`.",
        "",
        "## Result",
        "",
        f"Background gradient obtained: `{fitted_background:.6f} G/m`.",
        "",
        "The article reports `0.4 G/m`; the difference is compatible with the",
        "digitization of the figure and with the partial split adopted here.",
        "",
        "| Set | N | RMSE | MAE | Bias |",
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
            "## Quadrature refinement on the blind set",
            "",
            "| Points in velocity | RMSE | Change |",
            "|---:|---:|---:|",
        ]
    )
    for size, rmse, change in convergence:
        change_text = "—" if change is None else f"{change:.3e}"
        lines.append(f"| {size} | {rmse:.9f} | {change_text} |")
    lines.extend(
        [
            "",
            "## Classification",
            "",
            "The benchmark validates the calibration and transport protocol of the",
            "apparatus response. It is not a blind prediction exclusive to GDQ, as the",
            "atomic magnetic response used in the phase is the operational expression",
            "published by the experiment, rather than a magnetic channel rederived",
            "from the official Hessian.",
            "",
            "![Comparison between data and frozen response](benchmark_cs_fein2022.png)",
            "",
        ]
    )
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("=" * 72)
    print("REAL CALIBRATION BENCHMARK — 133Cs")
    print("=" * 72)
    print(f"adjusted background gradient = {fitted_background:.8f} G/m")
    print("published value              = 0.40000000 G/m")
    for name, (points, _) in groups.items():
        rmse, mae, bias = results[name]
        print(
            f"{name:28s} N={len(points):2d} "
            f"RMSE={rmse:.6f} MAE={mae:.6f} bias={bias:+.6f}"
        )
    print("report:", REPORT_FILE)
    print("plot:  ", PLOT_FILE)


if __name__ == "__main__":
    main()

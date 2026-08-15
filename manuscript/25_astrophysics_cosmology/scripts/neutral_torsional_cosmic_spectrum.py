#!/usr/bin/env python3
"""Conditional cosmic spectrum of neutral torsional modes.

Calculates the part that is independent of the still unknown normalization of the vertex:

    nu_i^(+) + nu_j^(-) -> gamma + gamma.

The candidate masses are frozen before comparison. The script produces:

1. the comb of energies and wavelengths;
2. thermal width of the relic neutral background;
3. homogeneous redshift kernel between z=0 and z=5;
4. band comparison with COBE/FIRAS/DIRBE and Spitzer;
5. inverse scale of <sigma v> and convergence/sensitivity tests.

The inverse scale is not a prediction. A prediction requires calculating the
torsion--torsion--radiation jet of the official action in the cosmological background.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


K_B_EV_K = 8.617333262e-5
H_EV_S = 4.135667696e-15
H_J_S = 6.62607015e-34
C = 299_792_458.0
EV_J = 1.602176634e-19
MPC_M = 3.085677581491367e22

T_CMB = 2.72548
T_NU = (4.0 / 11.0) ** (1.0 / 3.0) * T_CMB
KBT_NU = K_B_EV_K * T_NU

# Reduced neutral candidate already frozen in the previous chapter.
MASSES_EV = np.array([
    0.0,
    8.798417219655e-3,
    5.042386973059e-2,
])

# Reference cosmology and density: external boundary data.
H0 = 67.4 * 1000.0 / MPC_M
OMEGA_M = 0.315
OMEGA_L = 0.685
Z_MAX = 5.0
N_NU_ORIENTATION = 56.0e6
FIRAS_INTENSITY = 14.0e-9


@dataclass(frozen=True)
class Channel:
    """Channel composed of two conjugate neutral orientations."""

    i: int
    j: int
    energy_ev: float
    wavelength_um: float
    thermal_fraction: float

    @property
    def label(self) -> str:
        return rf"$\nu_{self.i + 1}\bar\nu_{self.j + 1}$"


def hubble(z: np.ndarray) -> np.ndarray:
    """Reference H(z) used only in the transport kernel."""

    return H0 * np.sqrt(OMEGA_M * (1.0 + z) ** 3 + OMEGA_L)


def characteristic_momentum_ev() -> float:
    """Mean Fermi--Dirac momentum after decoupling."""

    return 3.151374 * KBT_NU


def build_channels() -> list[Channel]:
    """Constructs the six channels i <= j and includes relic thermal energy."""

    pbar = characteristic_momentum_ev()
    channels: list[Channel] = []
    for i, j in combinations_with_replacement(range(3), 2):
        mi = MASSES_EV[i]
        mj = MASSES_EV[j]
        if mi == 0.0 and mj == 0.0:
            energy = pbar
        else:
            energy = 0.5 * (
                np.sqrt(mi * mi + pbar * pbar)
                + np.sqrt(mj * mj + pbar * pbar)
            )
        wavelength_um = H_EV_S * C / energy * 1.0e6

        vi = 1.0 if mi == 0.0 else pbar / np.sqrt(mi * mi + pbar * pbar)
        vj = 1.0 if mj == 0.0 else pbar / np.sqrt(mj * mj + pbar * pbar)
        width = max(
            np.sqrt(vi * vi + vj * vj) / (2.0 * np.sqrt(3.0)),
            1.0e-3,
        )
        channels.append(Channel(i, j, energy, wavelength_um, width))
    return channels


def redshift_kernel(
    wavelength_um: np.ndarray,
    channel: Channel,
) -> np.ndarray:
    """Normalized energy per d ln(lambda) in the homogeneous cosmological toy model."""

    log_wavelength = np.log(wavelength_um)
    z = np.linspace(0.0, Z_MAX, 2400)
    dz = z[1] - z[0]
    centres = np.log(channel.wavelength_um * (1.0 + z))
    weights = (1.0 + z) / hubble(z)
    sigma = channel.thermal_fraction
    kernel = np.zeros_like(wavelength_um)

    for start in range(0, z.size, 200):
        stop = min(start + 200, z.size)
        delta = log_wavelength[:, None] - centres[None, start:stop]
        gaussian = np.exp(-0.5 * (delta / sigma) ** 2)
        gaussian /= np.sqrt(2.0 * np.pi) * sigma
        kernel += np.sum(
            gaussian * weights[None, start:stop],
            axis=1,
        ) * dz

    normalization = np.trapezoid(kernel, log_wavelength)
    return kernel / normalization


def fixsen_firb_nuinu(wavelength_um: np.ndarray) -> np.ndarray:
    """Published FIRAS fit, in nW m^-2 sr^-1."""

    wavelength_m = wavelength_um * 1.0e-6
    frequency = C / wavelength_m
    frequency_0 = C / 100.0e-6
    temperature = 18.5
    x = H_J_S * frequency / (1.380649e-23 * temperature)
    planck = (
        2.0
        * H_J_S
        * frequency**3
        / C**2
        / np.expm1(x)
    )
    intensity = (
        1.3e-5
        * (frequency / frequency_0) ** 0.64
        * planck
    )
    return frequency * intensity * 1.0e9


def inverse_sigma_v(
    mass_ev: float,
    z_max: float = Z_MAX,
    n_grid: int = 200_001,
) -> tuple[float, float]:
    """Cross section that would saturate all of FIRAS and associated optical depth."""

    z = np.linspace(0.0, z_max, n_grid)
    intensity_integral = np.trapezoid((1.0 + z) / hubble(z), z)
    coefficient = (
        C
        / (4.0 * np.pi)
        * N_NU_ORIENTATION**2
        * (2.0 * mass_ev * EV_J)
        * intensity_integral
    )
    sigma_v = FIRAS_INTENSITY / coefficient
    tau_integral = np.trapezoid((1.0 + z) ** 2 / hubble(z), z)
    tau = N_NU_ORIENTATION * sigma_v * tau_integral
    return sigma_v, tau


def save_plot(channels: list[Channel], output: Path) -> None:
    """Compares normalized shapes and observed bands without adjusting amplitude."""

    wavelength = np.geomspace(5.0, 5000.0, 1400)
    figure, (axis_kernel, axis_data) = plt.subplots(
        2,
        1,
        figsize=(10.5, 9.0),
        sharex=True,
        constrained_layout=True,
    )

    for channel in channels:
        axis_kernel.plot(
            wavelength,
            redshift_kernel(wavelength, channel),
            lw=1.5,
            label=channel.label,
        )
        axis_kernel.axvline(channel.wavelength_um, lw=0.7, alpha=0.25)

    axis_kernel.set_xscale("log")
    axis_kernel.set_ylabel(r"normalized kernel $dE/d\ln\lambda$")
    axis_kernel.set_title(
        "Conditional GDQ positions; amplitudes not adjusted"
    )
    axis_kernel.legend(ncol=3, fontsize=9)
    axis_kernel.grid(True, which="both", alpha=0.25)

    in_firas = (wavelength >= 125.0) & (wavelength <= 2000.0)
    axis_data.plot(
        wavelength[in_firas],
        fixsen_firb_nuinu(wavelength[in_firas]),
        color="black",
        lw=2.0,
        label="COBE/FIRAS",
    )
    axis_data.errorbar(
        [140.0, 240.0],
        [25.0, 14.0],
        yerr=[7.0, 3.0],
        fmt="o",
        color="tab:red",
        label="COBE/DIRBE",
    )
    axis_data.errorbar(
        [24.0],
        [1.9],
        yerr=[0.6],
        fmt="s",
        color="tab:blue",
        label="Spitzer: lower count limit",
    )
    for channel in channels:
        axis_data.axvline(channel.wavelength_um, lw=0.9, alpha=0.5)

    axis_data.set_xscale("log")
    axis_data.set_yscale("log")
    axis_data.set_xlim(5.0, 5000.0)
    axis_data.set_ylim(0.2, 60.0)
    axis_data.set_xlabel(r"wavelength $\lambda$ [$\mu$m]")
    axis_data.set_ylabel(r"$\nu I_\nu$ [nW m$^{-2}$ sr$^{-1}$]")
    axis_data.grid(True, which="both", alpha=0.25)
    axis_data.legend(fontsize=9)

    figure.savefig(output, dpi=180)
    plt.close(figure)


def save_output(channels: list[Channel], output: Path) -> None:
    """Writes the table, diagnostics, and scientific classification."""

    sigma_2, tau_2 = inverse_sigma_v(MASSES_EV[1])
    convergence = [
        (points, *inverse_sigma_v(MASSES_EV[1], Z_MAX, points))
        for points in (2_001, 20_001, 200_001)
    ]
    sensitivity = [
        (z_max, *inverse_sigma_v(MASSES_EV[1], z_max, 100_001))
        for z_max in (1.0, 3.0, 5.0)
    ]

    line_22 = next(
        channel
        for channel in channels
        if channel.i == 1 and channel.j == 1
    )
    line_33 = next(
        channel
        for channel in channels
        if channel.i == 2 and channel.j == 2
    )
    z_240 = 240.0 / line_22.wavelength_um - 1.0

    lines = [
        "---",
        'title: "Output — neutral torsional cosmic spectrum"',
        "---",
        "",
        "# Neutral Torsional Cosmic Spectrum",
        "",
        "Classification: kinematic and conditional cosmological estimate.",
        "The absolute intensity is not a prediction.",
        "",
        "## Frozen Inputs",
        "",
        f"- $T_\\nu={T_NU:.12f}\\,\\mathrm{{K}}$;",
        f"- $k_BT_\\nu={KBT_NU:.12e}\\,\\mathrm{{eV}}$;",
        f"- masses: `{MASSES_EV.tolist()}` eV;",
        f"- $z_{{max}}={Z_MAX:.1f}$.",
        "",
        "## Local Comb",
        "",
        "| channel | energy (eV) | wavelength (um) | toy width |",
        "|---|---:|---:|---:|",
    ]
    for channel in channels:
        lines.append(
            f"| nu{channel.i + 1}-antinu{channel.j + 1} | "
            f"{channel.energy_ev:.12e} | "
            f"{channel.wavelength_um:.9f} | "
            f"{channel.thermal_fraction:.6e} |"
        )

    lines.extend([
        "",
        "## Band Comparison",
        "",
        f"- line 22 versus 140 um: "
        f"`{100.0 * (line_22.wavelength_um / 140.0 - 1.0):+.6f}%`;",
        f"- line 33 versus 24 um: "
        f"`{100.0 * (line_33.wavelength_um / 24.0 - 1.0):+.6f}%`;",
        f"- line 22 redshift to 240 um: `{z_240:.6f}`.",
        "",
        "## Extreme Inverse Scale, Mode 2",
        "",
        f"- $\\langle\\sigma v\\rangle={sigma_2:.12e}\\,\\mathrm{{m^3/s}}$;",
        f"- $\\tau_{{\\rm ann}}={tau_2:.12e}$.",
        "",
        "This number attributes all of FIRAS to the channel and is not a prediction.",
        "",
        "## Numerical Convergence",
        "",
        "| points | <sigma v> (m^3/s) | tau |",
        "|---:|---:|---:|",
    ])
    for points, sigma_v, tau in convergence:
        lines.append(f"| {points} | {sigma_v:.12e} | {tau:.12e} |")

    lines.extend([
        "",
        "## Sensitivity to Source History",
        "",
        "| z_max | <sigma v> (m^3/s) | tau |",
        "|---:|---:|---:|",
    ])
    for z_max, sigma_v, tau in sensitivity:
        lines.append(f"| {z_max:.1f} | {sigma_v:.12e} | {tau:.12e} |")

    lines.extend([
        "",
        "The quadrature converges, but the inverse scale shifts with the cosmological",
        "boundary. This confirms that the amplitude must come from the action.",
        "",
    ])
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    base = Path(__file__).resolve().parent
    channels = build_channels()
    save_output(
        channels,
        base / "output_neutral_torsional_cosmic_spectrum.md",
    )
    save_plot(
        channels,
        base / "espectro_cosmico_torsional_neutro.png",
    )
    print("Neutral torsional cosmic spectrum calculated.")


if __name__ == "__main__":
    main()

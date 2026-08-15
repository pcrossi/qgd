#!/usr/bin/env python3
"""
Chapter 4 — multispecies sweep of the no-pole condition.

Classification:
    Consistency test, not Lambda_EM prediction.

Calculates the formal boundary Pi_EM(infty)=1 for

    Pi_EM(infty)=alpha0/(3*pi) sum_f Nc_f Q_f^2 E1(m_f^2/Lambda_EM^2).

The boundary informs how extreme the point extrapolation would have to be to
produce a pole. It is not called a physical scale predicted by GDQ.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path


ALPHA0 = 1.0 / 137.035999084
EULER_GAMMA = 0.5772156649015329


@dataclass(frozen=True)
class Species:
    name: str
    mass_over_me: float
    charge: float
    colors: int
    provenance: str

    @property
    def weight(self) -> float:
        return self.colors * self.charge * self.charge


def exp1_log(log_z: float) -> float:
    """Approximates E1(exp(log_z)) with control for very small z."""
    if log_z < -35.0:
        z = math.exp(log_z)
        return -EULER_GAMMA - log_z + z
    if log_z > 60.0:
        z = math.exp(log_z)
        return math.exp(-z) / z
    z = math.exp(log_z)
    # Simple quadrature via transformation E1(z)=int_0^1 exp(-z/t)/t dt.
    n = 2000
    h = 1.0 / n
    total = 0.0
    for i in range(n + 1):
        t = i * h
        if t == 0.0:
            value = 0.0
        else:
            value = math.exp(-z / t) / t
        total += (1 if i in (0, n) else 4 if i % 2 else 2) * value
    return total * h / 3.0


def leptons_gdq() -> list[Species]:
    return [
        Species("e", 1.0, -1.0, 1, "metrological unit"),
        Species("mu", 206.767399, -1.0, 1, "geometric spectral ratio"),
        Species("tau", 3477.131776, -1.0, 1, "geometric spectral ratio"),
    ]


def charged_fermion_benchmark() -> list[Species]:
    me = 0.51099895
    rows = [
        ("e", 0.51099895, -1.0, 1, "external reference"),
        ("mu", 105.6583755, -1.0, 1, "external reference"),
        ("tau", 1776.86, -1.0, 1, "external reference"),
        ("u", 2.16, 2.0 / 3.0, 3, "scheme-dependent quark mass"),
        ("d", 4.67, -1.0 / 3.0, 3, "scheme-dependent quark mass"),
        ("s", 93.0, -1.0 / 3.0, 3, "scheme-dependent quark mass"),
        ("c", 1270.0, 2.0 / 3.0, 3, "scheme-dependent quark mass"),
        ("b", 4180.0, -1.0 / 3.0, 3, "scheme-dependent quark mass"),
        ("t", 172760.0, 2.0 / 3.0, 3, "scheme-dependent quark mass"),
    ]
    return [Species(n, m / me, q, nc, p) for n, m, q, nc, p in rows]


def pi_infinity(log10_lambda_over_me: float, species: list[Species]) -> float:
    log_lambda = log10_lambda_over_me * math.log(10.0)
    total = 0.0
    for item in species:
        log_z = 2.0 * math.log(item.mass_over_me) - 2.0 * log_lambda
        total += item.weight * exp1_log(log_z)
    return ALPHA0 * total / (3.0 * math.pi)


def bisect_root(species: list[Species], low: float = -3.0, high: float = 200.0) -> float:
    f_low = pi_infinity(low, species) - 1.0
    f_high = pi_infinity(high, species) - 1.0
    if f_low >= 0.0 or f_high <= 0.0:
        raise RuntimeError("interval without single root")
    for _ in range(120):
        mid = 0.5 * (low + high)
        f_mid = pi_infinity(mid, species) - 1.0
        if f_mid > 0.0:
            high = mid
        else:
            low = mid
    return 0.5 * (low + high)


def audit(name: str, species: list[Species]) -> dict[str, object]:
    critical = bisect_root(species)
    values = [pi_infinity(-3.0 + i * 0.25, species) for i in range(493)]
    return {
        "name": name,
        "species": species,
        "critical": critical,
        "critical_pi": pi_infinity(critical, species),
        "below": pi_infinity(critical - 1.0, species),
        "above": pi_infinity(critical + 1.0, species),
        "monotone": all(values[i + 1] >= values[i] - 1.0e-13 for i in range(len(values) - 1)),
        "weight": sum(item.weight for item in species),
    }


def main() -> None:
    results = [
        audit("geometric leptons", leptons_gdq()),
        audit("charged fermions — benchmark", charged_fermion_benchmark()),
    ]
    lines = [
        "---",
        'title: "Output — multispecies sweep without pole"',
        "---",
        "",
        "# Output — multispecies sweep without pole",
        "",
        "## Formula",
        "",
        "$$",
        "\\Pi_{\\rm EM}(\\infty)=\\frac{\\alpha_0}{3\\pi}",
        "\\sum_fN_c^{(f)}Q_f^2",
        "E_1\\left(\\frac{m_f^2}{\\Lambda_{\\rm EM}^2}\\right).",
        "$$",
        "",
        "The formal boundary is $\\Pi_{\\rm EM}(\\infty)=1$.",
        "",
        "| scenario | species | $\\sum N_cQ^2$ | $\\log_{10}(\\Lambda_{\\rm crit}/m_e)$ | $\\Pi$ at root |",
        "|:---|---:|---:|---:|---:|",
    ]
    for row in results:
        lines.append(
            f"| {row['name']} | `{len(row['species'])}` | `{row['weight']:.6f}` | "
            f"`{row['critical']:.9f}` | `{row['critical_pi']:.12f}` |"
        )
    lines += [
        "",
        "| scenario | $\\Pi(\\Lambda_{\\rm crit}/10)$ | $\\Pi(10\\Lambda_{\\rm crit})$ | monotonic |",
        "|:---|---:|---:|:---:|",
    ]
    for row in results:
        lines.append(
            f"| {row['name']} | `{row['below']:.9f}` | `{row['above']:.9f}` | `{row['monotone']}` |"
        )
    for row in results:
        lines += ["", f"## Spectrum: {row['name']}", ""]
        lines += [
            "| species | $m_f/m_e$ | $Q_f$ | $N_c$ | weight | provenance |",
            "|:---|---:|---:|---:|---:|:---|",
        ]
        for item in row["species"]:
            lines.append(
                f"| {item.name} | `{item.mass_over_me:.9g}` | `{item.charge:.6g}` | "
                f"`{item.colors}` | `{item.weight:.6g}` | {item.provenance} |"
            )
    lines += [
        "",
        "## Classification",
        "",
        "Consistency test. The extremely high root is a consequence of the",
        "effective extrapolation and should not be read as a predicted physical scale.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_multispecies_landau_sweep.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

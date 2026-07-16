"""Montagem de Galerkin para um modo tensorial físico da GDQ.

Este módulo é infraestrutura, não contém um modo físico embutido. O chamador
deve fornecer as densidades de Taylor obtidas pela expansão da ação oficial no
background e no modo tensorial escolhidos. A montagem apenas faz quadratura,
normalização, auditoria por setor e análise da bifurcação reduzida.

Convenção para um representante ``mu`` com norma N_mu::

    lambda_mu = Q2 / N_mu
    g_mu      = Q4 / N_mu**2
    h_mu      = Q6 / N_mu**3
    C_i       = M_i / N_mu

Assim os coeficientes são invariantes sob uma reescala constante do modo.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Protocol

import numpy as np
from numpy.polynomial.legendre import leggauss


OFFICIAL_SECTORS = (
    "curvature",
    "dilaton_gradient",
    "dilaton_potential",
    "measure_volume",
    "torsion_bismut",
    "constraint",
    "boundary_interface",
)
MATCHING_KEYS = ("a", "c", "u")


@dataclass(frozen=True)
class GalerkinDensities:
    """Densidades locais já derivadas da ação oficial.

    Cada valor deve ser um array com o mesmo comprimento de ``points``.
    ``quadratic``/``quartic``/``sextic`` são separados por setor para impedir
    que uma concordância total esconda sinais ou cancelamentos incorretos.
    """

    norm: np.ndarray
    quadratic: Mapping[str, np.ndarray]
    quartic: Mapping[str, np.ndarray]
    matching: Mapping[str, np.ndarray]
    sextic: Mapping[str, np.ndarray] | None = None


class TensorModeProvider(Protocol):
    """Contrato que o modo tensorial físico deverá implementar."""

    label: str

    def densities(
        self, points: np.ndarray, harmonic_cutoff: int
    ) -> GalerkinDensities:
        """Avalia densidades em ``(r, chi, theta, phi)``.

        Derivadas radiais/angulares, contrações com o background e fatores da
        ação oficial pertencem ao provider; não são inferidos pela montagem.
        """


@dataclass(frozen=True)
class QuadratureSpec:
    radial_interval: tuple[float, float]
    radial_order: int = 48
    angular_order: int = 18
    radial_measure: Callable[[np.ndarray], np.ndarray] | None = None


@dataclass(frozen=True)
class GalerkinResult:
    label: str
    harmonic_cutoff: int
    norm: float
    lambda_mu: float
    g_mu: float
    h_mu: float
    C_a: float
    C_c: float
    C_u: float
    quadratic_by_sector: Mapping[str, float]
    quartic_by_sector: Mapping[str, float]
    sextic_by_sector: Mapping[str, float]
    raw_matching: Mapping[str, float]


def _gauss_interval(a: float, b: float, order: int) -> tuple[np.ndarray, np.ndarray]:
    if order < 2 or not b > a:
        raise ValueError("quadratura exige ordem >=2 e intervalo crescente")
    x, w = leggauss(order)
    return (a + b) / 2 + (b - a) * x / 2, (b - a) * w / 2


def s3_radial_grid(spec: QuadratureSpec) -> tuple[np.ndarray, np.ndarray]:
    """Produto Gauss--Legendre em I x S3, com dOmega3=sin²chi sin(theta)."""

    r, wr = _gauss_interval(*spec.radial_interval, spec.radial_order)
    chi, wc = _gauss_interval(0.0, np.pi, spec.angular_order)
    theta, wt = _gauss_interval(0.0, np.pi, spec.angular_order)
    phi, wp = _gauss_interval(0.0, 2 * np.pi, spec.angular_order)
    rr, cc, tt, pp = np.meshgrid(r, chi, theta, phi, indexing="ij")
    weights = (
        wr[:, None, None, None]
        * wc[None, :, None, None]
        * wt[None, None, :, None]
        * wp[None, None, None, :]
        * np.sin(cc) ** 2
        * np.sin(tt)
    )
    if spec.radial_measure is not None:
        weights = weights * np.asarray(spec.radial_measure(rr), dtype=float)
    points = np.column_stack((rr.ravel(), cc.ravel(), tt.ravel(), pp.ravel()))
    return points, weights.ravel()


def _checked_integral(values: np.ndarray, weights: np.ndarray, name: str) -> float:
    array = np.asarray(values)
    if array.shape != weights.shape:
        raise ValueError(f"{name}: shape {array.shape}, esperado {weights.shape}")
    if not np.all(np.isfinite(array)):
        raise FloatingPointError(f"{name}: densidade não finita")
    value = np.sum(weights * array)
    if abs(np.imag(value)) > 1e-10 * max(1.0, abs(value)):
        raise ValueError(f"{name}: coeficiente físico não real: {value}")
    return float(np.real(value))


def _integrate_sectors(
    values: Mapping[str, np.ndarray], weights: np.ndarray, prefix: str
) -> dict[str, float]:
    unknown = set(values) - set(OFFICIAL_SECTORS)
    if unknown:
        raise ValueError(f"setores não declarados em {prefix}: {sorted(unknown)}")
    return {
        sector: _checked_integral(density, weights, f"{prefix}:{sector}")
        for sector, density in values.items()
    }


def assemble_galerkin(
    provider: TensorModeProvider,
    spec: QuadratureSpec,
    harmonic_cutoff: int,
) -> GalerkinResult:
    """Calcula os coeficientes sem ajuste a um alvo fenomenológico."""

    if harmonic_cutoff < 0:
        raise ValueError("harmonic_cutoff deve ser não negativo")
    points, weights = s3_radial_grid(spec)
    d = provider.densities(points, harmonic_cutoff)
    norm = _checked_integral(d.norm, weights, "norm")
    if not norm > 0:
        raise ValueError(f"norma do modo deve ser positiva, obtido {norm}")
    q2 = _integrate_sectors(d.quadratic, weights, "quadratic")
    q4 = _integrate_sectors(d.quartic, weights, "quartic")
    q6 = _integrate_sectors(d.sextic or {}, weights, "sextic")
    if set(d.matching) != set(MATCHING_KEYS):
        raise ValueError("matching deve fornecer exatamente a, c, u")
    matching = {
        key: _checked_integral(d.matching[key], weights, f"matching:{key}")
        for key in MATCHING_KEYS
    }
    return GalerkinResult(
        label=provider.label,
        harmonic_cutoff=harmonic_cutoff,
        norm=norm,
        lambda_mu=sum(q2.values()) / norm,
        g_mu=sum(q4.values()) / norm**2,
        h_mu=sum(q6.values()) / norm**3,
        C_a=matching["a"] / norm,
        C_c=matching["c"] / norm,
        C_u=matching["u"] / norm,
        quadratic_by_sector=q2,
        quartic_by_sector=q4,
        sextic_by_sector=q6,
        raw_matching=matching,
    )


@dataclass(frozen=True)
class BifurcationPoint:
    amplitude: float
    amplitude_squared: float
    reduced_action_shift: float
    curvature: float
    stable: bool


def finite_amplitude_branches(result: GalerkinResult, atol: float = 1e-12) -> list[BifurcationPoint]:
    """Resolve dS/dA=0 para S-S0=lambda A²+g A⁴+h A⁶.

    Retorna apenas amplitudes reais não nulas. A estabilidade é decidida pela
    segunda derivada do funcional reduzido, não pelo sinal isolado de g.
    """

    lam, g, h = result.lambda_mu, result.g_mu, result.h_mu
    if abs(h) <= atol:
        roots = [] if abs(g) <= atol else [-lam / (2 * g)]
    else:
        roots = np.roots([3 * h, 2 * g, lam])
    branches: list[BifurcationPoint] = []
    for root in roots:
        if abs(np.imag(root)) > atol or np.real(root) <= atol:
            continue
        x = float(np.real(root))
        amplitude = np.sqrt(x)
        shift = lam * x + g * x**2 + h * x**3
        curvature = 2 * lam + 12 * g * x + 30 * h * x**2
        branches.append(BifurcationPoint(amplitude, x, shift, curvature, curvature > 0))
    return sorted(branches, key=lambda branch: branch.amplitude)


def convergence_table(
    provider: TensorModeProvider,
    base_spec: QuadratureSpec,
    radial_orders: list[int],
    angular_orders: list[int],
    harmonic_cutoffs: list[int],
) -> list[dict[str, float | int]]:
    """Varre resolução radial, angular e truncamento harmônico separadamente."""

    rows: list[dict[str, float | int]] = []
    for nr in radial_orders:
        for na in angular_orders:
            for cutoff in harmonic_cutoffs:
                spec = QuadratureSpec(base_spec.radial_interval, nr, na, base_spec.radial_measure)
                result = assemble_galerkin(provider, spec, cutoff)
                rows.append({
                    "radial_order": nr,
                    "angular_order": na,
                    "harmonic_cutoff": cutoff,
                    "norm": result.norm,
                    "lambda_mu": result.lambda_mu,
                    "g_mu": result.g_mu,
                    "h_mu": result.h_mu,
                    "C_a": result.C_a,
                    "C_c": result.C_c,
                    "C_u": result.C_u,
                })
    return rows


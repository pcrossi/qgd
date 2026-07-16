"""Tiro antipodal por continuação para o background GDQ com m=1.

Classificação: teste de existência/consistência numérica. Não usa observáveis
como alvos. O comprimento L/r0 é dado de contorno.
"""

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

from ponte_global_local_integrador import Parameters, constraint, rhs


@dataclass
class ShotResult:
    length: float
    a0: float
    pa0: float
    tau: float
    residual: np.ndarray
    cost: float
    success: bool
    max_constraint: float
    min_a: float
    min_c: float
    solution: object


def throat_u(a0, c0, tau, m=1, kappa=1.0):
    return (
        4.0 - 8.0 * tau / a0**2 + 4.0 * tau * c0**2 / a0**4
        - tau * kappa * m**2 / c0**2
    )


def integrate_half(
    x, length, c0=1.0, m=1, kappa=1.0, dense=False,
    rtol=2.0e-8, atol=2.0e-10, steps=80,
):
    loga, pa0, logtau = x
    a0, tau = np.exp(loga), np.exp(logtau)
    u0 = throat_u(a0, c0, tau, m, kappa)
    y0 = np.array([a0, c0, u0, 0.0, pa0, 0.0, 0.0])
    p = Parameters(tau=tau, h0=-2.0 * c0**2, pv=0.0, hopf_m=m, kappa_psi=kappa)

    def positivity(_, y):
        return min(y[0], y[1]) - 1.0e-5

    positivity.terminal = True
    positivity.direction = -1
    sol = solve_ivp(
        lambda s, y: rhs(s, y, p),
        (0.0, length / 2.0),
        y0,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=max(length / (2.0 * steps), 1.0e-5),
        events=positivity,
        dense_output=dense,
    )
    return sol, p


def residual_transformed(x, length, c0=1.0, m=1, kappa=1.0):
    try:
        sol, p = integrate_half(x, length, c0, m, kappa)
    except (FloatingPointError, OverflowError, ValueError):
        return np.full(3, 1.0e3)
    if not sol.success or sol.t[-1] < length / 2.0 * (1.0 - 1.0e-8):
        return np.full(3, 1.0e3)
    dy = rhs(sol.t[-1], sol.y[:, -1], p)
    scale = np.array([1.0, 1.0, 1.0])
    return dy[:3] / scale


def solve_shot(length, seed, c0=1.0, m=1, kappa=1.0, max_nfev=500):
    opt = least_squares(
        residual_transformed,
        seed,
        args=(length, c0, m, kappa),
        method="trf",
        xtol=2.0e-11,
        ftol=2.0e-11,
        gtol=2.0e-11,
        max_nfev=max_nfev,
        bounds=([-3.0, -200.0, -5.0], [3.0, 200.0, 8.0]),
    )
    sol, p = integrate_half(opt.x, length, c0, m, kappa, dense=True)
    constraints = np.array([constraint(y, p) for y in sol.y.T])
    a0, tau = np.exp(opt.x[0]), np.exp(opt.x[2])
    return ShotResult(
        length=length,
        a0=a0,
        pa0=opt.x[1],
        tau=tau,
        residual=residual_transformed(opt.x, length, c0, m, kappa),
        cost=opt.cost,
        success=bool(opt.success and opt.cost < 1.0e-14),
        max_constraint=float(np.max(np.abs(constraints))),
        min_a=float(np.min(sol.y[0])),
        min_c=float(np.min(sol.y[1])),
        solution=sol,
    ), opt.x


def continuation(lengths, seed=None, c0=1.0, m=1, kappa=1.0):
    if seed is None:
        seed = np.array([0.0, 0.0, 0.0])
    results = []
    current = np.asarray(seed, dtype=float)
    for length in lengths:
        result, candidate = solve_shot(length, current, c0, m, kappa)
        results.append(result)
        if result.success:
            current = candidate
        print(
            f"L={length:8.4g} a0={result.a0:11.6g} "
            f"pa0={result.pa0:12.6g} tau={result.tau:11.6g} "
            f"|R|={np.linalg.norm(result.residual):10.3e} "
            f"Cmax={result.max_constraint:10.3e} "
            f"mina={result.min_a:9.3e} minc={result.min_c:9.3e} "
            f"{'OK' if result.success else 'FAIL'}"
        )
    return results


if __name__ == "__main__":
    grid = np.geomspace(0.02, 2.0, 17)
    continuation(grid)

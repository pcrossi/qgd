#!/usr/bin/env python3
"""Busca da forma de uma sela refletida colar--exterior Berger.

Classificação: teste de existência numérico condicional. Não inclui ainda o
vínculo energético C_E e não constitui a sela física final.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

from ponte_global_local_integrador import Parameters, constraint as c_inner, rhs as rhs_inner


TAU_GLOBAL = 1.0


def throat_u(a0: float, c0: float, tau: float, m: int = 1) -> float:
    return 4.0 - 8.0 * tau / a0**2 + 4.0 * tau * c0**2 / a0**4 - tau * m**2 / c0**2


def integrate_inner_shape(params: np.ndarray, length: float | None = None):
    loga, logc, pa0, logtau, _px0, log_inner_length = params
    if length is None:
        length = np.exp(log_inner_length)
    a0, c0, tau = np.exp(loga), np.exp(logc), np.exp(logtau)
    u0 = throat_u(a0, c0, tau)
    state0 = np.array([a0, c0, u0, 0.0, pa0, 0.0, 0.0])
    p = Parameters(tau=tau, h0=-2.0 * c0**2, pv=0.0, hopf_m=1, kappa_psi=1.0)
    sol = solve_ivp(
        lambda s, Y: rhs_inner(s, Y, p),
        (0.0, length),
        state0,
        method="DOP853",
        rtol=2e-9,
        atol=2e-11,
        max_step=length / 100.0,
    )
    return sol, p


def ext_velocities(Y: np.ndarray, tau: float) -> tuple[float, ...]:
    x, y, z, u, _v, px, py, pz, pu, pv, _Z = Y
    vol = np.exp(4.0 * x + 2.0 * y + z - u)
    E = np.exp(z - 2.0 * y)
    rx, ry = px / (tau * vol), py / (tau * vol) - 4.0 * E
    rz, ru = pz / (tau * vol), pu / (tau * vol)
    return (
        -rx / 16.0 - ru / 4.0,
        -ry / 8.0 - ru / 4.0,
        -rz / 2.0 - ru / 2.0,
        -rx / 4.0 - ry / 4.0 - rz / 2.0 - 1.5 * ru,
        pv / (2.0 * tau * vol),
    )


def ext_constraint(Y: np.ndarray, tau: float) -> float:
    _x, y, z, u, *_ = Y
    dx, dy, dz, du, dv = ext_velocities(Y, tau)
    k2 = 8*dx**2 + 16*dx*dy + 8*dx*dz + 4*dy*dz - 8*du*dx - 4*du*dy - 2*du*dz + du**2 + dv**2
    potential = 8*np.exp(-2*y) - 4*np.exp(2*z - 4*y)
    return tau*(potential-k2) + u - 4.0


def ext_rhs(_s: float, Y: np.ndarray, tau: float) -> np.ndarray:
    x, y, z, u, _v, *_ = Y
    dx, dy, dz, du, dv = ext_velocities(Y, tau)
    vol, E = np.exp(4*x+2*y+z-u), np.exp(z-2*y)
    k2 = 8*dx**2 + 16*dx*dy + 8*dx*dz + 4*dy*dz - 8*du*dx - 4*du*dy - 2*du*dz + du**2 + dv**2
    K = k2 + 4*E*dy + 8*np.exp(-2*y) - 4*E**2
    F = tau*K + u - 4.0
    return np.array([
        dx, dy, dz, du, dv,
        4*vol*F,
        vol*(2*F + tau*(-8*E*dy - 16*np.exp(-2*y) + 16*E**2)),
        vol*(F + tau*(4*E*dy - 8*E**2)),
        vol*(1-F),
        0.0,
        vol,
    ])


def integrate_exterior(inner_end: np.ndarray, px0: float, tau: float, length: float):
    a, c, u, v, pia, pic, piu = inner_end
    Y0 = np.array([0.0, np.log(a), np.log(c), u, v, px0, a*pia, c*pic, piu, 0.0, 0.0])
    sol = solve_ivp(
        lambda s, Y: ext_rhs(s, Y, tau),
        (0.0, length), Y0, method="DOP853",
        rtol=2e-9, atol=2e-11, max_step=length/150.0,
    )
    return sol


def residual(params: np.ndarray, exterior_half=0.25) -> np.ndarray:
    try:
        inner, p = integrate_inner_shape(params)
        if not inner.success or np.min(inner.y[:2]) <= 1e-5:
            return np.full(6, 1e3)
        ext = integrate_exterior(inner.y[:7, -1], params[4], p.tau, exterior_half)
        if not ext.success:
            return np.full(6, 1e3)
        end = ext.y[:, -1]
        vel = np.array(ext_velocities(end, p.tau))
        # Reflexão no meio: quatro velocidades geométricas nulas; v já é nulo.
        # A quinta condição exige S3 redondo no plano de reflexão.
        interface_constraint = ext_constraint(ext.y[:, 0], p.tau)
        scale = np.ones(6)
        return np.array([
            vel[0], vel[1], vel[2], vel[3],
            end[1]-end[2], interface_constraint,
        ]) / scale
    except (FloatingPointError, OverflowError, ValueError):
        return np.full(6, 1e3)


def solve():
    seed = np.array([0.0, 0.0, 4.0, 0.0, 0.0, np.log(0.05)])
    opt = least_squares(
        residual,
        seed,
        bounds=(
            [-3.0, -3.0, -200.0, -5.0, -200.0, np.log(0.005)],
            [3.0, 3.0, 200.0, 5.0, 200.0, np.log(0.5)],
        ),
        xtol=1e-11, ftol=1e-11, gtol=1e-11, max_nfev=1200,
        verbose=0,
    )
    inner, p = integrate_inner_shape(opt.x)
    ext = integrate_exterior(inner.y[:7, -1], opt.x[4], p.tau, 0.25)
    cin = max(abs(c_inner(Y, p)) for Y in inner.y.T)
    cex = max(abs(ext_constraint(Y, p.tau)) for Y in ext.y.T)
    print("Busca condicional da forma da sela")
    accepted = bool(opt.success and np.linalg.norm(residual(opt.x)) < 1e-7)
    print("optimizer_success =", opt.success)
    print("accepted_as_root =", accepted)
    print("x =", opt.x)
    print("residual =", residual(opt.x))
    print("norm =", np.linalg.norm(residual(opt.x)))
    print("cost =", opt.cost)
    print("max|C_inner| =", cin)
    print("max|C_exterior| =", cex)
    print("Z_half_unscaled =", ext.y[-1, -1])
    print("tau =", p.tau)


if __name__ == "__main__":
    solve()

"""Integrador do colo GDQ com fluxo fixo e matriz variacional.

Classificação numérica:
  - teste de consistência das equações reduzidas;
  - teste de preservação da restrição;
  - infraestrutura para cálculo DtN.

Não contém dados experimentais e não constitui previsão física.
"""

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


@dataclass(frozen=True)
class Parameters:
    tau: float
    h0: float
    pv: float
    hopf_m: int = 0
    kappa_psi: float = 1.0


def lower_u_root(r0: float, tau: float, pv: float, hopf_m=0, kappa_psi=1.0) -> float:
    """Raiz inferior da equação de lapse na garganta redonda."""
    a0 = (
        4.0 - 4.0 * tau / r0**2
        - tau * kappa_psi * hopf_m**2 / r0**2
    )
    if pv == 0.0:
        return a0
    b0 = pv**2 / (4.0 * tau * r0**6)
    umax = 0.5 * np.log(1.0 / (2.0 * b0))
    fmax = umax - a0 - 0.5
    if fmax < 0.0:
        raise ValueError("A corrente excede o limite de existência da garganta")

    def equation(u):
        return u - a0 - b0 * np.exp(2.0 * u)

    left = min(a0, umax) - 2.0
    while equation(left) > 0.0:
        left -= 2.0
    return brentq(equation, left, umax)


def beta_value(y: np.ndarray, p: Parameters) -> float:
    a, c, u, _, pa, _, pu = y
    eu = np.exp(u)
    return (
        a * pa * eu + 4.0 * c**2 * p.tau + 4.0 * p.h0 * p.tau
        + 2.0 * pu * eu
    ) / (2.0 * a**2 * c * eu)


def constraint(y: np.ndarray, p: Parameters) -> float:
    """Numerador da restrição do lapse após eliminar beta."""
    a, c, u, _, pa, pc, pu = y
    t, h, pv = p.tau, p.h0, p.pv
    eu = np.exp(u)
    return (
        4.0 * a**4 * c**2 * t * (u - 4.0)
        + 32.0 * a**2 * c**2 * t**2
        - 4.0 * a * c**2 * pa * t * eu
        - 2.0 * a * h * pa * t * eu
        - 16.0 * c**4 * t**2
        - 8.0 * c**2 * h * t**2
        - 4.0 * h**2 * t**2
        + c**2 * pc**2 * eu**2
        - 8.0 * c**2 * pu * t * eu
        + 2.0 * c * pc * pu * eu**2
        - 4.0 * h * pu * t * eu
        - pv**2 * eu**2
        + 4.0 * p.kappa_psi * a**4 * p.hopf_m**2 * t**2
    )


def rhs(_, y: np.ndarray, p: Parameters) -> np.ndarray:
    a, c, u, _v, pa, pc, pu = y
    t, h, pv = p.tau, p.h0, p.pv
    if a <= 0.0 or c <= 0.0:
        raise FloatingPointError("A métrica perdeu positividade")
    eu = np.exp(u)
    emu = np.exp(-u)

    ad = (2.0 * c**2 + h) / (2.0 * a * c)
    cd = -(c * pc + pu) * eu / (2.0 * a**2 * t)
    ud = (4.0 * c**2 * t - c * pc * eu + 2.0 * h * t) / (
        2.0 * a**2 * c * t
    )
    vd = pv * eu / (2.0 * a**2 * c * t)

    pad_num = (
        4.0 * a**4 * c**2 * t * (u - 4.0)
        + 2.0 * a * c**2 * pa * t * eu
        + a * h * pa * t * eu
        + 16.0 * c**4 * t**2
        + 8.0 * c**2 * h * t**2
        - c**2 * pc**2 * eu**2
        + 8.0 * c**2 * pu * t * eu
        - 2.0 * c * pc * pu * eu**2
        + 4.0 * h**2 * t**2
        + 4.0 * h * pu * t * eu
        + pv**2 * eu**2
    )
    pad = emu * pad_num / (2.0 * a**3 * c * t)
    pad += 2.0 * t * p.kappa_psi * a * p.hopf_m**2 * emu / c

    pcd_num = (
        4.0 * a**4 * c**2 * t * (u - 4.0)
        + 32.0 * a**2 * c**2 * t**2
        - 4.0 * a * c**2 * pa * t * eu
        + 2.0 * a * h * pa * t * eu
        - 48.0 * c**4 * t**2
        - 8.0 * c**2 * h * t**2
        + c**2 * pc**2 * eu**2
        - 8.0 * c**2 * pu * t * eu
        + 4.0 * h**2 * t**2
        + 4.0 * h * pu * t * eu
        + pv**2 * eu**2
    )
    pcd = emu * pcd_num / (4.0 * a**2 * c**2 * t)
    pcd -= t * p.kappa_psi * a**2 * p.hopf_m**2 * emu / c**2

    pud_num = (
        4.0 * a**4 * c**2 * t * (u - 5.0)
        + 32.0 * a**2 * c**2 * t**2
        - 16.0 * c**4 * t**2
        - 8.0 * c**2 * h * t**2
        - c**2 * pc**2 * eu**2
        - 2.0 * c * pc * pu * eu**2
        - 4.0 * h**2 * t**2
        + pv**2 * eu**2
    )
    pud = -emu * pud_num / (4.0 * a**2 * c * t)
    pud -= t * p.kappa_psi * a**2 * p.hopf_m**2 * emu / c
    return np.array([ad, cd, ud, vd, pad, pcd, pud], dtype=float)


def numerical_jacobian(y: np.ndarray, p: Parameters) -> np.ndarray:
    """Jacobiana por passo complexo; rhs é analítica no domínio positivo."""
    n = y.size
    jac = np.empty((n, n), dtype=float)
    step = 1.0e-30
    for j in range(n):
        yc = y.astype(complex)
        yc[j] += 1j * step
        # Implementação inline sem a checagem de ordem para aceitar complexos.
        jac[:, j] = np.imag(rhs_complex(yc, p)) / step
    return jac


def rhs_complex(y: np.ndarray, p: Parameters) -> np.ndarray:
    """Versão complexa usada somente para diferenciação numérica."""
    a, c, u, _v, pa, pc, pu = y
    t, h, pv = p.tau, p.h0, p.pv
    eu, emu = np.exp(u), np.exp(-u)
    ad = (2 * c**2 + h) / (2 * a * c)
    cd = -(c * pc + pu) * eu / (2 * a**2 * t)
    ud = (4 * c**2 * t - c * pc * eu + 2 * h * t) / (2 * a**2 * c * t)
    vd = pv * eu / (2 * a**2 * c * t)
    pad_num = (
        4 * a**4 * c**2 * t * (u - 4) + 2 * a * c**2 * pa * t * eu
        + a * h * pa * t * eu + 16 * c**4 * t**2 + 8 * c**2 * h * t**2
        - c**2 * pc**2 * eu**2 + 8 * c**2 * pu * t * eu
        - 2 * c * pc * pu * eu**2 + 4 * h**2 * t**2
        + 4 * h * pu * t * eu + pv**2 * eu**2
    )
    pcd_num = (
        4 * a**4 * c**2 * t * (u - 4) + 32 * a**2 * c**2 * t**2
        - 4 * a * c**2 * pa * t * eu + 2 * a * h * pa * t * eu
        - 48 * c**4 * t**2 - 8 * c**2 * h * t**2
        + c**2 * pc**2 * eu**2 - 8 * c**2 * pu * t * eu
        + 4 * h**2 * t**2 + 4 * h * pu * t * eu + pv**2 * eu**2
    )
    pud_num = (
        4 * a**4 * c**2 * t * (u - 5) + 32 * a**2 * c**2 * t**2
        - 16 * c**4 * t**2 - 8 * c**2 * h * t**2
        - c**2 * pc**2 * eu**2 - 2 * c * pc * pu * eu**2
        - 4 * h**2 * t**2 + pv**2 * eu**2
    )
    result = np.array(
        [ad, cd, ud, vd,
         emu * pad_num / (2 * a**3 * c * t),
         emu * pcd_num / (4 * a**2 * c**2 * t),
         -emu * pud_num / (4 * a**2 * c * t)],
        dtype=complex,
    )
    result[4] += 2 * t * p.kappa_psi * a * p.hopf_m**2 * emu / c
    result[5] -= t * p.kappa_psi * a**2 * p.hopf_m**2 * emu / c**2
    result[6] -= t * p.kappa_psi * a**2 * p.hopf_m**2 * emu / c
    return result


def augmented_rhs(s: float, z: np.ndarray, p: Parameters) -> np.ndarray:
    n = 7
    y = z[:n]
    phi = z[n:].reshape(n, n)
    return np.concatenate((rhs(s, y, p), (numerical_jacobian(y, p) @ phi).ravel()))


def initial_state(
    r0: float, tau: float, pv: float, pa0: float, hopf_m=0, kappa_psi=1.0
) -> tuple[np.ndarray, Parameters]:
    u0 = lower_u_root(r0, tau, pv, hopf_m, kappa_psi)
    p = Parameters(
        tau=tau, h0=-2.0 * r0**2, pv=pv,
        hopf_m=hopf_m, kappa_psi=kappa_psi,
    )
    y0 = np.array([r0, r0, u0, 0.0, pa0, 0.0, 0.0], dtype=float)
    return y0, p


def integrate(
    r0=1.0, tau=1.0, pv=0.0, pa0=4.0, length=0.05,
    hopf_m=0, kappa_psi=1.0,
):
    y0, p = initial_state(r0, tau, pv, pa0, hopf_m, kappa_psi)
    n = y0.size
    z0 = np.concatenate((y0, np.eye(n).ravel()))
    sol = solve_ivp(
        lambda s, z: augmented_rhs(s, z, p),
        (0.0, length),
        z0,
        method="DOP853",
        rtol=1.0e-10,
        atol=1.0e-12,
        max_step=length / 100.0,
    )
    constraints = np.array([constraint(z[:n], p) for z in sol.y.T])
    return sol, constraints, p


if __name__ == "__main__":
    solution, constraints, parameters = integrate()
    scale = max(1.0, np.max(np.abs(solution.y[:7])))
    print("Integração local:", "OK" if solution.success else solution.message)
    print("Passos:", solution.t.size)
    print("Restrição inicial:", constraints[0])
    print("Máximo |restrição|:", np.max(np.abs(constraints)))
    print("Máximo relativo:", np.max(np.abs(constraints)) / scale)
    print("Estado final:", solution.y[:7, -1])

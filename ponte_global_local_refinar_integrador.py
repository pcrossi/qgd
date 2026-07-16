"""Refinamento de tolerância e passo do integrador local m=1."""

import numpy as np
from scipy.integrate import solve_ivp

from ponte_global_local_integrador import (
    augmented_rhs,
    constraint,
    initial_state,
)


def run(rtol, steps):
    length = 0.05
    y0, p = initial_state(1.0, 1.0, 0.0, 4.0, hopf_m=1, kappa_psi=1.0)
    n = y0.size
    z0 = np.concatenate((y0, np.eye(n).ravel()))
    sol = solve_ivp(
        lambda s, z: augmented_rhs(s, z, p),
        (0.0, length),
        z0,
        method="DOP853",
        rtol=rtol,
        atol=rtol * 1.0e-2,
        max_step=length / steps,
    )
    cons = np.array([constraint(z[:n], p) for z in sol.y.T])
    return sol.y[:n, -1], np.max(np.abs(cons)), sol.t.size


if __name__ == "__main__":
    reference, _, _ = run(1.0e-12, 800)
    print("rtol      steps  npts   max_constraint   endpoint_error")
    for rtol in (1.0e-6, 1.0e-8, 1.0e-10):
        for steps in (50, 100, 200, 400):
            endpoint, cmax, npts = run(rtol, steps)
            error = np.linalg.norm(endpoint - reference, ord=np.inf)
            print(
                f"{rtol:8.0e} {steps:6d} {npts:6d} "
                f"{cmax:16.8e} {error:16.8e}"
            )

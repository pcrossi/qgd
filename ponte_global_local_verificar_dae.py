"""Verificação simbólica do DAE bulk--interface da GDQ.

Classificação: avaliação direta de identidades já derivadas.
Não resolve o background e não usa dados experimentais.
"""

import sympy as sp


def build():
    a, c, u, v = sp.symbols("a c u v", positive=True, real=True)
    ad, cd, ud, vd = sp.symbols("ad cd ud vd", real=True)
    tau = sp.symbols("tau", positive=True, real=True)
    beta, h0 = sp.symbols("beta h0", real=True)

    q_kin = (
        4 * a * ad * cd
        - 4 * a * c * ud * ad
        - 2 * a**2 * ud * cd
        + a**2 * c * (ud**2 + vd**2)
    )
    linear = 4 * c**2 * ad / a
    potential = 8 * c - 4 * c**3 / a**2
    lagrangian = sp.exp(-u) * (
        tau * (q_kin + linear + potential) + a**2 * c * (u - 4)
    ) + beta * (2 * c * (a * ad - c) - h0)

    velocities = (ad, cd, ud, vd)
    momenta = tuple(sp.diff(lagrangian, velocity) for velocity in velocities)
    flux = sp.diff(lagrangian, beta)

    # A restrição do lapse inclui a contribuição do multiplicador porque, em
    # coordenada r, o vínculo é beta*[2*c*a*a' - N*(2*c**2+h0)].
    lapse = sp.simplify(
        -tau * q_kin + tau * potential + a**2 * c * (u - 4)
        - sp.exp(u) * beta * (2 * c**2 + h0)
    )

    return {
        "fields": (a, c, u, v),
        "velocities": velocities,
        "tau": tau,
        "beta": beta,
        "h0": h0,
        "q_kin": q_kin,
        "linear": linear,
        "potential": potential,
        "lagrangian": lagrangian,
        "momenta": momenta,
        "flux": sp.factor(flux),
        "lapse": lapse,
    }


def verify(data):
    a, c, u, _ = data["fields"]
    ad, cd, ud, vd = data["velocities"]
    tau = data["tau"]
    beta = data["beta"]

    expected = (
        tau * sp.exp(-u) * (4 * a * cd - 4 * a * c * ud + 4 * c**2 / a)
        + 2 * beta * a * c,
        tau * sp.exp(-u) * (4 * a * ad - 2 * a**2 * ud),
        tau
        * sp.exp(-u)
        * (-4 * a * c * ad - 2 * a**2 * cd + 2 * a**2 * c * ud),
        2 * tau * sp.exp(-u) * a**2 * c * vd,
    )
    assert all(
        sp.simplify(got - want) == 0
        for got, want in zip(data["momenta"], expected)
    )

    r0, jv = sp.symbols("r0 jv", positive=True, real=True)
    throat_subs = {
        a: r0,
        c: r0,
        ad: 0,
        cd: 0,
        ud: 0,
        vd: jv * sp.exp(u) / (2 * tau * r0**3),
        data["h0"]: -2 * r0**2,
    }
    throat_lapse = sp.factor(data["lapse"].subs(throat_subs) / r0**3)
    expected_throat = sp.factor(
        tau * jv**2 * sp.exp(2 * u) / (4 * tau**2 * r0**6)
        * (-1)
        + 4 * tau / r0**2
        + u
        - 4
    )
    assert sp.simplify(throat_lapse - expected_throat) == 0

    return throat_lapse


if __name__ == "__main__":
    system = build()
    throat_equation = verify(system)
    print("Identidades canônicas: OK")
    print("Vínculo de fluxo:", system["flux"])
    print("Restrição do lapse na garganta:", throat_equation, "= 0")

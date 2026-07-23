"""
GDQ — Solução Dilatônica com Imersão Dinâmica

Baseado em 37-3.md: o vínculo constitutivo h_ij = gamma_0_ij é relaxado
para permitir que a imersão i_b seja dinâmica. A métrica induzida no
espaço-tempo físico N é:

    i_b^*(g)_ij = b(t)^2 * gamma_0_ij

A equação dilatônica em FLRW com fator de escala b(t) e dilaton f(t)
torna-se:

    ü + 3H u̇ + (3/2)(b̈/b + H² + k/b²)u = 0,   u = e^{-f/2}

onde k = 0, +1, -1 é a curvatura espacial. O vínculo constitutivo
relaxado permite escolher b(t) dinamicamente.

Objetivo: encontrar um background (b(t), f(t)) globalmente regular.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import warnings
warnings.filterwarnings('ignore')


def solve_dilaton_dinamico(b_func, db_func, ddb_func, k, t_span, u0, du0,
                           n_points=5000):
    """
    Resolve ü + 3H u̇ + (3/2)(b̈/b + H² + k/b²)u = 0
    para b(t) arbitrário e curvatura espacial k.
    """
    def eq(t, y):
        b = b_func(t)
        db = db_func(t)
        ddb = ddb_func(t)
        H = db / b
        coeff = (3.0 / 2.0) * (ddb / b + H**2 + k / b**2)
        return [y[1], -3.0 * H * y[1] - coeff * y[0]]

    t_eval = np.linspace(t_span[0], t_span[1], n_points)
    sol = solve_ivp(eq, t_span, [u0, du0], t_eval=t_eval,
                    dense_output=True, max_step=0.005,
                    rtol=1e-10, atol=1e-12)
    return sol


def diagnose_background(name, b_func, db_func, ddb_func, k, t_span):
    """Diagnostica um candidato de background."""
    u0, du0 = 1.0, 0.0
    sol = solve_dilaton_dinamico(b_func, db_func, ddb_func, k, t_span, u0, du0)
    u_vals = sol.y[0]
    t_vals = sol.t
    f_vals = np.where(np.abs(u_vals) > 1e-10,
                      -2 * np.log(np.abs(u_vals)), np.nan)

    sign_changes = np.where(np.diff(np.sign(u_vals)))[0]
    has_zeros = len(sign_changes) > 0
    min_u = np.min(u_vals)
    max_f = np.nanmax(np.abs(f_vals))

    status = "SINGULAR" if has_zeros or min_u < 1e-6 else "CANDIDATO"
    return {
        'name': name,
        't': t_vals,
        'u': u_vals,
        'f': f_vals,
        'zeros': len(sign_changes),
        'min_u': min_u,
        'max_f': max_f,
        'status': status,
    }


def find_regular_power_law(k=0, t0=0.1, t1=10.0):
    """
    Busca uma lei de potência b(t) = t^p que produza u > 0 global.
    Para b = t^p:
        H = p/t
        b̈/b = p(p-1)/t²
        coeff = (3/2)[p(p-1) + p² + k/t^{2(1-p)}]/t²
    """
    print("\n" + "=" * 70)
    print("BUSCA POR LEI DE POTÊNCIA REGULAR")
    print("=" * 70)

    best = None
    for p in np.linspace(0.1, 2.0, 39):
        def b(t): return t**p
        def db(t): return p * t**(p - 1)
        def ddb(t): return p * (p - 1) * t**(p - 2)

        sol = solve_dilaton_dinamico(b, db, ddb, k, (t0, t1), 1.0, 0.0)
        u_vals = sol.y[0]
        min_u = np.min(u_vals)
        zeros = len(np.where(np.diff(np.sign(u_vals)))[0])

        if zeros == 0 and min_u > 1e-6:
            print(f"p = {p:.3f}: CANDIDATO (min u = {min_u:.4e})")
            if best is None or min_u > best['min_u']:
                best = {'p': p, 'min_u': min_u}
        else:
            print(f"p = {p:.3f}: singular (zeros={zeros}, min u={min_u:.4e})")

    if best:
        print(f"\nMelhor candidato: p = {best['p']:.3f}, min u = {best['min_u']:.4e}")
    else:
        print("\nNenhum candidato regular encontrado.")
    return best


if __name__ == "__main__":
    t0, t1 = 0.1, 10.0

    # Testar backgrounds conhecidos com imersão dinâmica (k=0)
    candidates = {
        "b=t^{1/2}": {
            "b": lambda t: t**0.5,
            "db": lambda t: 0.5 * t**(-0.5),
            "ddb": lambda t: -0.25 * t**(-1.5),
            "k": 0,
        },
        "b=t^{2/3}": {
            "b": lambda t: t**(2.0/3.0),
            "db": lambda t: (2.0/3.0) * t**(-1.0/3.0),
            "ddb": lambda t: -(2.0/9.0) * t**(-4.0/3.0),
            "k": 0,
        },
        "b=t (Milne)": {
            "b": lambda t: t,
            "db": lambda t: np.ones_like(t) if isinstance(t, np.ndarray) else 1.0,
            "ddb": lambda t: np.zeros_like(t) if isinstance(t, np.ndarray) else 0.0,
            "k": 0,
        },
        "b=e^t (de Sitter)": {
            "b": lambda t: np.exp(t),
            "db": lambda t: np.exp(t),
            "ddb": lambda t: np.exp(t),
            "k": 0,
        },
    }

    results = []
    for name, funcs in candidates.items():
        r = diagnose_background(name, funcs["b"], funcs["db"],
                                funcs["ddb"], funcs["k"], (t0, t1))
        results.append(r)

    # Plot
    fig, axes = plt.subplots(len(results), 2, figsize=(14, 4 * len(results)))
    fig.suptitle("GDQ — Dilaton com Imersão Dinâmica", fontsize=14,
                 fontweight='bold')

    for ax_row, r in zip(axes, results):
        ax_row[0].plot(r['t'], r['u'], 'b-', lw=1.5, label='u(t)')
        ax_row[0].axhline(0, color='r', lw=0.8, ls='--')
        ax_row[0].set_title(f"{r['name']}\n{r['status']}", fontsize=9)
        ax_row[0].set_ylabel("u = e^{-f/2}")
        ax_row[0].set_xlabel("t")
        ax_row[0].legend(fontsize=7)

        ax_row[1].plot(r['t'], r['f'], 'g-', lw=1.5, label='f(t)')
        ax_row[1].set_title(f"Dilaton — zeros de u = {r['zeros']}", fontsize=9)
        ax_row[1].set_ylabel("f(t)")
        ax_row[1].set_xlabel("t")
        ax_row[1].set_ylim(-20, 20)
        ax_row[1].legend(fontsize=7)

    plt.tight_layout()
    plt.savefig("/home/pedro/Dropbox/obs/todo/37p/dilaton_dinamico.png",
                dpi=150, bbox_inches='tight')
    plt.close()

    # Resumo
    print("=" * 70)
    print("GDQ — DIAGNÓSTICO DILATÔNICO COM IMERSÃO DINÂMICA")
    print("=" * 70)
    for r in results:
        print(f"\n{r['status']} | {r['name']}")
        print(f"  Zeros de u: {r['zeros']}")
        print(f"  Min u: {r['min_u']:.4e}")
        print(f"  |f|_max: {r['max_f']:.2f}")

    # Busca por lei de potência regular
    find_regular_power_law(k=0, t0=t0, t1=t1)

    print(f"\nFigura salva: /home/pedro/Dropbox/obs/todo/37p/dilaton_dinamico.png")

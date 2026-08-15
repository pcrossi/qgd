#!/usr/bin/env python3
"""
GDQ — Chapter 6 / Causal clock homomorphism.

Objective:
    Verify in a self-contained way the construction used in Chapter 6:
    if the physical clock t forms the additive group of translations and the flux
    parameter tau belongs to the positive multiplicative group, group compatibility
    imposes f(t1+t2)=f(t1)f(t2). Under regularity, the solution is
    f(t)=exp(kappa t), i.e., tau_gamma(t)=tau0 exp(kappa t).

Theoretical source:
    manuscript/06_global_local_bridge/06.8 - Clock, current and continuity in the laboratory.md
    manuscript/notes/equations/Audit of the canonical term rho d_t S_R.md

Classification:
    Symbolic-numerical consistency verification. It is not a physical prediction.

Equation:
    f(t1+t2)=f(t1)f(t2)
    tau_gamma(t)=tau0 exp(kappa t)
    gamma^*(d tau/tau)=kappa dt

Domain and boundary:
    Real additive group of local time and positive real multiplicative group
    of the scale parameter; no PDE and no spatial boundary.

Parameters:
    Universal/structural:
        logarithmic form d tau/tau.
    Apparatus/experiment data:
        none.
    Numerical:
        tau0 and kappa chosen only for algebraic test.

Output:
    output_verify_clock_homomorphism.md

Observation:
    The test verifies the mathematical form of the homomorphism. It does not by itself
    derive the complete physical dynamics of the apparatus nor does it fix kappa metrologically.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_clock_homomorphism.md")


def main() -> None:
    tau0 = 2.0
    kappa = 0.37
    pairs = [(-1.0, 0.25), (0.1, 0.9), (1.0, 2.0), (-0.4, 1.7)]
    rows = []
    for t1, t2 in pairs:
        f1 = math.exp(kappa * t1)
        f2 = math.exp(kappa * t2)
        f12 = math.exp(kappa * (t1 + t2))
        defect = abs(f12 - f1 * f2)
        rows.append((t1, t2, f12, f1 * f2, defect))

    dt = 1e-5
    t = 0.8
    tau = lambda x: tau0 * math.exp(kappa * x)
    numerical_pullback = (math.log(tau(t + dt)) - math.log(tau(t - dt))) / (2 * dt)

    lines = [
        "---",
        'title: "Output — causal clock homomorphism"',
        "---",
        "",
        "# Output — causal clock homomorphism",
        "",
        "Classification: symbolic-numerical consistency verification.",
        "",
        f"Educational parameters: $\\tau_0={tau0}$, $\\kappa={kappa}$.",
        "",
        "| $t_1$ | $t_2$ | $f(t_1+t_2)$ | $f(t_1)f(t_2)$ | defect |",
        "|---:|---:|---:|---:|---:|",
    ]
    for t1, t2, f12, prod, defect in rows:
        lines.append(f"| {t1:.2f} | {t2:.2f} | {f12:.12f} | {prod:.12f} | {defect:.3e} |")

    lines += [
        "",
        f"Numerical derivative of $\\log\\tau_\\gamma(t)$ at $t={t}$: `{numerical_pullback:.12f}`.",
        "",
        "Conclusion: the pullback of the logarithmic form satisfies",
        "$\\gamma^*(d\\tau/\\tau)=\\kappa dt$ in the exponential clock.",
        "This verifies the mathematical form of the conditional theorem; it does not by",
        "itself derive the complete physical dynamics of the apparatus.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

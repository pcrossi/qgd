#!/usr/bin/env python3
"""
GDQ — Chapter 12 / Delayed choice with causal kernel

Objective:
    Integrate a temporal impedance switching from off to on and calculate
    Gamma_det(t_f) via an exponential causal kernel.

Theoretical source:
    manuscript/12_tunneling_interference_transport/notes/delayed_choice_boundary_not_retrocausal.md

Classification:
    Reduced transport. It is not a complete simulation of the official action.

Output:
    scripts/output_delayed_choice_kernel.md
"""

from __future__ import annotations

import numpy as np
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_delayed_choice_kernel.md"

    t = np.linspace(0, 10, 4001)
    tf = 10.0
    tc = 6.0
    tau_switch = 0.35
    tau_mem = 1.0
    r_off = 0.0
    r_on = 3.0
    delta_phi_sq = 1.0
    s = 1.0 / (1.0 + np.exp(-(t - tc) / tau_switch))
    r_t = r_off + s * (r_on - r_off)
    w = np.exp(-(tf - t) / tau_mem)
    w[t > tf] = 0.0
    w = w / np.trapezoid(w, t)
    gamma = 0.5 * np.trapezoid(delta_phi_sq * r_t * w, t)
    coherence = np.exp(-gamma)

    text = f"""# Output — delayed choice with causal kernel

Classification: reduced transport.

| quantity | value |
|---|---:|
| t_f | {tf:.12f} |
| t_c | {tc:.12f} |
| tau_switch | {tau_switch:.12f} |
| tau_mem | {tau_mem:.12f} |
| Gamma_det(t_f) | {gamma:.12f} |
| exp(-Gamma_det) | {coherence:.12f} |

Interpretation: the final registration depends on the weighted causal history of the apparatus boundary. There is no support for times later than t_f.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

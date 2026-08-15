#!/usr/bin/env python3
"""
Self-contained contract for the integrated cosmological solver of GDQ.

Classification:
    structural/symbolic verification of solver architecture.

This script does not calculate CMB, BAO, BBN, or lensing. It records, in an
executable form, the minimal chain that a future metrological solver must obey:

    S_GDQ -> Phi_cos* -> K_cos^phys -> cosmological observables.

The practical utility is to prevent each cosmological anomaly from receiving its own
independent factor adjusted afterwards. The same set P_cos must feed all blocks.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_integrated_cosmology_contraction.md"


def main() -> None:
    inputs = [
        "Phi_cos*=(g,J,H,f,U)_cos",
        "R_H",
        "eta_b",
        "T_0",
        "P_prim",
        "B_boundary",
    ]
    observables = [
        "H(z)",
        "SN",
        "BAO",
        "CMB",
        "BBN/lithium",
        "lensing",
        "growth",
        "birefringence",
    ]
    prohibitions = [
        "independent factor for Hubble",
        "independent factor for lithium",
        "independent factor for Bullet Cluster",
        "independent factor for birefringence",
        "changing boundary after comparison",
    ]

    lines = [
        "---",
        'title: "Output — integrated cosmology contract"',
        "---",
        "",
        "# Output — integrated cosmology contract",
        "",
        "## Single input",
        "",
        "$$",
        "\\mathcal P_{\\rm cos}=(\\Phi_*^{\\rm cos},R_H,\\eta_b,T_0,\\mathcal P_{\\rm prim},\\mathcal B_{\\rm contorno})",
        "$$",
        "",
        "| Item | Role |",
        "|---|---|",
    ]
    for item in inputs:
        lines.append(f"| `{item}` | frozen data before comparison |")

    lines += [
        "",
        "## Common chain",
        "",
        "$$",
        "\\mathcal S_{\\rm GDQ}\\to\\Phi_*^{\\rm cos}\\to K_{\\rm cos}^{\\rm phys}\\to\\delta\\Phi_{\\rm cos}\\to\\text{observables}",
        "$$",
        "",
        "$$",
        "K_{\\rm cos}^{\\rm phys}=P_{\\rm cos}^{\\rm phys}\\operatorname{Hess}\\mathcal S_{\\rm GDQ}P_{\\rm cos}^{\\rm phys}",
        "$$",
        "",
        "$$",
        "K_{\\rm cos}^{\\rm phys}\\delta\\Phi_{\\rm cos}=J_{\\rm bar}+J_\\gamma+J_\\nu+J_H",
        "$$",
        "",
        "## Mandatory observables",
        "",
        "| Observable | Must use |",
        "|---|---|",
    ]
    for obs in observables:
        lines.append(f"| `{obs}` | the same `P_cos` and the same background |")

    lines += [
        "",
        "## Closure prohibitions",
        "",
        "| Prohibition | Reason |",
        "|---|---|",
    ]
    for item in prohibitions:
        lines.append(f"| `{item}` | would break integrated cosmology |")

    lines += [
        "",
        "## Classification",
        "",
        "Structurally closed formulation. Joint metrological solver remains a future extension.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

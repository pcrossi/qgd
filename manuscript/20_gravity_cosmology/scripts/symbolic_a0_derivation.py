#!/usr/bin/env python3
"""
Symbolic and dimensional derivation of the GDQ critical galactic acceleration.

Classification:
    symbolic/dimensional evaluation of reduced formula.

The script does not fit parameters to the MOND/RAR phenomenological value. It shows:

1. the cosmological boundary datum R_H=c/H0;
2. the horizon acceleration a_H=c^2/R_H=cH0;
3. the circular projection per cycle, a0=a_H/(2*pi);
4. the distinction between the main scale and the auxiliary de Sitter scale.

Numerical comparisons are in the script `calculate_galactic_a0.py`.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_symbolic_a0_derivation.md"


def main() -> None:
    lines = [
        "---",
        'title: "Output — symbolic derivation of a0"',
        "---",
        "",
        "# Output — symbolic derivation of $a_0$",
        "",
        "## Chain",
        "",
        "$$",
        "R_H=\\frac{c}{H_0}",
        "$$",
        "",
        "$$",
        "a_H=\\frac{c^2}{R_H}=cH_0",
        "$$",
        "",
        "$$",
        "a_0^{\\rm GDQ}=\\frac{a_H}{2\\pi}=\\frac{cH_0}{2\\pi}",
        "$$",
        "",
        "## Dimension",
        "",
        "$$",
        "[cH_0]=\\frac{L}{T}\\frac{1}{T}=\\frac{L}{T^2}",
        "$$",
        "",
        "Hence $a_0^{\\rm GDQ}$ has the dimension of acceleration.",
        "",
        "## Auxiliary scale",
        "",
        "$$",
        "a_{\\rm dS}^{(2\\pi)}=\\frac{cH_0\\sqrt{\\Omega_\\Lambda}}{2\\pi}",
        "$$",
        "",
        "This scale uses the de Sitter factor and is not the main definition of $a_0^{\\rm GDQ}$.",
        "",
        "## Classification",
        "",
        "Symbolic/dimensional verification. No MOND experimental value enters the deduction.",
        "",
    ]
    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

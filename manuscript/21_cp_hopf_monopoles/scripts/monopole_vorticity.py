#!/usr/bin/env python3
"""
Objective:
    Self-contained log of the `monopole vorticity` verification associated with chapter `21_cp_hopf_monopoles`.
Chapter 21 — didactic test of vorticity without local monopole.

Classification:
    symbolic/didactic verification of differential identity.

We use a simple regular velocity field:

    v = (-y, x, 0)

Then:

    curl(v) = (0, 0, 2)
    div(curl(v)) = 0.

This illustrates the local readout: if B is regular vorticity, there is no local
point magnetic source. Global bundle topology is another level of the problem.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    # Field v=(-y,x,0). Analytical derivatives:
    curl_v = (0.0, 0.0, 2.0)
    div_curl_v = 0.0

    lines = [
        '---',
        'title: "Output — local monopole and vorticity"',
        '---',
        '',
        '# Output — local monopole and vorticity',
        '',
        'Regular test field:',
        '',
        '$$',
        '\\mathbf v=(-y,x,0)',
        '$$',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| $\\nabla\\times\\mathbf v$ | `{curl_v}` |',
        f'| $\\nabla\\cdot(\\nabla\\times\\mathbf v)$ | `{div_curl_v:.12f}` |',
        '',
        'Conclusion: in the regular sector, a magnetic field modeled as vorticity has no local divergence.',
        'This does not exclude global bundle classes or quantized flows across multiple charts.',
        '',
    ]

    out = Path(__file__).with_name('output_monopole_vorticity.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

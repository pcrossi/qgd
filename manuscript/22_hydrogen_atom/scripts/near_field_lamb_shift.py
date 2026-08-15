#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `near field lamb shift` verification associated with chapter `22_hydrogen_atom`.
Chapter 22 — near-field operator scale for Lamb shift.

Classification:
    scale diagnostic, not a prediction. The metrological value enters only to
    indicate how much the DtN/near operator must produce.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    h = 4.135_667_696e-15  # eV s
    lamb_hz = 1.057_845e9
    finite_size_eV = 5.715_065_938_837e-10
    lamb_eV = h * lamb_hz
    near_req_eV = lamb_eV - finite_size_eV
    near_req_hz = near_req_eV / h

    lines = [
        '---',
        'title: "Output — Lamb shift as near field"',
        '---',
        '',
        '# Output — Lamb shift as near field',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| Lamb used for diagnosis | `{lamb_hz:.12e}` Hz |',
        f'| Lamb in energy | `{lamb_eV:.12e}` eV |',
        f'| finite size 2s | `{finite_size_eV:.12e}` eV |',
        f'| required near operator | `{near_req_eV:.12e}` eV |',
        f'| required near operator | `{near_req_hz:.12e}` Hz |',
        '',
        'Classification: diagnostic scale of the DtN/near operator, not a fit.',
        '',
    ]
    out = Path(__file__).with_name('output_near_field_lamb_shift.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

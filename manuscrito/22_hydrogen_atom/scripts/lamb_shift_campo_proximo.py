#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `lamb shift campo proximo` associada ao capítulo `22_hydrogen_atom`.
Capítulo 22 — escala do operador de campo próximo para Lamb shift.

Classificação:
    diagnóstico de escala, não previsão. O valor metrológico entra apenas para
    indicar quanto o operador DtN/near deve produzir.
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
        'title: "Saída — Lamb shift como campo próximo"',
        '---',
        '',
        '# Saída — Lamb shift como campo próximo',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| Lamb usado para diagnóstico | `{lamb_hz:.12e}` Hz |',
        f'| Lamb em energia | `{lamb_eV:.12e}` eV |',
        f'| tamanho finito 2s | `{finite_size_eV:.12e}` eV |',
        f'| operador near requerido | `{near_req_eV:.12e}` eV |',
        f'| operador near requerido | `{near_req_hz:.12e}` Hz |',
        '',
        'Classificação: escala diagnóstica do operador DtN/near, não ajuste.',
        '',
    ]
    out = Path(__file__).with_name('saida_lamb_shift_campo_proximo.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

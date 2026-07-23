#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `monopolo vorticidade` associada ao capítulo `21_cp_hopf_monopoles`.
Capítulo 21 — teste didático de vorticidade sem monopolo local.

Classificação:
    verificação simbólica/didática de identidade diferencial.

Usamos um campo de velocidade regular simples:

    v = (-y, x, 0)

Então:

    curl(v) = (0, 0, 2)
    div(curl(v)) = 0.

Isso ilustra a leitura local: se B é vorticidade regular, não há fonte
magnética pontual local. Topologia global de fibrado é outro nível do problema.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    # Campo v=(-y,x,0). Derivadas analíticas:
    curl_v = (0.0, 0.0, 2.0)
    div_curl_v = 0.0

    lines = [
        '---',
        'title: "Saída — monopolo local e vorticidade"',
        '---',
        '',
        '# Saída — monopolo local e vorticidade',
        '',
        'Campo teste regular:',
        '',
        '$$',
        '\\mathbf v=(-y,x,0)',
        '$$',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $\\nabla\\times\\mathbf v$ | `{curl_v}` |',
        f'| $\\nabla\\cdot(\\nabla\\times\\mathbf v)$ | `{div_curl_v:.12f}` |',
        '',
        'Conclusão: no setor regular, um campo magnético modelado como vorticidade não possui divergência local.',
        'Isso não exclui classes globais de fibrado ou fluxos quantizados em múltiplas cartas.',
        '',
    ]

    out = Path(__file__).with_name('saida_monopolo_vorticidade.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

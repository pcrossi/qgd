#!/usr/bin/env python3
"""
Gera uma matriz autocontida de status das objeções do Capítulo 28.

O objetivo não é calcular nova física. O script documenta a classificação
conservadora usada no FAQ técnico, para que a tabela possa ser regenerada e
auditada sem depender de arquivos históricos externos ao manuscrito.
"""

from pathlib import Path


ITEMS = [
    {
        "objecao": "A ação muda para bater números?",
        "resposta": "Não. Mudam background, contorno, fonte, vínculo, projetor e observável.",
        "status": "definição metodológica",
        "acao": "preservar a ação oficial e declarar dados externos",
    },
    {
        "objecao": "A GDQ é o Modelo Padrão renomeado?",
        "resposta": "Não. O Modelo Padrão aparece apenas como redução operacional setorial.",
        "status": "redução efetiva",
        "acao": "não inverter a cadeia dedutiva",
    },
    {
        "objecao": "Perelman 3D foi aplicado em 8D?",
        "resposta": "A aplicação é setorial por fatoração; backgrounds mistos exigem Hessiana completa.",
        "status": "teorema condicional",
        "acao": "indicar domínio produto ou misto",
    },
    {
        "objecao": "Born foi assumido?",
        "resposta": "Born é operacional no Hilbert físico; o evento individual exige aparelho.",
        "status": "fechado estruturalmente",
        "acao": "separar probabilidade de mecanismo de registro",
    },
    {
        "objecao": "Bell/no-signalling está provado?",
        "resposta": "A geometria do emaranhamento está formulada; aparelhos reais são extensão.",
        "status": "programa operacional futuro",
        "acao": "calcular marginais com impedâncias reais",
    },
    {
        "objecao": "Fantasmas/BRST são ontologia?",
        "resposta": "Não. São linguagem auxiliar de auditoria de quociente, quando usados.",
        "status": "classificação ontológica",
        "acao": "usar Tr_phys log K_phys como objeto intrínseco",
    },
    {
        "objecao": "Bons números provam tudo?",
        "resposta": "Não. Eles reforçam cadeias derivadas, mas não substituem derivação.",
        "status": "critério numérico",
        "acao": "classificar comparação e congelar parâmetros",
    },
    {
        "objecao": "Massas absolutas são previstas do nada?",
        "resposta": "Não. Unidades exigem calibração; a teoria mira razões adimensionais.",
        "status": "metrologia",
        "acao": "separar régua dimensional de razão geométrica",
    },
]


def render_table() -> str:
    lines = [
        "---",
        'title: "Saída — matriz de status do FAQ"',
        "---",
        "",
        "# Saída — matriz de status do FAQ",
        "",
        "| Objeção | Resposta curta | Status | Ação recomendada |",
        "|---|---|---|---|",
    ]
    for item in ITEMS:
        lines.append(
            f"| {item['objecao']} | {item['resposta']} | {item['status']} | {item['acao']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    out = Path(__file__).with_name("saida_faq_status_matrix.md")
    out.write_text(render_table(), encoding="utf-8")
    print(f"Arquivo gerado: {out.name}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `tabela status numerico` associada ao capítulo `27_numeric_experimental_program`.
Tabela de status numérico dos blocos principais.

Classificação:
    consolidação documental.

O script reúne o status conservador dos blocos numéricos já incorporados ao
manuscrito, sem transformar reduções em fechamento metrológico final.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_tabela_status_numerico.md"


@dataclass(frozen=True)
class Block:
    name: str
    status: str
    next_step: str


BLOCKS = [
    Block("ponte global-local", "teorema condicional e testes reduzidos", "robustez em classes mais gerais"),
    Block("problema do sinal", "benchmark reduzido positivo", "algoritmo assintótico e variância"),
    Block("três estômatos", "seleção reduzida", "elevação global/covariante"),
    Block("eletrofraco", "quebra estrutural e W/Z reduzidos", "transporte e normas globais"),
    Block("confinamento", "lei de área estrutural", "perfil funcional e comparação ampla"),
    Block("alpha", "origem global condicionada", "backgrounds warped/mistos"),
    Block("G", "contorno global estrutural", "prefatores locais/warp"),
    Block("massas leptônicas", "produto 8D condicional", "warped/misto"),
    Block("bárions", "estrutura reduzida forte", "fatores diferenciais"),
    Block("hidrogênio", "estrutural com metrologia líder", "Hessiana protônica fina"),
    Block("decaimento alfa", "prova de conceito reduzida", "Hessiana nuclear completa"),
    Block("buracos negros", "redução estável", "sela covariante 8D"),
    Block("cosmologia", "estrutura e escalas", "solver integrado"),
]


def main() -> None:
    lines = ["# Saída — status numérico consolidado\n\n"]
    lines.append("Classificação: consolidação documental.\n\n")
    lines.append("| bloco | status | próximo passo |\n")
    lines.append("|---|---|---|\n")
    for block in BLOCKS:
        lines.append(f"| {block.name} | {block.status} | {block.next_step} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("Os blocos têm status heterogêneo; o capítulo padroniza como prosseguir.\n")
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

